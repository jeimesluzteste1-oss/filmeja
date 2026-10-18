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
  return [
    { tipo: 'list' },
    { tipo: 'react' },
    { tipo: 'episodio' },
    { tipo: 'lancamento' },
  ];
}

export async function generateMetadata({ params }: TipoPageProps): Promise<Metadata> {
  let title = 'Filmes e Séries | FilmeJá';
  let description = 'Confira as melhores recomendações e novidades no FilmeJá.';

  if (params.tipo === 'list') {
    title = 'Top Listas de Filmes (Top 5 e Top 10) | FilmeJá';
    description = 'Descubra seleções com os melhores filmes de terror, suspense e ficção ordenados por nota e relevância.';
  } else if (params.tipo === 'react') {
    title = 'Reacts e Análises Sinceras de Lançamentos | FilmeJá';
    description = 'Veja nossas impressões honestas, prós, contras e veredito dos últimos lançamentos de cinema e streaming.';
  } else if (params.tipo === 'episodio') {
    title = 'Séries em Alta: Que Dia Sai o Próximo Episódio? | FilmeJá';
    description = 'Calendário de episódios semanais, datas, horários no Brasil e onde assistir às séries mais comentadas do streaming.';
  } else if (params.tipo === 'lancamento') {
    title = 'Calendário de Estreias e Lançamentos Mais Esperados | FilmeJá';
    description = 'Datas de estreias confirmadas, trailers e previsão de chegada aos streamings e cinemas.';
  }

  return {
    title,
    description,
    alternates: {
      canonical: `https://filmeja.com.br/tipo/${params.tipo}`,
    },
  };
}

export default function TipoPage({ params }: TipoPageProps) {
  const validTypes = ['list', 'react', 'episodio', 'lancamento'];
  if (!validTypes.includes(params.tipo)) {
    notFound();
  }

  const posts = getPostsByType(params.tipo as PostType);
  
  let pageHeading = 'Artigos da Redação';
  let pageDesc = 'Navegue pelo nosso acervo exclusivo.';
  let breadcrumbLabel = 'Artigos';

  if (params.tipo === 'list') {
    pageHeading = 'Top Listas de Filmes';
    pageDesc = 'Rankings minuciosamente selecionados para você maratonar hoje sem erro.';
    breadcrumbLabel = 'Top Listas';
  } else if (params.tipo === 'react') {
    pageHeading = 'Reacts & Críticas';
    pageDesc = 'Nossas impressões sinceras, veredito e onde assistir aos filmes do momento.';
    breadcrumbLabel = 'Reacts & Críticas';
  } else if (params.tipo === 'episodio') {
    pageHeading = 'Séries & Calendário de Episódios';
    pageDesc = 'Descubra que dia e horário sai o novo episódio da sua série favorita no streaming.';
    breadcrumbLabel = 'Séries & Episódios';
  } else if (params.tipo === 'lancamento') {
    pageHeading = 'Próximos Lançamentos';
    pageDesc = 'Calendário completo dos filmes e temporadas mais aguardados do cinema e streaming.';
    breadcrumbLabel = 'Lançamentos';
  }

  return (
    <div className="container" style={{ paddingBottom: '4rem' }}>
      <nav aria-label="Breadcrumb" className="article-breadcrumbs" style={{ marginTop: '2rem' }}>
        <Link href="/">Início</Link>
        <ChevronRight size={14} />
        <span style={{ color: 'var(--text-main)' }}>
          {breadcrumbLabel}
        </span>
      </nav>

      <div className="hero-banner" style={{ border: 'none', padding: '1rem 0 2.5rem' }}>
        <h1 className="hero-title" style={{ fontSize: '2.5rem' }}>
          {pageHeading}
        </h1>
        <p className="hero-desc">
          {pageDesc}
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
