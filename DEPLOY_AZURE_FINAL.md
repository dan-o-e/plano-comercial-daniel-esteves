# 🚀 DEPLOY FINAL - AZURE + STREAMLIT CLOUD

## Passo a Passo Completo

### ✅ ETAPA 1: FINALIZAR AZURE POSTGRESQL

1. **Complete a criação do banco no Azure** (se ainda não terminou)
2. **Anote as informações:**
   - Host: `plano-comercial-daniel.postgres.database.azure.com`
   - Port: `5432`
   - Database: `postgres`
   - Username: `postgres`
   - Password: [sua senha]

### ✅ ETAPA 2: MIGRAR DADOS PARA AZURE

1. **Execute o script de migração:**
   ```bash
   migrate_azure.bat
   ```

2. **Digite a senha do Azure** quando solicitado

3. **Aguarde a migração** (pode demorar alguns minutos)

4. **Copie a string de conexão** que aparecerá no final

### ✅ ETAPA 3: DEPLOY NO STREAMLIT CLOUD

1. **Acesse:** https://share.streamlit.io

2. **Faça login** com sua conta GitHub

3. **Clique em "New app"**

4. **Configure:**
   - Repository: `dan-o-e/plano-comercial-daniel-esteves`
   - Branch: `main`
   - Main file path: `streamlit_app.py`

5. **Em "Advanced settings" → "Secrets"**, adicione:
   ```toml
   [connections.postgresql]
   dialect = "postgresql"
   host = "plano-comercial-daniel.postgres.database.azure.com"
   port = "5432"  
   database = "postgres"
   username = "postgres"
   password = "SUA_SENHA_AZURE"
   ```

6. **Clique em "Deploy!"**

### ✅ ETAPA 4: CONFIGURAR FIREWALL AZURE

Depois do deploy, você pode precisar adicionar o IP do Streamlit Cloud no firewall:

1. **No Azure Portal**, vá para seu PostgreSQL
2. **Connection security** → **Firewall rules**
3. **Adicione regra:**
   - Nome: `Streamlit-Cloud`
   - IP inicial: `0.0.0.0`
   - IP final: `255.255.255.255`
   
   **(Temporário para teste - depois restringir)**

### 🎉 RESULTADO FINAL

Após completar todos os passos:

- ✅ **Banco Azure PostgreSQL** funcionando
- ✅ **Dados migrados** do local para nuvem
- ✅ **App Streamlit** rodando na web
- ✅ **URL pública** para acesso

### 🔧 TROUBLESHOOTING

**Se der erro de conexão:**
1. Verifique se o firewall do Azure permite conexões
2. Confirme se a senha está correta nos secrets
3. Teste a conexão com: `python migrate_to_azure.py`

**Se a migração falhar:**
1. Execute `migrate_azure.bat` novamente
2. Verifique se o banco local está rodando
3. Confirme se as credenciais do Azure estão corretas

**Se o Streamlit der erro:**
1. Verifique os logs no Streamlit Cloud
2. Confirme se os secrets estão configurados
3. Verifique se requirements.txt está atualizado

### 📞 SUPORTE

Se precisar de ajuda, execute:
```bash
python migrate_to_azure.py
```

Para testar apenas a conexão com Azure.