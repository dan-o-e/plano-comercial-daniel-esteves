@echo off
cls
echo ========================================
echo   PLANO COMERCIAL DANIEL ESTEVES
echo ========================================
echo.

REM Verificar se Python esta instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python nao encontrado!
    echo    Instale Python 3.7+ primeiro
    pause
    exit /b 1
)

REM Verificar se requirements esta instalado
echo 🔍 Verificando dependencias...
python -c "import streamlit, pandas, psycopg2, plotly" >nul 2>&1
if errorlevel 1 (
    echo 📦 Instalando dependencias...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ Erro ao instalar dependencias!
        pause
        exit /b 1
    )
    echo ✅ Dependencias instaladas!
)

REM Verificar se banco tem dados
echo 🔍 Verificando banco de dados...
python -c "import psycopg2; conn = psycopg2.connect(host='localhost', port=5433, user='postgres', password='postgres', database='base_btg'); cur = conn.cursor(); cur.execute('SELECT COUNT(*) FROM base_btg'); print('✅ Banco OK -', cur.fetchone()[0], 'registros'); conn.close()" 2>nul
if errorlevel 1 (
    echo ⚠️  Banco nao encontrado ou sem dados
    echo    Execute primeiro: python import_excel_to_postgres.py
    echo.
    set /p choice="Importar dados agora? (s/N): "
    if /i "%choice%"=="s" (
        echo 📊 Importando dados...
        python import_excel_to_postgres.py
        if errorlevel 1 (
            echo ❌ Erro ao importar dados!
            pause
            exit /b 1
        )
    )
)

echo.
echo 🚀 Iniciando Streamlit...
echo    O navegador sera aberto automaticamente
echo    URL: http://localhost:8501
echo.
echo    Para parar: Ctrl+C
echo.

REM Aguardar 2 segundos e abrir navegador
timeout /t 2 /nobreak >nul
start http://localhost:8501

REM Executar Streamlit
python -m streamlit run streamlit_app.py --server.headless=false --server.runOnSave=true

echo.
echo Aplicacao finalizada.
pause