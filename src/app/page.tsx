import Link from 'next/link';
import Image from 'next/image';
import { getAllPosts, getAllGenres } from '@/lib/posts';
import { Flame, Star, Sparkles, Clock, Calendar, ArrowRight, PlayCircle, Award, Film } from 'lucide-react';

export default function HomePage() {
  const posts = getAllPosts();
  const genres = getAllGenres();
  const featuredPost = posts[0];
  const listPosts = posts.filter((p) => p.type === 'list');
  const reactPosts = posts.filter((p) => p.type === 'react');

  return (
    <div>
      {/* Hero Section */}
      <section className="hero-banner">
        <div className="container">
          <div className="hero-tag">
            <Flame size={16} />
            <span>Destaque do Cinema 2026</span>
          </div>

          <h1 className="hero-title">
            Os Melhores Filmes, Listas <br />
            <span style={{ color: '#ff5e62' }}>Top 5 & Reacts Sinceros</span>
          </h1>

          <p className="hero-desc">
            Chega de perder 40 minutos navegando nos catálogos de streaming sem saber o que assistir.
            Aqui você encontra recomendações afiadas, listas dos melhores filmes de terror e suspense
            e análises completas sem enrolação.
          </p>

          {featuredPost && (
            <Link href={`/post/${featuredPost.slug}`} className="nav-link-cta" style={{ display: 'inline-flex', alignItems: 'center', gap: '8px' }}>
              <span>Ler Matéria em Destaque</span>
              <ArrowRight size={18} />
            </Link>
          )}
        </div>
      </section>

      {/* Categories Bar */}
      <div className="container">
        <div className="category-bar">
          <Link href="/" className="cat-pill active">
            Todos os Filmes
          </Link>
          <Link href="/tipo/list" className="cat-pill">
            🔥 Top Listas
          </Link>
          <Link href="/tipo/react" className="cat-pill">
            ⭐ Reacts & Críticas
          </Link>
          {genres.map((g) => (
            <Link key={g} href={`/genero/${encodeURIComponent(g.toLowerCase())}`} className="cat-pill">
              {g}
            </Link>
          ))}
        </div>
      </div>

      {/* Main Grid: Todos os Lançamentos e Artigos */}
      <div className="container">
        <div className="section-head">
          <div>
            <h2 className="section-title">
              <span className="bullet"></span>
              Últimas Publicações & Recomendações
            </h2>
          </div>
          <span style={{ color: 'var(--text-sub)', fontSize: '0.9rem' }}>
            Atualizado diariamente
          </span>
        </div>

        <div className="posts-grid">
          {posts.map((post) => (
            <article key={post.id} className="post-card">
              <Link href={`/post/${post.slug}`} className="post-card-thumb" aria-label={post.title}>
                <Image
                  src={post.coverImage}
                  alt={post.title}
                  fill
                  sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
                  style={{ objectFit: 'cover' }}
                  priority={post.id === 'post-1'}
                />
                <span className={`post-type-badge ${post.type}`}>
                  {post.type === 'list' ? 'Top Lista' : 'React & Análise'}
                </span>
              </Link>

              <div className="post-card-body">
                <div className="post-card-genres">
                  {post.genres.map((genre) => (
                    <span key={genre} className="genre-tag">
                      #{genre}
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

        {/* Bloco de SEO e Autoridade para o Google */}
        <section style={{
          background: 'var(--bg-card)',
          border: '1px solid var(--border-color)',
          borderRadius: 'var(--radius-lg)',
          padding: '2.5rem',
          margin: '3rem 0 4rem',
        }}>
          <h2 style={{ fontFamily: 'var(--font-heading)', fontSize: '1.5rem', marginBottom: '1rem', color: '#ff5e62' }}>
            FilmeJá: O Seu Portal de Recomendações e Críticas de Filmes
          </h2>
          <div style={{ color: 'var(--text-muted)', lineHeight: '1.8', fontSize: '0.95rem', display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <p>
              O <strong>FilmeJá</strong> nasceu para ser o seu destino principal quando a dúvida for: <em>&ldquo;O que assistir hoje à noite?&rdquo;</em>.
              Em um mercado saturado de produções semanais na Netflix, Prime Video, Max, Disney+ e cinemas, encontrar joias cinematográficas verdadeiras
              exige curadoria especializada.
            </p>
            <p>
              Nossa equipe se dedica a garimpar os melhores <strong>filmes de terror de 2025 e 2026</strong>, clássicos do suspense psicológico com reviravoltas
              inesperadas (plot twists) e análises em formato de <strong>react sem spoilers</strong>. Cada publicação traz a ficha técnica real, indicação
              precisa de onde assistir no Brasil e avaliações que vão direto ao ponto.
            </p>
          </div>
        </section>
      </div>
    </div>
  );
}
