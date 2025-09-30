# Plano Comercial Daniel Esteves

Este projeto importa dados do arquivo `Base BTG.xlsx` para um banco de dados PostgreSQL e apresenta um dashboard interativo para análise comercial.

## Configuração

### Pré-requisitos
- Python 3.7 ou superior
- PostgreSQL rodando em localhost:5433
- Usuário: postgres / Senha: postgres

### Instalação das Dependências

Execute o arquivo batch:
```
install_dependencies.bat
```

Ou instale manualmente:
```bash
pip install -r requirements.txt
```

## Como Usar

1. Certifique-se de que o arquivo `Base BTG.xlsx` está no mesmo diretório do script
2. Execute o script:
```bash
python import_excel_to_postgres.py
```

## O que o código faz

1. **Conecta ao PostgreSQL** usando as credenciais fornecidas
2. **Cria o banco de dados** `base_btg` se ele não existir
3. **Lê todas as abas** do arquivo Excel `Base BTG.xlsx`
4. **Limpa os nomes das colunas** para serem compatíveis com PostgreSQL:
   - Remove espaços extras
   - Converte para minúsculas
   - Substitui espaços por underscores
   - Remove caracteres especiais
5. **Cria tabelas** no banco baseadas no nome das abas
6. **Insere os dados** de cada aba na respectiva tabela
7. **Mostra um resumo** das tabelas criadas e quantos registros foram inseridos

## Configurações do Banco

```python
DB_CONFIG = {
    'host': 'localhost',
    'port': 5433,
    'user': 'postgres',
    'password': 'postgres',
    'database': 'base_btg'
}
```

## Estrutura de Arquivos

- `import_excel_to_postgres.py` - Script de importação dos dados
- `streamlit_app.py` - Aplicação web Streamlit
- `view_data.py` - Script para visualizar dados do banco
- `requirements.txt` - Dependências Python
- `install_dependencies.bat` - Script de instalação
- `run_streamlit.bat` - Script para executar o Streamlit
- `Base BTG.xlsx` - Arquivo Excel com os dados
- `README.md` - Este arquivo

## Como Executar Localmente

### 1. Importar os dados (apenas na primeira vez):
```bash
python import_excel_to_postgres.py
```

### 2. Executar a aplicação Streamlit:

**Opção A - Script simples (RECOMENDADO):**
```
run_simple.bat
```

**Opção B - Comando direto:**
```bash
streamlit run streamlit_app.py
```

**Opção C - Script completo:**
```
run_local.bat
```

### 3. Acessar no navegador:
- **URL:** http://localhost:8501
- **Para parar:** Pressione `Ctrl+C` no terminal

### ⚠️ Resolução de Problemas Locais:
- Se houver erro de configuração, use `run_simple.bat`
- Certifique-se de que o PostgreSQL está rodando
- Verifique se todas as dependências estão instaladas

## 🌐 Como Disponibilizar na Web para Outras Pessoas

### Opção 1: Streamlit Cloud (GRATUITO e RECOMENDADO)

1. **Criar conta no GitHub** (se não tiver):
   - Acesse https://github.com
   - Crie uma conta gratuita

2. **Fazer upload do projeto para GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Primeira versão do Plano Comercial BTG"
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/plano-comercial-btg.git
   git push -u origin main
   ```

3. **Deploy no Streamlit Cloud**:
   - Acesse https://share.streamlit.io
   - Faça login com sua conta GitHub
   - Clique em "New app"
   - Selecione seu repositório
   - Configure:
     - Repository: `SEU_USUARIO/plano-comercial-btg`
     - Branch: `main`
     - Main file path: `streamlit_app.py`
   - Clique em "Deploy!"

4. **Configurar variáveis de ambiente** (se necessário):
   - Na página do deploy, vá em "Settings"
   - Adicione as configurações do banco PostgreSQL

### Opção 2: Heroku (GRATUITO com limitações)

1. **Instalar Heroku CLI**:
   - Download: https://devcenter.heroku.com/articles/heroku-cli

2. **Criar arquivos necessários**:
   - `Procfile`
   - `setup.sh`
   - Atualizar `requirements.txt`

3. **Deploy**:
   ```bash
   heroku create seu-app-name
   git push heroku main
   ```

### Opção 3: Railway (FÁCIL e RÁPIDO)

1. **Acesse https://railway.app**
2. **Conecte com GitHub**
3. **Selecione seu repositório**
4. **Deploy automático**

### Opção 4: Render (GRATUITO)

1. **Acesse https://render.com**
2. **Conecte com GitHub**
3. **Crie um novo Web Service**
4. **Configure o ambiente**

### Opção 5: AWS/Azure/Google Cloud (PAGO)

Para uso empresarial com maior controle e recursos.

### ⚠️ IMPORTANTE - Configuração do Banco de Dados

Para produção, você precisará de um banco PostgreSQL na nuvem:

**Opções gratuitas:**
- **ElephantSQL** (PostgreSQL gratuito)
- **Supabase** (PostgreSQL com interface)
- **Railway** (PostgreSQL incluído)
- **Render** (PostgreSQL gratuito)

**Configuração:**
```python
# No streamlit_app.py, usar variáveis de ambiente
import os

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', 5433),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'postgres'),
    'database': os.getenv('DB_NAME', 'base_btg')
}
```

## Troubleshooting

### Erro de conexão
- Verifique se o PostgreSQL está rodando
- Confirme se as credenciais estão corretas
- Verifique se a porta 5433 está disponível

### Erro no arquivo Excel
- Certifique-se de que o arquivo `Base BTG.xlsx` existe
- Verifique se o arquivo não está aberto em outro programa
- Confirme se o arquivo não está corrompido

### Erro de dependências
- Execute `pip install --upgrade pip` antes de instalar as dependências
- Se usar Python virtual environment, ative-o antes da instalação