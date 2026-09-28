import type { Metadata } from 'next';
import Link from 'next/link';
import { ShieldCheck, ChevronRight } from 'lucide-react';

export const metadata: Metadata = {
  title: 'Política de Privacidade | FilmeJá',
  description: 'Política de privacidade, conformidade com a LGPD e termos de uso de cookies e publicidade do FilmeJá.',
  alternates: {
    canonical: 'https://filmeja.com.br/politica-de-privacidade',
  },
};

export default function PoliticaPrivacidadePage() {
  return (
    <div className="container" style={{ paddingBottom: '5rem', maxWidth: '900px' }}>
      <nav aria-label="Breadcrumb" className="article-breadcrumbs" style={{ marginTop: '2rem' }}>
        <Link href="/">Início</Link>
        <ChevronRight size={14} />
        <span style={{ color: 'var(--text-main)' }}>Política de Privacidade</span>
      </nav>

      <section style={{ padding: '2rem 0', borderBottom: '1px solid var(--border-color)' }}>
        <h1 style={{ fontFamily: 'var(--font-heading)', fontSize: 'clamp(2rem, 4vw, 2.8rem)', fontWeight: 800, marginBottom: '0.8rem' }}>
          Política de Privacidade
        </h1>
        <p style={{ color: 'var(--text-sub)', fontSize: '0.9rem' }}>
          Última atualização: {new Date().toLocaleDateString('pt-BR', { day: '2-digit', month: 'long', year: 'numeric' })}
        </p>
      </section>

      <div style={{ color: 'var(--text-muted)', lineHeight: '1.8', fontSize: '1rem', marginTop: '2.5rem', display: 'flex', flexDirection: 'column', gap: '1.8rem' }}>
        <p>
          A sua privacidade é extremamente importante para nós. É política do <strong>FilmeJá (filmeja.com.br)</strong> respeitar a sua privacidade em relação a qualquer informação sua que possamos coletar no site FilmeJá e outros sites que possuímos e operamos.
        </p>

        <h2 style={{ color: '#fff', fontSize: '1.4rem', fontFamily: 'var(--font-heading)' }}>1. Informações que Coletamos</h2>
        <p>
          Solicitamos informações pessoais apenas quando realmente precisamos delas para lhe fornecer um serviço, como o envio de newsletters ou resposta a mensagens enviadas pelo canal de contato. Fazemo-lo por meios justos e legais, com o seu conhecimento e consentimento, em total consonância com a <strong>Lei Geral de Proteção de Dados (LGPD - Lei nº 13.709/2018)</strong>.
        </p>

        <h2 style={{ color: '#fff', fontSize: '1.4rem', fontFamily: 'var(--font-heading)' }}>2. Cookies e Web Beacons</h2>
        <p>
          O site FilmeJá utiliza cookies para armazenar informações sobre as preferências dos visitantes e personalizar o conteúdo de acordo com o tipo de navegador ou outras informações enviadas pelo visitante.
        </p>

        <h2 style={{ color: '#fff', fontSize: '1.4rem', fontFamily: 'var(--font-heading)' }}>3. Publicidade e Cookies do Google (Google AdSense)</h2>
        <p>
          O Google é um fornecedor terceiro em nosso site. Ele utiliza cookies, conhecidos como cookies DART, para veicular anúncios aos visitantes do nosso site com base nas visitas feitas a este e a outros sites na Internet.
        </p>
        <p>
          Os visitantes podem optar por desativar o uso de cookies DART visitando a Política de Privacidade da rede de conteúdo e dos anúncios do Google no seguinte endereço:{' '}
          <a href="https://policies.google.com/technologies/ads" target="_blank" rel="noopener noreferrer" style={{ color: '#e50914', textDecoration: 'underline' }}>
            https://policies.google.com/technologies/ads
          </a>.
        </p>

        <h2 style={{ color: '#fff', fontSize: '1.4rem', fontFamily: 'var(--font-heading)' }}>4. Links para Sites de Terceiros</h2>
        <p>
          O nosso site contém links para sites externos (como serviços de streaming oficiais, trailers no YouTube, TMDB e plataformas parceiras). Não somos responsáveis pelas práticas de privacidade ou pelo conteúdo desses sites externos. Recomendamos que os usuários consultem as políticas de privacidade de qualquer site de terceiros que visitarem.
        </p>

        <h2 style={{ color: '#fff', fontSize: '1.4rem', fontFamily: 'var(--font-heading)' }}>5. Seus Direitos (LGPD)</h2>
        <p>
          Você tem o direito de solicitar a confirmação da existência de tratamento dos seus dados, o acesso aos dados coletados, a correção de dados incompletos ou a exclusão definitiva dos seus dados dos nossos registros a qualquer momento através do e-mail <strong>contato@filmeja.com.br</strong>.
        </p>
      </div>
    </div>
  );
}
