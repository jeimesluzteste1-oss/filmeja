import type { Metadata } from 'next';
import Link from 'next/link';
import './globals.css';
import { Film, Flame, Star, Sparkles, Popcorn, Compass } from 'lucide-react';

export const metadata: Metadata = {
  metadataBase: new URL('https://filmeja.com.br'),
  title: {
    default: 'FilmeJá | Recomendações, Top Listas e Reacts de Filmes',
    template: '%s | FilmeJá',
  },
  description: 'O seu portal definitivo de cinema: os melhores filmes de terror, suspense e lançamentos de 2025 e 2026, com análises sinceras, listas imperdíveis e onde assistir.',
  keywords: [
    'filmes',
    'filme já',
    'filmeja',
    'recomendações de filmes',
    'filmes de terror 2025',
    'filmes de terror 2026',
    'top 5 filmes',
    'onde assistir filmes',
    'react de filmes',
    'critica de cinema'
  ],
  authors: [{ name: 'FilmeJá Editorial' }],
  creator: 'FilmeJá',
  publisher: 'FilmeJá',
  formatDetection: {
    email: false,
    address: false,
    telephone: false,
  },
  alternates: {
    canonical: 'https://filmeja.com.br',
  },
  openGraph: {
    title: 'FilmeJá | O Melhor do Cinema e Streaming',
    description: 'Encontre o que assistir hoje: listas Top 5, análises sinceras e os filmes mais aterrorizantes e empolgantes.',
    url: 'https://filmeja.com.br',
    siteName: 'FilmeJá',
    locale: 'pt_BR',
    type: 'website',
    images: [
      {
        url: 'https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=1200&auto=format&fit=crop&q=80',
        width: 1200,
        height: 630,
        alt: 'FilmeJá - Portal de Cinema',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'FilmeJá | Recomendações e Reacts de Filmes',
    description: 'Listas, críticas sinceras e recomendações dos melhores filmes.',
    images: ['https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=1200&auto=format&fit=crop&q=80'],
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const jsonLdWebsite = {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    name: 'FilmeJá',
    url: 'https://filmeja.com.br',
    potentialAction: {
      '@type': 'SearchAction',
      target: 'https://filmeja.com.br/busca?q={search_term_string}',
      'query-input': 'required name=search_term_string',
    },
  };

  return (
    <html lang="pt-BR">
      <head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLdWebsite) }}
        />
      </head>
      <body>
        {/* Header */}
        <header className="site-header">
          <div className="container header-inner">
            <Link href="/" className="brand-logo" aria-label="FilmeJá Página Inicial">
              <Film className="w-6 h-6 text-red-600" color="#e50914" size={28} />
              <span>
                Filme<span className="logo-accent">Já</span>
              </span>
              <span className="brand-badge">2026</span>
            </Link>

            <nav className="main-nav" aria-label="Navegação Principal">
              <Link href="/" className="nav-link">
                Início
              </Link>
              <Link href="/genero/terror" className="nav-link">
                Terror
              </Link>
              <Link href="/genero/suspense" className="nav-link">
                Suspense
              </Link>
              <Link href="/tipo/list" className="nav-link">
                Top Listas
              </Link>
              <Link href="/tipo/react" className="nav-link nav-link-cta">
                <Sparkles size={16} style={{ display: 'inline', marginRight: '4px', verticalAlign: 'middle' }} />
                Reacts & Análises
              </Link>
            </nav>
          </div>
        </header>

        {/* Conteúdo Principal */}
        <main>{children}</main>

        {/* Footer */}
        <footer className="site-footer">
          <div className="container">
            <div className="footer-grid">
              <div className="footer-brand">
                <Link href="/" className="brand-logo">
                  <Film color="#e50914" size={26} />
                  <span>Filme<span className="logo-accent">Já</span></span>
                </Link>
                <p>
                  O seu guia inteligente de cinema. Análises sinceras, listas dos melhores filmes,
                  dicas de streaming e reacts dos lançamentos mais aguardados de 2025 e 2026.
                </p>
              </div>

              <div className="footer-col">
                <h4>Gêneros em Alta</h4>
                <ul className="footer-links">
                  <li><Link href="/genero/terror">Filmes de Terror</Link></li>
                  <li><Link href="/genero/suspense">Filmes de Suspense</Link></li>
                  <li><Link href="/genero/sobrenatural">Sobrenatural</Link></li>
                  <li><Link href="/genero/mistério">Mistério & Ocultismo</Link></li>
                </ul>
              </div>

              <div className="footer-col">
                <h4>Formatos</h4>
                <ul className="footer-links">
                  <li><Link href="/tipo/list">Listas Top 5 & Top 10</Link></li>
                  <li><Link href="/tipo/react">Reacts Sem Spoilers</Link></li>
                  <li><Link href="/onde-assistir">Onde Assistir no Streaming</Link></li>
                  <li><Link href="/lancamentos-2026">Lançamentos 2026</Link></li>
                </ul>
              </div>

              <div className="footer-col">
                <h4>Sobre & Contato</h4>
                <ul className="footer-links">
                  <li><Link href="/sobre">Sobre o FilmeJá</Link></li>
                  <li><Link href="/politica-de-privacidade">Política de Privacidade</Link></li>
                  <li><Link href="/termos-de-uso">Termos de Uso</Link></li>
                  <li><Link href="/contato">Fale Conosco</Link></li>
                </ul>
              </div>
            </div>

            <div className="footer-bottom">
              <div>
                &copy; {new Date().getFullYear()} FilmeJá (filmeja.com.br) &bull; Todos os direitos reservados.
              </div>
              <div>
                Otimizado para o Google &bull; Core Web Vitals 100%
              </div>
            </div>
          </div>
        </footer>
      </body>
    </html>
  );
}
