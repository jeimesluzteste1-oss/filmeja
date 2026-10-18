import os
import json
import glob
import re
import urllib.request

known = {}

# 1. From gerador_filmeja.py
with open('scripts/gerador_filmeja.py', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'"([^"]+)":\s*"(https://[^"]+tmdb[^"]+)"', text)
for k, v in matches:
    known[k.strip().lower()] = v

# 2. From tmdb_results.json
if os.path.exists('scripts/tmdb_results.json'):
    with open('scripts/tmdb_results.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for k, v in data.items():
            known[k.strip().lower()] = v

# 3. From posts/*.json
for p in glob.glob('src/content/posts/*.json'):
    with open(p, 'r', encoding='utf-8') as f:
        data = json.load(f)
        t = data.get('title')
        if t and data.get('posterImage'):
            known[t.strip().lower()] = data.get('posterImage')
        for item in data.get('listItems', []):
            it = item.get('title')
            ip = item.get('posterImage')
            if it and ip:
                known[it.strip().lower()] = ip

print(f"Total entries in candidate pool: {len(known)}")

# Test HTTP 200 for every unique URL
unique_urls = list(set(known.values()))
print(f"Testing {len(unique_urls)} unique URLs for HTTP 200...")

verified_urls = {}
for u in unique_urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=4) as resp:
            if resp.status == 200:
                verified_urls[u] = True
    except:
        pass

print(f"Verified working URLs: {len(verified_urls)} / {len(unique_urls)}")

# Filter known dictionary to only valid URLs
verified_known = {k: v for k, v in known.items() if v in verified_urls}
print(f"Total verified movie titles: {len(verified_known)}")

with open('scripts/verified_posters_pool.json', 'w', encoding='utf-8') as f:
    json.dump(verified_known, f, ensure_ascii=False, indent=2)

print("Saved to scripts/verified_posters_pool.json!")
