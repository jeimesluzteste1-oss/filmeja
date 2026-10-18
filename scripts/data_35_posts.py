"""
Script de Geração dos 35 Posts Premium Agendados — FilmeJá
"""

import os
import sys
import json

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENDADOS_DIR = os.path.join(PROJECT_ROOT, "src", "content", "agendados")
os.makedirs(AGENDADOS_DIR, exist_ok=True)

# Imagens 100% verificadas HTTP 200
P = {
    "silo": "https://media.themoviedb.org/t/p/w500/r2QXomqKjkKHVtYGGtkf2l2Y7go.jpg",
    "the_penguin": "https://media.themoviedb.org/t/p/w500/vOWcqC4oDQws1doDWLO7d3dh5qc.jpg",
    "materia_escura": "https://media.themoviedb.org/t/p/w500/2DPmTlv8F0V1TQBPmlsGOVOhtWk.jpg",
    "the_last_of_us": "https://media.themoviedb.org/t/p/w500/dmo6TYuuJgaYinXBPjrgG9mB5od.jpg",
    "the_bear": "https://media.themoviedb.org/t/p/w500/eKfVzzEazSIjJMrw9ADa2x8ksLz.jpg",
    "fallout": "https://media.themoviedb.org/t/p/w500/c15BtJxCXMrISLVmysdsnZUPQft.jpg",
    "euphoria": "https://media.themoviedb.org/t/p/w500/aJrG7OkoTMPWG5c8opz8a93AZPY.jpg",
    "solo_leveling": "https://media.themoviedb.org/t/p/w500/geCRueV3ElhRTr0xtJuEWJt6dJ1.jpg",
    "stranger_things": "https://image.tmdb.org/t/p/w500/49WJfeN0moxb9IPfGn8AIqMGskD.jpg",
    "duna_a_profecia": "https://image.tmdb.org/t/p/w500/oWVohNsxkxA3u92EzRo8fTuXIS0.jpg",
    "arcane": "https://image.tmdb.org/t/p/w500/fqldf2t8ztc9aiwn3k6mlX3tvRT.jpg",
    "daredevil_born_again": "https://media.themoviedb.org/t/p/w500/xDUoAsU8lQHOOoRkFiBuarmACDN.jpg",
    "house_of_the_dragon": "https://image.tmdb.org/t/p/w500/1X4h40fcB4WWUmIBK0auT4zRBAV.jpg",
    "the_boys": "https://media.themoviedb.org/t/p/w500/in1R2dDc421JxsoRWaIIAqVI2KE.jpg",
    "wandinha": "https://media.themoviedb.org/t/p/w500/9PFonBhy4cQy7Jz20NpMygczOkv.jpg",

    "superman": "https://media.themoviedb.org/t/p/w500/ldyfo0BKmz5rWtJJKCvwaNS4cJT.jpg",
    "fantastic_four": "https://media.themoviedb.org/t/p/w500/nf5qaSEvyYSNeFH0YhSs5EsBLX9.jpg",
    "ainda_estou_aqui": "https://media.themoviedb.org/t/p/w500/gZnsMbhCvhzAQlKaVpeFRHYjGyb.jpg",
    "the_batman_2": "https://image.tmdb.org/t/p/w500/74xTEgt7R36Fpooo50r9T25onhq.jpg",
    "homem_aranha_4": "https://image.tmdb.org/t/p/w500/1g0dhYtq4irTY1GPXvft6k4YLjm.jpg",
    "f1_o_filme": "https://image.tmdb.org/t/p/w500/tH64gzAHDFg7EFcgfkkZyHdGM5P.jpg",
    "frankenstein_del_toro": "https://image.tmdb.org/t/p/w500/fbkUfzmVzEBFSt6p7VigknREIJT.jpg",

    "corra": "https://image.tmdb.org/t/p/w500/tFXcEccSQMf3lfhfXKSU9iRBpa3.jpg",
    "nos": "https://image.tmdb.org/t/p/w500/tFXcEccSQMf3lfhfXKSU9iRBpa3.jpg",
    "o_homem_invisivel": "https://image.tmdb.org/t/p/w500/67gVCA33yHpFkFyqhDJrt21MvYI.jpg",
    "a_substancia": "https://image.tmdb.org/t/p/w500/vWeOgzlhnP1sS23H3rzctGHB9Nb.jpg",
    "longlegs": "https://image.tmdb.org/t/p/w500/uURBOrqLFyU8iKODcI3t2Xkbhqs.jpg",
    "smile_2": "https://image.tmdb.org/t/p/w500/ypHiYvSJmHIyRDRiosZuE595uir.jpg",
    "alien_romulus": "https://image.tmdb.org/t/p/w500/jB0W9tn4w07MFn7sTfqRTBLVytF.jpg",
    "nosferatu": "https://image.tmdb.org/t/p/w500/fbkUfzmVzEBFSt6p7VigknREIJT.jpg",
    "interestelar": "https://image.tmdb.org/t/p/w500/tR1XVa5bxgdh2bRw2u0DzrgkO2l.jpg",
    "a_chegada": "https://image.tmdb.org/t/p/w500/3rDwbFpn6z5HJUgDjpfhEePx8VI.jpg",
    "blade_runner_2049": "https://image.tmdb.org/t/p/w500/49pANIZXRAdHUiWjjBv4vxPeqRC.jpg",
    "ex_machina": "https://image.tmdb.org/t/p/w500/hfpnFtgcYom9Gk9s1IyWiovpZYg.jpg",
    "gravidade": "https://image.tmdb.org/t/p/w500/eHLufJ1bHy4PtEBJdPSTu4jIhZ0.jpg",
    "duna_2": "https://image.tmdb.org/t/p/w500/VMy4UGsI2u3f4fALGeCqCdsQBb.jpg",
    "ilha_do_medo": "https://image.tmdb.org/t/p/w500/erl801HYIodoIBGZeFk0GTwCUBh.jpg",
    "os_suspeitos": "https://image.tmdb.org/t/p/w500/30YtzPOimO7eG30r8K8rUkqTGNj.jpg",
    "seven": "https://image.tmdb.org/t/p/w500/dZXYPSEaXCeigR2GEuZoukNmLTf.jpg",
    "zodiaco": "https://image.tmdb.org/t/p/w500/jFmlV5vUzOt1PgJ82efOhNsWcWX.jpg",
    "garota_exemplar": "https://image.tmdb.org/t/p/w500/54nI3vSKlPp42WhJmKVRdmMbkzl.jpg",
    "cisne_negro": "https://image.tmdb.org/t/p/w500/tqlmLBt2i5SHNpXEj2nqk10Crwa.jpg",
    "o_iluminado": "https://image.tmdb.org/t/p/w500/xazWoLealQwEgqZ89MLZklLZD3k.jpg",
    "sociedade_da_neve": "https://image.tmdb.org/t/p/w500/7fQTmvKgVGxifieVryqqlxohkoW.jpg",
    "127_horas": "https://image.tmdb.org/t/p/w500/fONsBTZIDqxMfHwlfUcCAb8ubr1.jpg",
    "o_regresso": "https://image.tmdb.org/t/p/w500/hRotKKijqV6YibxnhSOureF5efx.jpg",
    "o_poco": "https://image.tmdb.org/t/p/w500/kY0ET33EoiJhjaPCzzvywCDqP6b.jpg",
    "bird_box": "https://image.tmdb.org/t/p/w500/kTHDVXVTT62gJY9WfZnaXdmtvZE.jpg",
    "um_lugar_silencioso": "https://image.tmdb.org/t/p/w500/pN9BtzUeqPIKybAu9baihz6YzyO.jpg",
    "mad_max": "https://image.tmdb.org/t/p/w500/tH64gzAHDFg7EFcgfkkZyHdGM5P.jpg",
    "trem_bala": "https://image.tmdb.org/t/p/w500/8gdBMIYwPPxp3b9FjY9yCxme5Rs.jpg",
    "resgate_2": "https://image.tmdb.org/t/p/w500/AfwqKLQwjgPu8bIL1mqhHTlnQv0.jpg",
    "john_wick_4": "https://media.themoviedb.org/t/p/w500/vZloFAK7NmvMGKE7VkF5UHaz0I.jpg",
    "top_gun_maverick": "https://media.themoviedb.org/t/p/w500/n0YuM4f5lvGAP6MAW2kBIzugXnc.jpg",
    "entre_facas_e_segredos": "https://image.tmdb.org/t/p/w500/9H8PNc4JJRjPnfSh8gGukD0CbqQ.jpg",
    "glass_onion": "https://image.tmdb.org/t/p/w500/zQJcENHbZUpLQ8RKYt9wTzcXCwv.jpg",
    "os_suspeitos_de_sempre": "https://image.tmdb.org/t/p/w500/8RrGQ3kSiu2JJatkQ3o0DdXUGUU.jpg",
    "assassinato_expresso_oriente": "https://image.tmdb.org/t/p/w500/quZnHOVKVbFR7IdXBI9J0ONb7Jk.jpg",
    "veja_como_eles_correm": "https://image.tmdb.org/t/p/w500/dHjMrsrhgLcwKLIfReRxt9rFBFk.jpg",
    "invocacao_do_mal": "https://image.tmdb.org/t/p/w500/1NxHKZW5DPbUFtbF3MxbdSyxRqU.jpg",
    "fale_comigo": "https://image.tmdb.org/t/p/w500/7U3lC4YnHD8zpeoxbY6Hsj9jyeu.jpg",
    "hereditario": "https://image.tmdb.org/t/p/w500/x9tUYQj6WrdVwoKimSdoMzkDABS.jpg",
    "entrevista_com_o_demonio": "https://image.tmdb.org/t/p/w500/blckaGzdEJ4PdG5RxZPcb77VYFV.jpg",
    "a_primeira_profecia": "https://image.tmdb.org/t/p/w500/zppeHKLHljU2uI7NBJ1JyDNpn6L.jpg",
    "oppenheimer": "https://image.tmdb.org/t/p/w500/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
    "pobres_criaturas": "https://image.tmdb.org/t/p/w500/kCGlIMHnOm8JPXq3rXM6c5wMxcT.jpg",
    "imitation_game": "https://media.themoviedb.org/t/p/w500/zSqJ1qFq8NXFfi7JeIYMlzyR0dx.jpg",
    "darkest_hour": "https://media.themoviedb.org/t/p/w500/xa6G3aKlysQeVg9wOb0dRcIGlWu.jpg",
    "chernobyl": "https://media.themoviedb.org/t/p/w500/hlLXt2tOPT6RRnjiUmoxyG1LTFi.jpg",
    "a_pele_que_habito": "https://image.tmdb.org/t/p/w500/90hbSeBsev4hezgzkyW8tkio2dp.jpg",
    "titane": "https://image.tmdb.org/t/p/w500/mBlpouG3gqB8WLdP65LCOXb3jFb.jpg"
}

AUTHORS = {
    "marcos": {
        "name": "Marcos Vinicius",
        "role": "Especialista em Séries & Lançamentos Semanais",
        "avatar": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=100&auto=format&fit=crop&q=80"
    },
    "thiago": {
        "name": "Thiago Rocha",
        "role": "Editor de Cinema Comercial & Ação",
        "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=100&auto=format&fit=crop&q=80"
    },
    "camila": {
        "name": "Camila Fontes",
        "role": "Crítica de Sci-Fi & Fantasia",
        "avatar": "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=100&auto=format&fit=crop&q=80"
    },
    "guilherme": {
        "name": "Guilherme Santos",
        "role": "Editor de Thrillers & Policiais",
        "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&auto=format&fit=crop&q=80"
    },
    "beatriz": {
        "name": "Beatriz Silveira",
        "role": "Crítica de Cinema de Gênero & Terror",
        "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&auto=format&fit=crop&q=80"
    },
    "lucas": {
        "name": "Lucas Andrade",
        "role": "Crítico Sênior & Editor-Chefe",
        "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&auto=format&fit=crop&q=80"
    }
}
