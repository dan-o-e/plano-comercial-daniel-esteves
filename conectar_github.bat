@echo off
echo ========================================
echo   CONECTAR COM GITHUB
echo ========================================
echo.
echo SUBSTITUA 'SEU_USUARIO' pelo seu username do GitHub
echo.
echo Exemplo de comandos:
echo git remote add origin https://github.com/danielesteves/plano-comercial-daniel-esteves.git
echo git push -u origin main
echo.
echo OU execute diretamente:
set /p username="Digite seu username do GitHub: "
if "%username%"=="" (
    echo Username não informado!
    pause
    exit
)

git remote add origin https://github.com/%username%/plano-comercial-daniel-esteves.git
git push -u origin main

echo.
echo ✅ Projeto enviado para GitHub!
echo.
echo PRÓXIMO PASSO: Deploy no Streamlit Cloud
echo 1. Acesse: https://share.streamlit.io
echo 2. Faça login com GitHub
echo 3. Selecione seu repositório: plano-comercial-daniel-esteves
echo 4. Main file path: streamlit_app.py
echo 5. Clique em Deploy!
echo.
pause