import Link from 'next/link';
import Image from 'next/image';
import { getAllPosts, getAllGenres } from '@/lib/posts';
import { Flame, Star, Sparkles, Clock, Calendar, ArrowRight, Eye, Film, TrendingUp } from 'lucide-react';

export default function HomePage() {
  const posts = getAllPosts();
  const genres = getAllGenres();
  
  // O post principal em destaque editorial
  const featuredPost = posts.find((p) => p.slug === 'react-nosferatu-2024-robert-eggers-vale-a-pena') || posts[0];
  const otherPosts = posts.filter((p) => p.id !== featuredPost?.id);

  return (
    <div>
      {/* Hero Editorial: Spotlight Cinematográfico Autoral */}
      {featuredPost && (
        <section style={{
          position: 'relative',
          minHeight: '480px',
          display: 'flex',
          alignItems: 'center',
          borderBottom: '1px solid var(--border-color)',
          overflow: 'hidden',
          background: '#0a0a0e',
        }}>
          {/* Imagem de Fundo (Backdrop HD com gradiente de cinema) */}
          <div style={{
            position: 'absolute',
            inset: 0,
            zIndex: 0,
          }}>
            <Image
              src={featuredPost.coverImage}
              alt={featuredPost.title}
              fill
              priority
              style={{
                objectFit: 'cover',
                objectPosition: 'center 20%',
                opacity: 0.38,
                filter: 'brightness(0.7) contrast(1.15)',
              }}
            />
            {/* Gradientes de escurecimento e vinheta */}
            <div style={{
              position: 'absolute',
              inset: 0,
              background: 'linear-gradient(90deg, #0a0a0e 0%, rgba(10, 10, 14, 0.92) 50%, rgba(10, 10, 14, 0.6) 100%), linear-gradient(0deg, #0a0a0e 0%, transparent 60%)',
            }} />
          </div>

          <div className="container" style={{ position: 'relative', zIndex: 1, padding: '3.5rem 1.25rem' }}>
            <div style={{ maxWidth: '780px' }}>
              <div style={{
                display: 'inline-flex',
                alignItems: 'center',
                gap: '6px',
                padding: '4px 12px',
                borderRadius: '6px',
                background: '#e50914',
                color: '#fff',
                fontSize: '0.75rem',
                fontWeight: 800,
                letterSpacing: '1px',
                textTransform: 'uppercase',
                marginBottom: '1.2rem',
                boxShadow: '0 4px 15px rgba(229, 9, 20, 0.5)',
              }}>
                <Flame size={14} />
                Destaque da Redação
              </div>

              <h1 style={{
                fontFamily: 'var(--font-heading)',
                fontSize: 'clamp(2rem, 4.5vw, 3.2rem)',
                fontWeight: 800,
                lineHeight: 1.15,
                letterSpacing: '-0.8px',
                marginBottom: '1rem',
                color: '#ffffff',
              }}>
                {featuredPost.title}
              </h1>

              <p style={{
                fontSize: '1.1rem',
                color: 'var(--text-muted)',
                lineHeight: '1.6',
                marginBottom: '1.8rem',
              }}>
                {featuredPost.subtitle}
              </p>

              <div style={{
                display: 'flex',
                alignItems: 'center',
                flexWrap: 'wrap',
                gap: '1.5rem',
                marginBottom: '2rem',
                fontSize: '0.85rem',
                color: 'var(--text-sub)',
              }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  {featuredPost.author.avatar && (
                    <Image
                      src={featuredPost.author.avatar}
                      alt={featuredPost.author.name}
                      width={28}
                      height={28}
                      style={{ borderRadius: '50%' }}
                    />
                  )}
                  <span style={{ color: 'var(--text-main)', fontWeight: 600 }}>
                    Por {featuredPost.author.name}
                  </span>
                </div>
                <span>&bull;</span>
                <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                  <Clock size={14} />
                  {featuredPost.readingTime}
                </span>
                <span>&bull;</span>
                <span style={{ color: '#ffb703', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '4px' }}>
                  <Star size={14} fill="#ffb703" />
                  9.4/10 Avaliação FilmeJá
                </span>
              </div>

              <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', flexWrap: 'wrap' }}>
                <Link
                  href={`/post/${featuredPost.slug}`}
                  className="nav-link-cta"
                  style={{
                    padding: '0.65rem 1.4rem',
                    fontSize: '0.95rem',
                    display: 'inline-flex',
                    alignItems: 'center',
                    gap: '8px',
                  }}
                >
                  <Eye size={17} />
                  <span>Ler Crítica Completa</span>
                  <ArrowRight size={16} />
                </Link>

                <Link
                  href="/tipo/list"
                  className="cat-pill"
                  style={{
                    padding: '0.65rem 1.2rem',
                    fontSize: '0.95rem',
                    color: 'var(--text-main)',
                    display: 'inline-flex',
                    alignItems: 'center',
                    gap: '6px',
                  }}
                >
                  <TrendingUp size={16} color="#e50914" />
                  <span>Ver Rankings Top 5</span>
                </Link>
              </div>
            </div>
          </div>
        </section>
      )}

      {/* Barra de Filtros Editoriais */}
      <div className="container" style={{ paddingTop: '1rem' }}>
        <div className="category-bar">
          <Link href="/" className="cat-pill active">
            Todos os Artigos
          </Link>
          <Link href="/tipo/list" className="cat-pill">
            🔥 Rankings Top 5
          </Link>
          <Link href="/tipo/react" className="cat-pill">
            ⭐ Críticas & Reacts
          </Link>
          {genres.map((g) => (
            <Link key={g} href={`/genero/${encodeURIComponent(g.toLowerCase())}`} className="cat-pill">
              {g}
            </Link>
          ))}
        </div>
      </div>

      {/* Grid Principal de Publicações */}
      <div className="container">
        <div className="section-head">
          <div>
            <h2 className="section-title">
              <span className="bullet"></span>
              Publicações Recentes da Redação
            </h2>
          </div>
          <span style={{ color: 'var(--text-sub)', fontSize: '0.85rem' }}>
            Atualizações diárias
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
                  {post.type === 'list' ? 'Top Ranking' : 'Crítica'}
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
                  <span style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                    <span style={{ fontWeight: 600, color: 'var(--text-main)' }}>
                      {post.author.name}
                    </span>
                  </span>
                  <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                    <Calendar size={13} />
                    {new Date(post.publishedAt).toLocaleDateString('pt-BR', {
                      day: '2-digit',
                      month: 'short',
                    })}
                  </span>
                </div>
              </div>
            </article>
          ))}
        </div>

        {/* Manifesto da Redação (Linguagem Humana e Editorial) */}
        <section style={{
          background: 'linear-gradient(180deg, #121217 0%, #0d0d12 100%)',
          border: '1px solid var(--border-color)',
          borderRadius: 'var(--radius-lg)',
          padding: '2.5rem',
          margin: '3rem 0 4rem',
        }}>
          <h2 style={{ fontFamily: 'var(--font-heading)', fontSize: '1.4rem', marginBottom: '0.8rem', color: '#ffffff' }}>
            Sobre o FilmeJá
          </h2>
          <div style={{ color: 'var(--text-muted)', lineHeight: '1.8', fontSize: '0.95rem', display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
            <p>
              O <strong>FilmeJá</strong> é um veículo editorial independente criado por cinéfilos que entendem a frustração de perder tempo rolando catálogos intermináveis de streaming.
              Nossas críticas e rankings são produzidos com rigor analítico, sem favorecimento a estúdios e com foco absoluto na experiência de quem assiste.
            </p>
            <p>
              Do terror gótico mais perturbador aos suspenses psicológicos com desfechos chocantes, nosso compromisso é entregar curadoria autêntica, links diretos de onde assistir e avaliações que vão direto ao ponto.
            </p>
          </div>
        </section>
      </div>
    </div>
  );
}
