export async function GET() {
  const content = 'google.com, pub-4175684739488041, DIRECT, f08c47fec0942fa0';
  return new Response(content, {
    headers: {
      'Content-Type': 'text/plain; charset=utf-8',
      'Cache-Control': 'public, max-age=3600',
    },
  });
}
