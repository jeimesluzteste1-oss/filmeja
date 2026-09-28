import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import Link from 'next/link';
import Image from 'next/image';
import { getPostsByType } from '@/lib/posts';
import { PostType } from '@/types/movie';
import { ChevronRight, Clock, Calendar } from 'lucide-react';

interface TipoPageProps {
  params: {
    tipo: string;
  };
}

export async function generateStaticParams() {
  return [{ tipo: 'list' }, { tipo: 'react' }];
}

export async function generateMetadata({ params }: TipoPageProps): Promise<Metadata> {
  const isList = params.tipo === 'list';
  const title = isList
    ? 'Top Listas de Filmes (Top 5 e Top 10) | FilmeJá'
    : 'Reacts e Análises Sinceras de Lançamentos | FilmeJá';
  const description = isList
    ? 'Descubra seleções com os melhores filmes de terror, suspense e ficção ordenados por nota e relevância.'
    : 'Veja nossas impressões honestas, prós, contras e veredito dos últimos lançamentos de cinema e streaming.';

  return {
    title,
    description,
    alternates: {
      canonical: `https://filmeja.com.br/tipo/${params.tipo}`,
    },
  };
}

export default function TipoPage({ params }: TipoPageProps) {
  if (params.tipo !== 'list' && params.tipo !== 'react') {
    notFound();
  }

  const posts = getPostsByType(params.tipo as PostType);
  const isList = params.tipo === 'list';

  return (
    <div className="container" style={{ paddingBottom: '4rem' }}>
      <nav aria-label="Breadcrumb" className="article-breadcrumbs" style={{ marginTop: '2rem' }}>
        <Link href="/">Início</Link>
        <ChevronRight size={14} />
        <span style={{ color: 'var(--text-main)' }}>
          {isList ? 'Top Listas' : 'Reacts & Análises'}
        </span>
      </nav>

      <div className="hero-banner" style={{ border: 'none', padding: '1rem 0 2.5rem' }}>
        <h1 className="hero-title" style={{ fontSize: '2.5rem' }}>
          {isList ? 'Top Listas de Filmes' : 'Reacts & Críticas'}
        </h1>
        <p className="hero-desc">
          {isList
            ? 'Rankings minuciosamente selecionados para você maratonar hoje sem erro.'
            : 'Nossas impressões sinceras, veredito e onde assistir aos filmes do momento.'}
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
