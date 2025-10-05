# 📊 Plano Comercial Daniel Esteves

Dashboard interativo para análise do plano comercial com dados importados do Excel para PostgreSQL.

## 🚀 Início Rápido

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Importar dados (primeira vez)
python import_excel_to_postgres.py

# 3. Executar aplicação
run.bat
```

**Acesse:** http://localhost:8501

## 📋 Pré-requisitos

- Python 3.7+
- PostgreSQL (localhost:5433, user: postgres, password: postgres)

## 🌐 Deploy na Web

1. **Streamlit Cloud:** https://share.streamlit.io
2. **Repositório:** `dan-o-e/plano-comercial-daniel-esteves`
3. **Main file:** `streamlit_app.py`

Para detalhes completos, veja: `GUIA_COMPLETO.md`

## 📊 Funcionalidades

- ✅ Dashboard com gráficos interativos
- ✅ Lista de captação editável
- ✅ Cálculos automáticos
- ✅ Filtros e exportação
- ✅ 57 registros importados

## 🗂️ Arquivos Principais

```python
streamlit_app.py          # Aplicação principal
import_excel_to_postgres.py # Import de dados
run.bat                   # Execução automática
requirements.txt          # Dependências
GUIA_COMPLETO.md         # Documentação detalhada
    'host': 'localhost',

- Verifique se o arquivo não está aberto em outro programa
- Confirme se o arquivo não está corrompido

### Erro de dependências
- Execute `pip install --upgrade pip` antes de instalar as dependências
- Se usar Python virtual environment, ative-o antes da instalação
