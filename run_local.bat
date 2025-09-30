@echo off
echo ======================================
echo  PLANO COMERCIAL DANIEL ESTEVES
echo ======================================
echo.
echo Iniciando aplicacao localmente...
echo.
echo ACESSE NO NAVEGADOR:
echo http://localhost:8501
echo.
echo Para parar: Pressione Ctrl+C
echo ======================================
echo.

REM Remove arquivo de config problemático temporariamente
if exist .streamlit\config.toml (
    ren .streamlit\config.toml config.toml.bak
)

REM Executa o streamlit
C:/Users/danie/AppData/Local/Programs/Python/Python313/python.exe -m streamlit run streamlit_app.py

REM Restaura o arquivo de config
if exist .streamlit\config.toml.bak (
    ren .streamlit\config.toml.bak config.toml
)