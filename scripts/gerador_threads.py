"""
Script de Automacao de Posts para o Threads (Meta) — FilmeJa (filmeja.com.br)
Gera fios (threads) de alta viralidade baseados nos artigos publicados no site.
"""

import os
import sys
import json
import argparse
from datetime import datetime

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_DIR = os.path.join(PROJECT_ROOT, "src", "content", "posts")
OUTPUT_FILE = os.path.join(PROJECT_ROOT, "threads_prontas_para_publicar.md")

def carregar_posts():
    posts = []
    if not os.path.exists(POSTS_DIR):
        return posts
    for f in os.listdir(POSTS_DIR):
        if f.endswith(".json"):
            path = os.path.join(POSTS_DIR, f)
            with open(path, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                    posts.append(data)
                except Exception:
                    pass
    return sorted(posts, key=lambda x: x.get("publishedAt", ""), reverse=True)

def formatar_thread(post: dict) -> str:
    tipo = post.get("type", "list")
    titulo = post.get("title", "")
    slug = post.get("slug", "")
    url = f"https://filmeja.com.br/post/{slug}"
    
    if tipo == "episodio":
        info = post.get("seriesInfo", {})
        serie = info.get("seriesTitle", "Série")
        ep = info.get("episodeNumber", 1)
        data = info.get("nextEpisodeDate", "esta semana")
        hora = info.get("nextEpisodeTime", "22h")
        plataforma = info.get("platform", "Streaming")
        
        return f"""### 🧵 THREAD: {serie} (Episódio {ep})
**Post 1 (Gancho Principal):**
Para quem está roendo as unhas com {serie}: o episódio {ep} já tem data e horário confirmados no Brasil! 📺👇

**Post 2:**
📅 Quando estreia: {data}
⏰ Horário no Brasil: {hora}
🍿 Onde assistir: {plataforma}

O Season Finale promete responder as maiores pontas soltas da temporada.

**Post 3 (Chamada de Ação):**
Deixamos o resumo completo sem spoilers e o cronograma de todos os episódios no link abaixo:
🔗 {url}

---
"""
    elif tipo == "list":
        items = post.get("listItems", [])
        itens_txt = ""
        for it in items[:4]:
            itens_txt += f"▫️ {it.get('title', '')} ({it.get('year', '')}) — Nota: {it.get('score', 9.0)}/10\n"
            
        return f"""### 🧵 THREAD: {titulo}
**Post 1 (Gancho Viral):**
Cansado de perder 40 minutos procurando filme no streaming e não achar nada que preste? 

Separei as opções que realmente prendem do início ao fim sem enrolação 🧵👇

**Post 2:**
{itens_txt}
**Post 3 (Chamada de Ação):**
A lista completa com sinopses detalhadas e onde encontrar cada um no Brasil está no FilmeJá:
🔗 {url}

---
"""
    else: # react / review
        sub = post.get("subtitle", "")
        return f"""### 🧵 THREAD: {titulo}
**Post 1 (Gancho Crítica):**
{titulo} 👀🍿

Assistimos ao lançamento e o veredito sincero e sem spoilers está no ar 🧵👇

**Post 2:**
{sub}

**Post 3 (Chamada de Ação):**
Confira nossa análise detalhada de direção, atuações e se realmente vale o seu tempo no link:
🔗 {url}

---
"""

def main():
    parser = argparse.ArgumentParser(description="Gerador de Threads Virais FilmeJá")
    parser.add_argument("--limite", type=int, default=5, help="Quantidade de artigos recentes para gerar fios")
    args = parser.parse_args()

    posts = carregar_posts()
    if not posts:
        print("Nenhum post encontrado em src/content/posts")
        return

    selecionados = posts[:args.limite]
    conteudo_md = f"# 🧵 FIOS PRONTOS PARA O THREADS — FILMEJÁ ({datetime.now().strftime('%d/%m/%Y')})\n\n"
    conteudo_md += "> Copie e cole no aplicativo do Threads para gerar tráfego imediato e cliques no site.\n\n---\n\n"

    for p in selecionados:
        conteudo_md += formatar_thread(p)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(conteudo_md)

    print(f"✅ {len(selecionados)} fios do Threads gerados com sucesso em:\n{OUTPUT_FILE}")

if __name__ == "__main__":
    main()
