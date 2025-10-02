# 🚀 GUIA SUPABASE - Banco PostgreSQL Gratuito

## ⭐ Por que Supabase?
- ✅ **500MB gratuito** (muito generoso)
- ✅ **50.000 usuários mensais**
- ✅ **Interface web linda** para gerenciar dados
- ✅ **API automática** para seus dados
- ✅ **Backup automático**
- ✅ **Sem limite de tempo** (sempre gratuito)

## 📋 Passo a Passo:

### 1. Criar Conta
1. Acesse: https://supabase.com
2. Clique em "Start your project"
3. Entre com GitHub (recomendado)

### 2. Criar Projeto
1. Clique em "New Project"
2. Preencha:
   - **Name:** plano-comercial-daniel
   - **Database Password:** [crie uma senha forte]
   - **Region:** East US (Virginia) - mais rápido
3. Clique em "Create new project"
4. Aguarde 2-3 minutos (criação do banco)

### 3. Obter Credenciais
1. No painel do projeto, vá em **Settings**
2. Clique em **Database**
3. Na seção "Connection info", você verá:
   - **Host:** db.xxxxxxxxxxxxx.supabase.co
   - **Database name:** postgres
   - **Port:** 5432
   - **User:** postgres
   - **Password:** [a senha que você criou]

### 4. Testar Conexão Local
Edite o arquivo `import_excel_to_postgres.py`:

```python
DB_CONFIG = {
    'host': 'db.xxxxxxxxxxxxx.supabase.co',  # Substitua pelos seus dados
    'port': 5432,
    'user': 'postgres',
    'password': 'sua_senha_forte',
    'database': 'postgres'
}
```

Execute: `python import_excel_to_postgres.py`

### 5. Configurar no Streamlit Cloud
No Streamlit Cloud → Settings → Secrets:

```toml
[database]
host = "db.xxxxxxxxxxxxx.supabase.co"
port = 5432
user = "postgres"
password = "sua_senha_forte"
database = "postgres"
```

## 🎯 Vantagens do Supabase:

### Interface Web
- **Table Editor:** Visualize e edite dados direto no navegador
- **SQL Editor:** Execute queries SQL
- **API Explorer:** API REST automática

### Recursos Extras
- **Real-time:** Dados em tempo real
- **Storage:** Armazenamento de arquivos
- **Auth:** Sistema de autenticação
- **Edge Functions:** Funções serverless

## 🔧 Troubleshooting:

### Erro de Conexão
- Verifique se copiou o host correto (com db. no início)
- Confirme a senha
- Teste conexão no SQL Editor do Supabase primeiro

### Importação Lenta
- Normal na primeira vez
- Supabase pode levar alguns segundos para "acordar"

### Limites
- **500MB de dados** (muito para seu projeto)
- **Pause após 7 dias de inatividade** (reactiva automaticamente)

## ✅ Resultado Final
Banco PostgreSQL profissional e gratuito, com interface web moderna e todas as credenciais prontas para usar no Streamlit Cloud!

## 🌟 Dica Extra
No painel do Supabase você pode:
- Ver seus dados em tabelas
- Fazer backup manual
- Monitorar uso
- Executar SQL direto no navegador