/**
 * Utilitário para gerar links diretos de streaming / busca para cada filme.
 */
export function getStreamingSearchUrl(platform: string, movieTitle: string): string {
  const query = encodeURIComponent(movieTitle);
  const plat = platform.toLowerCase();

  if (plat.includes('netflix')) {
    return `https://www.netflix.com/search?q=${query}`;
  }
  if (plat.includes('prime') || plat.includes('amazon')) {
    return `https://www.primevideo.com/search/ref=atv_nb_sr?phrase=${query}`;
  }
  if (plat.includes('disney')) {
    return `https://www.disneyplus.com/search?q=${query}`;
  }
  if (plat.includes('max') || plat.includes('hbo')) {
    return `https://www.max.com/search?q=${query}`;
  }
  if (plat.includes('paramount')) {
    return `https://www.paramountplus.com/search/?q=${query}`;
  }
  if (plat.includes('mubi')) {
    return `https://mubi.com/pt/search?query=${query}`;
  }
  if (plat.includes('apple')) {
    return `https://tv.apple.com/br/search?term=${query}`;
  }
  if (plat.includes('globo') || plat.includes('telecine')) {
    return `https://globoplay.globo.com/busca/?q=${query}`;
  }
  if (plat.includes('cinema') || plat.includes('ingresso')) {
    return `https://www.ingresso.com/busca?q=${query}`;
  }

  // Fallback para Google Search do filme no streaming
  return `https://www.google.com/search?q=onde+assistir+${query}+streaming+brasil`;
}
