@echo off
setlocal
cd /d "%~dp0"

echo ========================================================
echo        FILMEJA - GERADOR E PUBLICADOR AUTOMATICO
echo ========================================================
echo.

REM 1. Verifica se o Python esta instalado
where python >nul 2>nul
if %errorlevel% neq 0 (
    where py >nul 2>nul
    if %errorlevel% neq 0 (
        echo [ERRO] Python nao foi encontrado no sistema.
        echo Por favor, instale o Python ou marque 'Add Python to PATH'.
        pause
        exit /b 1
    ) else (
        set PYTHON_CMD=py
    )
) else (
    set PYTHON_CMD=python
)

echo Escolha uma opcao:
echo   [1] Gerar e publicar novo artigo (tema personalizado)
echo   [2] Publicar alteracoes pendentes (GitHub + Vercel)
echo   [3] Sincronizar e verificar acervo de artigos
echo.
choice /c 123 /n /m "Digite a opcao desejada [1, 2 ou 3]: "
if errorlevel 3 goto :opcao_sincronizar
if errorlevel 2 goto :fazer_deploy
if errorlevel 1 goto :opcao_personalizado

:opcao_personalizado
echo.
set /p TEMA="Digite o tema do artigo (ex: suspense psicologico, sci-fi): "
if "%TEMA%"=="" (
    echo [ERRO] O tema nao pode ficar vazio.
    pause
    exit /b 1
)

set /p GENERO="Digite o genero principal (ex: Suspense, Terror, Acao, Sci-Fi): "
if "%GENERO%"=="" set GENERO=Cinema

echo.
echo [1/3] Gerando artigo com fotos reais e SEO otimizado...
%PYTHON_CMD% scripts/gerador_filmeja.py --tema "%TEMA%" --genero "%GENERO%"
if %errorlevel% neq 0 (
    echo [ERRO] Falha na geracao do artigo.
    pause
    exit /b 1
)
goto :fazer_deploy

:opcao_sincronizar
echo.
echo [*] Verificando acervo e integridade dos posts...
%PYTHON_CMD% scripts/gerador_filmeja.py --lote
goto :fazer_deploy

:fazer_deploy
echo.
echo [2/3] Sincronizando com GitHub...
git add .
git diff --cached --quiet
if %errorlevel% neq 0 (
    git commit -m "feat: novos artigos publicados automaticamente"
    git push origin main
) else (
    echo [INFO] Nenhuma alteracao pendente para commit no Git.
)

echo.
echo [3/3] Publicando versao de producao na Vercel...
call npx -y vercel --prod --yes

echo.
echo ========================================================
echo   PUBLICACAO CONCLUIDA COM SUCESSO!
echo   Acesse em: https://filmeja.com.br
echo ========================================================
pause
