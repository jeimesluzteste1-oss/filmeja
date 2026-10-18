import urllib.request
import json

candidate_movies = {
    # Lista 1: Filmes parecidos com Corra
    "nos": "https://image.tmdb.org/t/p/w500/tFXcEccSQMf3lfhfXKSU9iRBpa3.jpg",
    "o_homem_invisivel": "https://image.tmdb.org/t/p/w500/67gVCA33yHpFkFyqhDJrt21MvYI.jpg",
    "fuja": "https://image.tmdb.org/t/p/w500/eNcmw7x6z01l0q09nSvhJmYx35r.jpg",
    "corrente_do_mal": "https://image.tmdb.org/t/p/w500/h6g2XkO9wWf83RzQO5rS8QZ7rS.jpg",
    "midsommar": "https://image.tmdb.org/t/p/w500/7LEI8ulBsDU7UIJ2i0RDVZwIoFZ.jpg",

    # Lista 2: Filmes parecidos com Interestelar
    "a_chegada": "https://image.tmdb.org/t/p/w500/3rDwbFpn6z5HJUgDjpfhEePx8VI.jpg",
    "contato": "https://image.tmdb.org/t/p/w500/772Yv5XGjE4tX7Kq3bC6m4jF9n0.jpg",
    "gravidade": "https://image.tmdb.org/t/p/w500/eHLufJ1bHy4PtEBJdPSTu4jIhZ0.jpg",
    "ad_astra": "https://image.tmdb.org/t/p/w500/xBHvZcjRiWyobQ9kxBhO6B2dtRI.jpg",
    "primeiro_homem": "https://image.tmdb.org/t/p/w500/6iA3Lp2K1hL098m2V8p2qX9P9h.jpg",

    # Lista 3: Filmes parecidos com Ilha do Medo
    "os_outros": "https://image.tmdb.org/t/p/w500/5WkQ18Yv8tV3F3U9P9h9b2v8X9.jpg",
    "memento": "https://image.tmdb.org/t/p/w500/yuNs09hvpHVU1cBTCAk9zxsL2oW.jpg",
    "o_sexto_sentido": "https://image.tmdb.org/t/p/w500/4c55v89x8t2v9x2b3n4m5v6b7.jpg",
    "o_iluminado": "https://image.tmdb.org/t/p/w500/xazWoLealQwEgqZ89MLZklLZD3k.jpg",
    "cisne_negro": "https://image.tmdb.org/t/p/w500/tqlmLBt2i5SHNpXEj2nqk10Crwa.jpg",

    # Lista 4: Filmes parecidos com Garota Exemplar
    "os_suspeitos": "https://image.tmdb.org/t/p/w500/30YtzPOimO7eG30r8K8rUkqTGNj.jpg",
    "zodiaco": "https://image.tmdb.org/t/p/w500/jFmlV5vUzOt1PgJ82efOhNsWcWX.jpg",
    "animais_noturnos": "https://image.tmdb.org/t/p/w500/eN7iB4U4x5h8m8v7y6t5r4e3w2.jpg",
    "um_pequeno_favor": "https://image.tmdb.org/t/p/w500/5O9n1b8v7X6m5P4k3J2h1g0f9.jpg",
    "a_garota_no_trem": "https://image.tmdb.org/t/p/w500/2y4P9Q8b7X6m5P4k3J2h1g0f9.jpg",

    # Lista 5: Filmes parecidos com Longlegs
    "seven": "https://image.tmdb.org/t/p/w500/dZXYPSEaXCeigR2GEuZoukNmLTf.jpg",
    "silencio_dos_inocentes": "https://image.tmdb.org/t/p/w500/uS9m8OBk1A8eM9I042bx8rK7qO.jpg",
    "hereditario": "https://image.tmdb.org/t/p/w500/x9tUYQj6WrdVwoKimSdoMzkDABS.jpg",
    "a_primeira_profecia": "https://image.tmdb.org/t/p/w500/zppeHKLHljU2uI7NBJ1JyDNpn6L.jpg",
    "entrevista_com_o_demonio": "https://image.tmdb.org/t/p/w500/blckaGzdEJ4PdG5RxZPcb77VYFV.jpg",

    # Lista 6: Filmes parecidos com Oppenheimer
    "o_jogo_da_imitacao": "https://image.tmdb.org/t/p/w500/zSqJ1qFq9v7P9n4k5m6l7o8p9.jpg",
    "o_destino_de_uma_nacao": "https://image.tmdb.org/t/p/w500/4n7Y8v9x1b2c3d4e5f6g7h8i9.jpg",
    "ponte_dos_espioes": "https://image.tmdb.org/t/p/w500/7v4P9Q8b7X6m5P4k3J2h1g0f9.jpg",
    "chernobyl": "https://image.tmdb.org/t/p/w500/hlLXt2tOPT6RRnjiUmoxyG9LTFi.jpg",
    "doutor_fantastico": "https://image.tmdb.org/t/p/w500/7v4P9Q8b7X6m5P4k3J2h1g0f8.jpg",

    # Lista 7: Filmes parecidos com Pobres Criaturas
    "a_favorita": "https://image.tmdb.org/t/p/w500/4v4P9Q8b7X6m5P4k3J2h1g0f9.jpg",
    "o_lagosta": "https://image.tmdb.org/t/p/w500/8v4P9Q8b7X6m5P4k3J2h1g0f9.jpg",
    "o_grande_hotel_budapeste": "https://image.tmdb.org/t/p/w500/nX5XotDM9AqSu7zgP8JvXW47.jpg",
    "a_substancia": "https://image.tmdb.org/t/p/w500/vWeOgzlhnP1sS23H3rzctGHB9Nb.jpg",
    "tudo_em_todo_lugar": "https://image.tmdb.org/t/p/w500/rKgvtzI5nKZY0949whHGg1G2.jpg"
}

results = {}
for k, u in candidate_movies.items():
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}), timeout=4)
        results[k] = (r.status == 200, u)
    except Exception as e:
        results[k] = (False, str(e))

valid = {k: v[1] for k, v in results.items() if v[0]}
invalid = {k: v[1] for k, v in results.items() if not v[0]}

print(f"Valid: {len(valid)} / {len(candidate_movies)}")
print("Invalid keys:", list(invalid.keys()))
