# 📊 Plano Comercial Daniel Esteves - Guia Completo

## 🚀 Início Rápido

### **Execução Local:**
```bash
# Instalar dependências (primeira vez)
pip install -r requirements.txt

# Executar aplicação
python -m streamlit run streamlit_app.py --server.headless=false

# Ou usar o script automatizado
run.bat
```

### **Importar dados (primeira vez):**
```bash
python import_excel_to_postgres.py
```

### **Acessar:** http://localhost:8501

---

## 📋 Pré-requisitos

- Python 3.7+
- PostgreSQL rodando em localhost:5433
- Credenciais: postgres/postgres
- Base de dados: base_btg

---

## 🌐 Deploy na Web

### **Opção 1: Streamlit Cloud (Gratuito)**
1. Repositório já está no GitHub: `dan-o-e/plano-comercial-daniel-esteves`
2. Acesse: https://share.streamlit.io
3. Configure:
   - Repository: `dan-o-e/plano-comercial-daniel-esteves`
   - Branch: `main`
   - Main file: `streamlit_app.py`

### **Opção 2: Supabase + Streamlit Cloud**
1. Crie conta no Supabase: https://supabase.com
2. Novo projeto → PostgreSQL gratuito
3. Migre dados: `python migrate_to_supabase.py`
4. Configure secrets no Streamlit Cloud

### **Secrets do Streamlit Cloud:**
```toml
[connections.postgresql]
dialect = "postgresql"
host = "SEU_HOST"
port = "5432"
database = "postgres"
username = "postgres"
password = "SUA_SENHA"
```

---

## 🔧 Troubleshooting

### **Erro de conexão com banco:**
- Verificar se PostgreSQL está rodando
- Confirmar porta 5433
- Testar credenciais postgres/postgres

### **Streamlit não abre navegador:**
```bash
python -m streamlit run streamlit_app.py --server.headless=false
```

### **Warnings normais (ignorar):**
- `"general.email" is not a valid config option` ✅ OK
- `Failed to schedule watch observer` ✅ OK  
- `server.enableCORS warnings` ✅ OK

### **Módulos não encontrados:**
```bash
pip install -r requirements.txt
```

---

## 📊 Funcionalidades

- ✅ Dashboard interativo com gráficos
- ✅ Lista de captação de clientes editável
- ✅ Cálculos automáticos de metas
- ✅ Filtros por período e status
- ✅ Exportação para Excel
- ✅ Visualizações com Plotly
- ✅ Responsivo para mobile

---

## 🗂️ Estrutura do Projeto

```
📁 plano-comercial-daniel-esteves/
├── 📄 streamlit_app.py          # Aplicação principal
├── 📄 import_excel_to_postgres.py # Import de dados
├── 📄 requirements.txt          # Dependências Python
├── 📄 README.md                # Documentação
├── 📄 run.bat                  # Script de execução
├── 📁 .streamlit/
│   └── 📄 config.toml          # Configuração Streamlit
├── 📊 Base BTG.xlsx            # Dados originais
└── 📊 Plano Comercial_Daniel_Esteves.xlsx # Planilha de trabalho
```

---

## 💡 Dicas

### **Desenvolvimento Local:**
- Use `run.bat` para execução rápida
- Dados ficam no PostgreSQL local
- Auto-reload ao salvar arquivos

### **Deploy Produção:**
- Supabase é mais fácil que Azure
- Streamlit Cloud é gratuito
- Railway como alternativa ($5/mês)

### **Dados:**
- 57 registros importados do Excel
- Estrutura otimizada para PostgreSQL
- Backup automático no Git

---

## 📞 Suporte

Para problemas:
1. Verificar se PostgreSQL está rodando
2. Conferir se dados foram importados
3. Testar conexão: `python import_excel_to_postgres.py`
4. Logs do Streamlit para debug

---

## 🎯 Comandos Rápidos

```bash
# Instalar e executar (primeira vez)
pip install -r requirements.txt
python import_excel_to_postgres.py
python -m streamlit run streamlit_app.py --server.headless=false

# Executar (próximas vezes)
python -m streamlit run streamlit_app.py --server.headless=false

# Ou simplesmente
run.bat
```