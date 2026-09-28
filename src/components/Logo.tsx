import React from 'react';

interface LogoProps {
  size?: 'sm' | 'md' | 'lg';
  showTagline?: boolean;
}

export default function Logo({ size = 'md', showTagline = false }: LogoProps) {
  const iconDimensions = size === 'sm' ? 28 : size === 'lg' ? 44 : 36;
  const fontSize = size === 'sm' ? '1.25rem' : size === 'lg' ? '1.85rem' : '1.5rem';

  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: '10px', textDecoration: 'none' }}>
      {/* Ícone de Marca Autoral (Emblema Cinema FilmeJá) */}
      <div
        style={{
          width: `${iconDimensions}px`,
          height: `${iconDimensions}px`,
          borderRadius: '10px',
          background: 'linear-gradient(135deg, #e50914 0%, #8e050c 100%)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          boxShadow: '0 4px 15px rgba(229, 9, 20, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.3)',
          position: 'relative',
          flexShrink: 0,
        }}
      >
        <svg
          width={iconDimensions * 0.62}
          height={iconDimensions * 0.62}
          viewBox="0 0 24 24"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          {/* Símbolo dinâmico de filme com claquete e play integrado */}
          <path
            d="M4 6C4 4.89543 4.89543 4 6 4H18C19.1046 4 20 4.89543 20 6V18C20 19.1046 19.1046 20 18 20H6C4.89543 20 4 19.1046 4 18V6Z"
            stroke="white"
            strokeWidth="2"
            strokeLinecap="round"
          />
          <path
            d="M9.5 8.5L16 12L9.5 15.5V8.5Z"
            fill="white"
          />
          <circle cx="7" cy="7" r="1" fill="white" opacity="0.6" />
          <circle cx="17" cy="7" r="1" fill="white" opacity="0.6" />
          <circle cx="7" cy="17" r="1" fill="white" opacity="0.6" />
          <circle cx="17" cy="17" r="1" fill="white" opacity="0.6" />
        </svg>
      </div>

      {/* Tipografia de Marca */}
      <div style={{ display: 'flex', flexDirection: 'column', lineHeight: 1 }}>
        <div
          style={{
            fontFamily: 'var(--font-heading)',
            fontSize: fontSize,
            fontWeight: 800,
            letterSpacing: '-0.5px',
            color: '#ffffff',
            display: 'flex',
            alignItems: 'baseline',
          }}
        >
          FILME<span style={{ color: '#e50914', textShadow: '0 0 20px rgba(229, 9, 20, 0.6)' }}>JÁ</span>
        </div>
        {showTagline && (
          <span
            style={{
              fontSize: '0.62rem',
              fontWeight: 700,
              letterSpacing: '1.5px',
              textTransform: 'uppercase',
              color: 'var(--text-sub)',
              marginTop: '3px',
            }}
          >
            Portal de Cinema
          </span>
        )}
      </div>
    </div>
  );
}
