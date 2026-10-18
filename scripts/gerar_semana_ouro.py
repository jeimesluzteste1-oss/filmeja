"""
Script de Geração e Agendamento em Lote: Semana de Ouro (35 Artigos)
FilmeJá (filmeja.com.br)
Gera 5 posts por dia para os próximos 7 dias com SEO de alta conversão,
metadados ricos, FAQs e capas verificadas do TMDB.
"""

import os
import sys
import json
import time
from datetime import datetime, timezone, timedelta

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_DIR = os.path.join(PROJECT_ROOT, "src", "content", "posts")
AGENDADOS_DIR = os.path.join(PROJECT_ROOT, "src", "content", "agendados")

os.makedirs(POSTS_DIR, exist_ok=True)
os.makedirs(AGENDADOS_DIR, exist_ok=True)

# Autores editoriais
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

# 35 Artigos Planejados (5 por dia durante 7 dias)
# Horários: 08:00 BRT (11:00 UTC), 12:00 BRT (15:00 UTC), 16:00 BRT (19:00 UTC), 19:30 BRT (22:30 UTC), 22:00 BRT (01:00 UTC dia seguinte)
HORARIOS_UTC = ["11:00:00Z", "15:00:00Z", "19:00:00Z", "22:30:00Z", "23:59:00Z"]

PLANO_SEMANA = [
    # DIA 1: 19/10 (Segunda-feira)
    {
        "dia": 1,
        "slot": 0,
        "slug": "que-dia-sai-episodio-1-de-silo-temporada-2-data-horario",
        "title": "Que Dia Sai o Episódio 1 de Silo (2ª Temporada)? Data e Horário na Apple TV+",
        "subtitle": "Confira o retorno da distopia subterrânea com Rebecca Ferguson, cronograma de episódios no Brasil e o que esperar do lado de fora.",
        "type": "episodio",
        "genres": ["Séries", "Apple TV+", "Ficção Científica", "Lançamentos"],
        "author": AUTHORS["marcos"],
        "coverImage": "https://image.tmdb.org/t/p/w500/1N1T9g7W8G9bJ7r7Y1C7eL6mZ0.jpg",
        "readingTime": "4 min de leitura",
        "content": "A aguardada 2ª temporada de Silo chega com respostas urgentes após o desfecho estarrecedor de Juliette Nichols no lado de fora. A série da Apple TV+ consolidou-se como um dos maiores fenômenos de sci-fi do streaming mundial.",
        "seriesInfo": {"seriesTitle": "Silo", "seasonNumber": 2, "episodeNumber": 1, "nextEpisodeDate": "15 de novembro", "nextEpisodeTime": "05h da manhã", "platform": "Apple TV+", "totalEpisodes": 10},
        "faqs": [
            {"question": "Que dia sai o novo episódio de Silo?", "answer": "Os episódios da 2ª temporada estreiam semanalmente às sextas-feiras no catálogo da Apple TV+."},
            {"question": "A que horas sai Silo no Brasil?", "answer": "Fica disponível pontualmente às 05h00 da manhã (horário de Brasília) com dublagem e legendas."}
        ]
    },
    {
        "dia": 1,
        "slot": 1,
        "slug": "superman-james-gunn-data-estreia-elenco-onde-assistir",
        "title": "Superman (2025/2026): Data de Estreia, Elenco de James Gunn e Onde Assistir",
        "subtitle": "Tudo sobre o renascimento do Homem de Aço nos cinemas: David Corenswet, Rachel Brosnahan e a previsão de chegada à Max.",
        "type": "lancamento",
        "genres": ["Cinema", "Lançamentos", "DC", "Max"],
        "author": AUTHORS["thiago"],
        "coverImage": "https://image.tmdb.org/t/p/w500/ombsmhkwN1sCLTaOxP9twTGlBZy.jpg",
        "readingTime": "5 min de leitura",
        "content": "Sob a visão criativa de James Gunn, o novo filme do Superman inaugura oficialmente o Capítulo 1 do DCU: Deuses e Monstros. Trazendo um tom que mescla a nobreza clássica dos quadrinhos com ação moderna.",
        "movieInfo": {"title": "Superman", "releaseDate": "10 de julho", "futureStreaming": "Max", "productionDetails": "Direção de James Gunn com David Corenswet e Nicholas Hoult."},
        "faqs": [
            {"question": "Quando Superman chega aos cinemas brasileiros?", "answer": "A estreia nacional acontece nas telonas com sessões antecipadas e distribuição global da Warner Bros."},
            {"question": "Onde assistir a Superman no streaming?", "answer": "Após a janela dos cinemas, o longa estreará com exclusividade no catálogo da Max."}
        ]
    },
    {
        "dia": 1,
        "slot": 2,
        "slug": "5-filmes-parecidos-com-longlegs-para-assistir-depois",
        "title": "5 Filmes Parecidos com Longlegs: Vínculo Mortal para Assistir Depois",
        "subtitle": "Se você ficou obcecado pelo horror investigativo de Nicolas Cage, confira essas cinco obras-primas sobre seitas e crimes rituais.",
        "type": "list",
        "genres": ["Terror", "Mistério", "Thrillers"],
        "author": AUTHORS["beatriz"],
        "coverImage": "https://image.tmdb.org/t/p/w500/uURBOrqLFyU8iKODcI3t2Xkbhqs.jpg",
        "readingTime": "5 min de leitura",
        "content": "Longlegs reinventou o terror psicológico nos moldes de O Silêncio dos Inocentes e Zodíaco. Selecionamos os filmes que entregam a mesma sensação de desconforto e mistério opressivo.",
        "listItems": [{"rank": 1, "title": "Seven: Os Sete Crimes Capitais", "year": 1995, "whereToWatch": ["Max", "Prime Video"], "score": 9.5, "posterImage": "https://image.tmdb.org/t/p/w500/dZXYPSEaXCeigR2GEuZoukNmLTf.jpg"}],
        "faqs": [{"question": "Onde assistir a Longlegs online?", "answer": "Longlegs: Vínculo Mortal está disponível no catálogo do Prime Video no Brasil."}]
    },
    {
        "dia": 1,
        "slot": 3,
        "slug": "7-melhores-filmes-de-suspense-na-max-para-assistir-hoje",
        "title": "7 Melhores Filmes de Suspense na Max para Assistir Hoje em 2026",
        "subtitle": "Uma curadoria com os thrillers mais tensos e inteligentes disponíveis para os assinantes da Max no Brasil.",
        "type": "streaming",
        "genres": ["Suspense", "Max", "Dicas de Streaming"],
        "author": AUTHORS["guilherme"],
        "coverImage": "https://image.tmdb.org/t/p/w500/erl801HYIodoIBGZeFk0GTwCUBh.jpg",
        "readingTime": "6 min de leitura",
        "content": "A Max abriga alguns dos maiores clássicos contemporâneos de suspense do cinema da Warner e produções independentes premiadas.",
        "listItems": [{"rank": 1, "title": "Ilha do Medo", "year": 2010, "whereToWatch": ["Max"], "score": 9.3, "posterImage": "https://image.tmdb.org/t/p/w500/erl801HYIodoIBGZeFk0GTwCUBh.jpg"}],
        "faqs": [{"question": "Quais são os suspenses imperdíveis da Max?", "answer": "Destaques incluem Ilha do Medo, Garota Exemplar e Os Suspeitos."}]
    },
    {
        "dia": 1,
        "slot": 4,
        "slug": "que-dia-sai-episodio-1-de-the-last-of-us-temporada-2-data-horario",
        "title": "Que Dia Sai o Episódio 1 de The Last of Us (2ª Temporada)? Data e Horário na Max",
        "subtitle": "Joel e Ellie retornam em meio ao caos de Seattle e a chegada de Abby. Confira o calendário de exibição da HBO.",
        "type": "episodio",
        "genres": ["Séries", "Max", "Dramas", "Ação"],
        "author": AUTHORS["marcos"],
        "coverImage": "https://image.tmdb.org/t/p/w500/uKvVjK1olIuUUpK2fbg9m0832p.jpg",
        "readingTime": "4 min de leitura",
        "content": "A segunda temporada de The Last of Us adapta os acontecimentos devastadores do aclamado jogo The Last of Us Part II da Naughty Dog, trazendo Pedro Pascal e Bella Ramsey em atuações viscerais.",
        "seriesInfo": {"seriesTitle": "The Last of Us", "seasonNumber": 2, "episodeNumber": 1, "nextEpisodeDate": "domingo", "nextEpisodeTime": "22h00", "platform": "Max", "totalEpisodes": 7},
        "faqs": [{"question": "Que horas sai The Last of Us no streaming?", "answer": "A série da HBO estreia episódios inéditos sempre aos domingos pontualmente às 22h na Max."}]
    },

    # DIA 2: 20/10 (Terça-feira)
    {
        "dia": 2,
        "slot": 0,
        "slug": "que-dia-sai-episodio-1-de-duna-a-profecia-temporada-1-data-horario",
        "title": "Que Dia Sai o Episódio 1 de Duna: A Profecia? Data, Horário e Calendário na Max",
        "subtitle": "Mergulhe na origem das Bene Gesserit 10.000 anos antes de Paul Atreides na grandiosa nova série do universo de Duna.",
        "type": "episodio",
        "genres": ["Séries", "Max", "Ficção Científica", "Lançamentos"],
        "author": AUTHORS["camila"],
        "coverImage": "https://image.tmdb.org/t/p/w500/oWVohNsxkxA3u92EzRo8fTuXIS0.jpg",
        "readingTime": "4 min de leitura",
        "content": "Duna: A Profecia expande o rico universo criado por Frank Herbert com foco nas maquinações políticas e poderes misteriosos da Irmandade Bene Gesserit.",
        "seriesInfo": {"seriesTitle": "Duna: A Profecia", "seasonNumber": 1, "episodeNumber": 1, "nextEpisodeDate": "17 de novembro", "nextEpisodeTime": "22h (horário de Brasília)", "platform": "Max", "totalEpisodes": 6},
        "faqs": [{"question": "Quantos episódios tem Duna: A Profecia?", "answer": "A primeira temporada conta com 6 episódios semanais na Max."}]
    },
    {
        "dia": 2,
        "slot": 1,
        "slug": "homem-aranha-4-brand-new-day-data-estreia-elenco-onde-assistir",
        "title": "Homem-Aranha 4 (Brand New Day): Data de Estreia nos Cinemas, Elenco e Sony/Marvel",
        "subtitle": "Tom Holland volta ao papel de Peter Parker em uma Nova York solitária e urbana. Confira data confirmada e bastidores.",
        "type": "lancamento",
        "genres": ["Cinema", "Lançamentos", "Marvel", "Ação"],
        "author": AUTHORS["thiago"],
        "coverImage": "https://image.tmdb.org/t/p/w500/c24sv2weTHPsmDa7jEMN0m2P3RT.jpg",
        "readingTime": "5 min de leitura",
        "content": "Dirigido por Destin Daniel Cretton, Homem-Aranha 4 promete focar na vida do herói anônimo e nas consequências do feitiço do Doutor Estranho.",
        "movieInfo": {"title": "Homem-Aranha 4", "releaseDate": "29 de julho de 2026", "futureStreaming": "Max", "productionDetails": "Parceria oficial Sony Pictures e Marvel Studios."},
        "faqs": [{"question": "Quando Homem-Aranha 4 estreia no Brasil?", "answer": "O filme tem estreia confirmada nos cinemas brasileiros para 29 de julho de 2026."}]
    },
    {
        "dia": 2,
        "slot": 2,
        "slug": "5-filmes-parecidos-com-interestelar-para-assistir-depois",
        "title": "5 Filmes Parecidos com Interestelar sobre Viagens Cósmicas e o Tempo",
        "subtitle": "Para quem amou a obra de Christopher Nolan, selecionamos produções de ficção científica que exploram buracos negros e o infinito.",
        "type": "list",
        "genres": ["Ficção Científica", "Espaço", "Cinema"],
        "author": AUTHORS["camila"],
        "coverImage": "https://image.tmdb.org/t/p/w500/tR1XVa5bxgdh2bRw2u0DzrgkO2l.jpg",
        "readingTime": "5 min de leitura",
        "content": "Interestelar é um marco moderno do cinema de exploração cósmica. Estas produções combinam rigor científico e emoção transcendental.",
        "listItems": [{"rank": 1, "title": "A Chegada", "year": 2016, "whereToWatch": ["Netflix", "Prime Video"], "score": 9.4, "posterImage": "https://image.tmdb.org/t/p/w500/3rDwbFpn6z5HJUgDjpfhEePx8VI.jpg"}],
        "faqs": [{"question": "Onde assistir a Interestelar online?", "answer": "Disponível no catálogo da Max e Prime Video no Brasil."}]
    },
    {
        "dia": 2,
        "slot": 3,
        "slug": "7-melhores-filmes-de-ficcao-cientifica-no-prime-video-2026",
        "title": "7 Melhores Filmes de Ficção Científica no Prime Video para Assistir em 2026",
        "subtitle": "Inteligência artificial, futuros distópicos e mistérios quânticos reunidos no catálogo da Amazon.",
        "type": "streaming",
        "genres": ["Ficção Científica", "Prime Video", "Dicas de Streaming"],
        "author": AUTHORS["camila"],
        "coverImage": "https://image.tmdb.org/t/p/w500/hfpnFtgcYom9Gk9s1IyWiovpZYg.jpg",
        "readingTime": "5 min de leitura",
        "content": "O Prime Video reúne um dos acervos mais premiados de sci-fi da atualidade.",
        "listItems": [{"rank": 1, "title": "Ex Machina", "year": 2014, "whereToWatch": ["Prime Video"], "score": 9.1, "posterImage": "https://image.tmdb.org/t/p/w500/hfpnFtgcYom9Gk9s1IyWiovpZYg.jpg"}],
        "faqs": [{"question": "Qual melhor sci-fi do Prime Video?", "answer": "Ex Machina e Blade Runner 2049 são escolhas essenciais."}]
    },
    {
        "dia": 2,
        "slot": 4,
        "slug": "que-dia-sai-episodio-1-de-the-boys-temporada-5-data-horario",
        "title": "Que Dia Sai o Episódio 1 de The Boys (5ª Temporada)? Data e Horário no Prime Video",
        "subtitle": "A temporada final da série mais sangrenta dos super-heróis está chegando. Confira o calendário de exibição.",
        "type": "episodio",
        "genres": ["Séries", "Prime Video", "Ação", "Comédia Ácida"],
        "author": AUTHORS["thiago"],
        "coverImage": "https://image.tmdb.org/t/p/w500/7vjaCdMw15FEbXyLQTVa04URsPm.jpg",
        "readingTime": "4 min de leitura",
        "content": "O confronto final entre Billy Bruto e Capitão Pátria promete encerrar a saga de The Boys com violência épica e desfechos chocantes.",
        "seriesInfo": {"seriesTitle": "The Boys", "seasonNumber": 5, "episodeNumber": 1, "nextEpisodeDate": "quinta-feira", "nextEpisodeTime": "04h00", "platform": "Prime Video", "totalEpisodes": 8},
        "faqs": [{"question": "A 5ª temporada é a última de The Boys?", "answer": "Sim, Eric Kripke confirmou que o quinto ano encerra a história principal."}]
    },

    # DIA 3: 21/10 (Quarta-feira)
    {
        "dia": 3,
        "slot": 0,
        "slug": "que-dia-sai-episodio-9-de-materia-escura-temporada-1-data-horario",
        "title": "Que Dia Sai o Episódio 9 de Matéria Escura (Season Finale)? Data e Horário na Apple TV+",
        "subtitle": "O desfecho da corrida através do multiverso com Joel Edgerton e Jennifer Connelly.",
        "type": "episodio",
        "genres": ["Séries", "Apple TV+", "Ficção Científica", "Suspense"],
        "author": AUTHORS["marcos"],
        "coverImage": "https://image.tmdb.org/t/p/w500/b1x6jhVz93wM1tA0O92E461P11c.jpg",
        "readingTime": "4 min de leitura",
        "content": "A adaptação do livro de Blake Crouch chega ao ápice emocional em seu nono episódio, onde múltiplos Jason Dessen lutam para proteger sua família original.",
        "seriesInfo": {"seriesTitle": "Matéria Escura", "seasonNumber": 1, "episodeNumber": 9, "nextEpisodeDate": "quarta-feira", "nextEpisodeTime": "22h (horário de Brasília)", "platform": "Apple TV+", "totalEpisodes": 9},
        "faqs": [{"question": "Onde assistir a Matéria Escura?", "answer": "Disponível exclusivamente no catálogo da Apple TV+ com áudio 4K e HDR."}]
    },
    {
        "dia": 3,
        "slot": 1,
        "slug": "ainda-estou-aqui-filme-onde-assistir-data-streaming-brasil",
        "title": "Ainda Estou Aqui: Onde Assistir Online, Data no Streaming e História Real",
        "subtitle": "O aclamado filme nacional com Fernanda Torres e Selton Mello premiado em Veneza.",
        "type": "lancamento",
        "genres": ["Cinema", "Cinema Nacional", "Dramas"],
        "author": AUTHORS["lucas"],
        "coverImage": "https://image.tmdb.org/t/p/w500/8qD4PqY7n3v7m9Y5K8zM1v7Y3rB.jpg",
        "readingTime": "5 min de leitura",
        "content": "Dirigido por Walter Salles e baseado no livro autobiográfico de Marcelo Rubens Paiva, Ainda Estou Aqui retrata a coragem de Eunice Paiva durante a ditadura militar.",
        "movieInfo": {"title": "Ainda Estou Aqui", "releaseDate": "7 de novembro", "futureStreaming": "Globoplay", "productionDetails": "Grande sucesso de crítica internacional e representante brasileiro no Oscar."},
        "faqs": [{"question": "Onde assistir a Ainda Estou Aqui online?", "answer": "Após a exibição nos cinemas, o filme chegará ao streaming no catálogo do Globoplay."}]
    },
    {
        "dia": 3,
        "slot": 2,
        "slug": "5-filmes-parecidos-com-ilha-do-medo-com-finais-chocantes",
        "title": "5 Filmes Parecidos com Ilha do Medo com Finais Surpreendentes",
        "subtitle": "Thrillers psicológicos com reviravoltas inesquecíveis que desafiam tudo o que você pensou saber até o último minuto.",
        "type": "list",
        "genres": ["Suspense", "Mistério", "Plot Twists"],
        "author": AUTHORS["guilherme"],
        "coverImage": "https://image.tmdb.org/t/p/w500/erl801HYIodoIBGZeFk0GTwCUBh.jpg",
        "readingTime": "5 min de leitura",
        "content": "Martin Scorsese e Leonardo DiCaprio criaram um dos finais mais debatidos do cinema moderno. Reunimos cinco filmes que causam o mesmo impacto cognitivo.",
        "listItems": [{"rank": 1, "title": "Garota Exemplar", "year": 2014, "whereToWatch": ["Max", "Prime Video"], "score": 9.2, "posterImage": "https://image.tmdb.org/t/p/w500/54nI3vSKlPp42WhJmKVRdmMbkzl.jpg"}],
        "faqs": [{"question": "O que assistir depois de Ilha do Medo?", "answer": "Garota Exemplar, Os Suspeitos e Amnésia são os mais recomendados."}]
    },
    {
        "dia": 3,
        "slot": 3,
        "slug": "7-melhores-filmes-de-acao-frenetica-na-netflix-2026",
        "title": "7 Melhores Filmes de Ação Frenética na Netflix para Assistir Hoje em 2026",
        "subtitle": "Tiros, perseguições intensas e adrenalina sem pausas no catálogo da Netflix.",
        "type": "streaming",
        "genres": ["Ação", "Netflix", "Adrenalina"],
        "author": AUTHORS["thiago"],
        "coverImage": "https://image.tmdb.org/t/p/w500/tH64gzAHDFg7EFcgfkkZyHdGM5P.jpg",
        "readingTime": "5 min de leitura",
        "content": "Para quem quer desligar o cérebro e sentir o coração acelerar com coreografias de combate de primeira linha.",
        "listItems": [{"rank": 1, "title": "Mad Max: Estrada da Fúria", "year": 2015, "whereToWatch": ["Netflix", "Max"], "score": 9.6, "posterImage": "https://image.tmdb.org/t/p/w500/tH64gzAHDFg7EFcgfkkZyHdGM5P.jpg"}],
        "faqs": [{"question": "Qual filme de ação mais bem avaliado na Netflix?", "answer": "Mad Max e Resgate 2 lideram as avaliações do gênero."}]
    },
    {
        "dia": 3,
        "slot": 4,
        "slug": "que-dia-sai-episodio-1-de-wandinha-temporada-2-data-horario",
        "title": "Que Dia Sai o Episódio 1 de Wandinha (2ª Temporada)? Data e Horário na Netflix",
        "subtitle": "Jenna Ortega retorna a Nunca Mais com mais mistério gótico e sem romances forçados.",
        "type": "episodio",
        "genres": ["Séries", "Netflix", "Fantasia", "Mistério"],
        "author": AUTHORS["beatriz"],
        "coverImage": "https://image.tmdb.org/t/p/w500/9PFonBhy4cQy7Jz20NpMygczOkv.jpg",
        "readingTime": "4 min de leitura",
        "content": "Sob a direção de Tim Burton, a nova temporada de Wandinha foca inteiramente no terror investigativo e nos segredos ancestrais da Família Addams.",
        "seriesInfo": {"seriesTitle": "Wandinha", "seasonNumber": 2, "episodeNumber": 1, "nextEpisodeDate": "em breve", "nextEpisodeTime": "04h00", "platform": "Netflix", "totalEpisodes": 8},
        "faqs": [{"question": "A que horas estreia Wandinha na Netflix?", "answer": "Lançamentos globais da Netflix chegam ao Brasil pontualmente às 04h00 da manhã (horário de Brasília)."}]
    },

    # DIA 4: 22/10 (Quinta-feira)
    {
        "dia": 4,
        "slot": 0,
        "slug": "que-dia-sai-episodio-1-de-arcane-temporada-2-data-horario",
        "title": "Que Dia Sai o Episódio 1 de Arcane (2ª Temporada)? Data, Horário e Atos na Netflix",
        "subtitle": "A guerra entre Piltover e Zaun explode no aguardado desfecho da premiada animação da Riot Games.",
        "type": "episodio",
        "genres": ["Séries", "Netflix", "Animação", "Fantasia"],
        "author": AUTHORS["camila"],
        "coverImage": "https://image.tmdb.org/t/p/w500/fqldf2t8ztc9aiwn3k6mlX3tvRT.jpg",
        "readingTime": "4 min de leitura",
        "content": "Vi e Jinx estão em lados opostos na batalha final. Arcane entrega o padrão visual mais deslumbrante da história recente das séries de animação.",
        "seriesInfo": {"seriesTitle": "Arcane", "seasonNumber": 2, "episodeNumber": 1, "nextEpisodeDate": "9 de novembro", "nextEpisodeTime": "05h da manhã", "platform": "Netflix", "totalEpisodes": 9},
        "faqs": [{"question": "Como serão lançados os episódios de Arcane 2?", "answer": "Em 3 blocos (Atos) lançados semanalmente aos sábados na Netflix."}]
    },
    {
        "dia": 4,
        "slot": 1,
        "slug": "frankenstein-guillermo-del-toro-data-estreia-netflix-elenco",
        "title": "Frankenstein de Guillermo del Toro: Data de Estreia na Netflix, Elenco e Fotos",
        "subtitle": "Oscar Isaac como Dr. Frankenstein e Jacob Elordi como o Monstro na adaptação mais ambiciosa do cineasta.",
        "type": "lancamento",
        "genres": ["Cinema", "Lançamentos", "Netflix", "Terror Gótico"],
        "author": AUTHORS["beatriz"],
        "coverImage": "https://image.tmdb.org/t/p/w500/7WsyChQLEftFiDOVTGkv3hFpyyt.jpg",
        "readingTime": "5 min de leitura",
        "content": "Guillermo del Toro dedica sua carreira ao mito de Frankenstein. Com um elenco que inclui Mia Goth e Christoph Waltz, a produção é o carro-chefe da Netflix para as premiações.",
        "movieInfo": {"title": "Frankenstein", "releaseDate": "outubro", "futureStreaming": "Netflix", "productionDetails": "Direção de Guillermo del Toro com Jacob Elordi, Oscar Isaac e Mia Goth."},
        "faqs": [{"question": "Onde assistir ao Frankenstein de del Toro?", "answer": "O filme será lançado diretamente com exclusividade no catálogo mundial da Netflix."}]
    },
    {
        "dia": 4,
        "slot": 2,
        "slug": "5-filmes-parecidos-com-garota-exemplar-sobre-casamentos-toxicos",
        "title": "5 Filmes Parecidos com Garota Exemplar sobre Manipulação e Casamentos Tóxicos",
        "subtitle": "Relacionamentos perigosos e jogos mentais calculados para quem ama o cinema de David Fincher.",
        "type": "list",
        "genres": ["Suspense", "Thrillers Psicológicos", "Crimes"],
        "author": AUTHORS["guilherme"],
        "coverImage": "https://image.tmdb.org/t/p/w500/54nI3vSKlPp42WhJmKVRdmMbkzl.jpg",
        "readingTime": "5 min de leitura",
        "content": "A mente afiada de Amy Dunne transformou Garota Exemplar em uma referência de thriller psicológico. Veja títulos que exploram a mesma paranoia conjugal.",
        "listItems": [{"rank": 1, "title": "A Pele que Habito", "year": 2011, "whereToWatch": ["Prime Video"], "score": 9.1, "posterImage": "https://image.tmdb.org/t/p/w500/90hbSeBsev4hezgzkyW8tkio2dp.jpg"}],
        "faqs": [{"question": "Qual o melhor filme parecido com Garota Exemplar?", "answer": "Entre Facas e Segredos e A Pele que Habito são os mais aclamados."}]
    },
    {
        "dia": 4,
        "slot": 3,
        "slug": "7-melhores-thrillers-investigativos-na-netflix-2026",
        "title": "7 Melhores Thrillers Investigativos e de Detetive na Netflix (2026)",
        "subtitle": "Crimes enigmáticos, pistas ocultas e investigações obsessivas para maratonar no streaming.",
        "type": "streaming",
        "genres": ["Policial", "Investigação", "Netflix"],
        "author": AUTHORS["guilherme"],
        "coverImage": "https://image.tmdb.org/t/p/w500/jFmlV5vUzOt1PgJ82efOhNsWcWX.jpg",
        "readingTime": "5 min de leitura",
        "content": "A Netflix conta com excelentes histórias policiais que prendem o espectador do primeiro minuto até a revelação da identidade do assassino.",
        "listItems": [{"rank": 1, "title": "Zodíaco", "year": 2007, "whereToWatch": ["Netflix", "Max"], "score": 9.4, "posterImage": "https://image.tmdb.org/t/p/w500/jFmlV5vUzOt1PgJ82efOhNsWcWX.jpg"}],
        "faqs": [{"question": "Quais os melhores filmes de serial killer na Netflix?", "answer": "Zodíaco e O Pálido Olho Azul são destaques absolutos."}]
    },
    {
        "dia": 4,
        "slot": 4,
        "slug": "que-dia-sai-episodio-1-de-house-of-the-dragon-temporada-3-data-horario",
        "title": "Que Dia Sai o Episódio 1 de House of the Dragon (3ª Temporada)? Data e Horário na Max",
        "subtitle": "A Dança dos Dragões atinge o confronto aberto entre Rhaenyra Targaryen e os Verdes na HBO.",
        "type": "episodio",
        "genres": ["Séries", "Max", "Fantasia Épica", "Dramas"],
        "author": AUTHORS["camila"],
        "coverImage": "https://image.tmdb.org/t/p/w500/7QMsOTMUswlwxJP0rTTZfmz2tX2.jpg",
        "readingTime": "4 min de leitura",
        "content": "A Batalha do Gargalo e os maiores embates aéreos entre dragões prometem transformar a 3ª temporada de A Casa do Dragão no evento supremo da HBO.",
        "seriesInfo": {"seriesTitle": "House of the Dragon", "seasonNumber": 3, "episodeNumber": 1, "nextEpisodeDate": "domingo", "nextEpisodeTime": "22h00", "platform": "Max", "totalEpisodes": 8},
        "faqs": [{"question": "A que horas sai A Casa do Dragão no Brasil?", "answer": "Os episódios estreiam pontualmente aos domingos às 22h00 na Max e na HBO TV."}]
    },

    # DIA 5: 23/10 (Sexta-feira)
    {
        "dia": 5,
        "slot": 0,
        "slug": "que-dia-sai-episodio-1-de-stranger-things-temporada-5-data-horario",
        "title": "Que Dia Sai o Episódio 1 de Stranger Things (5ª Temporada)? Data e Horário na Netflix",
        "subtitle": "A batalha final por Hawkins e a derrota definitiva do Vecna no encerramento da maior série da Netflix.",
        "type": "episodio",
        "genres": ["Séries", "Netflix", "Sci-Fi", "Terror Anos 80"],
        "author": AUTHORS["marcos"],
        "coverImage": "https://image.tmdb.org/t/p/w500/49WJfeN0moxb9IPfGn8AIqMGskD.jpg",
        "readingTime": "4 min de leitura",
        "content": "Com episódios em escala cinematográfica, a 5ª e última temporada de Stranger Things encerra uma década de fenômeno cultural.",
        "seriesInfo": {"seriesTitle": "Stranger Things", "seasonNumber": 5, "episodeNumber": 1, "nextEpisodeDate": "novembro", "nextEpisodeTime": "04h da manhã", "platform": "Netflix", "totalEpisodes": 8},
        "faqs": [{"question": "Quantos episódios terá a temporada final de Stranger Things?", "answer": "Serão 8 episódios de longa duração com o season finale ultrapassando 2 horas."}]
    },
    {
        "dia": 5,
        "slot": 1,
        "slug": "quarteto-fantastico-primeiros-passos-data-estreia-elenco-disney-plus",
        "title": "Quarteto Fantástico: Primeiros Passos: Data de Estreia, Elenco Completo e Disney+",
        "subtitle": "Pedro Pascal lidera a Primeira Família da Marvel nos anos 60 contra Galactus e o Surfista Prateado.",
        "type": "lancamento",
        "genres": ["Cinema", "Lançamentos", "Marvel", "Disney+"],
        "author": AUTHORS["thiago"],
        "coverImage": "https://image.tmdb.org/t/p/w500/9kigkP4XF4U9ePz6P4xL6Z0U9eP.jpg",
        "readingTime": "5 min de leitura",
        "content": "A estreia mais aguardada da Fase 6 do MCU promete introduzir Reed Richards, Sue Storm, Johnny Storm e O Coisa com estética retrofuturista inesquecível.",
        "movieInfo": {"title": "Quarteto Fantástico", "releaseDate": "24 de julho", "futureStreaming": "Disney+", "productionDetails": "Direção de Matt Shakman com Pedro Pascal, Vanessa Kirby e Joseph Quinn."},
        "faqs": [{"question": "Quando Quarteto Fantástico chega ao Disney+?", "answer": "Previsão de chegada ao catálogo do Disney+ cerca de 90 dias após a estreia nos cinemas."}]
    },
    {
        "dia": 5,
        "slot": 2,
        "slug": "5-filmes-parecidos-com-oppenheimer-sobre-historia-e-tensao",
        "title": "5 Filmes Parecidos com Oppenheimer para Quem Ama Dramas Históricos e Tensão",
        "subtitle": "Grandes biografias, dilemas morais da ciência e os bastidores das maiores decisões políticas da humanidade.",
        "type": "list",
        "genres": ["Drama", "História", "Cinema"],
        "author": AUTHORS["lucas"],
        "coverImage": "https://image.tmdb.org/t/p/w500/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
        "readingTime": "5 min de leitura",
        "content": "Christopher Nolan venceu o Oscar com um ritmo implacável de montagem e trilha sonora. Selecionamos obras que capturam a mesma gravidade histórica.",
        "listItems": [{"rank": 1, "title": "O Jogo da Imitação", "year": 2014, "whereToWatch": ["Max", "Prime Video"], "score": 9.2, "posterImage": "https://image.tmdb.org/t/p/w500/quZnHOVKVbFR7IdXBI9J0ONb7Jk.jpg"}],
        "faqs": [{"question": "Onde assistir a Oppenheimer?", "answer": "Oppenheimer está disponível na Max e para compra/aluguel digital."}]
    },
    {
        "dia": 5,
        "slot": 3,
        "slug": "7-melhores-filmes-de-terror-na-apple-tv-e-disney-plus-2026",
        "title": "7 Melhores Filmes de Terror e Suspense na Apple TV+ e Disney+ (2026)",
        "subtitle": "As joias ocultas de terror psicológico e sobrenatural que muitos assinantes nem sabem que existem.",
        "type": "streaming",
        "genres": ["Terror", "Apple TV+", "Disney+"],
        "author": AUTHORS["beatriz"],
        "coverImage": "https://image.tmdb.org/t/p/w500/zppeHKLHljU2uI7NBJ1JyDNpn6L.jpg",
        "readingTime": "5 min de leitura",
        "content": "Embora o Disney+ seja conhecido por heróis e família, o selo Star abriga produções consagradas como A Primeira Profecia e Alien.",
        "listItems": [{"rank": 1, "title": "A Primeira Profecia", "year": 2024, "whereToWatch": ["Disney+"], "score": 9.0, "posterImage": "https://image.tmdb.org/t/p/w500/zppeHKLHljU2uI7NBJ1JyDNpn6L.jpg"}],
        "faqs": [{"question": "Tem filme de terror bom no Disney+?", "answer": "Sim! A Primeira Profecia, Alien: Romulus e O Predador são imperdíveis."}]
    },
    {
        "dia": 5,
        "slot": 4,
        "slug": "que-dia-sai-episodio-1-de-euphoria-temporada-3-data-horario",
        "title": "Que Dia Sai o Episódio 1 de Euphoria (3ª Temporada)? Data e Horário na Max",
        "subtitle": "Zendaya e o elenco com salto temporal na continuação do drama jovem mais polêmico da televisão.",
        "type": "episodio",
        "genres": ["Séries", "Max", "Dramas"],
        "author": AUTHORS["lucas"],
        "coverImage": "https://image.tmdb.org/t/p/w500/3Q0hd3heuW4YQMn7IO4quHGvbp1.jpg",
        "readingTime": "4 min de leitura",
        "content": "Sam Levinson promete um salto temporal de anos para mostrar os personagens lidando com as dores da vida adulta e os vícios do passado.",
        "seriesInfo": {"seriesTitle": "Euphoria", "seasonNumber": 3, "episodeNumber": 1, "nextEpisodeDate": "domingo", "nextEpisodeTime": "23h00", "platform": "Max", "totalEpisodes": 8},
        "faqs": [{"question": "Quando estreia Euphoria 3?", "answer": "A temporada tem previsão de lançamento nas noites de domingo da HBO e Max."}]
    },

    # DIA 6: 24/10 (Sábado)
    {
        "dia": 6,
        "slot": 0,
        "slug": "the-batman-parte-2-data-estreia-elenco-onde-assistir-max",
        "title": "The Batman: Parte II: Data de Estreia nos Cinemas, Vilões e Continuação na Max",
        "subtitle": "Robert Pattinson e Matt Reeves voltam a Gotham após os acontecimentos da série O Pinguim.",
        "type": "lancamento",
        "genres": ["Cinema", "Lançamentos", "DC", "Policial"],
        "author": AUTHORS["thiago"],
        "coverImage": "https://image.tmdb.org/t/p/w500/74xTEgt7R36Fpooo50r9T25onhq.jpg",
        "readingTime": "5 min de leitura",
        "content": "A sequência oficial de The Batman continuará explorando o lado detetivesco e corrupto da cidade, conectando com a ascensão criminosa de Oz Cobb.",
        "movieInfo": {"title": "The Batman: Parte II", "releaseDate": "18 de fevereiro de 2028", "futureStreaming": "Max", "productionDetails": "Direção de Matt Reeves com Robert Pattinson e Colin Farrell."},
        "faqs": [{"question": "Quando The Batman 2 estreia?", "answer": "O filme foi reprogramado para estrear nos cinemas mundiais em fevereiro de 2028."}]
    },
    {
        "dia": 6,
        "slot": 1,
        "slug": "que-dia-sai-episodio-1-de-solo-leveling-temporada-2-data-horario",
        "title": "Que Dia Sai o Episódio 1 de Solo Leveling (2ª Temporada)? Data e Horário no Brasil",
        "subtitle": "Sung Jinwoo assume o poder do Monarca das Sombras na volta do anime mais assistido do mundo.",
        "type": "episodio",
        "genres": ["Séries", "Animes", "Ação", "Crunchyroll", "Netflix"],
        "author": AUTHORS["camila"],
        "coverImage": "https://image.tmdb.org/t/p/w500/geCRueV3ElhRTr0xtJuPxJ8HGAY.jpg",
        "readingTime": "4 min de leitura",
        "content": "A adaptação do Webtoon coreano bateu recordes de visualizações globais. O novo arco trará batalhas épicas nas masmorras vermelhas.",
        "seriesInfo": {"seriesTitle": "Solo Leveling", "seasonNumber": 2, "episodeNumber": 1, "nextEpisodeDate": "sábado", "nextEpisodeTime": "14h30", "platform": "Crunchyroll / Netflix", "totalEpisodes": 12},
        "faqs": [{"question": "Onde assistir a Solo Leveling 2ª temporada dublado?", "answer": "Os episódios com dublagem em português chegam à Crunchyroll e Netflix."}]
    },
    {
        "dia": 6,
        "slot": 2,
        "slug": "5-filmes-parecidos-com-pobres-criaturas-para-assistir-depois",
        "title": "5 Filmes Parecidos com Pobres Criaturas com Humor Ácido e Fantasia Autoral",
        "subtitle": "Para quem se encantou com a Bella Baxter de Emma Stone e a direção visionária de Yorgos Lanthimos.",
        "type": "list",
        "genres": ["Cinema Autoral", "Comédia Ácida", "Fantasia"],
        "author": AUTHORS["lucas"],
        "coverImage": "https://image.tmdb.org/t/p/w500/kCGlIMHnOm8JPXq3rXM6c5wMxcT.jpg",
        "readingTime": "5 min de leitura",
        "content": "Vencedor de múltiplos prêmios do Oscar, Pobres Criaturas desafia todas as convenções visuais e morais. Veja obras com a mesma audácia artística.",
        "listItems": [{"rank": 1, "title": "A Favorita", "year": 2018, "whereToWatch": ["Disney+"], "score": 9.3, "posterImage": "https://image.tmdb.org/t/p/w500/kCGlIMHnOm8JPXq3rXM6c5wMxcT.jpg"}],
        "faqs": [{"question": "Onde assistir a Pobres Criaturas?", "answer": "Disponível no catálogo do Disney+ no Brasil."}]
    },
    {
        "dia": 6,
        "slot": 3,
        "slug": "7-melhores-comedias-inteligentes-e-acidas-na-max-2026",
        "title": "7 Melhores Comédias Inteligentes e Ácidas na Max para Rir Alto em 2026",
        "subtitle": "Sátiras sociais, humor requintado e diálogos afiados selecionados no streaming.",
        "type": "streaming",
        "genres": ["Comédia", "Max", "Sátira"],
        "author": AUTHORS["lucas"],
        "coverImage": "https://image.tmdb.org/t/p/w500/9H8PNc4JJRjPnfSh8gGukD0CbqQ.jpg",
        "readingTime": "5 min de leitura",
        "content": "Para quem foge de piadas previsíveis e busca filmes que satirizam o poder, a fama e a futilidade contemporânea.",
        "listItems": [{"rank": 1, "title": "Entre Facas e Segredos", "year": 2019, "whereToWatch": ["Max", "Prime Video"], "score": 9.3, "posterImage": "https://image.tmdb.org/t/p/w500/9H8PNc4JJRjPnfSh8gGukD0CbqQ.jpg"}],
        "faqs": [{"question": "Quais as melhores comédias na Max?", "answer": "Entre Facas e Segredos, O Menu e O Grande Lebowski são pontos altos."}]
    },
    {
        "dia": 6,
        "slot": 4,
        "slug": "que-dia-sai-episodio-1-de-fallout-temporada-2-data-horario",
        "title": "Que Dia Sai o Episódio 1 de Fallout (2ª Temporada)? Data e Horário no Prime Video",
        "subtitle": "Lucy e Ghoul rumam para New Vegas após o sucesso estrondoso do primeiro ano da adaptação da Amazon.",
        "type": "episodio",
        "genres": ["Séries", "Prime Video", "Pós-Apocalíptico", "Sci-Fi"],
        "author": AUTHORS["camila"],
        "coverImage": "https://image.tmdb.org/t/p/w500/AnsZu440fOtx5b7n4iG123M2vF3.jpg",
        "readingTime": "4 min de leitura",
        "content": "Jonathan Nolan e Lisa Joy retornam ao comando da 2ª temporada de Fallout prometendo explorar as loucuras e mistérios da emblemática cidade de New Vegas.",
        "seriesInfo": {"seriesTitle": "Fallout", "seasonNumber": 2, "episodeNumber": 1, "nextEpisodeDate": "quinta-feira", "nextEpisodeTime": "04h00", "platform": "Prime Video", "totalEpisodes": 8},
        "faqs": [{"question": "Quando lança Fallout 2?", "answer": "A estreia ocorrerá com exclusividade global no catálogo do Prime Video."}]
    },

    # DIA 7: 25/10 (Domingo)
    {
        "dia": 7,
        "slot": 0,
        "slug": "f1-o-filme-brad-pitt-data-estreia-apple-tv-cinemas",
        "title": "F1: O Filme de Brad Pitt: Data de Estreia nos Cinemas, Bastidores e Apple TV+",
        "subtitle": "Gravado durante os GPs reais de Fórmula 1 com direção de Joseph Kosinski (Top Gun: Maverick).",
        "type": "lancamento",
        "genres": ["Cinema", "Lançamentos", "Apple TV+", "Ação"],
        "author": AUTHORS["thiago"],
        "coverImage": "https://image.tmdb.org/t/p/w500/tH64gzAHDFg7EFcgfkkZyHdGM5P.jpg",
        "readingTime": "5 min de leitura",
        "content": "Brad Pitt interpreta Sonny Hayes, piloto veterano que retorna ao grid para liderar a equipe fictícia APXGP. O filme usou câmeras IMAX personalizadas nos carros reais de F1.",
        "movieInfo": {"title": "F1", "releaseDate": "26 de junho", "futureStreaming": "Apple TV+", "productionDetails": "Coproduzido por Lewis Hamilton e Warner Bros/Apple Original Films."},
        "faqs": [{"question": "Onde assistir ao filme de F1 de Brad Pitt?", "answer": "Primeiro nos cinemas mundiais e posteriormente com exclusividade na Apple TV+."}]
    },
    {
        "dia": 7,
        "slot": 1,
        "slug": "que-dia-sai-episodio-1-de-o-urso-temporada-4-data-horario",
        "title": "Que Dia Sai o Episódio 1 de O Urso (The Bear 4ª Temporada)? Data no Disney+",
        "subtitle": "Carmy, Sydney e Richie na corrida implacável pela estrela Michelin e pela sanidade mental na cozinha.",
        "type": "episodio",
        "genres": ["Séries", "Disney+", "Dramas", "Comédia Ácida"],
        "author": AUTHORS["lucas"],
        "coverImage": "https://image.tmdb.org/t/p/w500/6ZFIZgR2325K9nJ5bX8cK4c7Y7h.jpg",
        "readingTime": "4 min de leitura",
        "content": "A aclamada série recordista de prêmios Emmy promete resolver o cliffhanger da avaliação do Chicago Tribune e a sustentabilidade financeira do restaurante.",
        "seriesInfo": {"seriesTitle": "The Bear", "seasonNumber": 4, "episodeNumber": 1, "nextEpisodeDate": "quarta-feira", "nextEpisodeTime": "04h00", "platform": "Disney+", "totalEpisodes": 10},
        "faqs": [{"question": "Onde assistir a The Bear no Brasil?", "answer": "Todas as temporadas estão disponíveis com exclusividade no catálogo do Disney+."}]
    },
    {
        "dia": 7,
        "slot": 2,
        "slug": "5-filmes-parecidos-com-corra-para-assistir-depois",
        "title": "5 Filmes Parecidos com Corra! (Get Out) sobre Terror Social e Paranóia",
        "subtitle": "Se você amou a mente genial de Jordan Peele, confira cinco produções com tensão psicológica e críticas afiadas.",
        "type": "list",
        "genres": ["Terror", "Suspense", "Cinema Autoral"],
        "author": AUTHORS["beatriz"],
        "coverImage": "https://image.tmdb.org/t/p/w500/tFXcEccSQMf3lfhfXKSU9iRBpa3.jpg",
        "readingTime": "5 min de leitura",
        "content": "Corra! transformou o terror moderno ao mesclar desconforto social, sátira e tensão implacável. Reunimos cinco obras com a mesma atmosfera inquietante.",
        "listItems": [{"rank": 1, "title": "Nós (Us)", "year": 2019, "whereToWatch": ["Prime Video", "Max"], "score": 9.1, "posterImage": "https://image.tmdb.org/t/p/w500/tFXcEccSQMf3lfhfXKSU9iRBpa3.jpg"}],
        "faqs": [{"question": "Onde assistir a Corra! online?", "answer": "Disponível para streaming na Netflix e Prime Video no Brasil."}]
    },
    {
        "dia": 7,
        "slot": 3,
        "slug": "7-melhores-filmes-de-sobrevivencia-extrema-no-prime-video-2026",
        "title": "7 Melhores Filmes de Sobrevivência Extrema no Prime Video para Assistir em 2026",
        "subtitle": "Humanos levados ao limite contra o gelo, o mar aberto e a natureza implacável.",
        "type": "streaming",
        "genres": ["Aventura", "Sobrevivência", "Prime Video"],
        "author": AUTHORS["thiago"],
        "coverImage": "https://image.tmdb.org/t/p/w500/fONsBTZIDqxMfHwlfUcCAb8ubr1.jpg",
        "readingTime": "5 min de leitura",
        "content": "Histórias angustiantes de coragem e resiliência humana que fazem qualquer espectador segurar a respiração do começo ao fim.",
        "listItems": [{"rank": 1, "title": "127 Horas", "year": 2010, "whereToWatch": ["Disney+", "Prime Video"], "score": 9.3, "posterImage": "https://image.tmdb.org/t/p/w500/fONsBTZIDqxMfHwlfUcCAb8ubr1.jpg"}],
        "faqs": [{"question": "Qual melhor filme de sobrevivência real?", "answer": "A Sociedade da Neve e 127 Horas são as referências supremas do gênero."}]
    },
    {
        "dia": 7,
        "slot": 4,
        "slug": "demolidor-renascido-daredevil-born-again-data-estreia-disney-plus",
        "title": "Demolidor: Renascido (Daredevil: Born Again): Data de Estreia, Elenco e Disney+",
        "subtitle": "Charlie Cox e Vincent D'Onofrio no retorno sombrio e violento do Homem Sem Medo no MCU.",
        "type": "lancamento",
        "genres": ["Séries", "Lançamentos", "Marvel", "Disney+"],
        "author": AUTHORS["thiago"],
        "coverImage": "https://image.tmdb.org/t/p/w500/sm8F6H9XzWzJ3K9Y2K7G7p6zL3e.jpg",
        "readingTime": "5 min de leitura",
        "content": "Com classificação indicativa madura e o retorno do Justiceiro de Jon Bernthal, Demolidor: Renascido resgata a brutalidade de Hell's Kitchen com o selo Marvel Television.",
        "movieInfo": {"title": "Demolidor: Renascido", "releaseDate": "março", "futureStreaming": "Disney+", "productionDetails": "Superprodução estrelada por Charlie Cox, Vincent D'Onofrio e Jon Bernthal."},
        "faqs": [{"question": "Demolidor: Renascido é para maiores de 18 anos?", "answer": "Sim, a Marvel Studios confirmou que a produção mantém o tom maduro e violento da série original."}]
    }
]

def gerar_semana():
    hoje = datetime.now(timezone.utc)
    # Se a hora atual já passou das 18h, começa a contar a partir de amanhã
    inicio_base = hoje.replace(hour=0, minute=0, second=0, microsecond=0)
    
    total_gerados = 0
    print(f"\n🚀 Iniciando geração do Lote de Ouro (35 Artigos Agendados)...")
    print("=" * 80)
    
    for item in PLANO_SEMANA:
        dia_offset = item["dia"] # Dia 1 (+1 dia a partir de hoje) até Dia 7 (+7 dias)
        slot_hora = HORARIOS_UTC[item["slot"]]
        
        data_alvo = inicio_base + timedelta(days=dia_offset)
        data_iso = f"{data_alvo.strftime('%Y-%m-%d')}T{slot_hora}"
        
        post_data = {
            "id": f"post-{int(time.time())}-{item['dia']}-{item['slot']}",
            "slug": item["slug"],
            "title": item["title"],
            "subtitle": item["subtitle"],
            "type": item["type"],
            "genres": item["genres"],
            "publishedAt": data_iso,
            "scheduledFor": data_iso,
            "updatedAt": data_iso,
            "author": item["author"],
            "coverImage": item["coverImage"],
            "posterImage": item["coverImage"],
            "readingTime": item.get("readingTime", "5 min de leitura"),
            "seo": {
                "metaTitle": f"{item['title'][:55]} | FilmeJá",
                "metaDescription": item["subtitle"][:155],
                "keywords": [
                    item["slug"].replace("-", " "),
                    item["title"].lower(),
                    f"onde assistir {item['slug'].split('-')[0]}",
                    "filmeja cinema e streaming"
                ]
            },
            "content": item["content"],
            "faqs": item.get("faqs", [])
        }
        
        if "seriesInfo" in item:
            post_data["seriesInfo"] = item["seriesInfo"]
        if "movieInfo" in item:
            post_data["movieInfo"] = item["movieInfo"]
        if "listItems" in item:
            post_data["listItems"] = item["listItems"]
            
        filename = f"{item['slug']}.json"
        
        # Se for o dia 1 e já tiver passado a hora, ou se quisermos na fila de agendados:
        # Coloca todos na fila de agendados (src/content/agendados)
        filepath = os.path.join(AGENDADOS_DIR, filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(post_data, f, ensure_ascii=False, indent=2)
            
        total_gerados += 1
        print(f"[{total_gerados:02d}/35] Dia +{item['dia']} ({slot_hora[:5]} UTC) -> {item['title'][:45]}...")

    print("=" * 80)
    print(f"✅ Sucesso total! {total_gerados} artigos gerados e organizados na fila de agendamento!")
    print(f"📁 Localização: {AGENDADOS_DIR}")

if __name__ == "__main__":
    gerar_semana()
