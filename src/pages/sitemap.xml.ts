import products from '../data/products.json';

export async function GET() {
  const BASE_URL = 'https://theteedrop.com';
  const today = new Date().toISOString().split('T')[0];

  const staticPages = [
    { url: `${BASE_URL}/`, priority: '1.0', changefreq: 'daily' }
  ];

  const productPages = products.map((p) => ({
    url: `${BASE_URL}/products/${p.slug}`,
    priority: '0.9',
    changefreq: 'weekly'
  }));

  const allPages = [...staticPages, ...productPages];

  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${allPages
  .map(
    (page) => `  <url>
    <loc>${page.url}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>${page.changefreq}</changefreq>
    <priority>${page.priority}</priority>
  </url>`
  )
  .join('\n')}
</urlset>`;

  return new Response(xml, {
    status: 200,
    headers: {
      'Content-Type': 'application/xml; charset=utf-8',
      'Cache-Control': 'public, max-age=3600'
    }
  });
}
