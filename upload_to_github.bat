@echo off
echo ========================================
echo   SINCRONIZANDO COM GITHUB
echo ========================================
echo.

REM Verificar se é inicialização ou atualização
if exist .git (
    echo Repositório Git já existe. Fazendo atualização...
    goto UPDATE
) else (
    echo Inicializando novo repositório Git...
    goto INIT
)

:INIT
echo.
echo === INICIALIZANDO REPOSITÓRIO ===
git init
git add .
git commit -m "Initial commit - Plano Comercial Daniel Esteves"
git branch -M main
echo.
echo PRÓXIMO PASSO:
echo 1. Crie um repositório no GitHub chamado: plano-comercial-daniel-esteves
echo 2. Execute os comandos abaixo (substitua SEU_USUARIO):
echo.
echo git remote add origin https://github.com/SEU_USUARIO/plano-comercial-daniel-esteves.git
echo git push -u origin main
echo.
goto END

:UPDATE
echo.
echo === ATUALIZANDO REPOSITÓRIO ===
git status
echo.
git add .
echo Digite a mensagem do commit (ex: Atualização do dashboard):
set /p commit_msg="Mensagem: "
if "%commit_msg%"=="" set commit_msg=Atualização automática
git commit -m "%commit_msg%"
git push
echo.
echo ✅ Atualização enviada para GitHub!
goto END

:END
echo.
echo ========================================
echo   PROCESSO CONCLUÍDO
echo ========================================
pause