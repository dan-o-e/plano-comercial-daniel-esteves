@echo off
echo ========================================
echo   MIGRAÇÃO PARA AZURE POSTGRESQL
echo ========================================
echo.

REM Solicitar senha do Azure
set /p azure_password="Digite a senha do Azure PostgreSQL: "
if "%azure_password%"=="" (
    echo ❌ Senha não informada!
    pause
    exit
)

REM Definir variável de ambiente
set AZURE_DB_PASSWORD=%azure_password%

echo.
echo 🚀 Iniciando migração...
echo.

REM Executar migração
python migrate_to_azure.py

echo.
echo ========================================
echo   MIGRAÇÃO CONCLUÍDA
echo ========================================
echo.
echo 📋 PRÓXIMOS PASSOS:
echo.
echo 1. Copie a string de conexão que apareceu acima
echo 2. Acesse: https://share.streamlit.io
echo 3. Configure o app com:
echo    - Repository: dan-o-e/plano-comercial-daniel-esteves
echo    - Branch: main
echo    - Main file: streamlit_app.py
echo 4. Em Advanced Settings ^> Secrets, adicione:
echo.
echo [connections.postgresql]
echo dialect = "postgresql"
echo host = "plano-comercial-daniel.postgres.database.azure.com"
echo port = "5432"
echo database = "postgres"
echo username = "postgres"
echo password = "SUA_SENHA_AZURE"
echo.
pause