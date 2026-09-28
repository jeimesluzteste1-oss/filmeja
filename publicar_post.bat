@echo off
chcp 65001 > nul
echo ========================================================
echo        🎬 FILMEJÁ - GERADOR E PUBLICADOR AUTOMÁTICO
echo ========================================================
echo.
set /p TEMA="Digite o tema da lista (ex: suspense psicologico, terror 2026): "
set /p GENERO="Digite o gênero principal (ex: Terror, Suspense, Sci-Fi): "

echo.
echo [1/3] Gerando artigo com fotos reais e SEO otimizado...
python scripts/gerador_filmeja.py --tema "%TEMA%" --genero "%GENERO%"

echo.
echo [2/3] Enviando para o GitHub e Vercel...
git add .
git commit -m "feat: novo post automatizado %TEMA%"
git push
npx vercel --prod --yes

echo.
echo ========================================================
echo  🚀 POST PUBLICADO COM SUCESSO EM HTTPS://FILMEJA.COM.BR!
echo ========================================================
pause
