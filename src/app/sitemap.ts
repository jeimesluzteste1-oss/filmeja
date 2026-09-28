import { MetadataRoute } from 'next';
import { getAllPosts, getAllGenres } from '@/lib/posts';

export default function sitemap(): MetadataRoute.Sitemap {
  const baseUrl = 'https://filmeja.com.br';
  const posts = getAllPosts();
  const genres = getAllGenres();

  const postsUrls: MetadataRoute.Sitemap = posts.map((post) => ({
    url: `${baseUrl}/post/${post.slug}`,
    lastModified: new Date(post.updatedAt || post.publishedAt),
    changeFrequency: 'weekly',
    priority: 0.8,
  }));

  const genresUrls: MetadataRoute.Sitemap = genres.map((genre) => ({
    url: `${baseUrl}/genero/${encodeURIComponent(genre.toLowerCase())}`,
    lastModified: new Date(),
    changeFrequency: 'daily',
    priority: 0.7,
  }));

  const staticUrls: MetadataRoute.Sitemap = [
    {
      url: baseUrl,
      lastModified: new Date(),
      changeFrequency: 'daily',
      priority: 1.0,
    },
    {
      url: `${baseUrl}/tipo/list`,
      lastModified: new Date(),
      changeFrequency: 'daily',
      priority: 0.7,
    },
    {
      url: `${baseUrl}/tipo/react`,
      lastModified: new Date(),
      changeFrequency: 'daily',
      priority: 0.7,
    },
  ];

  return [...staticUrls, ...postsUrls, ...genresUrls];
}
