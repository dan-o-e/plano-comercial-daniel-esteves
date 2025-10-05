#!/usr/bin/env python3
"""
Script para configurar Supabase como alternativa ao Azure PostgreSQL
Supabase é mais fácil e rápido de configurar
"""

import pandas as pd
import psycopg2
from sqlalchemy import create_engine, text
import os
from urllib.parse import urlparse

def parse_supabase_url(database_url):
    """Extrair componentes da URL do Supabase"""
    parsed = urlparse(database_url)
    return {
        'host': parsed.hostname,
        'port': parsed.port or 5432,
        'user': parsed.username,
        'password': parsed.password,
        'database': parsed.path[1:]  # Remove a barra inicial
    }

def migrate_to_supabase():
    """Migrar dados para Supabase"""
    print("🚀 MIGRAÇÃO PARA SUPABASE POSTGRESQL")
    print("=" * 50)
    
    # Solicitar URL do Supabase
    print("📋 Para obter a URL de conexão:")
    print("1. Acesse: https://supabase.com")
    print("2. Crie um projeto (gratuito)")
    print("3. Vá em Settings > Database")
    print("4. Copie a 'Connection string' (URI)")
    print()
    
    database_url = input("Cole a URL de conexão do Supabase: ").strip()
    
    if not database_url:
        print("❌ URL não informada!")
        return
    
    try:
        # Configurar bancos
        LOCAL_CONFIG = {
            'host': 'localhost',
            'port': 5433,
            'user': 'postgres', 
            'password': 'postgres',
            'database': 'base_btg'
        }
        
        supabase_config = parse_supabase_url(database_url)
        
        print(f"🔗 Conectando ao Supabase: {supabase_config['host']}")
        
        # Conectar ao banco local
        local_engine = create_engine(f"postgresql://{LOCAL_CONFIG['user']}:{LOCAL_CONFIG['password']}@{LOCAL_CONFIG['host']}:{LOCAL_CONFIG['port']}/{LOCAL_CONFIG['database']}")
        
        # Conectar ao Supabase
        supabase_engine = create_engine(database_url)
        
        # Testar conexões
        print("🔍 Testando conexão local...")
        with local_engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("✅ Conexão local OK!")
        
        print("🔍 Testando conexão Supabase...")
        with supabase_engine.connect() as conn:
            result = conn.execute(text("SELECT version()"))
            version = result.fetchone()[0]
        print(f"✅ Conexão Supabase OK! Versão: {version}")
        
        # Listar e migrar tabelas
        with local_engine.connect() as conn:
            result = conn.execute(text("SELECT tablename FROM pg_tables WHERE schemaname = 'public';"))
            tables = [row[0] for row in result]
        
        print(f"📊 Encontradas {len(tables)} tabelas para migrar...")
        
        for table in tables:
            print(f"📤 Migrando: {table}")
            
            # Ler dados
            df = pd.read_sql_table(table, local_engine)
            print(f"   📦 {len(df)} registros")
            
            # Migrar para Supabase
            df.to_sql(table, supabase_engine, if_exists='replace', index=False)
            print(f"   ✅ {table} migrada!")
        
        print("\n🎉 MIGRAÇÃO CONCLUÍDA!")
        print("=" * 50)
        print("📋 CONFIGURAÇÃO PARA STREAMLIT CLOUD:")
        print()
        print("[connections.postgresql]")
        print("dialect = \"postgresql\"")
        print(f'host = "{supabase_config["host"]}"')
        print(f'port = "{supabase_config["port"]}"')
        print(f'database = "{supabase_config["database"]}"')
        print(f'username = "{supabase_config["user"]}"')
        print(f'password = "{supabase_config["password"]}"')
        print()
        print("🔗 URL completa para backup:")
        print(database_url)
        print()
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        print()
        print("💡 Soluções:")
        print("- Verifique se a URL está correta")
        print("- Confirme se o banco local está rodando")
        print("- Teste a conexão Supabase no navegador")
    
    finally:
        try:
            local_engine.dispose()
            supabase_engine.dispose()
        except:
            pass

if __name__ == "__main__":
    migrate_to_supabase()