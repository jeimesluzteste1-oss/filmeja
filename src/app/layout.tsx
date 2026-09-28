import type { Metadata } from 'next';
import Link from 'next/link';
import './globals.css';
import Logo from '@/components/Logo';
import { Sparkles, Flame, Tv, Compass } from 'lucide-react';

export const metadata: Metadata = {
  metadataBase: new URL('https://filmeja.com.br'),
  title: {
    default: 'FilmeJá | Críticas, Rankings e Onde Assistir aos Melhores Filmes',
    template: '%s | FilmeJá',
  },
  description: 'O seu portal definitivo de cinema e streaming: os filmes de terror, suspense e lançamentos que realmente valem o seu tempo, com análises sinceras e sem spoilers.',
  keywords: [
    'filmes',
    'filme já',
    'filmeja',
    'recomendações de filmes',
    'filmes de terror',
    'filmes de suspense',
    'top 5 filmes',
    'onde assistir filmes',
    'critica de cinema',
    'react filmes'
  ],
  authors: [{ name: 'Redação FilmeJá' }],
  creator: 'FilmeJá',
  publisher: 'FilmeJá',
  alternates: {
    canonical: 'https://filmeja.com.br',
  },
  openGraph: {
    title: 'FilmeJá | O Melhor do Cinema e Streaming',
    description: 'Encontre o que assistir hoje: rankings afiados, críticas sinceras e onde encontrar cada produção no Brasil.',
    url: 'https://filmeja.com.br',
    siteName: 'FilmeJá',
    locale: 'pt_BR',
    type: 'website',
    images: [
      {
        url: 'https://image.tmdb.org/t/p/original/fbkUfzmVzEBFSt6p7VigknREIJT.jpg',
        width: 1200,
        height: 630,
        alt: 'FilmeJá - Portal de Cinema',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'FilmeJá | Críticas e Rankings de Cinema',
    description: 'Listas, críticas sinceras e recomendações dos melhores filmes.',
    images: ['https://image.tmdb.org/t/p/original/fbkUfzmVzEBFSt6p7VigknREIJT.jpg'],
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
        {/* Header Profissional com Logo Autoral */}
        <header className="site-header">
          <div className="container header-inner">
            <Link href="/" aria-label="FilmeJá Página Inicial">
              <Logo size="md" showTagline={true} />
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
                Rankings & Top 5
              </Link>
              <Link href="/tipo/react" className="nav-link nav-link-cta">
                <Sparkles size={15} style={{ display: 'inline', marginRight: '5px', verticalAlign: 'middle' }} />
                Críticas & Reacts
              </Link>
            </nav>
          </div>
        </header>

        {/* Conteúdo Principal */}
        <main>{children}</main>

        {/* Footer Editorial Limpo */}
        <footer className="site-footer">
          <div className="container">
            <div className="footer-grid">
              <div className="footer-brand">
                <Link href="/">
                  <Logo size="md" showTagline={true} />
                </Link>
                <p>
                  Curadoria independente de cinema e streaming. Análises sinceras, listas dos melhores filmes
                  e onde assistir às produções mais marcantes da atualidade.
                </p>
              </div>

              <div className="footer-col">
                <h4>Gêneros</h4>
                <ul className="footer-links">
                  <li><Link href="/genero/terror">Terror & Horror</Link></li>
                  <li><Link href="/genero/suspense">Suspense Psicológico</Link></li>
                  <li><Link href="/genero/sobrenatural">Sobrenatural</Link></li>
                  <li><Link href="/genero/mistério">Mistério & Ocultismo</Link></li>
                </ul>
              </div>

              <div className="footer-col">
                <h4>Formatos</h4>
                <ul className="footer-links">
                  <li><Link href="/tipo/list">Rankings Top 5 & Top 10</Link></li>
                  <li><Link href="/tipo/react">Críticas Sem Spoilers</Link></li>
                  <li><Link href="/genero/cinema">Em Cartaz & Novidades</Link></li>
                </ul>
              </div>

              <div className="footer-col">
                <h4>Editorial</h4>
                <ul className="footer-links">
                  <li><Link href="/sobre">Sobre a Redação</Link></li>
                  <li><Link href="/politica-de-privacidade">Privacidade</Link></li>
                  <li><Link href="/termos-de-uso">Termos de Uso</Link></li>
                  <li><Link href="/contato">Contato</Link></li>
                </ul>
              </div>
            </div>

            <div className="footer-bottom">
              <div>
                &copy; {new Date().getFullYear()} FilmeJá. Todos os direitos reservados.
              </div>
              <div style={{ color: 'var(--text-sub)' }}>
                Feito com paixão por cinema &bull; Curadoria independente
              </div>
            </div>
          </div>
        </footer>
      </body>
    </html>
  );
}
