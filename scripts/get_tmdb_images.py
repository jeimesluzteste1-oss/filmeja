import urllib.request
import re
import json

movies = {
    'nosferatu': '426063-nosferatu',
    'smile2': '1100782-smile-2',
    'first_omen': '437342-the-first-omen',
    'substance': '933260-the-substance',
    'longlegs': '1226578-longlegs',
    'shutter_island': '11324-shutter-island',
    'gone_girl': '210577-gone-girl',
    'prisoners': '146233-prisoners',
    'get_out': '419430-get-out',
    'the_invitation': '306947-the-invitation',
    'alien_romulus': '945961-alien-romulus'
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
