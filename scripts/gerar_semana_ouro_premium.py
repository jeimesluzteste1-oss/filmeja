"""
Orquestrador Final da Semana de Ouro Premium — 35 Artigos com Qualidade Extrema
FilmeJá (filmeja.com.br)
"""

import os
import sys
import json
import urllib.request

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENDADOS_DIR = os.path.join(PROJECT_ROOT, "src", "content", "agendados")
os.makedirs(AGENDADOS_DIR, exist_ok=True)

from posts_builder_part1 import posts as p1
from posts_builder_part2 import posts as p2
from posts_builder_part3 import posts as p3
from posts_builder_part4 import posts as p4

todos_posts = p1 + p2 + p3 + p4

print(f"📦 Total de posts carregados: {len(todos_posts)}")
assert len(todos_posts) == 35, f"Esperado 35 posts, obtido {len(todos_posts)}"

# 1. Coleta e teste de sanidade de 100% das imagens usadas
print("🔍 Verificando status HTTP de todas as imagens utilizadas...")
todas_imagens = set()
for p in todos_posts:
    if p.get("coverImage"):
        todas_imagens.add(p["coverImage"])
    if p.get("posterImage"):
        todas_imagens.add(p["posterImage"])
    for item in p.get("listItems", []):
        if item.get("posterImage"):
            todas_imagens.add(item["posterImage"])

print(f"Total de URLs de imagens únicas nos 35 posts: {len(todas_imagens)}")

falhas = []
for idx, url in enumerate(sorted(todas_imagens), 1):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            if resp.status != 200:
                falhas.append((url, resp.status))
    except Exception as e:
        falhas.append((url, str(e)))

if falhas:
    print(f"❌ ATENÇÃO: {len(falhas)} imagem(ns) falharam:")
    for f in falhas:
        print("  -", f)
    sys.exit(1)
else:
    print("✅ 100% das imagens foram testadas e retornaram HTTP 200 com sucesso!")

# 2. Escrita dos 35 arquivos JSON em src/content/agendados/
print("\n📝 Gravando arquivos JSON em src/content/agendados/...")
salvos = 0
for post in todos_posts:
    slug = post["slug"]
    caminho = os.path.join(AGENDADOS_DIR, f"{slug}.json")
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(post, f, ensure_ascii=False, indent=2)
    salvos += 1

print(f"\n🎉 SUCESSO ABSOLUTO! {salvos} artigos com Qualidade Extrema foram gravados em 'src/content/agendados/'!")
print("Cada post conta com metadados ricos, conteúdo aprofundado, FAQs, imagens 100% verificadas e horários distribuídos cronologicamente.")
