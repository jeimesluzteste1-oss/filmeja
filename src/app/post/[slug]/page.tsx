import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import Image from 'next/image';
import Link from 'next/link';
import { getAllPosts, getPostBySlug, getRelatedPosts } from '@/lib/posts';
import { getStreamingSearchUrl } from '@/lib/streaming';
import {
  Star,
  Clock,
  Calendar,
  Tv,
  CheckCircle2,
  XCircle,
  HelpCircle,
  Film,
  ExternalLink,
  ChevronRight,
  Award,
  Sparkles,
  Users,
  Eye,
} from 'lucide-react';

interface PostPageProps {
  params: {
    slug: string;
  };
}

export async function generateStaticParams() {
  const posts = getAllPosts();
  return posts.map((post) => ({
    slug: post.slug,
  }));
}

export async function generateMetadata({ params }: PostPageProps): Promise<Metadata> {
  const post = getPostBySlug(params.slug);
  if (!post) {
    return {
      title: 'Post não encontrado | FilmeJá',
    };
  }

  const postUrl = `https://filmeja.com.br/post/${post.slug}`;
  const ogImage = post.coverImage || post.posterImage;

  return {
    title: post.seo.metaTitle,
    description: post.seo.metaDescription,
    keywords: post.seo.keywords,
    alternates: {
      canonical: postUrl,
    },
    openGraph: {
      title: post.seo.metaTitle,
      description: post.seo.metaDescription,
      url: postUrl,
      siteName: 'FilmeJá',
      type: 'article',
      publishedTime: post.publishedAt,
      modifiedTime: post.updatedAt,
      authors: [post.author.name],
      images: [
        {
          url: ogImage,
          width: 1200,
          height: 630,
          alt: post.title,
        },
      ],
    },
    twitter: {
      card: 'summary_large_image',
      title: post.seo.metaTitle,
      description: post.seo.metaDescription,
      images: [ogImage],
    },
  };
}

export default function PostPage({ params }: PostPageProps) {
  const post = getPostBySlug(params.slug);

  if (!post) {
    notFound();
  }

  const relatedPosts = getRelatedPosts(post.slug, post.genres);

  // Schema.org BreadcrumbList
  const breadcrumbJsonLd = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      {
        '@type': 'ListItem',
        position: 1,
        name: 'Início',
        item: 'https://filmeja.com.br',
      },
      {
        '@type': 'ListItem',
        position: 2,
        name: post.genres[0] || 'Filmes',
        item: `https://filmeja.com.br/genero/${encodeURIComponent((post.genres[0] || 'filmes').toLowerCase())}`,
      },
      {
        '@type': 'ListItem',
        position: 3,
        name: post.title,
        item: `https://filmeja.com.br/post/${post.slug}`,
      },
    ],
  };

  // Schema.org FAQPage
  const faqJsonLd = post.faqs && post.faqs.length > 0 ? {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: post.faqs.map((faq) => ({
      '@type': 'Question',
      name: faq.question,
      acceptedAnswer: {
        '@type': 'Answer',
        text: faq.answer,
      },
    })),
  } : null;

  // Schema.org ItemList (para listas de filmes)
  const itemListJsonLd = post.type === 'list' && post.listItems ? {
    '@context': 'https://schema.org',
    '@type': 'ItemList',
    name: post.title,
    description: post.subtitle,
    itemListElement: post.listItems.map((item, idx) => ({
      '@type': 'ListItem',
      position: idx + 1,
      item: {
        '@type': 'Movie',
        name: item.title,
        dateCreated: item.year.toString(),
        director: {
          '@type': 'Person',
          name: item.director,
        },
        image: item.posterImage,
      },
    })),
  } : null;

  // Schema.org Review & Movie (para reacts e análises individuais)
  const reviewJsonLd = post.featuredMovie ? {
    '@context': 'https://schema.org',
    '@type': 'Review',
    itemReviewed: {
      '@type': 'Movie',
      name: post.featuredMovie.title,
      sameAs: post.featuredMovie.originalTitle,
      dateCreated: post.featuredMovie.year.toString(),
      director: {
        '@type': 'Person',
        name: post.featuredMovie.director,
      },
      image: post.posterImage,
      aggregateRating: {
        '@type': 'AggregateRating',
        ratingValue: post.featuredMovie.ratingTmdb.toString(),
        bestRating: '10',
        worstRating: '1',
        ratingCount: '150',
      },
    },
    reviewRating: {
      '@type': 'Rating',
      ratingValue: post.featuredMovie.ratingFilmeJa.toString(),
      bestRating: '10',
      worstRating: '1',
    },
    author: {
      '@type': 'Person',
      name: post.author.name,
    },
    publisher: {
      '@type': 'Organization',
      name: 'FilmeJá',
      url: 'https://filmeja.com.br',
    },
  } : null;

  return (
    <article className="container" style={{ paddingBottom: '4rem' }}>
      {/* JSON-LD Structured Data */}
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbJsonLd) }}
      />
      {faqJsonLd && (
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(faqJsonLd) }}
        />
      )}
      {itemListJsonLd && (
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(itemListJsonLd) }}
        />
      )}
      {reviewJsonLd && (
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(reviewJsonLd) }}
        />
      )}

      {/* Breadcrumbs */}
      <nav aria-label="Breadcrumb" className="article-breadcrumbs" style={{ marginTop: '2rem' }}>
        <Link href="/">Início</Link>
        <ChevronRight size={14} />
        <Link href={`/genero/${encodeURIComponent((post.genres[0] || 'geral').toLowerCase())}`}>
          {post.genres[0]}
        </Link>
        <ChevronRight size={14} />
        <span style={{ color: 'var(--text-main)' }}>{post.title}</span>
      </nav>

      {/* Header do Artigo */}
      <header className="article-header">
        <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '1rem', flexWrap: 'wrap' }}>
          {post.genres.map((genre) => (
            <span key={genre} className="genre-tag" style={{ background: 'rgba(229,9,20,0.1)', padding: '3px 10px', borderRadius: '4px' }}>
              #{genre}
            </span>
          ))}
        </div>

        <h1 className="article-title">{post.title}</h1>
        <p className="article-subtitle">{post.subtitle}</p>

        <div className="article-meta-row">
          <div className="author-chip">
            {post.author.avatar && (
              <Image
                src={post.author.avatar}
                alt={post.author.name}
                width={44}
                height={44}
                style={{ borderRadius: '50%' }}
              />
            )}
            <div>
              <div className="author-name">{post.author.name}</div>
              <div className="author-role">{post.author.role}</div>
            </div>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '1.5rem', fontSize: '0.85rem', color: 'var(--text-sub)' }}>
            <span style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
              <Clock size={16} />
              {post.readingTime}
            </span>
            <span style={{ display: 'flex', alignItems: 'center', gap: '5px' }}>
              <Calendar size={16} />
              {new Date(post.publishedAt).toLocaleDateString('pt-BR', {
                day: '2-digit',
                month: 'long',
                year: 'numeric',
              })}
            </span>
          </div>
        </div>
      </header>

      {/* Se for um REACT / REVIEW: Box de Ficha Técnica e Veredito */}
      {post.featuredMovie && (
        <section className="movie-specs-box">
          <div className="specs-poster">
            <Image
              src={post.posterImage}
              alt={post.featuredMovie.title}
              width={240}
              height={360}
              style={{ width: '100%', height: 'auto', display: 'block' }}
              priority
            />
          </div>

          <div className="specs-details">
            <div className="specs-score-bar">
              <div className="score-badge">
                <Star size={20} fill="#ffb703" />
                <span className="score-val">{post.featuredMovie.ratingFilmeJa}</span>
                <span className="score-max">/10 Nota FilmeJá</span>
              </div>
              <div style={{ fontSize: '0.9rem', color: 'var(--text-sub)' }}>
                ⭐ TMDB: <strong>{post.featuredMovie.ratingTmdb}</strong>
              </div>
            </div>

            <h2 style={{ fontFamily: 'var(--font-heading)', fontSize: '1.8rem' }}>
              {post.featuredMovie.title} ({post.featuredMovie.year})
            </h2>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: '0.6rem', fontSize: '0.9rem', color: 'var(--text-muted)' }}>
              <div><strong>Direção:</strong> {post.featuredMovie.director}</div>
              <div><strong>Duração:</strong> {post.featuredMovie.duration}</div>
              <div style={{ gridColumn: '1 / -1' }}>
                <strong>Elenco:</strong> {post.featuredMovie.cast.join(', ')}
              </div>
            </div>

            <div>
              <div style={{ fontSize: '0.85rem', color: 'var(--text-sub)', display: 'flex', alignItems: 'center', gap: '5px', marginBottom: '0.3rem' }}>
                <Tv size={15} />
                <strong>Onde Assistir no Brasil (Clique para abrir):</strong>
              </div>
              <div className="where-to-watch-pills">
                {post.featuredMovie.whereToWatch.map((plat) => (
                  <a
                    key={plat}
                    href={getStreamingSearchUrl(plat, post.featuredMovie?.title || '')}
                    target="_blank"
                    rel="noopener noreferrer nofollow"
                    className="watch-pill watch-pill-link"
                    title={`Assistir ${post.featuredMovie?.title} no ${plat}`}
                  >
                    <span>{plat}</span>
                    <ExternalLink size={12} style={{ opacity: 0.7 }} />
                  </a>
                ))}
              </div>
            </div>

            <p style={{ fontSize: '0.95rem', color: 'var(--text-muted)', lineHeight: '1.6', marginTop: '0.5rem' }}>
              <strong>Sinopse Oficial:</strong> {post.featuredMovie.synopsis}
            </p>
          </div>
        </section>
      )}

      {/* Se for uma LISTA TOP 5 / TOP 10: Cards Ordenados com Links Clicáveis */}
      {post.type === 'list' && post.listItems && (
        <section className="list-ranking-container">
          {post.listItems.map((item) => (
            <div key={item.rank} className="ranking-card" id={`filme-${item.rank}`}>
              <div className="ranking-number">#{item.rank}</div>

              <div className="ranking-poster">
                {item.reviewSlug ? (
                  <Link href={`/post/${item.reviewSlug}`} title={`Ver react e crítica de ${item.title}`}>
                    <Image
                      src={item.posterImage}
                      alt={item.title}
                      width={180}
                      height={270}
                      style={{ width: '100%', height: 'auto', display: 'block', borderRadius: '8px' }}
                    />
                  </Link>
                ) : (
                  <Image
                    src={item.posterImage}
                    alt={item.title}
                    width={180}
                    height={270}
                    style={{ width: '100%', height: 'auto', display: 'block', borderRadius: '8px' }}
                  />
                )}
              </div>

              <div className="ranking-info">
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '0.5rem' }}>
                  {item.reviewSlug ? (
                    <Link href={`/post/${item.reviewSlug}`} className="ranking-title-link">
                      <h3 style={{ display: 'inline-flex', alignItems: 'center', gap: '6px' }}>
                        {item.title} ({item.year})
                        <ChevronRight size={18} color="#e50914" />
                      </h3>
                    </Link>
                  ) : (
                    <h3>{item.title} ({item.year})</h3>
                  )}

                  {item.highlightTag && (
                    <span style={{ fontSize: '0.75rem', fontWeight: 'bold', background: 'rgba(229,9,20,0.15)', color: '#ff5e62', padding: '3px 8px', borderRadius: '4px' }}>
                      {item.highlightTag}
                    </span>
                  )}
                </div>

                <div className="ranking-meta">
                  Direção: <strong>{item.director}</strong> &bull; Nota FilmeJá: <strong style={{ color: '#ffb703' }}>{item.score}/10</strong>
                </div>

                {item.cast && item.cast.length > 0 && (
                  <div style={{ fontSize: '0.85rem', color: 'var(--text-sub)', marginBottom: '0.6rem', display: 'flex', alignItems: 'center', gap: '6px' }}>
                    <Users size={14} />
                    <span><strong>Elenco:</strong> {item.cast.join(', ')}</span>
                  </div>
                )}

                {item.synopsis && (
                  <p style={{ fontSize: '0.9rem', color: 'var(--text-sub)', fontStyle: 'italic', marginBottom: '0.8rem', lineHeight: '1.5' }}>
                    &ldquo;{item.synopsis}&rdquo;
                  </p>
                )}

                <p className="ranking-reason">
                  {item.whyWatch}
                </p>

                {item.highlightPoints && item.highlightPoints.length > 0 && (
                  <div style={{ background: '#181822', padding: '0.9rem 1.2rem', borderRadius: '8px', marginBottom: '1.2rem', border: '1px solid var(--border-color)' }}>
                    <div style={{ fontSize: '0.8rem', fontWeight: 'bold', color: '#ff5e62', textTransform: 'uppercase', marginBottom: '0.4rem', letterSpacing: '0.5px' }}>
                      Destaques da Produção:
                    </div>
                    <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '0.35rem', fontSize: '0.85rem', color: 'var(--text-muted)' }}>
                      {item.highlightPoints.map((pt, pti) => (
                        <li key={pti}>&bull; {pt}</li>
                      ))}
                    </ul>
                  </div>
                )}

                {/* Onde Assistir com Links Reais Clicáveis */}
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', flexWrap: 'wrap', marginBottom: item.reviewSlug ? '1.2rem' : '0' }}>
                  <span style={{ fontSize: '0.8rem', color: 'var(--text-sub)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                    <Tv size={14} />
                    Onde assistir:
                  </span>
                  {item.whereToWatch.map((plat) => (
                    <a
                      key={plat}
                      href={getStreamingSearchUrl(plat, item.title)}
                      target="_blank"
                      rel="noopener noreferrer nofollow"
                      className="watch-pill watch-pill-link"
                      title={`Assistir ${item.title} no ${plat}`}
                    >
                      <span>{plat}</span>
                      <ExternalLink size={12} style={{ opacity: 0.7 }} />
                    </a>
                  ))}
                </div>

                {/* Botão de Ler Crítica Completa se houver review individual */}
                {item.reviewSlug && (
                  <div style={{ marginTop: '0.8rem' }}>
                    <Link href={`/post/${item.reviewSlug}`} className="nav-link-cta" style={{ fontSize: '0.85rem', padding: '0.45rem 1rem', display: 'inline-flex', alignItems: 'center', gap: '6px' }}>
                      <Eye size={15} />
                      <span>Ler React & Crítica Completa de {item.title}</span>
                      <ChevronRight size={15} />
                    </Link>
                  </div>
                )}
              </div>
            </div>
          ))}
        </section>
      )}

      {/* Trailer Oficial do YouTube (se houver) */}
      {post.featuredMovie?.trailerYoutubeId && (
        <section style={{ margin: '3rem 0' }}>
          <h2 style={{ fontFamily: 'var(--font-heading)', fontSize: '1.4rem', marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <Film color="#e50914" size={22} />
            Trailer Oficial
          </h2>
          <div className="trailer-box">
            <iframe
              src={`https://www.youtube-nocookie.com/embed/${post.featuredMovie.trailerYoutubeId}?rel=0`}
              title={`Trailer de ${post.featuredMovie.title}`}
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowFullScreen
            ></iframe>
          </div>
        </section>
      )}

      {/* Prós e Contras (se houver) */}
      {post.featuredMovie && (
        <section className="pros-cons-grid">
          <div className="pros-box">
            <h4>
              <CheckCircle2 color="#10b981" size={20} />
              Pontos Fortes (O que brilha)
            </h4>
            <ul>
              {post.featuredMovie.pros.map((pro, i) => (
                <li key={i}>&bull; {pro}</li>
              ))}
            </ul>
          </div>

          <div className="cons-box">
            <h4>
              <XCircle color="#ef4444" size={20} />
              Pontos Fracos (Onde peca)
            </h4>
            <ul>
              {post.featuredMovie.cons.map((con, i) => (
                <li key={i}>&bull; {con}</li>
              ))}
            </ul>
          </div>
        </section>
      )}

      {/* Veredito Final (se houver) */}
      {post.featuredMovie?.verdict && (
        <section style={{
          background: 'linear-gradient(135deg, rgba(229, 9, 20, 0.1) 0%, rgba(20, 20, 26, 0.9) 100%)',
          border: '1px solid rgba(229, 9, 20, 0.3)',
          borderRadius: 'var(--radius-lg)',
          padding: '2rem',
          margin: '2.5rem 0',
        }}>
          <h3 style={{ fontFamily: 'var(--font-heading)', fontSize: '1.3rem', color: '#ff5e62', marginBottom: '0.8rem', display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Award size={22} />
            Veredito FilmeJá: Vale a Pena?
          </h3>
          <p style={{ fontSize: '1.05rem', color: 'var(--text-main)', lineHeight: '1.7' }}>
            {post.featuredMovie.verdict}
          </p>
        </section>
      )}

      {/* Conteúdo Editorial do Post */}
      <section style={{
        color: 'var(--text-muted)',
        fontSize: '1.1rem',
        lineHeight: '1.8',
        margin: '3rem 0',
        whiteSpace: 'pre-line',
      }}>
        {post.content}
      </section>

      {/* FAQ Acordeão (Rich Snippets para o Google) */}
      {post.faqs && post.faqs.length > 0 && (
        <section className="faq-section">
          <h2 className="faq-title">
            <HelpCircle color="#e50914" size={24} />
            Perguntas Frequentes (FAQ)
          </h2>
          <div className="faq-list">
            {post.faqs.map((faq, i) => (
              <div key={i} className="faq-item">
                <h3 className="faq-question">{faq.question}</h3>
                <p className="faq-answer">{faq.answer}</p>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Posts Relacionados (Links Internos para SEO) */}
      {relatedPosts.length > 0 && (
        <section style={{ marginTop: '4rem', paddingTop: '2.5rem', borderTop: '1px solid var(--border-color)' }}>
          <h2 className="section-title" style={{ marginBottom: '1.5rem' }}>
            <span className="bullet"></span>
            Você Também Pode Gostar
          </h2>
          <div className="posts-grid">
            {relatedPosts.map((rel) => (
              <article key={rel.id} className="post-card">
                <Link href={`/post/${rel.slug}`} className="post-card-thumb">
                  <Image
                    src={rel.coverImage}
                    alt={rel.title}
                    fill
                    sizes="(max-width: 768px) 100vw, 33vw"
                    style={{ objectFit: 'cover' }}
                  />
                </Link>
                <div className="post-card-body">
                  <Link href={`/post/${rel.slug}`}>
                    <h3 className="post-card-title" style={{ fontSize: '1.05rem' }}>
                      {rel.title}
                    </h3>
                  </Link>
                  <p className="post-card-excerpt" style={{ fontSize: '0.85rem' }}>
                    {rel.subtitle}
                  </p>
                </div>
              </article>
            ))}
          </div>
        </section>
      )}
    </article>
  );
}
