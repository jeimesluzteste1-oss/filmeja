import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import Link from 'next/link';
import Image from 'next/image';
import { getAllGenres, getPostsByGenre } from '@/lib/posts';
import { ChevronRight, Clock, Calendar, Film } from 'lucide-react';

interface GeneroPageProps {
  params: {
    genero: string;
  };
}

export async function generateStaticParams() {
  const genres = getAllGenres();
  return genres.map((g) => ({
    genero: encodeURIComponent(g.toLowerCase()),
  }));
}

export async function generateMetadata({ params }: GeneroPageProps): Promise<Metadata> {
  const decodedGenre = decodeURIComponent(params.genero);
  const capitalized = decodedGenre.charAt(0).toUpperCase() + decodedGenre.slice(1);

  return {
    title: `Melhores Filmes de ${capitalized} (2025/2026) | Recomendações FilmeJá`,
    description: `Confira os melhores filmes de ${decodedGenre}, listas Top 5, análises sinceras e onde assistir nos principais streamings.`,
    alternates: {
      canonical: `https://filmeja.com.br/genero/${params.genero}`,
    },
    openGraph: {
      title: `Filmes de ${capitalized} | FilmeJá`,
      description: `Recomendações e listas dos filmes de ${decodedGenre} mais comentados e aclamados.`,
    },
  };
}

export default function GeneroPage({ params }: GeneroPageProps) {
  const decodedGenre = decodeURIComponent(params.genero);
  const posts = getPostsByGenre(decodedGenre);
  const capitalized = decodedGenre.charAt(0).toUpperCase() + decodedGenre.slice(1);

  if (posts.length === 0) {
    notFound();
  }

  return (
    <div className="container" style={{ paddingBottom: '4rem' }}>
      {/* Breadcrumbs */}
      <nav aria-label="Breadcrumb" className="article-breadcrumbs" style={{ marginTop: '2rem' }}>
        <Link href="/">Início</Link>
        <ChevronRight size={14} />
        <span>Gêneros</span>
        <ChevronRight size={14} />
        <span style={{ color: 'var(--text-main)' }}>{capitalized}</span>
      </nav>

      <div className="hero-banner" style={{ border: 'none', padding: '1rem 0 2.5rem' }}>
        <h1 className="hero-title" style={{ fontSize: '2.5rem' }}>
          Filmes de <span style={{ color: '#ff5e62' }}>{capitalized}</span>
        </h1>
        <p className="hero-desc">
          Encontre os lançamentos mais marcantes, listas dos melhores filmes de {decodedGenre} e recomendações sem spoilers.
        </p>
      </div>

      <div className="posts-grid">
        {posts.map((post) => (
          <article key={post.id} className="post-card">
            <Link href={`/post/${post.slug}`} className="post-card-thumb">
              <Image
                src={post.coverImage}
                alt={post.title}
                fill
                sizes="(max-width: 768px) 100vw, 33vw"
                style={{ objectFit: 'cover' }}
              />
              <span className={`post-type-badge ${post.type}`}>
                {post.type === 'list' ? 'Top Lista' : 'React'}
              </span>
            </Link>

            <div className="post-card-body">
              <div className="post-card-genres">
                {post.genres.map((g) => (
                  <span key={g} className="genre-tag">
                    #{g}
                  </span>
                ))}
              </div>

              <Link href={`/post/${post.slug}`}>
                <h3 className="post-card-title">{post.title}</h3>
              </Link>

              <p className="post-card-excerpt">{post.subtitle}</p>

              <div className="post-card-footer">
                <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                  <Clock size={14} />
                  {post.readingTime}
                </span>
                <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                  <Calendar size={14} />
                  {new Date(post.publishedAt).toLocaleDateString('pt-BR', {
                    day: '2-digit',
                    month: 'short',
                    year: 'numeric',
                  })}
                </span>
              </div>
            </div>
          </article>
        ))}
      </div>
    </div>
  );
}
