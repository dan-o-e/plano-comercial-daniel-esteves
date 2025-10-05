@echo off
echo ========================================
echo   ALTERNATIVA: SUPABASE POSTGRESQL
echo ========================================
echo.
echo 🎯 Supabase eh mais facil que Azure!
echo.
echo 📋 PASSOS:
echo 1. Acesse: https://supabase.com
echo 2. Faca login com GitHub
echo 3. Clique "New Project"
echo 4. Escolha nome: plano-comercial-daniel
echo 5. Senha forte: Daniel123!@#
echo 6. Regiao: East US (Virginia)
echo 7. Aguarde criacao (2-3 minutos)
echo.
echo 8. Va em Settings ^> Database
echo 9. Copie "Connection string" (URI)
echo 10. Execute este script
echo.
pause
echo.
echo 🚀 Iniciando migracao...
python migrate_to_supabase.py
echo.
echo ========================================
echo   MIGRACAO CONCLUIDA
echo ========================================
echo.
echo 📋 PROXIMO PASSO:
echo.
echo 1. Acesse: https://share.streamlit.io
echo 2. Configure app:
echo    - Repository: dan-o-e/plano-comercial-daniel-esteves
echo    - Branch: main
echo    - Main file: streamlit_app.py
echo 3. Use as configuracoes que apareceram acima
echo.
pause