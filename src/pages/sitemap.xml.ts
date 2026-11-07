import products from '../data/products.json';
import articles from '../data/articles.json';
import hubs from '../data/hubs.json';

export async function GET() {
  const BASE_URL = 'https://theteedrop.com';
  const today = new Date().toISOString().split('T')[0];

  const staticPages = [
    { url: `${BASE_URL}/`, priority: '1.0', changefreq: 'daily' },
    { url: `${BASE_URL}/blog`, priority: '0.9', changefreq: 'daily' },
    { url: `${BASE_URL}/size-guide`, priority: '0.8', changefreq: 'monthly' }
  ];

  const productPages = products.map((p) => ({
    url: `${BASE_URL}/products/${p.slug}`,
    priority: '0.95',
    changefreq: 'daily'
  }));

  const blogPages = articles.map((a) => ({
    url: `${BASE_URL}/blog/${a.slug}`,
    priority: '0.85',
    changefreq: 'weekly'
  }));

  const hubPages = hubs.map((h) => ({
    url: `${BASE_URL}/hubs/${h.slug}`,
    priority: '0.8',
    changefreq: 'weekly'
  }));

  const allPages = [...staticPages, ...productPages, ...blogPages, ...hubPages];

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
