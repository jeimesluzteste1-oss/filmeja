import type { Metadata } from 'next';
import Image from 'next/image';
import Link from 'next/link';
import { getAllAuthors } from '@/lib/authors';
import { Film, Award, ShieldCheck, Heart, Sparkles, ChevronRight } from 'lucide-react';

export const metadata: Metadata = {
  title: 'Sobre a Redação e Linha Editorial | FilmeJá',
  description: 'Conheça a equipe de críticos e editores do FilmeJá, nossos princípios éticos de curadoria independente e nossa paixão por cinema e streaming.',
  alternates: {
    canonical: 'https://filmeja.com.br/sobre',
  },
};

export default function SobrePage() {
  const authors = getAllAuthors();

  return (
    <div className="container" style={{ paddingBottom: '5rem' }}>
      <nav aria-label="Breadcrumb" className="article-breadcrumbs" style={{ marginTop: '2rem' }}>
        <Link href="/">Início</Link>
        <ChevronRight size={14} />
        <span style={{ color: 'var(--text-main)' }}>Sobre a Redação</span>
      </nav>

      {/* Hero Institucional */}
      <section style={{ padding: '2.5rem 0 3rem', borderBottom: '1px solid var(--border-color)' }}>
        <h1 style={{ fontFamily: 'var(--font-heading)', fontSize: 'clamp(2.2rem, 5vw, 3.2rem)', fontWeight: 800, marginBottom: '1rem', letterSpacing: '-0.8px' }}>
          Quem Somos &bull; <span style={{ color: '#e50914' }}>FilmeJá</span>
        </h1>
        <p style={{ fontSize: '1.2rem', color: 'var(--text-muted)', lineHeight: '1.7', maxWidth: '820px' }}>
          O <strong>FilmeJá</strong> é um portal brasileiro de jornalismo cultural e curadoria cinematográfica independente.
          Nascemos da convicção de que você não deveria gastar meia hora navegando em menus confusos de streaming para encontrar um filme ruim.
        </p>
      </section>

      {/* Nossos Princípios */}
      <section style={{ margin: '3.5rem 0' }}>
        <h2 style={{ fontFamily: 'var(--font-heading)', fontSize: '1.7rem', marginBottom: '1.5rem', display: 'flex', alignItems: 'center', gap: '8px' }}>
          <ShieldCheck color="#e50914" size={24} />
          Nossos Compromissos Editoriais
        </h2>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '1.5rem' }}>
          <div style={{ background: 'var(--bg-card)', padding: '1.8rem', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-color)' }}>
            <h3 style={{ fontSize: '1.15rem', color: '#ff5e62', marginBottom: '0.6rem' }}>1. Opinião 100% Independente</h3>
            <p style={{ color: 'var(--text-muted)', fontSize: '0.95rem', lineHeight: '1.6' }}>
              Nossos críticos avaliam cada filme sem qualquer interferência de estúdios ou distribuidoras. Se o filme for uma obra-prima, nós aplaudimos; se decepcionar, dizemos abertamente.
            </p>
          </div>

          <div style={{ background: 'var(--bg-card)', padding: '1.8rem', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-color)' }}>
            <h3 style={{ fontSize: '1.15rem', color: '#ffb703', marginBottom: '0.6rem' }}>2. Sem Spoilers Desnecessários</h3>
            <p style={{ color: 'var(--text-muted)', fontSize: '0.95rem', lineHeight: '1.6' }}>
              Nossos reacts e críticas são construídos para ajudar você a decidir se vale a pena assistir à produção, respeitando sempre o prazer de descobrir a história na tela.
            </p>
          </div>

          <div style={{ background: 'var(--bg-card)', padding: '1.8rem', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-color)' }}>
            <h3 style={{ fontSize: '1.15rem', color: '#10b981', marginBottom: '0.6rem' }}>3. Onde Assistir de Verdade</h3>
            <p style={{ color: 'var(--text-muted)', fontSize: '0.95rem', lineHeight: '1.6' }}>
              Todas as nossas recomendações apontam diretamente para as plataformas oficiais onde os filmes estão disponíveis no Brasil, combatendo a pirataria e facilitando seu acesso.
            </p>
          </div>
        </div>
      </section>

      {/* Os 5 Críticos da Redação */}
      <section style={{ margin: '4rem 0' }}>
        <h2 style={{ fontFamily: 'var(--font-heading)', fontSize: '1.8rem', marginBottom: '2rem', display: 'flex', alignItems: 'center', gap: '8px' }}>
          <Sparkles color="#e50914" size={24} />
          Conheça os Críticos & Editores
        </h2>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: '2rem' }}>
          {authors.map((author) => (
            <div
              key={author.id}
              style={{
                background: 'var(--bg-card)',
                borderRadius: 'var(--radius-lg)',
                padding: '2rem',
                border: '1px solid var(--border-color)',
                display: 'flex',
                flexDirection: 'column',
                gap: '1.2rem',
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: '1.2rem' }}>
                <div style={{ position: 'relative', width: '70px', height: '70px', flexShrink: 0 }}>
                  <Image
                    src={author.avatar}
                    alt={author.name}
                    fill
                    style={{ borderRadius: '50%', objectFit: 'cover', border: '2px solid #e50914' }}
                  />
                </div>
                <div>
                  <h3 style={{ fontFamily: 'var(--font-heading)', fontSize: '1.25rem', color: '#ffffff' }}>
                    {author.name}
                  </h3>
                  <div style={{ fontSize: '0.85rem', color: '#ff5e62', fontWeight: 600 }}>
                    {author.role}
                  </div>
                </div>
              </div>

              <div style={{ fontSize: '0.82rem', color: 'var(--text-sub)', fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                Especialidade: <span style={{ color: 'var(--text-main)' }}>{author.specialty}</span>
              </div>

              <p style={{ color: 'var(--text-muted)', fontSize: '0.92rem', lineHeight: '1.6', flexGrow: 1 }}>
                {author.bio}
              </p>

              <div style={{ borderTop: '1px solid var(--border-color)', paddingTop: '0.8rem', fontSize: '0.85rem', color: 'var(--text-sub)' }}>
                <em>Estilo de escrita: {author.writingStyle}</em>
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
