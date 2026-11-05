import re

with open('src/layouts/BaseLayout.astro', 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'/\*\s*Main Professional Header\s*\*/\s*header\s*\{', '/* Main Professional Header */\n    header.site-header {', text)
text = re.sub(r'<\s*header\s*>', '<header class="site-header">', text)

with open('src/layouts/BaseLayout.astro', 'w', encoding='utf-8') as f:
    f.write(text)

# Also let's update collections/[category].astro to use a div instead of header tag
with open('src/pages/collections/[category].astro', 'r', encoding='utf-8') as f:
    cat_text = f.read()

cat_text = cat_text.replace('<header class="cat-header">', '<div class="cat-header">')
cat_text = cat_text.replace('</header>', '</div>')

with open('src/pages/collections/[category].astro', 'w', encoding='utf-8') as f:
    f.write(cat_text)

# Also collections/index.astro
with open('src/pages/collections/index.astro', 'r', encoding='utf-8') as f:
    col_text = f.read()

col_text = col_text.replace('<header class="collections-header">', '<div class="collections-header">')
col_text = col_text.replace('</header>', '</div>')

with open('src/pages/collections/index.astro', 'w', encoding='utf-8') as f:
    f.write(col_text)

print('Headers fixed cleanly!')
