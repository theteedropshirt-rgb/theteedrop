#!/usr/bin/env python3
"""
The Tee Drop - Fast Product Adder for Astro
Usage:
  python add_product.py
"""

import sys
import os
import json
import re
import argparse
import subprocess

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def main():
    parser = argparse.ArgumentParser(description="Add a new t-shirt drop to The Tee Drop (Astro)")
    parser.add_argument("--title", help="Product Title")
    parser.add_argument("--price", type=float, help="Selling Price (e.g. 26.99)")
    parser.add_argument("--compare", type=float, default=38.00, help="Compare at price (e.g. 38.00)")
    parser.add_argument("--category-slug", default="vintage-streetwear", help="Category slug")
    parser.add_argument("--badge", default="New Drop", help="Badge text")
    parser.add_argument("--image", help="Image URL or local path")
    parser.add_argument("--checkout", default="https://ecotwins.store", help="Mayzing product checkout URL")
    
    args = parser.parse_args()

    title = args.title or input("👕 Product Title (e.g. 'Vintage Heavyweight Gym Tee'): ").strip()
    if not title:
        print("❌ Error: Title is required!")
        return

    price_str = args.price or input("💰 Selling Price (e.g. 27.99): ").strip()
    price = float(price_str)
    compare_price = args.compare

    # Load categories for selection
    categories_path = os.path.join("src", "data", "categories.json")
    with open(categories_path, "r", encoding="utf-8") as f:
        categories = json.load(f)

    print("\nAvailable Categories:")
    for i, cat in enumerate(categories, 1):
        print(f"  [{i}] {cat['name']} ({cat['slug']})")
    
    choice = input("\nSelect category number [1-10] or press Enter for default (1): ").strip()
    if choice and choice.isdigit() and 1 <= int(choice) <= len(categories):
        selected_cat = categories[int(choice) - 1]
    else:
        selected_cat = categories[0]

    category_name = selected_cat["name"]
    category_slug = selected_cat["slug"]

    badge = args.badge or input("🔥 Badge [New Drop / Best Seller / Viral Drop]: ").strip()
    if not badge:
        badge = "New Drop"

    image = args.image or input("🖼️ Image URL (Mockup link): ").strip()
    if not image:
        image = "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=900&auto=format&fit=crop&q=80"

    checkout = args.checkout or input("🛒 Mayzing Checkout Link [press Enter for default store]: ").strip()
    if not checkout:
        checkout = "https://store.theteedrop.com/store/MNye"

    slug = slugify(title)
    desc = f"Heavyweight 240+ GSM graphic tee: {title}. Printed on 100% combed ringspun cotton with soft, non-toxic water-based inks. Tailored with an intentional relaxed streetwear drape for everyday wear."

    new_product = {
        "id": f"drop-{slug[:8]}",
        "slug": slug,
        "title": title,
        "price": price,
        "compare_at_price": compare_price,
        "category": category_name,
        "category_slug": category_slug,
        "badge": badge,
        "rating": 4.9,
        "reviews_count": 52,
        "image": image,
        "description": desc,
        "features": [
            "240+ GSM heavyweight 100% combed ringspun cotton",
            "Drop-shoulder boxy streetwear silhouette",
            "Eco-friendly water-based fade-proof DTG print",
            "Printed on demand & shipped locally across US and Europe"
        ],
        "mayzing_checkout_url": checkout
    }

    # Save to src/data/products.json
    products_path = os.path.join("src", "data", "products.json")
    with open(products_path, "r", encoding="utf-8") as f:
        products = json.load(f)

    products.insert(0, new_product)

    with open(products_path, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2)

    print(f"\n🎉 Successfully added '{title}' to {products_path}!")
    print("⚡ Triggering Astro static build...")

    npm_cmd = "npm.cmd" if sys.platform == "win32" else "npm"
    subprocess.run([npm_cmd, "run", "build"], check=True)

    print("\n🚀 All done! Your new product and sitemap are compiled and ready in /dist!")

if __name__ == "__main__":
    main()
