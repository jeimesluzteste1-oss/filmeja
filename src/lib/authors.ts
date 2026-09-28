export interface Author {
  id: string;
  name: string;
  role: string;
  avatar: string;
  bio: string;
  specialty: string;
  writingStyle: string;
  social: {
    instagram?: string;
    letterboxd?: string;
    twitter?: string;
  };
}

export const AUTHORS: Record<string, Author> = {
  lucas: {
    id: 'lucas',
    name: 'Lucas Andrade',
    role: 'Crítico Sênior & Editor-Chefe',
    avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200&auto=format&fit=crop&q=80',
    bio: 'Jornalista cultural formado pela USP e cinéfilo obstinado. Especialista em cinema de autor, horror psicológico, A24 e direção de arte. Viciado na obra de Robert Eggers e Ari Aster.',
    specialty: 'Horror Psicológico, Gótico e Cinema de Autor',
    writingStyle: 'Analítico, denso, refinado e focado na atmosfera, iluminação e metáforas visuais. Evita clichês e valoriza o cinema sensorial.',
    social: {
      letterboxd: 'https://letterboxd.com',
      twitter: 'https://x.com',
    },
  },
  beatriz: {
    id: 'beatriz',
    name: 'Beatriz Silveira',
    role: 'Crítica de Cinema de Gênero',
    avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200&auto=format&fit=crop&q=80',
    bio: 'Produtora audiovisual e fã inveterada de slashers, possessões demoníacas e body horror. Acredita que um bom filme de terror precisa deixar o espectador tenso na cadeira.',
    specialty: 'Slasher, Terror Sobrenatural e Body Horror',
    writingStyle: 'Direta, apaixonada, dinâmica e bem-humorada. Foca no ritmo dos sustos, efeitos práticos de sangue e maquiagem e no valor de entretenimento puro.',
    social: {
      instagram: 'https://instagram.com',
      letterboxd: 'https://letterboxd.com',
    },
  },
  guilherme: {
    id: 'guilherme',
    name: 'Guilherme Santos',
    role: 'Editor de Thrillers & Policiais',
    avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=200&auto=format&fit=crop&q=80',
    bio: 'Escritor de ficção policial e crítico obcecado por enredos labirínticos, mistérios de assassinato e plot twists que desafiam a lógica.',
    specialty: 'Suspense Psicológico, Neo-Noir e Mistérios',
    writingStyle: 'Investigativo, meticuloso e cético. Analisa cada pista do roteiro, furos de coerência e a psicologia dos personagens com precisão clínica.',
    social: {
      twitter: 'https://x.com',
    },
  },
  camila: {
    id: 'camila',
    name: 'Camila Fontes',
    role: 'Crítica de Sci-Fi & Fantasia',
    avatar: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=200&auto=format&fit=crop&q=80',
    bio: 'Pesquisadora em transmídia e entusiasta de ficção científica distópica, viagens no tempo e suspense espacial. Fascinada pelo impacto da tecnologia na narrativa.',
    specialty: 'Ficção Científica, Suspense Espacial e Distopias',
    writingStyle: 'Reflexiva, envolvente e filosófica. Disseca o subtexto futurista, a verossimilhança científica e o peso dramático das escolhas humanas no cosmos.',
    social: {
      letterboxd: 'https://letterboxd.com',
    },
  },
  thiago: {
    id: 'thiago',
    name: 'Thiago Rocha',
    role: 'Editor de Cinema Comercial & Ação',
    avatar: 'https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?w=200&auto=format&fit=crop&q=80',
    bio: 'Crítico de cinema de entretenimento e aficionado por coreografias de dublês, planos-sequência de tirar o fôlego e narrativas de sobrevivência extrema.',
    specialty: 'Filmes de Ação, Sobrevivência e Blockbusters',
    writingStyle: 'Energético, direto ao ponto e focado na adrenalina. Avalia se o filme entrega o que promete, o dinamismo da montagem e o carisma do elenco.',
    social: {
      instagram: 'https://instagram.com',
    },
  },
};

export function getAuthorById(id: string): Author {
  return AUTHORS[id] || AUTHORS.lucas;
}

export function getAllAuthors(): Author[] {
  return Object.values(AUTHORS);
}
