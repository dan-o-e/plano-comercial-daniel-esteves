# ☁️ GUIA AZURE - PostgreSQL na Nuvem Microsoft

## 🏢 Azure Database for PostgreSQL

### ⭐ Vantagens do Azure:
- ✅ **Créditos gratuitos** ($200 por 30 dias)
- ✅ **12 meses grátis** para muitos serviços
- ✅ **Integração Microsoft** completa
- ✅ **Alta disponibilidade** (99.99% SLA)
- ✅ **Backup automático** por 35 dias
- ✅ **Segurança enterprise**
- ✅ **Suporte 24/7**

## 📋 Opções no Azure:

### Opção 1: Azure Database for PostgreSQL - Flexible Server
**Recomendado para Produção**
- **Burstable B1ms:** ~$12-15/mês
- **Compute + Storage separados**
- **Escalabilidade automática**
- **Melhor performance**

### Opção 2: Azure Database for PostgreSQL - Single Server
**Mais Simples (Deprecated em 2025)**
- **Basic B1:** ~$25/mês
- **Configuração mais simples**
- **Sendo descontinuado**

### Opção 3: Azure Container Instances + PostgreSQL
**Mais Barato para Desenvolvimento**
- **~$5-10/mês**
- **Container com PostgreSQL**
- **Ideal para testes**

## 🚀 Passo a Passo - Flexible Server:

### 1. Criar Conta Azure
1. Acesse: https://azure.microsoft.com/free
2. Cadastre-se (crédito de $200 grátis)
3. Entre no Portal: https://portal.azure.com

### 2. Criar PostgreSQL Flexible Server
1. No Portal Azure, clique **"Create a resource"**
2. Busque **"Azure Database for PostgreSQL"**
3. Selecione **"Flexible server"**
4. Clique **"Create"**

### 3. Configurar Servidor
**Basics:**
- **Subscription:** Free trial
- **Resource group:** plano-comercial-rg (criar novo)
- **Server name:** plano-comercial-daniel
- **Region:** East US (mais barato)
- **Version:** PostgreSQL 15
- **Workload type:** Development

**Compute + Storage:**
- **Compute tier:** Burstable
- **Compute size:** B1ms (1 vCore, 2GB RAM)
- **Storage:** 32 GB (mínimo)
- **Backup retention:** 7 days

**Authentication:**
- **Admin username:** postgres
- **Password:** [senha forte - anote!]

**Networking:**
- **Connectivity method:** Public access
- **Allow access from Azure services:** Yes
- **Add current client IP:** Yes

### 4. Após Criação
1. Anote o **Server name**: plano-comercial-daniel.postgres.database.azure.com
2. Vá em **Connection security**
3. Adicione sua regra de firewall (0.0.0.0 - 255.255.255.255 para acesso total)

### 5. Credenciais para Conectar
```python
DB_CONFIG = {
    'host': 'plano-comercial-daniel.postgres.database.azure.com',
    'port': 5432,
    'user': 'postgres',
    'password': 'sua_senha_forte',
    'database': 'postgres'
}
```

### 6. Configurar no Streamlit Cloud
```toml
[database]
host = "plano-comercial-daniel.postgres.database.azure.com"
port = 5432
user = "postgres"
password = "sua_senha_forte"
database = "postgres"
```

## 💰 Custos Estimados:

### Com Créditos Grátis
- **Primeiros 30 dias:** GRÁTIS ($200 de crédito)
- **B1ms:** ~$12/mês após créditos
- **Storage 32GB:** ~$3/mês
- **Total:** ~$15/mês após período gratuito

### Otimização de Custos
- **Parar servidor quando não usar**
- **Auto-pause:** Configure para pausar automaticamente
- **Monitoramento:** Use Azure Cost Management

## 🔧 Vantagens Específicas:

### Gerenciamento
- **Azure Portal:** Interface web completa
- **Azure CLI:** Automação via linha de comando
- **PowerShell:** Scripts de automação
- **ARM Templates:** Infraestrutura como código

### Monitoramento
- **Azure Monitor:** Métricas detalhadas
- **Alertas:** Notificações automáticas
- **Logs:** Auditoria completa
- **Performance Insights:** Otimização de queries

### Segurança
- **SSL/TLS obrigatório**
- **Firewall configurável**
- **Azure AD integration**
- **Private endpoints**

### Backup/Recovery
- **Backup automático diário**
- **Point-in-time recovery**
- **Geo-redundant backups**
- **Restore para novo servidor**

## 🎯 Alternativas Mais Baratas no Azure:

### Azure Container Instances
```bash
# Criar container PostgreSQL
az container create \
  --resource-group plano-comercial-rg \
  --name postgres-container \
  --image postgres:15 \
  --dns-name-label plano-comercial-db \
  --ports 5432 \
  --environment-variables POSTGRES_PASSWORD=sua_senha
```
**Custo:** ~$5-8/mês

### Azure App Service + PostgreSQL Add-on
- **App Service:** Para hospedar Streamlit também
- **PostgreSQL Add-on:** Banco integrado
- **Custo combinado:** ~$10-15/mês

## 🔍 Comparação Rápida:

| Serviço | Custo/Mês | Pros | Contras |
|---------|-----------|------|---------|
| **Supabase** | Grátis | Interface moderna, APIs | Limites mais restritivos |
| **Azure Flexible** | ~$15 | Enterprise, SLA 99.99% | Mais caro |
| **Azure Container** | ~$8 | Flexível, barato | Mais configuração |
| **Neon** | Grátis | Rápido, simples | Menos recursos |

## 🚀 Recomendação:

**Para Produção Séria:** Azure Database for PostgreSQL
**Para Desenvolvimento:** Supabase (gratuito)
**Para Economia:** Azure Container Instances

## 📞 Suporte:
- **Documentação:** https://docs.microsoft.com/azure/postgresql/
- **Suporte Azure:** Chat 24/7 disponível
- **Community:** Stack Overflow + Azure Forums