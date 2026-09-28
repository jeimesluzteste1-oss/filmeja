import type { Metadata } from 'next';
import Link from 'next/link';
import { ChevronRight } from 'lucide-react';

export const metadata: Metadata = {
  title: 'Termos de Uso | FilmeJá',
  description: 'Termos e condições de uso do portal FilmeJá.',
  alternates: {
    canonical: 'https://filmeja.com.br/termos-de-uso',
  },
};

export default function TermosUsoPage() {
  return (
    <div className="container" style={{ paddingBottom: '5rem', maxWidth: '900px' }}>
      <nav aria-label="Breadcrumb" className="article-breadcrumbs" style={{ marginTop: '2rem' }}>
        <Link href="/">Início</Link>
        <ChevronRight size={14} />
        <span style={{ color: 'var(--text-main)' }}>Termos de Uso</span>
      </nav>

      <section style={{ padding: '2rem 0', borderBottom: '1px solid var(--border-color)' }}>
        <h1 style={{ fontFamily: 'var(--font-heading)', fontSize: 'clamp(2rem, 4vw, 2.8rem)', fontWeight: 800, marginBottom: '0.8rem' }}>
          Termos de Uso
        </h1>
        <p style={{ color: 'var(--text-sub)', fontSize: '0.9rem' }}>
          Última atualização: {new Date().toLocaleDateString('pt-BR', { day: '2-digit', month: 'long', year: 'numeric' })}
        </p>
      </section>

      <div style={{ color: 'var(--text-muted)', lineHeight: '1.8', fontSize: '1rem', marginTop: '2.5rem', display: 'flex', flexDirection: 'column', gap: '1.8rem' }}>
        <p>
          Ao acessar o site <strong>FilmeJá (filmeja.com.br)</strong>, você concorda em cumprir estes termos de serviço, todas as leis e regulamentos aplicáveis e concorda que é responsável pelo cumprimento de todas as leis locais aplicáveis.
        </p>

        <h2 style={{ color: '#fff', fontSize: '1.4rem', fontFamily: 'var(--font-heading)' }}>1. Direitos Autorais e Propriedade Intelectual</h2>
        <p>
          Os textos originais, críticas e matérias publicados no FilmeJá são de propriedade exclusiva da redação do FilmeJá, protegidos pelas leis internacionais de direitos autorais. Pôsteres, imagens promocionais e marcas de filmes mencionados no site são de propriedade de seus respectivos estúdios e distribuidoras, utilizados aqui sob a doutrina de uso informativo e crítica cultural (fair use).
        </p>

        <h2 style={{ color: '#fff', fontSize: '1.4rem', fontFamily: 'var(--font-heading)' }}>2. Isenção de Responsabilidade</h2>
        <p>
          Os materiais no site do FilmeJá são fornecidos &ldquo;como estão&rdquo;. O FilmeJá não oferece garantias, expressas ou implícitas, sobre a disponibilidade contínua de títulos nos catálogos de plataformas de streaming terceiras, uma vez que tais plataformas alteram periodicamente seus acordos de licenciamento.
        </p>

        <h2 style={{ color: '#fff', fontSize: '1.4rem', fontFamily: 'var(--font-heading)' }}>3. Modificações dos Termos</h2>
        <p>
          O FilmeJá pode revisar estes termos de serviço do site a qualquer momento, sem aviso prévio. Ao usar este site, você concorda em ficar vinculado à versão atual desses termos de serviço.
        </p>
      </div>
    </div>
  );
}
