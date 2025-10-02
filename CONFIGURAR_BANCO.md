# 🗄️ CONFIGURAÇÃO DE BANCO DE DADOS

## 🆓 Opções de Banco PostgreSQL Gratuito:

### Opção 1: Supabase (RECOMENDADO - Mais Generoso)
1. **Acesse:** https://supabase.com
2. **Cadastre-se** gratuitamente
3. **Crie novo projeto:**
   - Name: plano-comercial-daniel
   - Password: [escolha uma senha forte]
   - Region: East US (Virginia)
4. **Vá em Settings > Database**
5. **Copie as credenciais de conexão**

### Opção 2: Neon (Muito Rápido)
1. **Acesse:** https://neon.tech
2. **Cadastre-se** com GitHub
3. **Crie novo projeto**
4. **Copie connection string**

### Opção 3: Railway (PostgreSQL Incluído)
1. **Acesse:** https://railway.app
2. **Crie projeto**
3. **Adicione PostgreSQL**
4. **Copie credenciais**

### Opção 4: Azure Database for PostgreSQL (Enterprise)
1. **Acesse:** https://azure.microsoft.com/free
2. **$200 créditos grátis** por 30 dias
3. **Flexible Server B1ms:** ~$15/mês após créditos
4. **Alta disponibilidade e backup automático**

### Opção 5: Render (Alternativa Sólida)
1. **Acesse:** https://render.com
2. **Crie PostgreSQL database**
3. **Plan: Free (90 dias, depois $7/mês)**
4. **Copie credenciais**

## 📊 Importar Dados para o Banco na Nuvem:

### Método 1: Editar Script Local
1. **Edite o arquivo:** `import_excel_to_postgres.py`
2. **Substitua as credenciais:**

```python
DB_CONFIG = {
    'host': 'SEU_HOST_DA_NUVEM',
    'port': 5432,
    'user': 'SEU_USUARIO',
    'password': 'SUA_SENHA',
    'database': 'SEU_BANCO'
}
```

3. **Execute:** `python import_excel_to_postgres.py`

## ⚙️ Configurar no Streamlit Cloud:

1. **Na página do seu app no Streamlit Cloud:**
2. **Clique em "Settings"**
3. **Vá para "Secrets"**
4. **Adicione:**

```toml
[database]
host = "db.xxxxxxxxxxxxx.supabase.co"
port = 5432
user = "postgres"
password = "sua_senha_super_secreta"
database = "postgres"
```

5. **Clique em "Save"**
6. **App será reiniciado automaticamente**

## ✅ Pronto!
Sua aplicação estará funcionando em: https://esteves.streamlit.app