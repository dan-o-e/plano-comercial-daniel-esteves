@echo off
echo ========================================
echo   ENVIANDO PARA GITHUB
echo ========================================
echo.

REM Inicializar repositório Git
git init

REM Adicionar todos os arquivos
git add .

REM Fazer primeiro commit
git commit -m "Initial commit - Plano Comercial Daniel Esteves"

REM Conectar com seu repositório GitHub
echo.
echo IMPORTANTE: Substitua SEU_USUARIO pelo seu username do GitHub
echo Exemplo: se seu usuario eh 'danielesteves', use:
echo git remote add origin https://github.com/danielesteves/plano-comercial-daniel-esteves.git
echo.
pause

REM Configurar branch principal
git branch -M main

echo.
echo Agora execute manualmente:
echo git remote add origin https://github.com/SEU_USUARIO/plano-comercial-daniel-esteves.git
echo git push -u origin main
echo.
pause