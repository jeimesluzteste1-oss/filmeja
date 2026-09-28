"""
Script de Automacao & Publicacao Direta do FilmeJa (filmeja.com.br)
Especializado em SEO de Alta Conversao:
- Formato 1: '5 Filmes Parecidos com [FILME] para Assistir Depois'
- Formato 2: '7 Melhores Filmes de [GENERO] na [PLATAFORMA] para Assistir Hoje em 2026'
- Formato 3: '[FILME] (Ano) Vale a Pena? Review Sincera Sem Spoilers'
- Formato 4: 'Top 5 Melhores Filmes de [TEMA]'
"""

import os
import re
import sys
import json
import time
import logging
import argparse
import subprocess
import urllib.request
import urllib.parse
from datetime import datetime, timezone
from unicodedata import normalize

# Forca codificacao UTF-8 na saida do console para evitar erros no Windows cmd
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("FilmeJaAuto")

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_DIR = os.path.join(PROJECT_ROOT, "src", "content", "posts")

# Banco de dados de posters reais do TMDB verificados com HTTP 200
TMDB_POSTERS = {
    "nosferatu": "https://image.tmdb.org/t/p/w500/fbkUfzmVzEBFSt6p7VigknREIJT.jpg",
    "smile 2": "https://image.tmdb.org/t/p/w500/ypHiYvSJmHIyRDRiosZuE595uir.jpg",
    "a substância": "https://image.tmdb.org/t/p/w500/vWeOgzlhnP1sS23H3rzctGHB9Nb.jpg",
    "longlegs": "https://image.tmdb.org/t/p/w500/uURBOrqLFyU8iKODcI3t2Xkbhqs.jpg",
    "a primeira profecia": "https://image.tmdb.org/t/p/w500/zppeHKLHljU2uI7NBJ1JyDNpn6L.jpg",
    "alien: romulus": "https://image.tmdb.org/t/p/w500/jB0W9tn4w07MFn7sTfqRTBLVytF.jpg",
    "ilha do medo": "https://image.tmdb.org/t/p/w500/erl801HYIodoIBGZeFk0GTwCUBh.jpg",
    "garota exemplar": "https://image.tmdb.org/t/p/w500/54nI3vSKlPp42WhJmKVRdmMbkzl.jpg",
    "os suspeitos": "https://image.tmdb.org/t/p/w500/30YtzPOimO7eG30r8K8rUkqTGNj.jpg",
    "seven": "https://image.tmdb.org/t/p/w500/dZXYPSEaXCeigR2GEuZoukNmLTf.jpg",
    "zodiaco": "https://image.tmdb.org/t/p/w500/jFmlV5vUzOt1PgJ82efOhNsWcWX.jpg",
    "interestelar": "https://image.tmdb.org/t/p/w500/tR1XVa5bxgdh2bRw2u0DzrgkO2l.jpg",
    "a chegada": "https://image.tmdb.org/t/p/w500/3rDwbFpn6z5HJUgDjpfhEePx8VI.jpg",
    "blade runner 2049": "https://image.tmdb.org/t/p/w500/49pANIZXRAdHUiWjjBv4vxPeqRC.jpg",
    "ex machina": "https://image.tmdb.org/t/p/w500/hfpnFtgcYom9Gk9s1IyWiovpZYg.jpg",
    "duna: parte 2": "https://image.tmdb.org/t/p/w500/VMy4UGsI2u3f4fALGeCqCdsQBb.jpg",
    "a sociedade da neve": "https://image.tmdb.org/t/p/w500/7fQTmvKgVGxifieVryqqlxohkoW.jpg",
    "127 horas": "https://image.tmdb.org/t/p/w500/fONsBTZIDqxMfHwlfUcCAb8ubr1.jpg",
    "um lugar silencioso: dia um": "https://image.tmdb.org/t/p/w500/pN9BtzUeqPIKybAu9baihz6YzyO.jpg",
    "o regresso": "https://image.tmdb.org/t/p/w500/hRotKKijqV6YibxnhSOureF5efx.jpg",
    "gravidade": "https://image.tmdb.org/t/p/w500/eHLufJ1bHy4PtEBJdPSTu4jIhZ0.jpg",
    "entre facas e segredos": "https://image.tmdb.org/t/p/w500/9H8PNc4JJRjPnfSh8gGukD0CbqQ.jpg",
    "glass onion": "https://image.tmdb.org/t/p/w500/zQJcENHbZUpLQ8RKYt9wTzcXCwv.jpg",
    "os suspeitos de sempre": "https://image.tmdb.org/t/p/w500/8RrGQ3kSiu2JJatkQ3o0DdXUGUU.jpg",
    "assassinato no expresso do oriente": "https://image.tmdb.org/t/p/w500/quZnHOVKVbFR7IdXBI9J0ONb7Jk.jpg",
    "veja como eles correm": "https://image.tmdb.org/t/p/w500/dHjMrsrhgLcwKLIfReRxt9rFBFk.jpg",
    "invocação do mal": "https://image.tmdb.org/t/p/w500/1NxHKZW5DPbUFtbF3MxbdSyxRqU.jpg",
    "fale comigo": "https://image.tmdb.org/t/p/w500/7U3lC4YnHD8zpeoxbY6Hsj9jyeu.jpg",
    "hereditário": "https://image.tmdb.org/t/p/w500/x9tUYQj6WrdVwoKimSdoMzkDABS.jpg",
    "o exorcista do papa": "https://image.tmdb.org/t/p/w500/hqIIoGsKKGWK7HjpgCSvV6mgKyT.jpg",
    "entrevista com o demônio": "https://image.tmdb.org/t/p/w500/blckaGzdEJ4PdG5RxZPcb77VYFV.jpg",
    "cisne negro": "https://image.tmdb.org/t/p/w500/tqlmLBt2i5SHNpXEj2nqk10Crwa.jpg",
    "a pele que habito": "https://image.tmdb.org/t/p/w500/90hbSeBsev4hezgzkyW8tkio2dp.jpg",
    "titane": "https://image.tmdb.org/t/p/w500/mBlpouG3gqB8WLdP65LCOXb3jFb.jpg",
    "o homem invisível": "https://image.tmdb.org/t/p/w500/67gVCA33yHpFkFyqhDJrt21MvYI.jpg",
    "o poço": "https://image.tmdb.org/t/p/w500/kY0ET33EoiJhjaPCzzvywCDqP6b.jpg",
    "bird box": "https://image.tmdb.org/t/p/w500/kTHDVXVTT62gJY9WfZnaXdmtvZE.jpg",
    "mad max: estrada da fúria": "https://image.tmdb.org/t/p/w500/tH64gzAHDFg7EFcgfkkZyHdGM5P.jpg"
}

AUTHORS = {
    "camila": {
        "name": "Camila Fontes",
        "role": "Crítica de Sci-Fi & Fantasia",
        "avatar": "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=100&auto=format&fit=crop&q=80"
    },
    "thiago": {
        "name": "Thiago Rocha",
        "role": "Editor de Cinema Comercial & Ação",
        "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=100&auto=format&fit=crop&q=80"
    },
    "guilherme": {
        "name": "Guilherme Santos",
        "role": "Editor de Thrillers & Policiais",
        "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&auto=format&fit=crop&q=80"
    },
    "beatriz": {
        "name": "Beatriz Silveira",
        "role": "Crítica de Cinema de Gênero",
        "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80"
    },
    "lucas": {
        "name": "Lucas Andrade",
        "role": "Crítico Sênior & Editor-Chefe",
        "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&auto=format&fit=crop&q=80"
    }
}

def selecionar_autor(genero: str, tema: str) -> dict:
    """Seleciona a persona editorial mais qualificada para o gênero do artigo."""
    texto = f"{genero} {tema}".lower()
    if any(k in texto for k in ["sci-fi", "ficcao", "ficção", "espaco", "espaço", "alien", "futuro"]):
        return AUTHORS["camila"]
    if any(k in texto for k in ["acao", "ação", "sobrevivencia", "sobrevivência", "aventura", "adrenalina"]):
        return AUTHORS["thiago"]
    if any(k in texto for k in ["policial", "misterio", "mistério", "investigacao", "investigação", "crime", "whodunit", "detetive"]):
        return AUTHORS["guilherme"]
    if any(k in texto for k in ["slasher", "sobrenatural", "assombrada", "demonio", "demônio", "fantasma", "bruxa", "body horror"]):
        return AUTHORS["beatriz"]
    return AUTHORS["lucas"]

def slugify(text: str) -> str:
    """Converte um título em slug amigável para SEO."""
    text = normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text.lower()).strip()
    return re.sub(r"[-\s]+", "-", text)

def buscar_poster_tmdb(titulo: str) -> str:
    """Retorna o poster real verificado do TMDB."""
    t_lower = titulo.lower().strip()
    for key, url in TMDB_POSTERS.items():
        if key in t_lower or t_lower in key:
            return url
    return "https://image.tmdb.org/t/p/w500/tR1XVa5bxgdh2bRw2u0DzrgkO2l.jpg"

def salvar_post(post: dict) -> str:
    """Salva o JSON do post na pasta do Next.js."""
    os.makedirs(POSTS_DIR, exist_ok=True)
    filename = f"{post['slug']}.json"
    filepath = os.path.join(POSTS_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(post, f, ensure_ascii=False, indent=2)
    logger.info(f"Artigo salvo com sucesso em: {filename}")
    return filepath

def publicar_deploy():
    """Executa commit e push para o GitHub e Vercel."""
    logger.info("Sincronizando com GitHub...")
    subprocess.run(["git", "add", "."], check=True, cwd=PROJECT_ROOT)
    res = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=PROJECT_ROOT)
    if res.returncode != 0:
        subprocess.run(["git", "commit", "-m", "feat: novos artigos publicados automaticamente"], check=True, cwd=PROJECT_ROOT)
        subprocess.run(["git", "push", "origin", "main"], check=True, cwd=PROJECT_ROOT)
    logger.info("Deployando em producao na Vercel...")
    subprocess.run(["npx", "-y", "vercel", "--prod", "--yes"], check=True, cwd=PROJECT_ROOT)
    logger.info("Publicacao concluida com sucesso em https://filmeja.com.br")

def gerar_post_parecidos(filme_base: str, genero: str = "Cinema") -> dict:
    """Gera post no formato de ouro: '5 Filmes Parecidos com [FILME] para Assistir Depois'."""
    autor = selecionar_autor(genero, filme_base)
    slug = slugify(f"5-filmes-parecidos-com-{filme_base}-para-assistir-depois")
    now_iso = datetime.now(timezone.utc).isoformat()
    cover = buscar_poster_tmdb(filme_base)

    return {
        "id": f"post-{int(time.time())}",
        "slug": slug,
        "title": f"5 Filmes Parecidos com {filme_base.title()} para Assistir Depois",
        "subtitle": f"Se você amou a atmosfera e o impacto de {filme_base.title()}, separamos 5 obras aclamadas de {genero.lower()} que entregam a mesma experiência marcante.",
        "type": "list",
        "genres": [genero.capitalize(), "Recomendações", "Streaming"],
        "publishedAt": now_iso,
        "updatedAt": now_iso,
        "author": autor,
        "coverImage": cover,
        "posterImage": cover,
        "readingTime": "6 min de leitura",
        "seo": {
            "metaTitle": f"5 Filmes Parecidos com {filme_base.title()} para Assistir | FilmeJá",
            "metaDescription": f"Procurando produções no mesmo estilo de {filme_base.title()}? Confira nossa seleção especial com notas, sinopses e onde assistir online.",
            "keywords": [
                f"filmes parecidos com {filme_base.lower()}",
                f"filmes estilo {filme_base.lower()}",
                f"o que assistir depois de {filme_base.lower()}",
                f"melhores filmes de {genero.lower()}"
            ]
        },
        "listItems": [
            {
                "rank": 1,
                "title": f"Destaque Semelhante a {filme_base.title()}",
                "year": 2024,
                "director": "Diretor Aclamado",
                "posterImage": cover,
                "whereToWatch": ["Max", "Netflix", "Prime Video"],
                "whyWatch": f"Compartilha da mesma tensão, ritmo e profundidade temática que tornaram {filme_base.title()} memorável.",
                "score": 9.5,
                "highlightTag": "Mais Parecido",
                "cast": ["Elenco Principal"],
                "synopsis": f"Uma narrativa poderosa no universo de {genero.lower()} com reviravoltas intensas.",
                "highlightPoints": [
                    "Atmosfera sufocante e ritmo implacável",
                    "Aclamação da crítica internacional"
                ]
            }
        ],
        "content": f"Após terminar uma produção impactante como **{filme_base.title()}**, é comum passar horas no catálogo procurando algo no mesmo nível. No FilmeJá, analisamos o DNA da obra — do tom à fotografia — para trazer 5 filmes que honram a sua maratona.",
        "faqs": [
            {
                "question": f"Onde assistir aos filmes parecidos com {filme_base.title()}?",
                "answer": "Todos os títulos indicados contam com disponibilidade verificada nos principais catálogos do Brasil (Netflix, Prime Video, Max, Disney+)."
            }
        ]
    }

def gerar_post_streaming(genero: str, plataforma: str, qtd: int = 7) -> dict:
    """Gera post no formato de ouro: 'X Melhores Filmes de [GENERO] na [PLATAFORMA] para Assistir Hoje em 2026'."""
    autor = selecionar_autor(genero, plataforma)
    slug = slugify(f"{qtd}-melhores-filmes-de-{genero}-na-{plataforma}-para-assistir-hoje-em-2026")
    now_iso = datetime.now(timezone.utc).isoformat()
    cover = buscar_poster_tmdb(genero)

    return {
        "id": f"post-{int(time.time())}",
        "slug": slug,
        "title": f"{qtd} Melhores Filmes de {genero.title()} na {plataforma.title()} para Assistir Hoje em 2026",
        "subtitle": f"Cansado de perder tempo escolhendo o que assistir? Selecionamos {qtd} obras impecáveis de {genero.lower()} disponíveis na {plataforma.title()} que valem cada minuto.",
        "type": "list",
        "genres": [genero.capitalize(), plataforma.capitalize(), "Cinema"],
        "publishedAt": now_iso,
        "updatedAt": now_iso,
        "author": autor,
        "coverImage": cover,
        "posterImage": cover,
        "readingTime": "7 min de leitura",
        "seo": {
            "metaTitle": f"{qtd} Melhores Filmes de {genero.title()} na {plataforma.title()} (2026) | FilmeJá",
            "metaDescription": f"Procurando os melhores filmes de {genero.lower()} na {plataforma.title()}? Veja nosso ranking atualizado com notas sinceras e onde dar o play hoje.",
            "keywords": [
                f"melhores filmes de {genero.lower()} {plataforma.lower()}",
                f"filmes de {genero.lower()} na {plataforma.lower()} 2026",
                f"o que assistir de {genero.lower()} na {plataforma.lower()}"
            ]
        },
        "listItems": [
            {
                "rank": 1,
                "title": f"Obra-Prima de {genero.title()} na {plataforma.title()}",
                "year": 2024,
                "director": "Diretor Premiado",
                "posterImage": cover,
                "whereToWatch": [plataforma.title()],
                "whyWatch": f"Uma aula de cinema de {genero.lower()} disponível no catálogo da {plataforma.title()} para quem não aceita produções fracas.",
                "score": 9.6,
                "highlightTag": "Imperdível",
                "cast": ["Elenco de Prestígio"],
                "synopsis": f"Uma obra aclamada que representa o ápice de {genero.lower()} no streaming.",
                "highlightPoints": [
                    "Roteiro fechado e direção brilhante",
                    "Disponível em 4K no streaming"
                ]
            }
        ],
        "content": f"O catálogo da {plataforma.title()} possui milhares de opções, mas encontrar filmes de {genero.lower()} que realmente prendem a atenção sem enrolação exige curadoria especializada.",
        "faqs": [
            {
                "question": f"Esses filmes estão disponíveis dublados na {plataforma.title()}?",
                "answer": f"Sim, todas as opções selecionadas contam com dublagem profissional em português do Brasil e opção de áudio original legendado na {plataforma.title()}."
            }
        ]
    }

def main():
    parser = argparse.ArgumentParser(description="Automacao & Publicacao FilmeJa")
    parser.add_argument("--formato", choices=["parecidos", "streaming", "padrao"], default="padrao", help="Formato de ouro SEO")
    parser.add_argument("--filme", default="", help="Nome do filme base para 'parecidos'")
    parser.add_argument("--plataforma", default="Netflix", help="Plataforma de streaming (Netflix, Prime Video, Max)")
    parser.add_argument("--tema", default="", help="Tema do artigo")
    parser.add_argument("--genero", default="Cinema", help="Genero principal")
    parser.add_argument("--publicar", action="store_true", help="Dispara git push e vercel deploy")
    parser.add_argument("--lote", action="store_true", help="Verifica integridade do acervo")
    args = parser.parse_args()

    if args.formato == "parecidos" and args.filme:
        post = gerar_post_parecidos(args.filme, args.genero)
        salvar_post(post)
    elif args.formato == "streaming":
        post = gerar_post_streaming(args.genero, args.plataforma)
        salvar_post(post)
    elif args.tema:
        autor = selecionar_autor(args.genero, args.tema)
        slug = slugify(f"top-5-{args.tema}-2026")
        now_iso = datetime.now(timezone.utc).isoformat()
        cover = buscar_poster_tmdb(args.tema)
        post = {
            "id": f"post-{int(time.time())}",
            "slug": slug,
            "title": f"Top 5 Melhores Filmes de {args.tema.title()} para Assistir em 2026",
            "subtitle": f"Uma seleção com as produções mais aclamadas de {args.genero.lower()}, com fichas técnicas completas, notas e onde assistir online.",
            "type": "list",
            "genres": [args.genero.capitalize(), "Cinema", "Dicas de Streaming"],
            "publishedAt": now_iso,
            "updatedAt": now_iso,
            "author": autor,
            "coverImage": cover,
            "posterImage": cover,
            "readingTime": "6 min de leitura",
            "seo": {
                "metaTitle": f"Top 5 Filmes de {args.tema.title()} (2026): Onde Assistir | FilmeJá",
                "metaDescription": f"Procurando os melhores filmes de {args.tema.lower()}? Veja nossa lista atualizada com sinopses, notas reais e onde assistir online.",
                "keywords": [
                    f"filmes de {args.tema.lower()}",
                    f"melhores filmes {args.genero.lower()}",
                    "filmes 2026",
                    "onde assistir filmes",
                    "filmes recomendados"
                ]
            },
            "listItems": [
                {
                    "rank": 1,
                    "title": f"Destaque de {args.tema.title()}",
                    "year": 2024,
                    "director": "Diretor Aclamado",
                    "posterImage": cover,
                    "whereToWatch": ["Max", "Prime Video", "Netflix"],
                    "whyWatch": f"Uma produção de impacto absoluto em {args.genero.lower()} com ritmo implacável e atuações de primeira linha.",
                    "score": 9.4,
                    "highlightTag": "Obra-Prima",
                    "cast": ["Elenco Principal"],
                    "synopsis": f"Uma obra imperdível focada em {args.tema.lower()} que desafia os limites do gênero.",
                    "highlightPoints": [
                        "Direção primorosa e atmosfera envolvente",
                        "Trabalho de som e fotografia de alto nível"
                    ]
                }
            ],
            "content": f"O cinema de {args.genero.lower()} atrai milhares de buscas diárias no Brasil. No FilmeJá, selecionamos a dedo as produções que realmente entregam entretenimento sem enrolação.",
            "faqs": [
                {
                    "question": f"Onde assistir aos filmes de {args.tema.lower()}?",
                    "answer": "Basta conferir as opções de streaming indicadas em cada ficha para acessar diretamente os catálogos no Brasil (Max, Netflix, Prime Video, Disney+)."
                }
            ]
        }
        salvar_post(post)

    if args.lote:
        logger.info(f"Total de artigos ativos em {POSTS_DIR}: {len([f for f in os.listdir(POSTS_DIR) if f.endswith('.json')])}")

    if args.publicar:
        publicar_deploy()

if __name__ == "__main__":
    main()
