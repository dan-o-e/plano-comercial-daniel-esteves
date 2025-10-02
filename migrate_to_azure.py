#!/usr/bin/env python3
"""
Script para migrar dados do PostgreSQL local para Azure PostgreSQL
"""

import pandas as pd
import psycopg2
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurações do banco LOCAL (origem)
LOCAL_CONFIG = {
    'host': 'localhost',
    'port': 5433,
    'user': 'postgres',
    'password': 'postgres',
    'database': 'base_btg'
}

# Configurações do banco AZURE (destino)
AZURE_CONFIG = {
    'host': 'plano-comercial-daniel.postgres.database.azure.com',
    'port': 5432,
    'user': 'postgres',
    'password': os.getenv('AZURE_DB_PASSWORD', ''),  # Defina a senha nas variáveis de ambiente
    'database': 'postgres'
}

def create_connection(config):
    """Criar conexão com o banco de dados"""
    try:
        connection_string = f"postgresql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
        engine = create_engine(connection_string)
        return engine
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return None

def migrate_data():
    """Migrar dados do banco local para Azure"""
    print("🚀 Iniciando migração para Azure PostgreSQL...")
    
    # Conectar ao banco local
    print("📡 Conectando ao banco local...")
    local_engine = create_connection(LOCAL_CONFIG)
    if not local_engine:
        print("❌ Erro ao conectar ao banco local!")
        return
    
    # Conectar ao banco Azure
    print("☁️  Conectando ao Azure PostgreSQL...")
    azure_engine = create_connection(AZURE_CONFIG)
    if not azure_engine:
        print("❌ Erro ao conectar ao Azure PostgreSQL!")
        print("💡 Verifique se:")
        print("   - O banco foi criado no Azure")
        print("   - A senha está correta")
        print("   - O firewall permite sua conexão")
        print("   - Definiu a variável AZURE_DB_PASSWORD")
        return
    
    try:
        # Listar tabelas no banco local
        print("📋 Listando tabelas no banco local...")
        with local_engine.connect() as conn:
            result = conn.execute(text("SELECT tablename FROM pg_tables WHERE schemaname = 'public';"))
            tables = [row[0] for row in result]
        
        print(f"📊 Encontradas {len(tables)} tabelas: {tables}")
        
        # Migrar cada tabela
        for table in tables:
            print(f"📤 Migrando tabela: {table}")
            
            # Ler dados do banco local
            df = pd.read_sql_table(table, local_engine)
            print(f"   📦 {len(df)} registros encontrados")
            
            # Escrever no banco Azure
            df.to_sql(table, azure_engine, if_exists='replace', index=False)
            print(f"   ✅ Tabela {table} migrada com sucesso!")
        
        print("\n🎉 MIGRAÇÃO CONCLUÍDA!")
        print("🔗 String de conexão para Streamlit Cloud:")
        print(f"postgresql://{AZURE_CONFIG['user']}:{AZURE_CONFIG['password']}@{AZURE_CONFIG['host']}:{AZURE_CONFIG['port']}/{AZURE_CONFIG['database']}")
        
    except Exception as e:
        print(f"❌ Erro durante a migração: {e}")
    
    finally:
        local_engine.dispose()
        azure_engine.dispose()

def test_azure_connection():
    """Testar conexão com Azure"""
    print("🔍 Testando conexão com Azure PostgreSQL...")
    
    engine = create_connection(AZURE_CONFIG)
    if not engine:
        return False
    
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            version = result.fetchone()[0]
            print(f"✅ Conexão bem-sucedida!")
            print(f"📋 Versão: {version}")
            return True
    except Exception as e:
        print(f"❌ Erro na conexão: {e}")
        return False
    finally:
        engine.dispose()

if __name__ == "__main__":
    print("=" * 50)
    print("  MIGRAÇÃO PARA AZURE POSTGRESQL")
    print("=" * 50)
    
    # Verificar se a senha foi definida
    if not AZURE_CONFIG['password']:
        print("❌ AZURE_DB_PASSWORD não definida!")
        print("💡 Defina a variável de ambiente:")
        print("   Windows: set AZURE_DB_PASSWORD=sua_senha")
        print("   ou crie arquivo .env com: AZURE_DB_PASSWORD=sua_senha")
        exit(1)
    
    # Testar conexão primeiro
    if test_azure_connection():
        # Fazer migração
        migrate_data()
    else:
        print("❌ Não foi possível conectar ao Azure. Verifique as configurações.")