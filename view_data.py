import pandas as pd
from sqlalchemy import create_engine, text
import sys

# Configurações de conexão (mesmas do script de importação)
DB_CONFIG = {
    'host': 'localhost',
    'port': 5433,
    'user': 'postgres',
    'password': 'postgres',
    'database': 'base_btg'
}

def get_engine():
    """Cria conexão SQLAlchemy com o banco de dados"""
    connection_string = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    return create_engine(connection_string)

def show_first_10_rows():
    """Mostra as 10 primeiras linhas da tabela export"""
    try:
        engine = get_engine()
        
        # Busca as 10 primeiras linhas
        query = "SELECT * FROM export LIMIT 10"
        df = pd.read_sql(query, engine)
        
        print("=== 10 PRIMEIRAS LINHAS DA TABELA 'export' ===")
        print(f"Total de colunas: {len(df.columns)}")
        print(f"Registros mostrados: {len(df)}")
        print("-" * 80)
        
        # Configura pandas para mostrar todas as colunas
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', 50)
        
        print(df)
        
        print("-" * 80)
        print("\n=== INFORMAÇÕES DAS COLUNAS ===")
        for i, col in enumerate(df.columns, 1):
            print(f"{i:2d}. {col}")
            
    except Exception as e:
        print(f"Erro ao consultar o banco: {e}")
        sys.exit(1)

def show_sample_data():
    """Mostra dados amostrais de algumas colunas principais"""
    try:
        engine = get_engine()
        
        # Seleciona algumas colunas principais para melhor visualização
        query = """
        SELECT 
            conta,
            nome,
            assessor,
            tipo_parceiro,
            cidade,
            estado,
            pl_total,
            aportes,
            data_de_abertura
        FROM export 
        LIMIT 10
        """
        
        df = pd.read_sql(query, engine)
        
        print("\n=== DADOS PRINCIPAIS (10 PRIMEIRAS LINHAS) ===")
        print("-" * 120)
        
        # Formatação melhor para visualização
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 120)
        pd.set_option('display.max_colwidth', 20)
        
        print(df.to_string(index=False))
        
    except Exception as e:
        print(f"Erro ao consultar dados principais: {e}")

if __name__ == "__main__":
    show_first_10_rows()
    show_sample_data()