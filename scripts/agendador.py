"""
Sistema de Agendamento Automatico de Posts — FilmeJa (filmeja.com.br)
Permite criar lotes de posts prontos e agendar a publicacao para datas futuras.
"""

import os
import sys
import json
import time
import shutil
import logging
import argparse
import subprocess
from datetime import datetime, timezone, timedelta

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("FilmeJaAgendador")

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_DIR = os.path.join(PROJECT_ROOT, "src", "content", "posts")
AGENDADOS_DIR = os.path.join(PROJECT_ROOT, "src", "content", "agendados")

os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(AGENDADOS_DIR, exist_ok=True)

def listar_agendados():
    """Lista todos os posts atualmente na fila de agendamento."""
    arquivos = [f for f in os.listdir(AGENDADOS_DIR) if f.endswith(".json")]
    if not arquivos:
        print("\n📭 Nenhum post na fila de agendamento no momento.")
        return []

    print(f"\n📅 FILA DE POSTS AGENDADOS ({len(arquivos)} post(s)):")
    print("-" * 75)
    lista = []
    for f in arquivos:
        path = os.path.join(AGENDADOS_DIR, f)
        try:
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)
                agendado_para = data.get("scheduledFor", data.get("publishedAt", "Data nao definida"))
                titulo = data.get("title", f)
                autor = data.get("author", {}).get("name", "Redacao")
                lista.append({
                    "arquivo": f,
                    "titulo": titulo,
                    "autor": autor,
                    "agendado_para": agendado_para,
                    "caminho": path
                })
                print(f"⏰ {agendado_para} | {titulo[:42]}... | Autor: {autor}")
        except Exception as e:
            print(f"⚠️ Erro ao ler {f}: {e}")
    print("-" * 75)
    return lista

def agendar_post(caminho_post: str, data_publicacao_iso: str):
    """Move um post para a fila de agendados com a data programada."""
    caminho_real = caminho_post
    if not os.path.exists(caminho_real):
        tentativa = os.path.join(POSTS_DIR, caminho_post)
        if os.path.exists(tentativa):
            caminho_real = tentativa
        elif not caminho_post.endswith(".json") and os.path.exists(tentativa + ".json"):
            caminho_real = tentativa + ".json"
        elif not caminho_post.endswith(".json") and os.path.exists(caminho_post + ".json"):
            caminho_real = caminho_post + ".json"
        else:
            logger.error(f"Arquivo nao encontrado: {caminho_post}")
            return False

    with open(caminho_real, "r", encoding="utf-8") as f:
        data = json.load(f)

    data["scheduledFor"] = data_publicacao_iso
    data["publishedAt"] = data_publicacao_iso
    data["updatedAt"] = data_publicacao_iso

    filename = os.path.basename(caminho_real)
    destino = os.path.join(AGENDADOS_DIR, filename)

    with open(destino, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Se estava na pasta de posts ativos, remove de la
    if os.path.dirname(os.path.abspath(caminho_real)) == os.path.abspath(POSTS_DIR):
        try:
            os.remove(caminho_real)
        except Exception:
            pass

    logger.info(f"✅ Post agendado com sucesso para {data_publicacao_iso}: {filename}")
    return True

def publicar_vencidos():
    """Verifica posts agendados cuja data ja chegou e os publica imediatamente."""
    arquivos = [f for f in os.listdir(AGENDADOS_DIR) if f.endswith(".json")]
    if not arquivos:
        logger.info("Nenhum post agendado para verificar.")
        return 0

    agora = datetime.now(timezone.utc)
    publicados = 0

    for f in arquivos:
        path = os.path.join(AGENDADOS_DIR, f)
        try:
            with open(path, "r", encoding="utf-8") as file:
                data = json.load(file)
            
            data_str = data.get("scheduledFor", data.get("publishedAt"))
            if not data_str:
                continue

            data_post = datetime.fromisoformat(data_str.replace("Z", "+00:00"))

            if data_post <= agora:
                logger.info(f"🚀 Publicando post agendado: {data.get('title')}")
                destino = os.path.join(POSTS_DIR, f)
                shutil.move(path, destino)
                publicados += 1
            else:
                logger.info(f"⏳ Post aguardando data ({data_str}): {data.get('title')[:35]}...")
        except Exception as e:
            logger.error(f"Erro ao processar {f}: {e}")

    if publicados > 0:
        logger.info(f"✅ {publicados} post(s) movidos para publicacao ativa!")
        logger.info("Sincronizando com GitHub...")
        try:
            subprocess.run(["git", "add", "."], check=True, cwd=PROJECT_ROOT)
            subprocess.run(["git", "commit", "-m", f"feat(agendador): publica {publicados} post(s) programados"], check=True, cwd=PROJECT_ROOT)
            subprocess.run(["git", "push", "origin", "main"], check=True, cwd=PROJECT_ROOT)
            logger.info("Push enviado para o GitHub!")
        except Exception as e:
            logger.warning(f"Aviso ao sincronizar Git: {e}")

        logger.info("Disparando atualizacao na Vercel...")
        try:
            subprocess.run(["npx", "-y", "vercel", "--prod", "--yes"], check=False, cwd=PROJECT_ROOT)
            logger.info("Deploy concluido!")
        except Exception as e:
            logger.warning(f"Aviso no comando Vercel CLI: {e}. O deploy continuara automaticamente pelo GitHub.")
    else:
        logger.info("Nenhum post agendado venceu o horario ainda.")

    return publicados

def distribuir_fila(arquivos_posts: list, inicio_dias: int = 1, intervalo_dias: int = 1):
    """Distribui uma lista de posts programando um para cada dia."""
    for idx, arq in enumerate(arquivos_posts):
        dias = inicio_dias + (idx * intervalo_dias)
        futuro = datetime.now(timezone.utc) + timedelta(days=dias)
        data_iso = futuro.strftime("%Y-%m-%dT12:00:00Z") # 09:00 Horário de Brasília
        agendar_post(arq, data_iso)

def main():
    parser = argparse.ArgumentParser(description="Agendador de Posts FilmeJá")
    parser.add_argument("--listar", action="store_true", help="Lista posts na fila de agendamento")
    parser.add_argument("--verificar", action="store_true", help="Publica posts cuja data ja chegou")
    parser.add_argument("--agendar-arquivo", help="Caminho ou nome do arquivo JSON para agendar")
    parser.add_argument("--data", help="Data/hora futura ISO (ex: 2026-10-20T12:00:00Z)")
    parser.add_argument("--dias-a-frente", type=int, default=0, help="Agendar X dias a partir de hoje")
    args = parser.parse_args()

    if args.listar:
        listar_agendados()
    elif args.verificar:
        publicar_vencidos()
    elif args.agendar_arquivo:
        data_final = args.data
        if not data_final and args.dias_a_frente > 0:
            futuro = datetime.now(timezone.utc) + timedelta(days=args.dias_a_frente)
            data_final = futuro.strftime("%Y-%m-%dT12:00:00Z")
        elif not data_final:
            data_final = datetime.now(timezone.utc).isoformat()
        
        agendar_post(args.agendar_arquivo, data_final)
    else:
        listar_agendados()

if __name__ == "__main__":
    main()
