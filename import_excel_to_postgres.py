import pandas as pd
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine, text
import sys
import os
import re

# Configurações de conexão
DB_CONFIG = {
    'host': 'localhost',
    'port': 5433,
    'user': 'postgres',
    'password': 'postgres',
    'database': 'base_btg'
}

def create_database_if_not_exists():
    """Cria o banco de dados se ele não existir"""
    try:
        # Conecta ao PostgreSQL (banco padrão 'postgres')
        conn = psycopg2.connect(
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database='postgres'
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        # Verifica se o banco existe
        cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (DB_CONFIG['database'],))
        exists = cursor.fetchone()
        
        if not exists:
            # Cria o banco de dados
            cursor.execute(f"CREATE DATABASE {DB_CONFIG['database']}")
            print(f"Banco de dados '{DB_CONFIG['database']}' criado com sucesso!")
        else:
            print(f"Banco de dados '{DB_CONFIG['database']}' já existe.")
            
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"Erro ao criar banco de dados: {e}")
        sys.exit(1)

def get_engine():
    """Cria conexão SQLAlchemy com o banco de dados"""
    connection_string = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    return create_engine(connection_string)

def clean_column_names(df):
    """Limpa os nomes das colunas para serem compatíveis com PostgreSQL"""
    df.columns = df.columns.str.strip()  # Remove espaços
    df.columns = df.columns.str.lower()  # Converte para minúsculas
    df.columns = df.columns.str.replace(' ', '_', regex=False)  # Substitui espaços por underscore
    df.columns = df.columns.str.replace('[^a-z0-9_]', '', regex=True)  # Remove caracteres especiais
    return df

def import_excel_to_postgres(excel_file):
    """Importa dados do Excel para PostgreSQL"""
    try:
        # Verifica se o arquivo existe
        if not os.path.exists(excel_file):
            print(f"Arquivo não encontrado: {excel_file}")
            return
        
        print(f"Lendo arquivo Excel: {excel_file}")
        
        # Lê todas as abas do Excel
        excel_data = pd.read_excel(excel_file, sheet_name=None)
        
        # Cria conexão com o banco
        engine = get_engine()
        
        # Processa cada aba
        for sheet_name, df in excel_data.items():
            if df.empty:
                print(f"Aba '{sheet_name}' está vazia, pulando...")
                continue
                
            print(f"Processando aba: {sheet_name}")
            print(f"Dimensões: {df.shape[0]} linhas x {df.shape[1]} colunas")
            
            # Limpa os nomes das colunas
            df = clean_column_names(df)
            
            # Remove linhas completamente vazias
            df = df.dropna(how='all')
            
            # Nome da tabela baseado no nome da aba
            table_name = sheet_name.lower().replace(' ', '_')
            table_name = re.sub(r'[^a-z0-9_]', '', table_name)
            
            print(f"Criando tabela: {table_name}")
            print(f"Colunas: {list(df.columns)}")
            
            # Insere os dados na tabela
            df.to_sql(
                table_name, 
                engine, 
                if_exists='replace',  # Substitui a tabela se ela já existir
                index=False,
                method='multi'
            )
            
            print(f"✓ Dados da aba '{sheet_name}' inseridos na tabela '{table_name}' com sucesso!")
            print(f"  Total de registros inseridos: {len(df)}")
            print("-" * 50)
        
        print("Importação concluída com sucesso!")
        
        # Mostra resumo das tabelas criadas
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT table_name, 
                       (SELECT COUNT(*) FROM information_schema.columns 
                        WHERE table_name = t.table_name) as num_columns
                FROM information_schema.tables t
                WHERE table_schema = 'public'
                ORDER BY table_name
            """))
            
            print("\nResumo das tabelas criadas:")
            for row in result:
                # Conta registros na tabela
                count_result = conn.execute(text(f"SELECT COUNT(*) FROM {row[0]}"))
                count = count_result.scalar()
                print(f"  - {row[0]}: {count} registros, {row[1]} colunas")
        
    except Exception as e:
        print(f"Erro durante a importação: {e}")
        raise

def test_connection():
    """Testa a conexão com o banco de dados"""
    try:
        engine = get_engine()
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version()"))
            version = result.scalar()
            print(f"Conexão bem-sucedida! PostgreSQL Version: {version}")
            return True
    except Exception as e:
        print(f"Erro na conexão: {e}")
        return False

def main():
    """Função principal"""
    print("=== Importador Excel para PostgreSQL ===")
    print(f"Conectando em: {DB_CONFIG['host']}:{DB_CONFIG['port']}")
    print(f"Banco de dados: {DB_CONFIG['database']}")
    print("-" * 50)
    
    # Cria o banco de dados se não existir
    create_database_if_not_exists()
    
    # Testa a conexão
    if not test_connection():
        print("Falha na conexão. Verifique as configurações.")
        sys.exit(1)
    
    # Caminho do arquivo Excel
    excel_file = "Base BTG.xlsx"
    
    # Verifica se está no diretório correto
    if not os.path.exists(excel_file):
        excel_file = os.path.join(os.path.dirname(__file__), excel_file)
    
    # Importa os dados
    import_excel_to_postgres(excel_file)

if __name__ == "__main__":
    main()