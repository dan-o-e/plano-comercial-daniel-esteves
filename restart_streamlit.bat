@echo off
echo Parando aplicacao Streamlit anterior...
taskkill /f /im python.exe 2>nul
timeout /t 2 /nobreak >nul

echo Reiniciando aplicacao Streamlit...
echo.
echo Acesse: http://localhost:8501
echo.
echo Para parar a aplicacao, pressione Ctrl+C
echo.
C:/Users/danie/AppData/Local/Programs/Python/Python313/python.exe -m streamlit run streamlit_app.py