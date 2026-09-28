/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    unoptimized: true, // Desativa proxy do Vercel para eliminar erro 402 Payment Required e carregar 100% direto do TMDB/Unsplash
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'image.tmdb.org',
      },
      {
        protocol: 'https',
        hostname: 'images.unsplash.com',
      },
      {
        protocol: 'https',
        hostname: 'i.ytimg.com',
      },
      {
        protocol: 'https',
        hostname: 'm.media-amazon.com',
      }
    ],
  },
};

module.exports = nextConfig;
