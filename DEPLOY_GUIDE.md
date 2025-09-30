# 🚀 Guia Completo de Deploy - Plano Comercial Daniel Esteves

## 📋 Pré-requisitos
- Conta no GitHub
- Arquivo Excel com dados
- Banco PostgreSQL (pode ser na nuvem)

## 🌟 Opção 1: Streamlit Cloud (RECOMENDADO - GRATUITO)

### Passo 1: Preparar o Projeto
```bash
# 1. Inicializar repositório Git
git init

# 2. Adicionar arquivos
git add .

# 3. Fazer primeiro commit
git commit -m "Initial commit - Plano Comercial Daniel Esteves"

# 4. Conectar com GitHub (substitua SEU_USUARIO pelo seu username)
git remote add origin https://github.com/SEU_USUARIO/plano-comercial-daniel-esteves.git

# 5. Enviar para GitHub
git branch -M main
git push -u origin main
```

### Passo 2: Deploy no Streamlit Cloud
1. Acesse [share.streamlit.io](https://share.streamlit.io)
2. Faça login com sua conta GitHub
3. Clique em "New app"
4. Preencha:
   - **Repository**: `SEU_USUARIO/plano-comercial-daniel-esteves`
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py`
5. Clique em "Deploy!"

### Passo 3: Configurar Banco de Dados
1. Na página do app, clique em "Settings"
2. Vá para "Secrets"
3. Adicione as configurações do banco:

```toml
[database]
host = "seu-host-do-banco.com"
port = 5432
user = "seu_usuario"
password = "sua_senha"
database = "nome_do_banco"
```

## 🐘 Configurar Banco PostgreSQL na Nuvem

### Opção A: ElephantSQL (Gratuito)
1. Acesse [elephantsql.com](https://www.elephantsql.com)
2. Crie conta gratuita
3. Crie nova instância
4. Copie as credenciais de conexão

### Opção B: Supabase (Gratuito)
1. Acesse [supabase.com](https://supabase.com)
2. Crie novo projeto
3. Vá em Settings > Database
4. Copie connection string

### Opção C: Railway (Gratuito)
1. Acesse [railway.app](https://railway.app)
2. Crie novo projeto
3. Adicione PostgreSQL
4. Copie credenciais

## 📊 Importar Dados para o Banco na Nuvem

### Método 1: Adaptar Script Python
```python
# Edite import_excel_to_postgres.py com as novas credenciais
DB_CONFIG = {
    'host': 'SEU_HOST_NA_NUVEM',
    'port': 5432,
    'user': 'SEU_USUARIO',
    'password': 'SUA_SENHA',
    'database': 'SEU_BANCO'
}

# Execute o script
python import_excel_to_postgres.py
```

### Método 2: Upload Manual via Interface Web
- Muitos provedores oferecem interface para upload de dados
- Use o arquivo Excel diretamente

## 🎯 Opção 2: Railway (Simples e Rápido)

1. Acesse [railway.app](https://railway.app)
2. Conecte com GitHub
3. Selecione seu repositório
4. Railway detecta automaticamente o Streamlit
5. Adicione PostgreSQL como serviço
6. Configure variáveis de ambiente

## 🔧 Opção 3: Render (Gratuito)

1. Acesse [render.com](https://render.com)
2. Conecte com GitHub
3. Crie "New Web Service"
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0`
5. Adicione PostgreSQL separadamente

## 💡 Opção 4: Heroku

```bash
# 1. Instalar Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# 2. Login
heroku login

# 3. Criar app
heroku create seu-app-name

# 4. Adicionar PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# 5. Deploy
git push heroku main
```

## 🔐 Configurações de Segurança

### Para Streamlit Cloud:
- Use a seção "Secrets" no painel
- Nunca coloque senhas no código

### Para outras plataformas:
```bash
# Configurar variáveis de ambiente
export DB_HOST="seu_host"
export DB_PORT="5432"
export DB_USER="seu_usuario"
export DB_PASSWORD="sua_senha"
export DB_NAME="seu_banco"
```

## 🚨 Troubleshooting

### Erro de Conexão com Banco
- Verifique se o banco aceita conexões externas
- Confirme se as credenciais estão corretas
- Teste a conexão localmente primeiro

### App não carrega
- Verifique os logs na plataforma
- Confirme se todos os arquivos foram enviados
- Teste localmente antes do deploy

### Problemas de Dependências
- Mantenha `requirements.txt` atualizado
- Use versões específicas dos packages

## 📱 Compartilhar com Usuários

Após o deploy, você receberá uma URL como:
- Streamlit Cloud: `https://seu-app.streamlit.app`
- Railway: `https://seu-app.up.railway.app`
- Render: `https://seu-app.onrender.com`
- Heroku: `https://seu-app.herokuapp.com`

## 🔄 Atualizações

Para atualizar a aplicação:
```bash
# 1. Fazer mudanças no código
# 2. Commit das mudanças
git add .
git commit -m "Atualização da aplicação"

# 3. Push para GitHub
git push

# A aplicação será atualizada automaticamente!
```

## 📞 Suporte

Se precisar de ajuda:
1. Verifique os logs da plataforma
2. Teste localmente primeiro
3. Consulte a documentação da plataforma escolhida