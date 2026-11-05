#!/usr/bin/env python3
"""
The Tee Drop - Clean, Human, Minimalist Storefront & Blog Generator
Palette: Crisp White & Light Sky Blue (Clean, Human DTC Brand, No AI Neons)
Features:
 - Full SEO, GEO & AEO Standards (Schema.org JSON-LD, llms.txt, robots.txt, sitemap.xml)
 - Editorial Blog / Journal for Topical Authority & Human E-E-A-T
 - Direct Mayzing Checkout Integration
"""

import os
import sys
import json
from datetime import datetime

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_URL = "https://theteedrop.com"
MAYZING_DEFAULT = "https://store.theteedrop.com/store/MNye"

def load_data():
    with open("products.json", "r", encoding="utf-8") as f:
        products = json.load(f)
    try:
        with open("articles.json", "r", encoding="utf-8") as f:
            articles = json.load(f)
    except FileNotFoundError:
        articles = []
    return products, articles

# Shared CSS string (Clean White + Light Blue)
SHARED_CSS = """
    :root {
      --bg: #ffffff;
      --bg-soft: #f8fafc;
      --bg-sky: #f0f9ff;
      --border: #e2e8f0;
      --border-focus: #bae6fd;
      --text: #0f172a;
      --text-muted: #64748b;
      --blue-primary: #0284c7;
      --blue-hover: #0369a1;
      --blue-light: #e0f2fe;
      --blue-soft: #38bdf8;
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: var(--bg);
      color: var(--text);
      font-family: var(--font-sans);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }
    a { color: inherit; text-decoration: none; transition: all 0.2s ease; }
    img { max-width: 100%; display: block; }

    /* Top Strip */
    .top-strip {
      background: var(--blue-light);
      color: var(--blue-hover);
      text-align: center;
      padding: 10px 16px;
      font-size: 0.85rem;
      font-weight: 600;
      letter-spacing: 0.2px;
      border-bottom: 1px solid #bae6fd;
    }
    .top-strip span { font-weight: 700; color: #0369a1; }

    /* Header */
    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px 6%;
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
    }
    .logo {
      font-size: 1.35rem;
      font-weight: 800;
      letter-spacing: -0.5px;
      color: var(--text);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .logo-dot {
      width: 10px;
      height: 10px;
      background: var(--blue-soft);
      border-radius: 50%;
      display: inline-block;
    }
    nav {
      display: flex;
      align-items: center;
      gap: 32px;
      font-size: 0.95rem;
      font-weight: 500;
      color: var(--text-muted);
    }
    nav a:hover { color: var(--blue-primary); }
    .btn-nav-cart {
      background: var(--blue-primary);
      color: #ffffff !important;
      padding: 10px 22px;
      border-radius: 999px;
      font-weight: 600;
      font-size: 0.85rem;
      box-shadow: 0 2px 8px rgba(2, 132, 199, 0.25);
    }
    .btn-nav-cart:hover {
      background: var(--blue-hover);
      transform: translateY(-1px);
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 24px;
    }

    /* Footer */
    footer {
      background: var(--bg-soft);
      border-top: 1px solid var(--border);
      padding: 60px 0 40px;
      margin-top: 100px;
      color: var(--text-muted);
      font-size: 0.9rem;
    }
    .footer-grid {
      display: grid;
      grid-template-columns: 2fr 1fr 1fr 1fr;
      gap: 40px;
      margin-bottom: 50px;
    }
    @media(max-width: 800px) {
      .footer-grid { grid-template-columns: 1fr; gap: 30px; }
      nav { display: none; }
    }
    .footer-brand h4 { color: var(--text); font-size: 1.1rem; margin-bottom: 12px; }
    .footer-col h5 { color: var(--text); font-size: 0.9rem; margin-bottom: 14px; text-transform: uppercase; letter-spacing: 0.5px; }
    .footer-col ul { list-style: none; }
    .footer-col ul li { margin-bottom: 8px; }
    .footer-col ul li a:hover { color: var(--blue-primary); }
    .footer-bottom {
      border-top: 1px solid var(--border);
      padding-top: 25px;
      text-align: center;
      font-size: 0.85rem;
    }
"""

HOME_EXTRA_CSS = """
    /* Hero Section - Clean, Human, Airy */
    .hero {
      padding: 80px 0 60px;
      text-align: center;
      background: radial-gradient(circle at 50% 20%, #f0f9ff 0%, #ffffff 80%);
      border-bottom: 1px solid var(--border);
    }
    .hero-label {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--blue-light);
      color: var(--blue-hover);
      padding: 6px 16px;
      border-radius: 999px;
      font-size: 0.85rem;
      font-weight: 600;
      margin-bottom: 24px;
    }
    .hero h1 {
      font-size: clamp(2.4rem, 5vw, 3.8rem);
      font-weight: 800;
      letter-spacing: -1.5px;
      line-height: 1.15;
      color: var(--text);
      max-width: 820px;
      margin: 0 auto 20px;
    }
    .hero h1 em {
      font-style: normal;
      color: var(--blue-primary);
    }
    .hero p {
      font-size: 1.15rem;
      color: var(--text-muted);
      max-width: 620px;
      margin: 0 auto 36px;
      font-weight: 400;
    }
    .hero-actions {
      display: flex;
      justify-content: center;
      gap: 16px;
      flex-wrap: wrap;
    }
    .btn-primary {
      background: var(--blue-primary);
      color: #ffffff;
      padding: 14px 32px;
      border-radius: 999px;
      font-weight: 600;
      font-size: 1rem;
      box-shadow: 0 4px 14px rgba(2, 132, 199, 0.3);
    }
    .btn-primary:hover {
      background: var(--blue-hover);
      transform: translateY(-2px);
    }
    .btn-secondary {
      background: #ffffff;
      color: var(--text);
      border: 1px solid var(--border);
      padding: 14px 28px;
      border-radius: 999px;
      font-weight: 600;
      font-size: 1rem;
    }
    .btn-secondary:hover {
      background: var(--bg-soft);
      border-color: #cbd5e1;
    }

    .trust-bar {
      display: flex;
      justify-content: center;
      gap: 36px;
      flex-wrap: wrap;
      padding: 30px 0 0;
      color: var(--text-muted);
      font-size: 0.85rem;
      font-weight: 500;
    }
    .trust-bar span { display: inline-flex; align-items: center; gap: 8px; }

    .section-head {
      margin: 70px 0 35px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }
    .section-head h2 {
      font-size: 1.8rem;
      font-weight: 800;
      letter-spacing: -0.5px;
    }
    .section-head p { color: var(--text-muted); font-size: 0.95rem; margin-top: 4px; }

    /* Product Grid */
    .product-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 32px;
    }
    .product-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      position: relative;
      transition: all 0.25s ease;
    }
    .product-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 12px 28px rgba(15, 23, 42, 0.07);
      border-color: var(--border-focus);
    }
    .product-badge {
      position: absolute;
      top: 14px;
      left: 14px;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(4px);
      color: var(--blue-primary);
      border: 1px solid var(--border);
      padding: 4px 12px;
      border-radius: 999px;
      font-size: 0.75rem;
      font-weight: 700;
      z-index: 2;
    }
    .product-thumb {
      display: block;
      background: var(--bg-soft);
      height: 380px;
      overflow: hidden;
    }
    .product-thumb img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.4s ease;
    }
    .product-card:hover .product-thumb img {
      transform: scale(1.04);
    }
    .product-body {
      padding: 22px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }
    .product-meta {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
      font-size: 0.8rem;
    }
    .product-category {
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      font-weight: 600;
    }
    .product-rating {
      color: #eab308;
      font-weight: 700;
    }
    .product-title {
      font-size: 1.15rem;
      font-weight: 700;
      line-height: 1.35;
      margin-bottom: 8px;
    }
    .product-title a:hover { color: var(--blue-primary); }
    .product-desc-snippet {
      color: var(--text-muted);
      font-size: 0.9rem;
      margin-bottom: 20px;
      line-height: 1.5;
    }
    .product-footer {
      margin-top: auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 16px;
      border-top: 1px solid var(--border);
    }
    .price-wrap { display: flex; align-items: baseline; gap: 8px; }
    .price { font-size: 1.35rem; font-weight: 800; color: var(--text); }
    .compare-price {
      font-size: 0.9rem;
      color: var(--text-muted);
      text-decoration: line-through;
    }
    .btn-order {
      background: var(--blue-primary);
      color: #ffffff;
      padding: 9px 20px;
      border-radius: var(--radius-sm);
      font-weight: 600;
      font-size: 0.85rem;
    }
    .btn-order:hover { background: var(--blue-hover); }

    .values-strip {
      background: var(--bg-sky);
      border: 1px solid #e0f2fe;
      border-radius: var(--radius-lg);
      padding: 50px 30px;
      margin: 90px 0;
    }
    .values-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 30px;
      text-align: center;
    }
    .value-item h4 { font-size: 1.1rem; font-weight: 700; margin-bottom: 8px; color: var(--text); }
    .value-item p { font-size: 0.9rem; color: var(--text-muted); line-height: 1.5; }

    /* Blog / Journal Grid */
    .blog-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
      gap: 32px;
    }
    .article-card {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: all 0.25s ease;
    }
    .article-card:hover {
      transform: translateY(-3px);
      box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
    }
    .article-thumb { height: 220px; overflow: hidden; background: var(--bg-soft); }
    .article-thumb img { width: 100%; height: 100%; object-fit: cover; }
    .article-body { padding: 24px; display: flex; flex-direction: column; flex-grow: 1; }
    .article-meta { font-size: 0.8rem; color: var(--text-muted); margin-bottom: 8px; }
    .article-title { font-size: 1.2rem; font-weight: 700; line-height: 1.35; margin-bottom: 10px; }
    .article-title a:hover { color: var(--blue-primary); }
    .article-excerpt { font-size: 0.9rem; color: var(--text-muted); margin-bottom: 16px; line-height: 1.5; }
    .read-more { font-weight: 600; color: var(--blue-primary); font-size: 0.85rem; margin-top: auto; }

    .faq-wrapper {
      max-width: 800px;
      margin: 40px auto 80px;
    }
    .faq-item {
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      margin-bottom: 12px;
      overflow: hidden;
    }
    .faq-item summary {
      padding: 18px 20px;
      cursor: pointer;
      font-weight: 600;
      color: var(--text);
    }
    .faq-item summary:hover { color: var(--blue-primary); }
    .faq-answer {
      padding: 0 20px 20px;
      color: var(--text-muted);
      font-size: 0.95rem;
    }
"""

def generate_index_html(products, articles):
    cards_html = ""
    for p in products:
        checkout_link = p.get("mayzing_checkout_url") or MAYZING_DEFAULT
        cards_html += f"""
        <article class="product-card">
          <div class="product-badge">{p.get('badge', 'New Drop')}</div>
          <a href="/products/{p['slug']}.html" class="product-thumb">
            <img src="{p['image']}" alt="{p['title']}" loading="lazy" width="400" height="400">
          </a>
          <div class="product-body">
            <div class="product-meta">
              <span class="product-category">{p['category']}</span>
              <span class="product-rating">★ {p['rating']}</span>
            </div>
            <h3 class="product-title">
              <a href="/products/{p['slug']}.html">{p['title']}</a>
            </h3>
            <p class="product-desc-snippet">{p['description'][:95]}...</p>
            <div class="product-footer">
              <div class="price-wrap">
                <span class="price">${p['price']:.2f}</span>
                <span class="compare-price">${p['compare_at_price']:.2f}</span>
              </div>
              <a href="{checkout_link}" class="btn-order" target="_blank" rel="noopener">
                Order Drop
              </a>
            </div>
          </div>
        </article>
        """

    blog_cards_html = ""
    for a in articles:
        blog_cards_html += f"""
        <article class="article-card">
          <a href="/blog/{a['slug']}.html" class="article-thumb">
            <img src="{a['image']}" alt="{a['title']}" loading="lazy" width="600" height="350">
          </a>
          <div class="article-body">
            <div class="article-meta">
              <span>{a['date']}</span> • <span>{a['read_time']}</span>
            </div>
            <h3 class="article-title">
              <a href="/blog/{a['slug']}.html">{a['title']}</a>
            </h3>
            <p class="article-excerpt">{a['excerpt']}</p>
            <a href="/blog/{a['slug']}.html" class="read-more">Read journal entry →</a>
          </div>
        </article>
        """

    schema_website = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "The Tee Drop",
        "url": BASE_URL,
        "description": "Clean, heavyweight graphic tees and oversized pump covers. Thoughtfully printed on 100% ringspun cotton with local US & European fulfillment."
    }

    schema_itemlist = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Live Drops",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "url": f"{BASE_URL}/products/{p['slug']}.html",
                "name": p["title"]
            } for i, p in enumerate(products)
        ]
    }

    schema_faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": "How does sizing and fit work on The Tee Drop shirts?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Our blanks are cut with an intentional relaxed streetwear silhouette with slightly lowered shoulder seams. Order your standard true-to-size for a comfortable everyday fit, or size up one size for a slouchy pump-cover skate fit."
                }
            },
            {
                "@type": "Question",
                "name": "Where are orders printed and shipped from?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "We print on-demand via certified regional facilities in North America (USA, Canada) and Western Europe (UK, EU). Orders typically arrive within 3 to 6 business days with door-to-door tracking."
                }
            },
            {
                "@type": "Question",
                "name": "What type of fabric and inks do you use?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Every drop uses 100% combed ringspun cotton (240+ GSM heavyweight) with pre-shrunk treatment. All designs are printed using eco-friendly water-based DTG inks that stay soft on skin and resist cracking."
                }
            }
        ]
    }

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Tee Drop | Thoughtfully Made Heavyweight Graphic Tees</title>
  <meta name="description" content="Minimalist, heavyweight graphic tees cut from 240+ GSM combed ringspun cotton. Printed on demand with local US & Europe delivery.">
  <link rel="canonical" href="{BASE_URL}/">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="The Tee Drop | Heavyweight Graphic Tees">
  <meta property="og:description" content="Clean streetwear drops and relaxed graphic tees. 100% combed cotton, printed and shipped locally in the US & Europe.">
  <meta property="og:url" content="{BASE_URL}/">
  <meta property="og:image" content="{products[0]['image'] if products else ''}">

  <!-- Twitter Meta -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="The Tee Drop">
  <meta name="twitter:description" content="Clean heavyweight graphic tees. Locally fulfilled in US & EU.">
  <meta name="twitter:image" content="{products[0]['image'] if products else ''}">

  <link rel="alternate" type="text/plain" href="{BASE_URL}/llms.txt" title="LLMs Context">

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {json.dumps(schema_website, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(schema_itemlist, indent=2)}
  </script>
  <script type="application/ld+json">
  {json.dumps(schema_faq, indent=2)}
  </script>

  <style>
  {SHARED_CSS}
  {HOME_EXTRA_CSS}
  </style>
</head>
<body>

  <!-- Top Strip -->
  <div class="top-strip">
    <span>Free US & Europe Delivery</span> on orders over $50 • Locally fulfilled on premium heavyweight blanks
  </div>

  <!-- Header -->
  <header>
    <a href="/" class="logo">
      <span class="logo-dot"></span> The Tee Drop
    </a>
    <nav>
      <a href="#drops">Drops</a>
      <a href="#journal">Journal</a>
      <a href="#fabric">Fabric & Sizing</a>
      <a href="#faq">FAQ</a>
    </nav>
    <a href="{MAYZING_DEFAULT}" class="btn-nav-cart" target="_blank" rel="noopener">Store Checkout 🛒</a>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="container">
      <div class="hero-label">Authentic Streetwear & Lifestyle Drops</div>
      <h1>Heavyweight Graphic Tees.<br><em>Built To Be Worn.</em></h1>
      <p>Clean silhouettes crafted from 240+ GSM combed ringspun cotton. Printed on demand with water-based DTG inks and shipped locally across North America and Europe.</p>
      
      <div class="hero-actions">
        <a href="#drops" class="btn-primary">Browse Current Drops</a>
        <a href="#journal" class="btn-secondary">Read The Journal</a>
      </div>

      <div class="trust-bar">
        <span>✓ 100% Pre-Shrunk Combed Cotton</span>
        <span>✓ 3–6 Day US & Canada Delivery</span>
        <span>✓ 4–7 Day UK & Europe Delivery</span>
        <span>✓ 30-Day Reprint Guarantee</span>
      </div>
    </div>
  </section>

  <!-- Live Drops Catalog -->
  <main class="container" id="drops">
    <div class="section-head">
      <div>
        <h2>Current Live Drops</h2>
        <p>Thoughtful graphic tees available in small batches. Shipped directly from certified local printers.</p>
      </div>
    </div>
    <div class="product-grid">
      {cards_html}
    </div>
  </main>

  <!-- Brand Fabric & Quality Strip -->
  <section class="container" id="fabric">
    <div class="values-strip">
      <div class="values-grid">
        <div class="value-item">
          <h4>240+ GSM Cotton</h4>
          <p>Heavy enough to hold its structured drape without clinging, light enough for all-day breathability.</p>
        </div>
        <div class="value-item">
          <h4>Water-Based DTG</h4>
          <p>Non-toxic inks cured directly into yarn fibers. Zero rubbery sticker feel; lasts 60+ cold washes.</p>
        </div>
        <div class="value-item">
          <h4>Regional Production</h4>
          <p>Printed locally via Mayzing partners in the US, UK, and EU. Shorter transit distances and faster arrival.</p>
        </div>
        <div class="value-item">
          <h4>Human Responsibility</h4>
          <p>Every piece is printed specifically for you upon ordering, eliminating dead unsold apparel waste.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Journal / Blog Section -->
  <section class="container" id="journal">
    <div class="section-head">
      <div>
        <h2>The Journal</h2>
        <p>Insights on fabric craftsmanship, styling oversized silhouettes, and print longevity.</p>
      </div>
    </div>
    <div class="blog-grid">
      {blog_cards_html}
    </div>
  </section>

  <!-- AEO FAQ Section -->
  <section class="container" id="faq">
    <div class="section-head" style="text-align: center; display: block; margin-top: 80px;">
      <h2>Frequently Asked Questions</h2>
      <p>Everything you need to know about our blanks, sizing, and fulfillment.</p>
    </div>
    <div class="faq-wrapper">
      <details class="faq-item">
        <summary>How do The Tee Drop shirts fit?</summary>
        <div class="faq-answer">
          Our graphics are printed on a contemporary relaxed streetwear cut with lowered shoulder points and a sturdy, lay-flat collar. We recommend choosing your standard true-to-size for an everyday relaxed drape, or going one size up if you prefer a pronounced oversized skate/gym pump-cover look.
        </div>
      </details>
      <details class="faq-item">
        <summary>How fast will my order arrive?</summary>
        <div class="faq-answer">
          Because we print locally in regional facilities closest to you (US, Canada, UK, and Europe), average transit is 3 to 6 business days. You will receive a tracking link the moment your shirt leaves the drying belt.
        </div>
      </details>
      <details class="faq-item">
        <summary>How should I care for my graphic tee?</summary>
        <div class="faq-answer">
          Machine wash cold (30°C) inside out with like colors. Air drying on a wooden hanger preserves fabric softness and prevents shrinkage. Avoid hot tumble dryers and do not iron directly across printed graphics.
        </div>
      </details>
      <details class="faq-item">
        <summary>What is your return and guarantee policy?</summary>
        <div class="faq-answer">
          If your item arrives with any manufacturing flaw, misprinted graphic, or transit damage, we will reprint and reship a brand-new replacement free of charge within 30 days.
        </div>
      </details>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <h4>The Tee Drop</h4>
          <p>Mindfully produced graphic tees and modern streetwear staples. Printed on demand on 100% combed ringspun cotton.</p>
        </div>
        <div class="footer-col">
          <h5>Shop</h5>
          <ul>
            <li><a href="#drops">All Drops</a></li>
            <li><a href="{MAYZING_DEFAULT}" target="_blank">Store Checkout</a></li>
            <li><a href="#fabric">Fabric Guide</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>Journal</h5>
          <ul>
            <li><a href="#journal">Style Guides</a></li>
            <li><a href="#journal">Fabric Longevity</a></li>
            <li><a href="/llms.txt" target="_blank">LLMs Context</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>Support</h5>
          <ul>
            <li><a href="#faq">FAQ</a></li>
            <li><a href="#faq">Shipping & Returns</a></li>
            <li><a href="mailto:support@theteedrop.com">Contact Team</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© {datetime.now().year} The Tee Drop (theteedrop.com). All rights reserved. Fulfillment powered by Mayzing Global.</p>
      </div>
    </div>
  </footer>

</body>
</html>
"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("✅ Created: Clean White & Light Sky Blue index.html")

PRODUCT_EXTRA_CSS = """
    .p-container {
      max-width: 1080px;
      margin: 40px auto 80px;
      padding: 0 24px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 50px;
    }
    @media(max-width: 768px) {
      .p-container { grid-template-columns: 1fr; gap: 30px; }
    }
    .p-gallery {
      background: var(--bg-soft);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      overflow: hidden;
    }
    .p-gallery img { width: 100%; height: auto; display: block; }
    .p-details { display: flex; flex-direction: column; }
    .p-badge {
      display: inline-block;
      background: var(--blue-light);
      color: var(--blue-hover);
      padding: 4px 12px;
      border-radius: 999px;
      font-size: 0.8rem;
      font-weight: 700;
      align-self: flex-start;
      margin-bottom: 12px;
    }
    .p-title { font-size: 2rem; font-weight: 800; line-height: 1.25; margin-bottom: 10px; }
    .p-rating { color: #eab308; font-size: 0.9rem; margin-bottom: 16px; font-weight: 600; }
    .p-rating span { color: var(--text-muted); }
    .p-price-row { display: flex; align-items: baseline; gap: 12px; margin-bottom: 24px; }
    .p-price { font-size: 1.8rem; font-weight: 800; color: var(--text); }
    .p-compare { font-size: 1.1rem; color: var(--text-muted); text-decoration: line-through; }
    .p-desc { color: var(--text-muted); font-size: 1rem; line-height: 1.6; margin-bottom: 24px; }
    .p-features { list-style: none; margin-bottom: 30px; }
    .p-features li { margin-bottom: 8px; color: var(--text); font-weight: 500; font-size: 0.95rem; }
    .btn-buy-lg {
      background: var(--blue-primary);
      color: #ffffff;
      padding: 16px 28px;
      border-radius: var(--radius-sm);
      font-weight: 700;
      font-size: 1.05rem;
      text-align: center;
      display: block;
      box-shadow: 0 4px 14px rgba(2, 132, 199, 0.25);
      margin-bottom: 20px;
    }
    .btn-buy-lg:hover { background: var(--blue-hover); transform: translateY(-1px); }
    .p-guarantee {
      background: var(--bg-sky);
      border: 1px solid #bae6fd;
      border-radius: var(--radius-sm);
      padding: 16px;
      font-size: 0.85rem;
      color: #0369a1;
      line-height: 1.5;
    }
    .back-btn { display: inline-block; margin-top: 24px; color: var(--text-muted); font-size: 0.9rem; }
    .back-btn:hover { color: var(--blue-primary); }
"""

def generate_product_pages(products):
    os.makedirs("products", exist_ok=True)
    for p in products:
        checkout_link = p.get("mayzing_checkout_url") or MAYZING_DEFAULT
        features_li = "".join([f"<li>✓ {f}</li>" for f in p.get("features", [])])
        
        product_schema = {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": p["title"],
            "image": [p["image"]],
            "description": p["description"],
            "sku": p["id"],
            "brand": { "@type": "Brand", "name": "The Tee Drop" },
            "offers": {
                "@type": "Offer",
                "url": f"{BASE_URL}/products/{p['slug']}.html",
                "priceCurrency": "USD",
                "price": f"{p['price']:.2f}",
                "priceValidUntil": "2027-12-31",
                "itemCondition": "https://schema.org/NewCondition",
                "availability": "https://schema.org/InStock"
            },
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": str(p["rating"]),
                "reviewCount": str(p["reviews_count"])
            }
        }

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{p['title']} | The Tee Drop</title>
  <meta name="description" content="{p['description']}">
  <link rel="canonical" href="{BASE_URL}/products/{p['slug']}.html">

  <meta property="og:type" content="product">
  <meta property="og:title" content="{p['title']} | The Tee Drop">
  <meta property="og:description" content="{p['description']}">
  <meta property="og:url" content="{BASE_URL}/products/{p['slug']}.html">
  <meta property="og:image" content="{p['image']}">

  <script type="application/ld+json">
  {json.dumps(product_schema, indent=2)}
  </script>

  <style>
  {SHARED_CSS}
  {PRODUCT_EXTRA_CSS}
  </style>
</head>
<body>

  <header>
    <a href="/" class="logo"><span class="logo-dot"></span> The Tee Drop</a>
    <a href="{checkout_link}" class="btn-nav-cart" target="_blank" rel="noopener">Store Checkout 🛒</a>
  </header>

  <main class="p-container">
    <div class="p-gallery">
      <img src="{p['image']}" alt="{p['title']}" width="600" height="600">
    </div>

    <div class="p-details">
      <div class="p-badge">{p.get('badge', 'Drop Release')}</div>
      <h1 class="p-title">{p['title']}</h1>
      <div class="p-rating">★ {p['rating']} <span>({p['reviews_count']} reviews)</span></div>

      <div class="p-price-row">
        <span class="p-price">${p['price']:.2f}</span>
        <span class="p-compare">${p['compare_at_price']:.2f}</span>
      </div>

      <p class="p-desc">{p['description']}</p>

      <ul class="p-features">
        {features_li}
      </ul>

      <a href="{checkout_link}" class="btn-buy-lg" target="_blank" rel="noopener">
        Order Drop via Official Store ⚡
      </a>

      <div class="p-guarantee">
        <strong>🔒 Secure Mayzing Order Fulfillment</strong><br>
        Direct shipping across North America and Europe. Every shirt comes with our 30-day reprint or refund guarantee.
      </div>

      <a href="/" class="back-btn">← Back to all drops</a>
    </div>
  </main>

</body>
</html>
"""
        with open(f"products/{p['slug']}.html", "w", encoding="utf-8") as f:
            f.write(html)
    print(f"✅ Created: {len(products)} Product SEO Pages")

BLOG_EXTRA_CSS = """
    .article-container {
      max-width: 760px;
      margin: 50px auto 80px;
      padding: 0 24px;
    }
    .article-header { margin-bottom: 30px; text-align: center; }
    .article-badge {
      display: inline-block;
      background: var(--blue-light);
      color: var(--blue-hover);
      padding: 4px 14px;
      border-radius: 999px;
      font-size: 0.8rem;
      font-weight: 700;
      margin-bottom: 16px;
    }
    .article-header h1 {
      font-size: clamp(2rem, 4.5vw, 2.7rem);
      font-weight: 800;
      line-height: 1.25;
      letter-spacing: -0.8px;
      margin-bottom: 16px;
      color: var(--text);
    }
    .byline { color: var(--text-muted); font-size: 0.9rem; }
    .hero-img {
      border-radius: var(--radius-lg);
      overflow: hidden;
      margin-bottom: 40px;
      border: 1px solid var(--border);
    }
    .hero-img img { width: 100%; height: auto; }
    .prose {
      font-size: 1.1rem;
      line-height: 1.8;
      color: #334155;
    }
    .prose p { margin-bottom: 24px; }
    .prose h3 {
      font-size: 1.45rem;
      font-weight: 700;
      color: var(--text);
      margin: 36px 0 16px;
      letter-spacing: -0.4px;
    }
    .prose ul { margin: 0 0 24px 24px; }
    .prose li { margin-bottom: 12px; }
    .article-cta {
      background: var(--bg-sky);
      border: 1px solid #bae6fd;
      border-radius: var(--radius-md);
      padding: 30px;
      margin-top: 50px;
      text-align: center;
    }
    .article-cta h4 { font-size: 1.3rem; margin-bottom: 10px; color: var(--text); }
    .article-cta p { color: var(--text-muted); margin-bottom: 20px; font-size: 0.95rem; }
    .back-home { display: inline-block; margin-top: 30px; color: var(--blue-primary); font-weight: 600; }
"""

def generate_blog_pages(articles):
    os.makedirs("blog", exist_ok=True)
    for a in articles:
        article_schema = {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": a["title"],
            "image": [a["image"]],
            "datePublished": "2026-11-01",
            "author": { "@type": "Person", "name": a["author"] },
            "publisher": { "@type": "Organization", "name": "The Tee Drop", "url": BASE_URL },
            "description": a["excerpt"]
        }

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{a['title']} | The Tee Drop Journal</title>
  <meta name="description" content="{a['excerpt']}">
  <link rel="canonical" href="{BASE_URL}/blog/{a['slug']}.html">

  <meta property="og:type" content="article">
  <meta property="og:title" content="{a['title']}">
  <meta property="og:description" content="{a['excerpt']}">
  <meta property="og:url" content="{BASE_URL}/blog/{a['slug']}.html">
  <meta property="og:image" content="{a['image']}">

  <script type="application/ld+json">
  {json.dumps(article_schema, indent=2)}
  </script>

  <style>
  {SHARED_CSS}
  {BLOG_EXTRA_CSS}
  </style>
</head>
<body>

  <header>
    <a href="/" class="logo"><span class="logo-dot"></span> The Tee Drop</a>
    <a href="{MAYZING_DEFAULT}" class="btn-nav-cart" target="_blank" rel="noopener">Store Checkout 🛒</a>
  </header>

  <article class="article-container">
    <div class="article-header">
      <div class="article-badge">The Tee Drop Journal</div>
      <h1>{a['title']}</h1>
      <div class="byline">By {a['author']} • {a['date']} • {a['read_time']}</div>
    </div>

    <div class="hero-img">
      <img src="{a['image']}" alt="{a['title']}" width="800" height="450">
    </div>

    <div class="prose">
      {a['content']}
    </div>

    <div class="article-cta">
      <h4>Experience The Heavyweight Standard</h4>
      <p>Browse our current drop collection and see how 240+ GSM combed cotton feels in person.</p>
      <a href="/#drops" class="btn-nav-cart">View Current Drops ⚡</a>
    </div>

    <a href="/" class="back-home">← Return to home</a>
  </article>

</body>
</html>
"""
        with open(f"blog/{a['slug']}.html", "w", encoding="utf-8") as f:
            f.write(html)
    print(f"✅ Created: {len(articles)} Editorial Journal Articles in /blog/ directory")

def generate_sitemap(products, articles):
    today = datetime.now().strftime("%Y-%m-%d")
    urls_xml = f"""  <url>
    <loc>{BASE_URL}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
"""
    for p in products:
        urls_xml += f"""  <url>
    <loc>{BASE_URL}/products/{p['slug']}.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
"""
    for a in articles:
        urls_xml += f"""  <url>
    <loc>{BASE_URL}/blog/{a['slug']}.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
"""
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls_xml}</urlset>
"""
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap)
    print("✅ Created: sitemap.xml with Product & Blog URLs")

if __name__ == "__main__":
    products, articles = load_data()
    generate_index_html(products, articles)
    generate_product_pages(products)
    generate_blog_pages(articles)
    generate_sitemap(products, articles)
    print("🎉 Fresh human-designed storefront & journal built successfully!")
