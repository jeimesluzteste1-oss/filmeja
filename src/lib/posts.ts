import fs from 'fs';
import path from 'path';
import { MoviePost, PostType } from '@/types/movie';

const postsDirectory = path.join(process.cwd(), 'src/content/posts');

export function getAllPosts(): MoviePost[] {
  try {
    if (!fs.existsSync(postsDirectory)) {
      return [];
    }
    const fileNames = fs.readdirSync(postsDirectory);
    const allPosts: MoviePost[] = fileNames
      .filter((fileName) => fileName.endsWith('.json'))
      .map((fileName) => {
        const fullPath = path.join(postsDirectory, fileName);
        const fileContents = fs.readFileSync(fullPath, 'utf8');
        const postData = JSON.parse(fileContents) as MoviePost;
        return postData;
      });

    // Ordenar posts do mais recente para o mais antigo
    return allPosts.sort((a, b) => {
      return new Date(b.publishedAt).getTime() - new Date(a.publishedAt).getTime();
    });
  } catch (error) {
    console.error('Erro ao carregar posts:', error);
    return [];
  }
}

export function getPostBySlug(slug: string): MoviePost | undefined {
  const posts = getAllPosts();
  return posts.find((post) => post.slug === slug);
}

export function getPostsByType(type: PostType): MoviePost[] {
  const posts = getAllPosts();
  return posts.filter((post) => post.type === type);
}

export function getPostsByGenre(genre: string): MoviePost[] {
  const posts = getAllPosts();
  const target = genre.toLowerCase();
  return posts.filter((post) =>
    post.genres.some((g) => g.toLowerCase() === target)
  );
}

export function getAllGenres(): string[] {
  const posts = getAllPosts();
  const genresSet = new Set<string>();
  posts.forEach((post) => {
    post.genres.forEach((genre) => genresSet.add(genre));
  });
  return Array.from(genresSet);
}

export function getRelatedPosts(currentSlug: string, genres: string[], limit: number = 3): MoviePost[] {
  const posts = getAllPosts();
  const normalizedGenres = genres.map((g) => g.toLowerCase());
  
  return posts
    .filter((post) => post.slug !== currentSlug)
    .sort((a, b) => {
      const matchA = a.genres.filter((g) => normalizedGenres.includes(g.toLowerCase())).length;
      const matchB = b.genres.filter((g) => normalizedGenres.includes(g.toLowerCase())).length;
      return matchB - matchA;
    })
    .slice(0, limit);
}
