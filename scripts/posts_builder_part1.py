"""
Script Mestre: Geração e Agendamento da Semana de Ouro (35 Artigos Completos)
FilmeJá (filmeja.com.br)
"""

import os
import sys
import json
from datetime import datetime, timezone, timedelta

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENDADOS_DIR = os.path.join(PROJECT_ROOT, "src", "content", "agendados")
os.makedirs(AGENDADOS_DIR, exist_ok=True)

from data_35_posts import AUTHORS, P

# Grade de Horários diários (BRT: 08:00, 12:00, 16:00, 19:30, 22:00)
HORARIOS_UTC = ["11:00:00Z", "15:00:00Z", "19:00:00Z", "22:30:00Z", "23:59:00Z"]

def data_iso(dia_idx: int, slot_idx: int) -> str:
    dt = datetime(2026, 10, 19, tzinfo=timezone.utc) + timedelta(days=dia_idx)
    return f"{dt.strftime('%Y-%m-%d')}T{HORARIOS_UTC[slot_idx]}"

posts = []

# ==============================================================================
# DIA 1: 19/10/2026 (Segunda-feira)
# ==============================================================================

# 1. Silo Temp 2 Ep 1 (Episódio)
posts.append({
    "id": "post-semana-ouro-01",
    "slug": "que-dia-sai-episodio-1-de-silo-temporada-2-data-horario",
    "title": "Que Dia Sai o Episódio 1 de Silo (2ª Temporada)? Data e Horário na Apple TV+",
    "subtitle": "Confira o retorno da distopia subterrânea com Rebecca Ferguson, cronograma de episódios no Brasil e o que esperar do lado de fora.",
    "type": "episodio",
    "genres": ["Séries", "Apple TV+", "Ficção Científica", "Lançamentos"],
    "publishedAt": data_iso(0, 0),
    "scheduledFor": data_iso(0, 0),
    "updatedAt": data_iso(0, 0),
    "author": AUTHORS["marcos"],
    "coverImage": P["silo"],
    "posterImage": P["silo"],
    "readingTime": "5 min de leitura",
    "seo": {
        "metaTitle": "Que Dia Sai Episódio 1 de Silo (2ª Temp)? Data e Horário | FilmeJá",
        "metaDescription": "Saiba que dia e que horas estreia o episódio 1 da 2ª temporada de Silo na Apple TV+. Confira o cronograma completo no Brasil e teorias.",
        "keywords": ["que dia sai silo temporada 2", "silo episodio 1 data", "silo horario apple tv brasil", "silo rebecca ferguson onde assistir"]
    },
    "content": """A 2ª temporada de **Silo** é uma das estreias mais aguardadas da ficção científica mundial no catálogo da Apple TV+. Após o final eletrizante da primeira temporada, quando Juliette Nichols (interpretada de maneira brilhante por Rebecca Ferguson) finalmente ultrapassou a colina e descobriu dezenas de outros silos espalhados pelo horizonte devastado, o público brasileiro busca saber com exatidão que dia e a que horas os novos episódios chegam ao streaming.

A trama agora se expande para além do confinamento dos 144 andares do silo original. Enquanto Juliette enfrenta os perigos imediatos da atmosfera tóxica e busca abrigo em uma estrutura aparentemente abandonada, os moradores do Silo 18 entram em colapso social após testemunharem que a limpeza não ocorreu como as autoridades do Judiciário previam. Bernard Holland (Tim Robbins) e Robert Sims (Common) precisarão tomar medidas drásticas para conter a rebelião popular iminente.

Como é padrão nas grandes séries originais da Apple TV+, os episódios não são lançados todos de uma vez: a plataforma adota o modelo de **lançamento semanal toda sexta-feira**, incentivando discussões e teorias que mantêm a audiência conectada do início ao fim da temporada. Prepare-se para respostas reveladoras sobre a fundação dos silos, o pacto original e o destino da humanidade.""",
    "seriesInfo": {
        "seriesTitle": "Silo",
        "originalTitle": "Silo",
        "seasonNumber": 2,
        "episodeNumber": 1,
        "nextEpisodeDate": "15 de novembro",
        "nextEpisodeTime": "05h00 da manhã (Horário de Brasília)",
        "platform": "Apple TV+",
        "totalEpisodes": 10,
        "recapPreviousEpisode": "No clímax da 1ª temporada, Juliette Nichols sobrevive à limpeza graças à fita adesiva especial providenciada pela equipe de suprimentos mecânicos, descobrindo que o mundo exterior é cercado por incontáveis outros silos.",
        "whatToExpect": "Juliette explora um silo vizinho em ruínas em busca de oxigênio e respostas, enquanto Bernard enfrenta protestos maciços no Silo 18 contra o controle autoritário do Judiciário.",
        "schedule": [
            {"episodeNumber": 1, "title": "O Engenheiro", "releaseDate": "15/11", "releaseTime": "05:00 BRT", "status": "proximo"},
            {"episodeNumber": 2, "title": "Ordem e Caos", "releaseDate": "22/11", "releaseTime": "05:00 BRT", "status": "a_estrear"},
            {"episodeNumber": 3, "title": "Relíquia", "releaseDate": "29/11", "releaseTime": "05:00 BRT", "status": "a_estrear"},
            {"episodeNumber": 4, "title": "A Chave Mestra", "releaseDate": "06/12", "releaseTime": "05:00 BRT", "status": "a_estrear"},
            {"episodeNumber": 5, "title": "Frequência Sombria", "releaseDate": "13/12", "releaseTime": "05:00 BRT", "status": "a_estrear"},
            {"episodeNumber": 6, "title": "O Silo Vizinho", "releaseDate": "20/12", "releaseTime": "05:00 BRT", "status": "a_estrear"},
            {"episodeNumber": 7, "title": "A Queda", "releaseDate": "27/12", "releaseTime": "05:00 BRT", "status": "a_estrear"},
            {"episodeNumber": 8, "title": "Legado Tóxico", "releaseDate": "03/01", "releaseTime": "05:00 BRT", "status": "a_estrear"},
            {"episodeNumber": 9, "title": "Ponto Sem Retorno", "releaseDate": "10/01", "releaseTime": "05:00 BRT", "status": "a_estrear"},
            {"episodeNumber": 10, "title": "A Verdade Revelada", "releaseDate": "17/01", "releaseTime": "05:00 BRT", "status": "a_estrear"}
        ]
    },
    "faqs": [
        {"question": "Que dia da semana sai o novo episódio de Silo?", "answer": "Os episódios da 2ª temporada de Silo saem semanalmente às sextas-feiras no catálogo da Apple TV+."},
        {"question": "A que horas Silo é liberado no streaming no Brasil?", "answer": "Os episódios são liberados pontualmente às 05h00 da manhã (horário de Brasília), com dublagem e legendas em português."},
        {"question": "Quantos episódios tem a 2ª temporada de Silo?", "answer": "A segunda temporada é composta por 10 episódios inéditos produzidos pela Apple TV+."}
    ]
})

# 2. Superman James Gunn (Lançamento)
posts.append({
    "id": "post-semana-ouro-02",
    "slug": "superman-james-gunn-data-estreia-elenco-onde-assistir",
    "title": "Superman (2025): Data de Estreia nos Cinemas, Elenco e Onde Assistir",
    "subtitle": "Tudo sobre o renascimento do Homem de Aço sob a direção de James Gunn: David Corenswet, Rachel Brosnahan e a previsão de chegada à Max.",
    "type": "lancamento",
    "genres": ["Cinema", "Lançamentos", "DC", "Max", "Blockbusters"],
    "publishedAt": data_iso(0, 1),
    "scheduledFor": data_iso(0, 1),
    "updatedAt": data_iso(0, 1),
    "author": AUTHORS["thiago"],
    "coverImage": P["superman"],
    "posterImage": P["superman"],
    "readingTime": "5 min de leitura",
    "seo": {
        "metaTitle": "Superman (2025): Data de Estreia nos Cinemas e Onde Assistir | FilmeJá",
        "metaDescription": "Saiba quando estreia Superman nos cinemas do Brasil. Veja o elenco oficial de James Gunn, detalhes de Metrópoles e previsão de lançamento na Max.",
        "keywords": ["superman data de estreia brasil", "superman james gunn elenco", "superman david corenswet", "quando superman chega na max"]
    },
    "content": """O filme **Superman** (anteriormente intitulado *Superman: Legacy*) marca o início oficial do novo Universo DC nos cinemas (DCU: Capítulo 1 - Deuses e Monstros), comandado por James Gunn e Peter Safran. Com David Corenswet assumindo a lendária capa vermelha e Rachel Brosnahan no papel da audaciosa repórter Lois Lane, o projeto busca devolver ao herói sua essência clássica: a personificação da verdade, justiça e compaixão em um mundo cínico.

Ao contrário de abordagens anteriores, a produção de James Gunn dispensa a recontagem da história de origem do bebê Kal-El caindo em Smallville. O longa já inicia com Clark Kent estabelecido como repórter do Planeta Diário e atuando como herói em Metrópoles, tentando conciliar sua herança extraterrestre de Krypton com os valores humanos ensinados por Jonathan e Martha Kent no Kansas.

O elenco conta ainda com Nicholas Hoult como o brilhante e vingativo Lex Luthor, Skyler Gisondo como Jimmy Olsen e a introdução de outros heróis clássicos como o Lanterna Verde Guy Gardner (Nathan Fillion) e a Mulher-Gavião (Isabela Merced). A Warner Bros. confirmou lançamento exclusivo nos cinemas com tecnologia IMAX e som imersivo Dolby Atmos antes da estreia no catálogo da Max.""",
    "movieInfo": {
        "title": "Superman",
        "releaseDate": "10 de julho de 2025",
        "futureStreaming": "Max",
        "directors": "James Gunn",
        "mainVillain": "Nicholas Hoult (Lex Luthor)",
        "confirmedCast": [
            "David Corenswet (Clark Kent / Superman)",
            "Rachel Brosnahan (Lois Lane)",
            "Nicholas Hoult (Lex Luthor)",
            "Nathan Fillion (Guy Gardner / Lanterna Verde)",
            "Isabela Merced (Mulher-Gavião)",
            "Edi Gathegi (Senhor Incrível)",
            "Skyler Gisondo (Jimmy Olsen)"
        ],
        "productionDetails": "Primeiro longa oficial do DC Studios, com direção e roteiro de James Gunn, filmado em IMAX com foco em efeitos práticos e tom humanista clássico."
    },
    "faqs": [
        {"question": "Quando Superman estreia nos cinemas brasileiros?", "answer": "A estreia nacional nos cinemas do Brasil acontece no dia 10 de julho de 2025, com sessões de pré-estreia na quarta-feira anterior."},
        {"question": "Quando o novo Superman chega à Max?", "answer": "Seguindo a janela tradicional de 60 a 90 dias da Warner Bros. Discovery para grandes blockbusters, a previsão de estreia na Max é entre setembro e outubro de 2025."},
        {"question": "Quem é o novo ator que interpreta o Superman?", "answer": "David Corenswet (de Pearl e Hollywood) foi o ator escolhido por James Gunn para viver o Homem de Aço."}
    ]
})

# 3. 5 Filmes Parecidos com Corra! (Lista)
posts.append({
    "id": "post-semana-ouro-03",
    "slug": "5-filmes-parecidos-com-corra-para-assistir-depois",
    "title": "5 Filmes Parecidos com Corra! (Get Out) sobre Terror Social e Paranóia",
    "subtitle": "Se você amou a mente genial de Jordan Peele, confira cinco produções com tensão psicológica sufocante, mistério e críticas afiadas.",
    "type": "list",
    "genres": ["Terror", "Suspense", "Cinema Autoral", "Streaming"],
    "publishedAt": data_iso(0, 2),
    "scheduledFor": data_iso(0, 2),
    "updatedAt": data_iso(0, 2),
    "author": AUTHORS["beatriz"],
    "coverImage": P["corra"],
    "posterImage": P["corra"],
    "readingTime": "7 min de leitura",
    "seo": {
        "metaTitle": "5 Filmes Parecidos com Corra! (Get Out) para Assistir Hoje | FilmeJá",
        "metaDescription": "Gostou de Corra!? Veja 5 filmes imperdíveis com suspense psicológico, paranóia e terror social para maratonar nos streamings.",
        "keywords": ["filmes parecidos com corra", "filmes estilo get out", "terror psicologico parecido com corra", "melhores filmes de terror social"]
    },
    "content": """Quando Jordan Peele lançou **Corra! (Get Out)** em 2017, ele não apenas revolucionou o cinema de suspense, mas redefiniu o gênero do 'terror social'. O desconforto palpável de estar em um ambiente aparentemente acolhedor, onde sorrisos forçados escondem intenções macabras, transformou-se em uma das marcas registradas mais imitadas da última década.

Se você está procurando produções que capturem essa mesma sensação de paranóia crescente — onde o protagonista percebe aos poucos que todos ao seu redor fazem parte de uma conspiração bizarra —, selecionamos cinco filmes impecáveis disponíveis nos catálogos de streaming brasileiros. De críticas afiadas a desfechos imprevisíveis, prepare a pipoca e apague as luzes.""",
    "listItems": [
        {
            "rank": 1,
            "title": "Nós (Us)",
            "year": 2019,
            "director": "Jordan Peele",
            "score": 9.2,
            "highlightTag": "Do Mesmo Diretor",
            "cast": ["Lupita Nyong'o", "Winston Duke", "Elisabeth Moss"],
            "posterImage": P["nos"],
            "whereToWatch": ["Prime Video", "Apple TV+"],
            "synopsis": "Uma família em férias na praia é aterrorizada por cópias idênticas e bizarras de si mesmos vestindo macacões vermelhos e empunhando tesouras douradas.",
            "whyWatch": "Lupita Nyong'o entrega uma atuação digna de Oscar em dose dupla. A direção de Jordan Peele mantém a tensão milimétrica e traz reflexões profundas sobre as divisões sociais da América.",
            "highlightPoints": [
                "Atuação arrebatadora de Lupita Nyong'o",
                "Trilha sonora inquietante com versões perturbadoras de clássicos do hip-hop"
            ]
        },
        {
            "rank": 2,
            "title": "O Homem Invisível (The Invisible Man)",
            "year": 2020,
            "director": "Leigh Whannell",
            "score": 8.9,
            "highlightTag": "Tensão Sufocante",
            "cast": ["Elisabeth Moss", "Oliver Jackson-Cohen", "Aldis Hodge"],
            "posterImage": P["o_homem_invisivel"],
            "whereToWatch": ["Netflix", "Prime Video"],
            "synopsis": "Após escapar de um relacionamento tóxico com um cientista abusivo, uma mulher passa a ser atormentada por uma presença invisível que ninguém mais acredita que existe.",
            "whyWatch": "O filme trabalha o conceito de 'gaslighting' de forma visceral, fazendo o espectador duvidar de cada canto vazio do enquadramento, exatamente como o horror social de Corra.",
            "highlightPoints": [
                "Uso brilhante de espaços vazios na câmera para gerar pavor",
                "Metáfora precisa e realista sobre abuso e manipulação psicológica"
            ]
        },
        {
            "rank": 3,
            "title": "Fale Comigo (Talk to Me)",
            "year": 2023,
            "director": "Danny Philippou e Michael Philippou",
            "score": 8.8,
            "highlightTag": "Sensação A24",
            "cast": ["Sophie Wilde", "Alexandra Jensen", "Joe Bird"],
            "posterImage": P["fale_comigo"],
            "whereToWatch": ["Max", "Prime Video"],
            "synopsis": "Jovens usam uma mão embalsamada para se conectar com espíritos como brincadeira de festa, até que uma das sessões ultrapassa o limite de tempo seguro e abre portas demoníacas.",
            "whyWatch": "Assim como Corra!, o longa australiano reinventa a dinâmica de grupo e o desconforto juvenil com uma originalidade crua que revitalizou o cinema de horror contemporâneo.",
            "highlightPoints": [
                "Efeitos práticos grotescos e maquiagem de altíssimo nível",
                "Ritmo elétrico sem espaço para respiro"
            ]
        },
        {
            "rank": 4,
            "title": "Hereditário (Hereditary)",
            "year": 2018,
            "director": "Ari Aster",
            "score": 9.4,
            "highlightTag": "Obra-Prima",
            "cast": ["Toni Collette", "Alex Wolff", "Gabriel Byrne"],
            "posterImage": P["hereditario"],
            "whereToWatch": ["Max", "Netflix"],
            "synopsis": "Após a morte da avó misteriosa, uma família começa a desvendar segredos ancestrais aterrorizantes enquanto uma presença sombria consome a sanidade de todos.",
            "whyWatch": "O horror que nasce do drama familiar e do luto. A sensação de conspiração inevitável lembra a impotência desesperadora do protagonista de Corra.",
            "highlightPoints": [
                "Atuação monumental de Toni Collette",
                "Finais chocantes que permanecem na cabeça por semanas"
            ]
        },
        {
            "rank": 5,
            "title": "Sorria 2 (Smile 2)",
            "year": 2024,
            "director": "Parker Finn",
            "score": 8.6,
            "highlightTag": "Paranóia Máxima",
            "cast": ["Naomi Scott", "Rosemarie DeWitt", "Lukas Gage"],
            "posterImage": P["smile_2"],
            "whereToWatch": ["Paramount+", "Apple TV+"],
            "synopsis": "À beira de iniciar uma turnê mundial, uma estrela pop começa a vivenciar eventos aterrorizantes envolvendo pessoas que a encaram com sorrisos macabros.",
            "whyWatch": "Trabalha com perfeição o medo do olhar alheio e da histeria coletiva, transformando o sorriso em uma arma psicológica letal com cenas de puro impacto visual.",
            "highlightPoints": [
                "Show de atuação física de Naomi Scott",
                "Sequências de suspense coreografadas de maneira impecável"
            ]
        }
    ],
    "faqs": [
        {"question": "Onde assistir aos filmes parecidos com Corra online?", "answer": "Todos os 5 filmes indicados estão disponíveis nos principais streamings no Brasil, como Netflix, Prime Video, Max e Apple TV+."},
        {"question": "Qual filme é mais parecido com Corra?", "answer": "Nós (Us) é a obra mais próxima por ser do próprio diretor Jordan Peele e compartilhar do mesmo estilo de humor ácido misturado a terror social."}
    ]
})

# 4. 7 Melhores Filmes de Ação Frenética na Netflix (Lista)
posts.append({
    "id": "post-semana-ouro-04",
    "slug": "7-melhores-filmes-de-acao-frenetica-na-netflix-2026",
    "title": "7 Melhores Filmes de Ação Frenética na Netflix para Assistir Hoje em 2026",
    "subtitle": "Sem enrolação: apenas tiros, lutas corpo a corpo inacreditáveis e perseguições que vão fazer seu coração disparar do primeiro ao último minuto.",
    "type": "list",
    "genres": ["Ação", "Netflix", "Adrenalina", "Streaming"],
    "publishedAt": data_iso(0, 3),
    "scheduledFor": data_iso(0, 3),
    "updatedAt": data_iso(0, 3),
    "author": AUTHORS["thiago"],
    "coverImage": P["mad_max"],
    "posterImage": P["mad_max"],
    "readingTime": "8 min de leitura",
    "seo": {
        "metaTitle": "7 Melhores Filmes de Ação Frenética na Netflix em 2026 | FilmeJá",
        "metaDescription": "Procurando ação pura? Confira os 7 filmes mais eletrizantes e rápidos da Netflix com lutas reais, perseguições insanas e sem enrolação.",
        "keywords": ["filmes de acao netflix 2026", "melhores filmes de acao netflix", "filmes de tiro e porrada netflix", "filmes com muita adrenalina netflix"]
    },
    "content": """Cansado de filmes com diálogos lentos e enrolação sem fim? Quando o objetivo é sentar no sofá e sentir a adrenalina correr nas veias, nada supera uma boa sessão de ação frenética. O catálogo da Netflix no Brasil está repleto de produções que priorizam coreografias de combate de alta fidelidade, dublês reais e ritmo implacável.

Para poupar o seu tempo na navegação, nossa equipe editorial selecionou os **7 melhores filmes de ação do catálogo**, avaliados por qualidade técnica, impacto sonoro e retenção máxima. Prepare-se para duas horas de pura adrenalina sem pausas.""",
    "listItems": [
        {
            "rank": 1,
            "title": "Mad Max: Estrada da Fúria",
            "year": 2015,
            "director": "George Miller",
            "score": 9.9,
            "highlightTag": "O Melhor do Século",
            "cast": ["Tom Hardy", "Charlize Theron", "Nicholas Hoult"],
            "posterImage": P["mad_max"],
            "whereToWatch": ["Netflix", "Max"],
            "synopsis": "Em um mundo pós-apocalíptico desértico, uma mulher rebelde lidera a fuga de um caminhão tanque contra as forças implacáveis de um senhor da guerra.",
            "whyWatch": "Vencedor de 6 Oscars técnicos, é uma ópera de metal e fogo rodada com veículos e dublês reais sem depender de CGI tosco. Duas horas de perseguição ininterrupta.",
            "highlightPoints": ["Carros reais construídos e destruídos no deserto", "Trilha sonora explosiva de Junkie XL"]
        },
        {
            "rank": 2,
            "title": "Trem-Bala (Bullet Train)",
            "year": 2022,
            "director": "David Leitch",
            "score": 9.1,
            "highlightTag": "Ação & Comédia Ácida",
            "cast": ["Brad Pitt", "Joey King", "Aaron Taylor-Johnson"],
            "posterImage": P["trem_bala"],
            "whereToWatch": ["Netflix", "Prime Video"],
            "synopsis": "Cinco assassinos profissionais descobrem que suas missões em um trem de alta velocidade no Japão estão caoticamente interligadas.",
            "whyWatch": "Brad Pitt em estado de graça com lutas rápidas em vagões apertados usando garrafas térmicas e maletas. Estiloso e muito divertido.",
            "highlightPoints": ["Combates criativos em ambientes fechados", "Química perfeita entre Lemon e Tangerine"]
        },
        {
            "rank": 3,
            "title": "Resgate 2 (Extraction 2)",
            "year": 2023,
            "director": "Sam Hargrave",
            "score": 8.9,
            "highlightTag": "Combate Físico Bruto",
            "cast": ["Chris Hemsworth", "Golshifteh Farahani", "Tornike Gogrichiani"],
            "posterImage": P["resgate_2"],
            "whereToWatch": ["Netflix"],
            "synopsis": "O mercenário Tyler Rake retorna dos mortos para resgatar a família torturada de um gângster georgiano de uma penitenciária impenetrável.",
            "whyWatch": "Apresenta um plano-sequência insano de 21 minutos com rebelião em prisão, helicópteros pousando em trens em movimento e combate corpo a corpo brutal.",
            "highlightPoints": ["Plano-sequência histórico de 21 minutos", "Chris Hemsworth em sua melhor performance física"]
        },
        {
            "rank": 4,
            "title": "John Wick 4: Baba Yaga",
            "year": 2023,
            "director": "Chad Stahelski",
            "score": 9.3,
            "highlightTag": "Ápice do Gun-Fu",
            "cast": ["Keanu Reeves", "Donnie Yen", "Bill Skarsgård"],
            "posterImage": P["john_wick_4"],
            "whereToWatch": ["Netflix", "Prime Video"],
            "synopsis": "Com o preço por sua cabeça disparando, John Wick enfrenta a Alta Cúpula em batalhas sangrentas de Osaka até Paris.",
            "whyWatch": "A sequência nas escadarias de Sacré-Cœur e a cena em vista aérea com espingarda de cartucho incendiário estão entre os maiores momentos do cinema de ação.",
            "highlightPoints": ["Donnie Yen roubando a cena como espadachim cego", "Quase 3 horas de coreografias perfeitas"]
        },
        {
            "rank": 5,
            "title": "Top Gun: Maverick",
            "year": 2022,
            "director": "Joseph Kosinski",
            "score": 9.5,
            "highlightTag": "Adrenalina nos Ares",
            "cast": ["Tom Cruise", "Miles Teller", "Jennifer Connelly"],
            "posterImage": P["top_gun_maverick"],
            "whereToWatch": ["Netflix", "Paramount+"],
            "synopsis": "Após décadas de serviço como um dos melhores aviadores da Marinha, Pete Maverick Mitchell treina uma equipe de graduados para uma missão quase suicida.",
            "whyWatch": "Tom Cruise colocou os atores reais dentro de caças F/A-18 militares sem computação gráfica falsa. O resultado na tela faz a poltrona vibrar.",
            "highlightPoints": ["Filmagem autêntica dentro de caças de combate", "Clímax emocionante com manobras aéreas reais"]
        },
        {
            "rank": 6,
            "title": "127 Horas",
            "year": 2010,
            "director": "Danny Boyle",
            "score": 8.7,
            "highlightTag": "Sobrevivência Pura",
            "cast": ["James Franco", "Amber Tamblyn", "Kate Mara"],
            "posterImage": P["127_horas"],
            "whereToWatch": ["Netflix", "Disney+"],
            "synopsis": "Um alpinista fica preso em uma fenda isolada em Utah com o braço esmagado por uma rocha e precisa lutar por 5 dias para continuar vivo.",
            "whyWatch": "Ação de sobrevivência em sua forma mais visceral. A edição acelerada de Danny Boyle transforma cada minuto em uma corrida desesperada contra o tempo.",
            "highlightPoints": ["Edição dinâmica e eletrizante", "História real impressionante de resiliência"]
        },
        {
            "rank": 7,
            "title": "O Regresso (The Revenant)",
            "year": 2015,
            "director": "Alejandro G. Iñárritu",
            "score": 9.0,
            "highlightTag": "Vencedor de 3 Oscars",
            "cast": ["Leonardo DiCaprio", "Tom Hardy", "Domhnall Gleeson"],
            "posterImage": P["o_regresso"],
            "whereToWatch": ["Netflix", "Max"],
            "synopsis": "Abandonado para morrer na neve após o ataque de um urso pardo, um caçador de peles rasteja pela selva congelada impulsionado apenas pelo desejo de vingança.",
            "whyWatch": "Fotografia vencedora do Oscar feita apenas com luz natural. O ataque do urso e as perseguições com flechas indígenas na água gelada são inesquecíveis.",
            "highlightPoints": ["Atuação visceral que deu o Oscar a DiCaprio", "Cenas brutais de combate em ambientes extremos"]
        }
    ],
    "faqs": [
        {"question": "Qual é o melhor filme de ação da Netflix atualmente?", "answer": "Mad Max: Estrada da Fúria e John Wick 4 são amplamente considerados pela crítica os pontos mais altos do gênero disponíveis na plataforma."},
        {"question": "Os filmes de ação da Netflix possuem dublagem em português?", "answer": "Sim, todos os 7 títulos selecionados contam com opções de dublagem e áudio original legendado em português."}
    ]
})

# 5. Duna: A Profecia Ep 1 (Episódio)
posts.append({
    "id": "post-semana-ouro-05",
    "slug": "que-dia-sai-episodio-1-de-duna-a-profecia-temporada-1-data-horario",
    "title": "Que Dia Sai o Episódio 1 de Duna: A Profecia? Data e Horário na Max",
    "subtitle": "Conheça as origens da mística irmandade Bene Gesserit 10.000 anos antes de Paul Atreides na superprodução da HBO.",
    "type": "episodio",
    "genres": ["Séries", "Max", "Ficção Científica", "Lançamentos"],
    "publishedAt": data_iso(0, 4),
    "scheduledFor": data_iso(0, 4),
    "updatedAt": data_iso(0, 4),
    "author": AUTHORS["camila"],
    "coverImage": P["duna_a_profecia"],
    "posterImage": P["duna_a_profecia"],
    "readingTime": "5 min de leitura",
    "seo": {
        "metaTitle": "Que Dia Sai Episódio 1 de Duna: A Profecia? Data e Horário | FilmeJá",
        "metaDescription": "Saiba que dia estreia o episódio 1 de Duna: A Profecia na Max. Veja o calendário de episódios no Brasil, elenco e conexões com os filmes.",
        "keywords": ["que dia sai duna a profecia", "duna a profecia episodio 1 horario max", "duna a profecia serie brasil", "duna serie max elenco"]
    },
    "content": """Expandindo o monumental universo cinematográfico criado por Denis Villeneuve e Frank Herbert, **Duna: A Profecia (Dune: Prophecy)** chega ao catálogo da Max como a nova superprodução de ficção científica da HBO. Ambientada 10.000 anos antes da ascensão de Paul Atreides, a trama revela como duas irmãs da Casa Harkonnen fundaram a lendária irmandade Bene Gesserit.

Com atuações lideradas por Emily Watson (Valya Harkonnen) e Olivia Williams (Tula Harkonnen), a série mergulha nos jogos políticos de bastidores, manipulações genéticas e profecias secretas que moldaram o futuro do Imperium. Enquanto o Imperador Javicco Corrino (Mark Strong) tenta manter o controle frágil sobre as Grandes Casas, uma nova ameaça misteriosa com poderes extraordinários surge nas sombras.

A exibição segue a consagrada tradição dos grandes sucessos da HBO (como Game of Thrones e Succession): **novos episódios todos os domingos às 22h00**, com transmissão simultânea no streaming da Max e no canal linear de televisão por assinatura.""",
    "seriesInfo": {
        "seriesTitle": "Duna: A Profecia",
        "originalTitle": "Dune: Prophecy",
        "seasonNumber": 1,
        "episodeNumber": 1,
        "nextEpisodeDate": "17 de novembro",
        "nextEpisodeTime": "22h00 (Horário de Brasília)",
        "platform": "Max",
        "totalEpisodes": 6,
        "recapPreviousEpisode": "Episódio piloto de estreia introduzindo o cenário galáctico 10.000 anos antes dos eventos dos filmes de Paul Atreides.",
        "whatToExpect": "As irmãs Valya e Tula Harkonnen consolidam os primeiros passos da Irmandade contra conspirações palacianas que ameaçam o trono do Imperador Corrino.",
        "schedule": [
            {"episodeNumber": 1, "title": "A Mão Oculta", "releaseDate": "17/11", "releaseTime": "22:00 BRT", "status": "proximo"},
            {"episodeNumber": 2, "title": "Duas Irmãs", "releaseDate": "24/11", "releaseTime": "22:00 BRT", "status": "a_estrear"},
            {"episodeNumber": 3, "title": "A Voz do Deserto", "releaseDate": "01/12", "releaseTime": "22:00 BRT", "status": "a_estrear"},
            {"episodeNumber": 4, "title": "Linhagem Proibida", "releaseDate": "08/12", "releaseTime": "22:00 BRT", "status": "a_estrear"},
            {"episodeNumber": 5, "title": "Traição em Salusa", "releaseDate": "15/12", "releaseTime": "22:00 BRT", "status": "a_estrear"},
            {"episodeNumber": 6, "title": "A Primeira Profecia", "releaseDate": "22/12", "releaseTime": "22:00 BRT", "status": "a_estrear"}
        ]
    },
    "faqs": [
        {"question": "Que dia sai o episódio novo de Duna: A Profecia?", "answer": "Os episódios estreiam semanalmente aos domingos às 22h00 na Max e no canal HBO."},
        {"question": "Duna: A Profecia tem relação direta com os filmes de Denis Villeneuve?", "answer": "Sim, a série se passa no mesmo universo oficial dos filmes, explorando o passado milenar da Bene Gesserit."}
    ]
})

print(f"Salvos 5 primeiros posts na memória...")
