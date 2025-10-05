# 💻 Execução Local - Guia Rápido

## ✅ SIM! Você pode executar localmente normalmente!

### 🚀 Formas de Executar:

#### **Opção 1 - Mais Simples:**
```bash
python -m streamlit run streamlit_app.py
```

#### **Opção 2 - Script Automatizado:**
```
run_simple.bat
```

#### **Opção 3 - Com tratamento de erros:**
```
run_local.bat
```

### 🌐 Acessar:
- **URL Principal:** http://localhost:8501
- **URL Alternativa:** http://localhost:8503 (se 8501 estiver ocupada)

### ⚙️ Pré-requisitos:
1. **PostgreSQL rodando** (localhost:5433)
2. **Dados importados** (execute `python import_excel_to_postgres.py` uma vez)
3. **Dependências instaladas** (`pip install -r requirements.txt`)

### ⚠️ Ignorar Warnings:
Os warnings que aparecem são normais e **NÃO afetam o funcionamento**:
- `"general.email" is not a valid config option` ✅ OK - Opção removida em versões recentes
- `Warning: the config option 'server.enableCORS=false'` ✅ OK - Ajuste automático de segurança
- `Failed to schedule watch observer` ✅ OK - Problema conhecido Python 3.13 + Windows
- `TypeError: 'handle' must be a _ThreadHandle` ✅ OK - Não afeta o funcionamento

### 🔧 Troubleshooting:

**Problema:** Erro de conexão com banco
**Solução:** Verificar se PostgreSQL está rodando na porta 5433

**Problema:** Porta ocupada
**Solução:** Usar porta diferente: `python -m streamlit run streamlit_app.py --server.port=8504`

**Problema:** Módulos não encontrados
**Solução:** `pip install -r requirements.txt`

### 📊 Funcionalidades Locais:
- ✅ Todas as funcionalidades funcionam igual
- ✅ Lista de clientes editável
- ✅ Gráficos interativos
- ✅ Exportação para Excel
- ✅ Cálculos automáticos
- ✅ Filtros da sidebar

### 🌐 Diferença Local vs Web:
- **Local:** Dados do seu PostgreSQL local
- **Web:** Dados de banco na nuvem (quando configurado)
- **Funcionalidade:** Idêntica em ambos

## ✨ Resumo:
**A aplicação funciona perfeitamente local E na web!** 
Você pode desenvolver localmente e depois fazer deploy quando quiser compartilhar.