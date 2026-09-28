'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import { Sparkles, Tv, Star, ArrowRight, RefreshCw, Film } from 'lucide-react';

interface QuickMovie {
  title: string;
  year: number;
  genre: string;
  rating: number;
  platform: string;
  poster: string;
  pitch: string;
  slug: string;
}

const MOVIES_DATABASE: QuickMovie[] = [
  {
    title: 'Nosferatu',
    year: 2024,
    genre: 'Terror',
    rating: 9.4,
    platform: 'Prime Video',
    poster: 'https://image.tmdb.org/t/p/w500/fbkUfzmVzEBFSt6p7VigknREIJT.jpg',
    pitch: 'A mais assustadora e bela releitura do vampirismo gótico já feita no cinema contemporâneo.',
    slug: 'react-nosferatu-2024-robert-eggers-vale-a-pena',
  },
  {
    title: 'A Substância',
    year: 2024,
    genre: 'Terror',
    rating: 9.5,
    platform: 'MUBI',
    poster: 'https://image.tmdb.org/t/p/w500/vWeOgzlhnP1sS23H3rzctGHB9Nb.jpg',
    pitch: 'Body horror chocante e visceral com atuações consagradas de Demi Moore e Margaret Qualley.',
    slug: 'react-a-substancia-2024-vale-a-pena',
  },
  {
    title: 'Seven: Os Sete Crimes Capitais',
    year: 1995,
    genre: 'Suspense',
    rating: 9.8,
    platform: 'Max',
    poster: 'https://image.tmdb.org/t/p/w500/dZXYPSEaXCeigR2GEuZoukNmLTf.jpg',
    pitch: 'A caçada policial definitiva entre detetives brilhantes e um serial killer meticuloso.',
    slug: 'top-5-thrillers-investigativos-com-crimes-obsessivos',
  },
  {
    title: 'Alien: Romulus',
    year: 2024,
    genre: 'Ficção Científica',
    rating: 9.1,
    platform: 'Disney+',
    poster: 'https://image.tmdb.org/t/p/w500/jB0W9tn4w07MFn7sTfqRTBLVytF.jpg',
    pitch: 'Terror e suspense espacial com efeitos práticos claustrofóbicos e ritmo implacável.',
    slug: 'react-alien-romulus-2024-suspense-espacial-vale-a-pena',
  },
  {
    title: 'Trem-Bala',
    year: 2022,
    genre: 'Ação',
    rating: 9.1,
    platform: 'Netflix',
    poster: 'https://image.tmdb.org/t/p/w500/8gdBMIYwPPxp3b9FjY9yCxme5Rs.jpg',
    pitch: 'Brad Pitt em uma comédia de ação explosiva e hilária dentro do trem mais rápido do Japão.',
    slug: 'top-5-filmes-de-acao-frenetica-e-adrenalina-pura-no-streaming',
  },
  {
    title: 'Ilha do Medo',
    year: 2010,
    genre: 'Suspense',
    rating: 9.5,
    platform: 'Netflix',
    poster: 'https://image.tmdb.org/t/p/w500/erl801HYIodoIBGZeFk0GTwCUBh.jpg',
    pitch: 'Leonardo DiCaprio em um manicômio isolado com um dos maiores plot twists da história.',
    slug: 'top-5-filmes-de-suspense-psicologico-com-finais-chocantes',
  },
  {
    title: 'Pânico VI',
    year: 2023,
    genre: 'Terror',
    rating: 9.2,
    platform: 'Paramount+',
    poster: 'https://image.tmdb.org/t/p/w500/y6OLmLAAblvGPrBWqghWhi3xK5b.jpg',
    pitch: 'Ghostface solto na cidade de Nova York com perseguições brutais e suspense sem pausa.',
    slug: 'top-5-filmes-de-terror-slasher-modernos-para-maratonar',
  },
];

export default function MovieFinder() {
  const [selectedGenre, setSelectedGenre] = useState<string>('Todos');
  const [selectedMovie, setSelectedMovie] = useState<QuickMovie>(MOVIES_DATABASE[0]);
  const [isSpinning, setIsSpinning] = useState<boolean>(false);

  const genres = ['Todos', 'Terror', 'Suspense', 'Ação', 'Ficção Científica'];

  const handleRecommend = () => {
    setIsSpinning(true);
    setTimeout(() => {
      const filtered = selectedGenre === 'Todos'
        ? MOVIES_DATABASE
        : MOVIES_DATABASE.filter((m) => m.genre === selectedGenre);

      const available = filtered.length > 0 ? filtered : MOVIES_DATABASE;
      const nextMovie = available[Math.floor(Math.random() * available.length)];
      setSelectedMovie(nextMovie);
      setIsSpinning(false);
    }, 250);
  };

  return (
    <section style={{
      background: 'linear-gradient(135deg, #161622 0%, #0e0e14 100%)',
      border: '1px solid rgba(229, 9, 20, 0.35)',
      borderRadius: 'var(--radius-lg)',
      padding: '2.5rem',
      margin: '3.5rem 0',
      boxShadow: '0 15px 40px -10px rgba(0, 0, 0, 0.8), 0 0 25px rgba(229, 9, 20, 0.1)',
    }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '1rem', marginBottom: '1.5rem' }}>
        <div>
          <div style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', fontSize: '0.8rem', fontWeight: 800, color: '#e50914', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '0.4rem' }}>
            <Sparkles size={15} />
            Ferramenta Interativa FilmeJá
          </div>
          <h2 style={{ fontFamily: 'var(--font-heading)', fontSize: '1.6rem', color: '#fff' }}>
            Sem Ideia do Que Assistir Hoje?
          </h2>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.95rem' }}>
            Escolha seu gênero preferido e deixe nosso curador indicar a melhor opção testada pela redação.
          </p>
        </div>

        {/* Botão de Sortear */}
        <button
          onClick={handleRecommend}
          className="nav-link-cta"
          style={{
            padding: '0.75rem 1.6rem',
            fontSize: '0.95rem',
            display: 'inline-flex',
            alignItems: 'center',
            gap: '8px',
            transform: isSpinning ? 'scale(0.96)' : 'none',
            transition: 'all 0.2s ease',
          }}
        >
          <RefreshCw size={18} style={{ transform: isSpinning ? 'rotate(180deg)' : 'none', transition: 'transform 0.3s ease' }} />
          <span>Sortear Novo Filme</span>
        </button>
      </div>

      {/* Seletor de Gênero */}
      <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap', marginBottom: '2rem' }}>
        {genres.map((g) => (
          <button
            key={g}
            onClick={() => setSelectedGenre(g)}
            style={{
              padding: '0.4rem 1rem',
              borderRadius: '9999px',
              fontSize: '0.85rem',
              fontWeight: 600,
              background: selectedGenre === g ? '#e50914' : '#1c1c28',
              color: selectedGenre === g ? '#fff' : 'var(--text-muted)',
              border: `1px solid ${selectedGenre === g ? '#e50914' : 'rgba(255,255,255,0.1)'}`,
              transition: 'all 0.2s ease',
            }}
          >
            {g}
          </button>
        ))}
      </div>

      {/* Card do Filme Sorteado */}
      {selectedMovie && (
        <div style={{
          background: '#0d0d12',
          border: '1px solid var(--border-color)',
          borderRadius: 'var(--radius-md)',
          padding: '1.5rem',
          display: 'grid',
          gridTemplateColumns: '120px 1fr',
          gap: '1.5rem',
          alignItems: 'center',
        }}>
          <div style={{ position: 'relative', width: '120px', height: '180px', borderRadius: '8px', overflow: 'hidden', flexShrink: 0 }}>
            <Image
              src={selectedMovie.poster}
              alt={selectedMovie.title}
              fill
              style={{ objectFit: 'cover' }}
            />
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.6rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap' }}>
              <span style={{ fontSize: '0.75rem', fontWeight: 800, background: 'rgba(229,9,20,0.15)', color: '#ff5e62', padding: '3px 8px', borderRadius: '4px' }}>
                #{selectedMovie.genre}
              </span>
              <span style={{ color: '#ffb703', fontSize: '0.85rem', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '4px' }}>
                <Star size={14} fill="#ffb703" />
                {selectedMovie.rating}/10
              </span>
              <span style={{ fontSize: '0.82rem', color: 'var(--text-sub)' }}>
                {selectedMovie.year}
              </span>
            </div>

            <h3 style={{ fontFamily: 'var(--font-heading)', fontSize: '1.4rem', color: '#fff' }}>
              {selectedMovie.title}
            </h3>

            <p style={{ color: 'var(--text-muted)', fontSize: '0.95rem', lineHeight: '1.5' }}>
              {selectedMovie.pitch}
            </p>

            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '1rem', marginTop: '0.5rem', paddingTop: '0.8rem', borderTop: '1px solid var(--border-color)' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.85rem', color: 'var(--text-sub)' }}>
                <Tv size={15} color="#e50914" />
                <span>Onde assistir: <strong style={{ color: 'var(--text-main)' }}>{selectedMovie.platform}</strong></span>
              </div>

              <Link
                href={`/post/${selectedMovie.slug}`}
                style={{
                  fontSize: '0.85rem',
                  fontWeight: 700,
                  color: '#ff5e62',
                  display: 'inline-flex',
                  alignItems: 'center',
                  gap: '4px',
                  textDecoration: 'none',
                }}
              >
                <span>Ler Crítica & Análise</span>
                <ArrowRight size={14} />
              </Link>
            </div>
          </div>
        </div>
      )}
    </section>
  );
}
