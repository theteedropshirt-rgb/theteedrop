# ⚡ The Tee Drop (theteedrop.com) — Powered by Astro 🚀

Architecture inspired by the organic search dominance of **TeeShirtPalace**, built with the **Astro** framework, **Clean White & Sky Blue** human aesthetic, and integrated directly with **Mayzing Print-on-Demand Checkout**.

---

## 🏗️ Architecture & Strategy (The TeeShirtPalace Blueprint)

1. **Category Silo Hubs (`/collections/[category]`)**:
   - Rather than cramming all shirts on one page, products are organized into targeted long-tail topic hubs:
     - `/collections/gym-pump-covers`
     - `/collections/nurses-healthcare`
     - `/collections/vintage-streetwear`
     - `/collections/coffee-obsessed`
     - `/collections/anime-cyberpunk`
     - `/collections/teachers-educators`
     - `/collections/dog-cat-lovers`
     - `/collections/coders-tech`
     - `/collections/outdoor-hiking`
     - `/collections/milestone-birthdays`
2. **The Journal (`/blog/[slug]`)**:
   - Rich human editorial articles giving the site genuine E-E-A-T and internal linking authority.
3. **Dedicated Size & Fit Guide (`/size-guide`)**:
   - Complete measurement charts in inches and cm for customer trust.
4. **Programmatic Indexation (`/sitemap.xml`)**:
   - Dynamically generated XML sitemap indexing all home, category, product, and blog URLs for Google.
5. **Mayzing Checkout Bridge (`store.theteedrop.com`)**:
   - Every product has a direct CTA that opens Mayzing's checkout for instant purchase, automatic DTG printing, and fulfillment.

---

## 🛠️ Commands

### 1. Run Local Development Server
```bash
npm.cmd run dev
```
Open [http://localhost:4321](http://localhost:4321) to preview your site.

### 2. Build for Production (Cloudflare Pages)
```bash
npm.cmd run build
```
Outputs the static production site directly to `dist/`.

### 3. Add a New Product Drop in 10 Seconds
```bash
python add_product.py
```
Prompts for Title, Price, Category, Mockup Image URL, and Mayzing Checkout URL, updates `src/data/products.json`, and automatically compiles the Astro site!

---

## 🚀 Deploy to Cloudflare Pages (Free in 60 Seconds)

1. Push this repository to GitHub:
   ```bash
   git init
   git add .
   git commit -m "feat: complete Astro storefront inspired by TeeShirtPalace"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/theteedrop.git
   git push -u origin main
   ```
2. Go to **Cloudflare Dashboard** -> **Workers & Pages** -> **Create application** -> **Pages**.
3. Select **Connect to Git** and pick `theteedrop`.
4. Build settings:
   - Framework preset: **Astro**
   - Build command: `npm run build`
   - Build output directory: `dist`
5. Click **Save and Deploy**. Your site is now live globally on Cloudflare!
