# Flex.Work

Flex.Work is an independent flexible-work hub. It covers remote, hybrid, part-time, freelance and four-day-week roles, and offers free tools, guides, talent matching and employer listings.

It's a static site (HTML, CSS and vanilla JS) built for **GitHub Pages on the free plan**, served from `main` at the repository root.

## Structure

| Path | What it is |
|---|---|
| `index.html`, `*.html` | Generated pages (committed, served as-is) |
| `tools/` | 8 interactive tools |
| `guides/` | 14 long-form guides |
| `assets/css/site.css` | Design system |
| `assets/js/main.js` | Menu, consent, form relay, multi-step forms, videos, hero widget |
| `assets/js/tools.js` | All tool logic and the role explorer |
| `assets/js/roles.js` | Role explorer data |
| `_build/` | Python generator: layout, page content, guides, data |
| `ads.txt`, `robots.txt`, `sitemap.xml`, `CNAME`, `.nojekyll` | Hosting and SEO files |

## Edit and rebuild

```bash
python3 _build/build.py
```

Change content in `_build/*.py`, rebuild, then commit the generated HTML. The **Build site** GitHub Action also regenerates and commits the HTML automatically whenever `_build/` or `assets/` changes on `main`.

## Forms

Every form posts through FormSubmit. The destination address is assembled at runtime in `assets/js/main.js` and never appears in the markup.

**First-time activation:** the first form submission triggers a one-time activation email from FormSubmit to the inbox. Click the link in that email and every form starts delivering.

## AdSense

- The Auto ads script is in the `<head>` of every content page.
- `ads.txt` is at the root.
- Reserved ad zones (`.ad-zone[data-slot]`) stay hidden until you add slot IDs to `FW.adSlots` in `main.js`.
- For EEA, UK and Swiss visitors, turn on Google's certified consent message in AdSense under **Privacy & messaging**.

## Custom domain

1. Go to **Settings → Pages**.
2. Under **Source**, choose **Deploy from a branch**, then `main` and `/ (root)`.
3. Enter `flex.work` as the custom domain, then turn on **Enforce HTTPS**.

DNS at your registrar:

| Type | Name | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | webworksa1.github.io |

See `PROMPTS.md` for the idea, revenue model and phase-wise build prompt, and `RESEARCH.md` for the competitive research.

Flex.Work is not affiliated with FlexJobs, Flexwork or any similarly named company.
