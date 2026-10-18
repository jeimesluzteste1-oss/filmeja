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

:menu_principal
echo.
echo ========================================================
echo Escolha o formato de ouro do artigo:
echo   [1] 5 Filmes Parecidos com [FILME] para Assistir Depois
echo   [2] 7 Melhores Filmes de [GENERO] na [PLATAFORMA] (2026)
echo   [3] Que Dia Sai o Episodio [X] de [SERIE]? (Calendario Semanal)
echo   [4] Lancamento Aguardado / Blockbuster (Data de Estreia, Elenco, Marvel/DC)
echo   [5] Top 5 Filmes por Tema Personalizado
echo   [6] Sincronizar alteracoes pendentes no GitHub e Vercel
echo   [7] Gerenciar Fila de Posts Agendados (Verificar e Publicar Vencidos)
echo.
choice /c 1234567 /n /m "Digite a opcao desejada [1 a 7]: "
if errorlevel 7 goto :opcao_agendamento
if errorlevel 6 goto :fazer_deploy
if errorlevel 5 goto :opcao_personalizado
if errorlevel 4 goto :opcao_lancamento
if errorlevel 3 goto :opcao_episodio
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
goto :decidir_publicacao_ou_agendamento

:opcao_streaming
echo.
set /p GENERO="Digite o genero do artigo (ex: Terror, Suspense, Acao): "
if "%GENERO%"=="" set GENERO=Terror
set /p PLATAFORMA="Digite a plataforma de streaming (ex: Netflix, Prime Video, Max, Disney+): "
if "%PLATAFORMA%"=="" set PLATAFORMA=Netflix

echo.
echo [1/3] Gerando lista de streaming otimizada com fotos reais e SEO...
%PYTHON_CMD% scripts/gerador_filmeja.py --formato streaming --genero "%GENERO%" --plataforma "%PLATAFORMA%"
if %errorlevel% neq 0 (
    echo [ERRO] Falha na geracao do artigo.
    pause
    exit /b 1
)
goto :decidir_publicacao_ou_agendamento

:opcao_episodio
echo.
set /p SERIE="Digite o nome da serie (ex: VisionQuest, O Pinguim, Ruptura): "
if "%SERIE%"=="" (
    echo [ERRO] O nome da serie nao pode ficar vazio.
    pause
    exit /b 1
)
set /p TEMPORADA="Digite a temporada (ex: 1 ou 2) [padrao: 1]: "
if "%TEMPORADA%"=="" set TEMPORADA=1
set /p EPISODIO="Digite o numero do proximo episodio (ex: 3) [padrao: 1]: "
if "%EPISODIO%"=="" set EPISODIO=1
set /p DATA_ESTREIA="Digite o dia de estreia (ex: terca-feira, 20 de outubro): "
if "%DATA_ESTREIA%"=="" set DATA_ESTREIA=terca-feira
set /p HORARIO="Digite o horario (ex: 22h ou 04h da manha) [padrao: 22h]: "
if "%HORARIO%"=="" set HORARIO=22h (horario de Brasilia)
set /p PLATAFORMA="Digite a plataforma (ex: Disney+, Max, Apple TV+, Netflix): "
if "%PLATAFORMA%"=="" set PLATAFORMA=Disney+

echo.
echo [1/3] Gerando artigo 'Que Dia Sai o Episodio' com SEO otimizado...
%PYTHON_CMD% scripts/gerador_filmeja.py --formato episodio --serie "%SERIE%" --temporada %TEMPORADA% --episodio %EPISODIO% --data-estreia "%DATA_ESTREIA%" --horario "%HORARIO%" --plataforma "%PLATAFORMA%"
if %errorlevel% neq 0 (
    echo [ERRO] Falha na geracao do artigo de serie.
    pause
    exit /b 1
)
goto :decidir_publicacao_ou_agendamento

:opcao_lancamento
echo.
set /p FILME="Digite o nome do filme/blockbuster (ex: Vingadores: Doomsday, Superman): "
if "%FILME%"=="" (
    echo [ERRO] O nome do filme nao pode ficar vazio.
    pause
    exit /b 1
)
set /p DATA_ESTREIA="Digite a data de estreia (ex: 17 de dezembro de 2026): "
if "%DATA_ESTREIA%"=="" set DATA_ESTREIA=17 de dezembro de 2026
set /p PLATAFORMA="Digite a plataforma de streaming futura (ex: Disney+, Max, Netflix): "
if "%PLATAFORMA%"=="" set PLATAFORMA=Disney+
set /p DETALHES="Digite um detalhe especial (ex: Robert Downey Jr. como Doutor Destino): "

echo.
echo [1/3] Gerando artigo de Lancamento Aguardado com SEO de alta conversao...
%PYTHON_CMD% scripts/gerador_filmeja.py --formato lancamento --filme "%FILME%" --data-estreia "%DATA_ESTREIA%" --detalhes "%DETALHES%" --plataforma "%PLATAFORMA%"
if %errorlevel% neq 0 (
    echo [ERRO] Falha na geracao do artigo.
    pause
    exit /b 1
)
goto :decidir_publicacao_ou_agendamento

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
goto :decidir_publicacao_ou_agendamento

:decidir_publicacao_ou_agendamento
set ULTIMO_POST=
if exist scripts\.ultimo_post.txt set /p ULTIMO_POST=<scripts\.ultimo_post.txt
echo.
echo ========================================================
echo   ARTIGO GERADO COM SUCESSO!
if not "%ULTIMO_POST%"=="" echo   Arquivo: %ULTIMO_POST%
echo ========================================================
echo.
echo ATENCAO: E OBRIGATORIO DEFINIR O DESTINO DESTE ARTIGO:
echo   [1] PUBLICAR AGORA (Sincronizar Git + Deploy Vercel Imediato)
echo   [2] AGENDAR PUBLICACAO (Mover para fila e programar data futura)
echo   [3] Manter apenas localmente como rascunho (Sem deploy)
echo.
choice /c 123 /n /m "Digite a opcao desejada [1, 2 ou 3]: "
if errorlevel 3 goto :manter_rascunho
if errorlevel 2 goto :agendar_recem_criado
if errorlevel 1 goto :fazer_deploy

:agendar_recem_criado
echo.
echo ========================================================
echo                AGENDAMENTO DO ARTIGO
echo ========================================================
if "%ULTIMO_POST%"=="" (
    set /p ULTIMO_POST="Digite o nome do arquivo JSON a agendar: "
) else (
    echo Artigo selecionado: %ULTIMO_POST%
)
echo.
set /p DIAS="Para daqui a quantos dias deseja agendar a publicacao? (ex: 1, 2, 3...): "
if "%DIAS%"=="" set DIAS=1
%PYTHON_CMD% scripts/agendador.py --agendar-arquivo "%ULTIMO_POST%" --dias-a-frente %DIAS%
echo.
echo [OK] Artigo movido para a fila de agendados com sucesso!
echo.
echo Sincronizando fila com o GitHub Actions para disparo automatico na nuvem...
git add src/content/agendados src/content/posts
git diff --cached --quiet
if %errorlevel% neq 0 (
    git commit -m "feat(agendador): programa %ULTIMO_POST% para daqui a %DIAS% dia(s)"
    git push origin main
    echo [OK] Fila sincronizada com o GitHub Actions!
)
pause
goto :menu_principal

:manter_rascunho
echo.
echo [INFO] Artigo mantido localmente como rascunho em src/content/posts/.
echo Nenhum deploy ou sincronizacao foi disparada.
pause
goto :menu_principal

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
goto :menu_principal

:opcao_agendamento
echo.
echo ========================================================
echo        GERENCIADOR DE AGENDAMENTO DE POSTS
echo ========================================================
echo   [1] Ver fila de posts agendados
echo   [2] Verificar e publicar posts vencidos agora (Deploy)
echo   [3] Agendar um post existente para data futura
echo   [4] Voltar ao menu principal
echo.
choice /c 1234 /n /m "Digite a opcao desejada [1, 2, 3 ou 4]: "
if errorlevel 4 goto :menu_principal
if errorlevel 3 goto :agendar_manual
if errorlevel 2 goto :publicar_agendados_agora
if errorlevel 1 goto :listar_fila

:listar_fila
echo.
%PYTHON_CMD% scripts/agendador.py --listar
echo.
pause
goto :opcao_agendamento

:publicar_agendados_agora
echo.
echo [1/1] Verificando posts agendados com data vencida...
%PYTHON_CMD% scripts/agendador.py --verificar
echo.
pause
goto :opcao_agendamento

:agendar_manual
echo.
echo Posts disponiveis na pasta de artigos ativos:
dir /b src\content\posts\*.json
echo.
set /p ARQ_POST="Digite o nome do arquivo JSON a agendar: "
if "%ARQ_POST%"=="" (
    echo [ERRO] O nome do arquivo nao pode ficar vazio.
    pause
    goto :opcao_agendamento
)
set /p DIAS="Para daqui a quantos dias deseja agendar? (ex: 1, 2, 3...): "
if "%DIAS%"=="" set DIAS=1
%PYTHON_CMD% scripts/agendador.py --agendar-arquivo "%ARQ_POST%" --dias-a-frente %DIAS%
echo.
pause
goto :opcao_agendamento
