import urllib.request
import re
import json

movies = {
    'scream6': '768362-scream-vi',
    'x': '760104-x',
    'pearl': '944401-pearl',
    'thanksgiving': '1071215-thanksgiving',
    'terrifier2': '663712-terrifier-2',
    'zodiac': '1949-zodiac',
    'se7en': '807-se7en',
    'bullet_train': '616037-bullet-train',
    'mad_max': '76341-mad-max-fury-road',
    'extraction2': '697843-extraction-2'
}

results = {}
for key, slug in movies.items():
    url = f'https://www.themoviedb.org/movie/{slug}'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
            m = re.search(r'"image":"(https://image\.tmdb\.org/t/p/[^"]+)"', html)
            if m:
                results[key] = m.group(1)
            else:
                m2 = re.search(r'src="(https://image\.tmdb\.org/t/p/[^"]+)"', html)
                results[key] = m2.group(1) if m2 else 'Not found'
    except Exception as e:
        results[key] = str(e)

print(json.dumps(results, indent=2))
