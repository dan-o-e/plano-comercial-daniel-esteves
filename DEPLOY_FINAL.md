# 🚀 GUIA FINAL - SEU DEPLOY EM 4 PASSOS

## ✅ Passo 1: GitHub
1. Acesse github.com
2. Crie repositório: "plano-comercial-daniel-esteves"
3. Execute: `upload_to_github.bat`
4. Envie arquivos com os comandos mostrados

## ✅ Passo 2: Streamlit Cloud  
1. Acesse: https://share.streamlit.io
2. Login com GitHub
3. "New app" → Selecione seu repositório
4. Main file: `streamlit_app.py`
5. Deploy!

## ✅ Passo 3: Banco de Dados
1. Crie conta no ElephantSQL (gratuito)
2. Crie instância PostgreSQL
3. Execute `import_excel_to_postgres.py` com as novas credenciais
4. Importe seus dados

## ✅ Passo 4: Configurar Secrets
1. No Streamlit Cloud → Settings → Secrets
2. Cole as credenciais do banco:
```toml
[database]
host = "seu-host.elephantsql.com"
port = 5432
user = "seu_usuario"
password = "sua_senha"
database = "seu_usuario"
```

## 🎯 RESULTADO:
Sua URL: **https://esteves.streamlit.app** (ou similar)

## 📁 Scripts Criados para Você:
- `upload_to_github.bat` - Para enviar ao GitHub
- `DEPLOY_CHECKLIST.md` - Lista de verificação
- `CONFIGURAR_BANCO.md` - Guia detalhado do banco

## 📞 Precisa de Ajuda?
Todos os guias detalhados estão nos arquivos .md criados!