"""Shared layout for Flex.Work static pages."""
import html, json

SITE = "https://flex.work"
ADSENSE = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>'
OWNER = "https://web.works/contact"

LOGO = ('<svg class="logo-mark" viewBox="0 0 32 32" aria-hidden="true">'
        '<rect x="2" y="6" width="17" height="20" rx="5" fill="#1B2A41"/>'
        '<rect x="11" y="6" width="17" height="20" rx="5" fill="#2F6B4F" opacity=".92"/>'
        '<circle cx="26" cy="7" r="4.5" fill="#E9B949"/></svg>')

NAV = [
    ("jobs.html", "Find roles", "jobs"),
    ("tools/index.html", "Tools", "tools"),
    ("guides/index.html", "Guides", "guides"),
    ("employers.html", "For employers", "employers"),
    ("videos.html", "Videos", "videos"),
    ("support.html", "Support", "support"),
]

def esc(s):
    return html.escape(s, quote=True)

def head(title, desc, path, root, noads=False, jsonld=None, noindex=False):
    canon = SITE + "/" + (path if path != "index.html" else "")
    if canon.endswith("/index.html"):
        canon = canon[:-10]
    ld = ""
    base_ld = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "Flex.Work",
        "url": SITE + "/",
        "potentialAction": {"@type": "SearchAction", "target": SITE + "/jobs.html?q={q}", "query-input": "required name=q"},
    }
    blocks = [base_ld] if path == "index.html" else []
    if jsonld:
        blocks += jsonld if isinstance(jsonld, list) else [jsonld]
    for b in blocks:
        ld += '<script type="application/ld+json">' + json.dumps(b, ensure_ascii=False, indent=1) + "</script>\n"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
{'<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'}
<meta property="og:type" content="website">
<meta property="og:site_name" content="Flex.Work">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1B2A41">
<meta name="google-adsense-account" content="ca-pub-6620975821265271">
<link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{root}site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,400..800&family=Hanken+Grotesk:ital,wght@0,400..700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/site.css">
{'' if noads else ADSENSE}
{ld}</head>
"""

def header(root, key):
    cur = ' aria-current="page"'
    links = "".join(
        f'<a href="{root}{h}"{cur if k == key else ""}>{t}</a>' for h, t, k in NAV
    )
    return f"""<body>
<a class="skip" href="#main">Skip to content</a>
<div class="ownerbar"><a href="{OWNER}" target="_blank" rel="noopener">Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership</a></div>
<header class="site-head">
 <div class="wrap">
  <a class="logo" href="{root}index.html" aria-label="Flex.Work home">{LOGO}<span>Flex<b>.</b>Work</span></a>
  <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav class="nav" id="nav" aria-label="Main">{links}<a class="btn sm" href="{root}talent.html">Join the talent network</a></nav>
 </div>
</header>
<main id="main">
"""

def footer(root, scripts=""):
    return f"""</main>
<footer class="site-foot">
 <div class="wrap">
  <div class="foot-grid">
   <div>
    <a class="logo" href="{root}index.html" style="color:#fff">{LOGO}<span>Flex<b style="color:#E9B949">.</b>Work</span></a>
    <p class="mt4">An independent guide to flexible work — remote, hybrid, part-time, freelance and four-day roles — with free tools for people and teams.</p>
    <form class="foot-news" data-form="Newsletter signup" aria-label="Newsletter">
     <div class="hp"><label>Leave empty<input name="_hp" tabindex="-1" autocomplete="off"></label></div>
     <label class="hp" for="nl-email">Email</label>
     <input id="nl-email" name="email" type="email" required placeholder="Your email" autocomplete="email">
     <button class="btn mari sm" type="submit">Subscribe</button>
    </form>
    <p class="form-status small" aria-live="polite"></p>
   </div>
   <div><h4>Find work</h4><ul>
    <li><a href="{root}jobs.html">Flexible role explorer</a></li>
    <li><a href="{root}talent.html">Join the talent network</a></li>
    <li><a href="{root}guides/remote-job-scams.html">Avoid job scams</a></li>
    <li><a href="{root}guides/how-to-ask-for-flexible-work.html">Ask for flexibility</a></li>
    <li><a href="{root}glossary.html">Flex work glossary</a></li>
   </ul></div>
   <div><h4>Employers</h4><ul>
    <li><a href="{root}employers.html">Hire flexible talent</a></li>
    <li><a href="{root}employers.html#post">Post a flexible role</a></li>
    <li><a href="{root}tools/flex-policy-builder.html">Policy builder</a></li>
    <li><a href="{root}guides/managing-flexible-teams.html">Managing flexible teams</a></li>
    <li><a href="{root}advertise.html">Advertise and sponsor</a></li>
   </ul></div>
   <div><h4>Flex.Work</h4><ul>
    <li><a href="{root}about.html">About and editorial policy</a></li>
    <li><a href="{root}support.html">Support the site</a></li>
    <li><a href="{root}contests.html">Contests and prizes</a></li>
    <li><a href="{root}careers.html">Work with us</a></li>
    <li><a href="{root}resources.html">Research and resources</a></li>
    <li><a href="{root}contact.html">Contact</a></li>
   </ul></div>
   <div><h4>Legal</h4><ul>
    <li><a href="{root}privacy.html">Privacy and cookies</a></li>
    <li><a href="{root}terms.html">Terms of use</a></li>
    <li><a href="{root}disclaimer.html">Disclaimer</a></li>
    <li><a href="{root}trademark.html">Trademark and copyright</a></li>
    <li><a href="{root}sitemap.html">Sitemap</a></li>
   </ul></div>
  </div>
  <div class="foot-legal">
   <p>&copy; <span data-year>2026</span> Flex.Work. Original content and tools. Flex.Work is an independent publication and is not affiliated with, endorsed by or connected to FlexJobs, Flexwork or any company using a similar name. Read the <a href="{root}trademark.html">trademark and copyright disclosure</a>.</p>
   <p><a href="{OWNER}" target="_blank" rel="noopener">Website, domain, sponsorship or partnership inquiries</a></p>
  </div>
 </div>
</footer>
<div class="consent" id="consent" role="dialog" aria-live="polite" aria-label="Cookie notice">
 <p>We use cookies for essential site functions and, with Google AdSense, to show and measure ads. Visitors in the EEA, UK and Switzerland see Google&rsquo;s consent choices. <a href="{root}privacy.html#cookies">How we use cookies</a>.</p>
 <div class="row"><button class="btn sm" data-consent="all">Accept</button><button class="btn ghost sm" data-consent="essential">Essential only</button></div>
</div>
<script src="{root}assets/js/main.js" defer></script>
{scripts}
</body>
</html>
"""

def ad(slot="display"):
    """Reserved ad zone. Empty (hidden) until a slot ID is set in main.js; Auto ads fill the page meanwhile."""
    return f'<div class="ad-zone" data-slot="{slot}"></div>'

def page(path, title, desc, body, key="", noads=False, jsonld=None, scripts="", noindex=False, root=None):
    depth = path.count("/")
    root = ("../" * depth) if root is None else root
    return head(title, desc, path, root, noads, jsonld, noindex) + header(root, key) + body.replace("{root}", root) + footer(root, scripts.replace("{root}", root))

def hp():
    return '<div class="hp"><label>Leave empty<input name="_hp" tabindex="-1" autocomplete="off"></label></div>'
