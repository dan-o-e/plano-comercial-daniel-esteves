# 🗄️ CONFIGURAÇÃO DE BANCO DE DADOS

## 🆓 Opções de Banco PostgreSQL Gratuito:

### Opção 1: ElephantSQL (RECOMENDADO)
1. **Acesse:** https://www.elephantsql.com
2. **Cadastre-se** gratuitamente
3. **Crie nova instância:**
   - Plan: Tiny Turtle (Free)
   - Name: plano-comercial-daniel
   - Region: US-East-1
4. **Copie as credenciais** da página de detalhes

### Opção 2: Supabase
1. **Acesse:** https://supabase.com
2. **Crie novo projeto**
3. **Vá em Settings > Database**
4. **Copie connection string**

### Opção 3: Railway
1. **Acesse:** https://railway.app
2. **Crie projeto**
3. **Adicione PostgreSQL**
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
host = "seu-host-elephantsql.com"
port = 5432
user = "seu_usuario"
password = "sua_senha_super_secreta"
database = "seu_usuario"
```

5. **Clique em "Save"**
6. **App será reiniciado automaticamente**

## ✅ Pronto!
Sua aplicação estará funcionando em: https://esteves.streamlit.app