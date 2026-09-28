import type { Metadata } from 'next';
import Link from 'next/link';
import { Mail, MessageSquare, Send, ChevronRight } from 'lucide-react';

export const metadata: Metadata = {
  title: 'Fale com a Redação & Contato | FilmeJá',
  description: 'Entre em contato com os editores e críticos do FilmeJá para sugestões de pauta, parcerias editoriais e assessoria de imprensa.',
  alternates: {
    canonical: 'https://filmeja.com.br/contato',
  },
};

export default function ContatoPage() {
  return (
    <div className="container" style={{ paddingBottom: '5rem', maxWidth: '800px' }}>
      <nav aria-label="Breadcrumb" className="article-breadcrumbs" style={{ marginTop: '2rem' }}>
        <Link href="/">Início</Link>
        <ChevronRight size={14} />
        <span style={{ color: 'var(--text-main)' }}>Contato</span>
      </nav>

      <section style={{ padding: '2rem 0', borderBottom: '1px solid var(--border-color)' }}>
        <h1 style={{ fontFamily: 'var(--font-heading)', fontSize: 'clamp(2rem, 4vw, 2.8rem)', fontWeight: 800, marginBottom: '0.8rem' }}>
          Fale Conosco
        </h1>
        <p style={{ color: 'var(--text-muted)', fontSize: '1.05rem', lineHeight: '1.6' }}>
          Dúvidas, sugestões de filmes para react, parcerias de imprensa ou propostas comerciais? Envie uma mensagem diretamente para a nossa redação.
        </p>
      </section>

      <div style={{ marginTop: '3rem', display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '2rem' }}>
        <div style={{ background: 'var(--bg-card)', padding: '2rem', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-color)' }}>
          <Mail color="#e50914" size={28} style={{ marginBottom: '1rem' }} />
          <h2 style={{ fontSize: '1.2rem', fontFamily: 'var(--font-heading)', color: '#fff', marginBottom: '0.5rem' }}>E-mail Direto da Redação</h2>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.95rem', marginBottom: '1.2rem' }}>
            Respondemos em até 24 horas em dias úteis.
          </p>
          <a
            href="mailto:contato@filmeja.com.br"
            style={{ color: '#ff5e62', fontWeight: 700, fontSize: '1.05rem', textDecoration: 'none' }}
          >
            contato@filmeja.com.br
          </a>
        </div>

        <div style={{ background: 'var(--bg-card)', padding: '2rem', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-color)' }}>
          <MessageSquare color="#ffb703" size={28} style={{ marginBottom: '1rem' }} />
          <h2 style={{ fontSize: '1.2rem', fontFamily: 'var(--font-heading)', color: '#fff', marginBottom: '0.5rem' }}>Assessoria & Parcerias</h2>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.95rem', marginBottom: '1.2rem' }}>
            Para envio de screeners, cabines de imprensa e licenciamento.
          </p>
          <a
            href="mailto:imprensa@filmeja.com.br"
            style={{ color: '#ffb703', fontWeight: 700, fontSize: '1.05rem', textDecoration: 'none' }}
          >
            imprensa@filmeja.com.br
          </a>
        </div>
      </div>
    </div>
  );
}
