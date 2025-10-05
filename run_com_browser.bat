@echo off
echo ========================================
echo   PLANO COMERCIAL DANIEL ESTEVES
echo ========================================
echo.
echo 🚀 Abrindo navegador automaticamente...
echo.

REM Aguardar alguns segundos e abrir o navegador
timeout /t 3 /nobreak >nul
start http://localhost:8501

REM Executar Streamlit
echo ⚡ Iniciando servidor Streamlit...
python -m streamlit run streamlit_app.py --server.headless=false --server.runOnSave=true

pause