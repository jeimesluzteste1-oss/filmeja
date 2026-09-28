@echo off
setlocal
cd /d "%~dp0"

echo ========================================================
echo        FILMEJA - GERADOR E PUBLICADOR AUTOMATICO (2026)
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

echo Escolha o formato de ouro do artigo:
echo   [1] 5 Filmes Parecidos com [FILME] para Assistir Depois
echo   [2] 7 Melhores Filmes de [GENERO] na [PLATAFORMA] (2026)
echo   [3] Top 5 Filmes por Tema Personalizado
echo   [4] Sincronizar alteracoes pendentes no GitHub e Vercel
echo.
choice /c 1234 /n /m "Digite a opcao desejada [1, 2, 3 ou 4]: "
if errorlevel 4 goto :fazer_deploy
if errorlevel 3 goto :opcao_personalizado
if errorlevel 2 goto :opcao_streaming
if errorlevel 1 goto :opcao_parecidos

:opcao_parecidos
echo.
set /p FILME="Digite o nome do filme base (ex: A Substancia, Duna, Longlegs): "
if "%FILME%"=="" (
    echo [ERRO] O nome do filme nao pode ficar vazio.
    pause
    exit /b 1
)
set /p GENERO="Digite o genero (ex: Terror, Ficcao Cientifica, Suspense): "
if "%GENERO%"=="" set GENERO=Cinema

echo.
echo [1/3] Gerando artigo '5 Filmes Parecidos' com SEO de alta conversao...
%PYTHON_CMD% scripts/gerador_filmeja.py --formato parecidos --filme "%FILME%" --genero "%GENERO%"
if %errorlevel% neq 0 (
    echo [ERRO] Falha na geracao do artigo.
    pause
    exit /b 1
)
goto :fazer_deploy

:opcao_streaming
echo.
set /p GENERO="Digite o genero do artigo (ex: Terror, Suspense, Acao): "
if "%GENERO%"=="" set GENERO=Terror
set /p PLATAFORMA="Digite a plataforma de streaming (ex: Netflix, Prime Video, Max): "
if "%PLATAFORMA%"=="" set PLATAFORMA=Netflix

echo.
echo [1/3] Gerando lista de streaming otimizada com fotos reais e SEO...
%PYTHON_CMD% scripts/gerador_filmeja.py --formato streaming --genero "%GENERO%" --plataforma "%PLATAFORMA%"
if %errorlevel% neq 0 (
    echo [ERRO] Falha na geracao do artigo.
    pause
    exit /b 1
)
goto :fazer_deploy

:opcao_personalizado
echo.
set /p TEMA="Digite o tema da lista (ex: suspense psicologico, sci-fi mental): "
if "%TEMA%"=="" (
    echo [ERRO] O tema nao pode ficar vazio.
    pause
    exit /b 1
)
set /p GENERO="Digite o genero principal (ex: Suspense, Terror, Acao): "
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

:fazer_deploy
echo.
echo [2/3] Sincronizando com GitHub...
git add .
git diff --cached --quiet
if %errorlevel% neq 0 (
    git commit -m "feat: novos artigos publicados automaticamente com cluster de ouro"
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
