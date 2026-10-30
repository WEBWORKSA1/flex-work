"""Build Flex.Work into static HTML at the repo root.  Run:  python3 _build/build.py"""
import os, re, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from layout import page, ad, SITE
from guides_a import GUIDES_A
from guides_b import GUIDES_B
import pages_core as C
import pages_home as H
import pages_tools as T

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TODAY = datetime.date.today().isoformat()
GUIDES = GUIDES_A + GUIDES_B
written = []

def wrap_lines(html):
    """Keep source lines short: break between adjacent block-level tags."""
    return re.sub(r"(</(?:div|li|tr|article|fieldset|label|section|details|ul|ol|a|option)>)(?=<)", "\\1\n", html)

def write(path, html, prio="0.6", index=True):
    if path.endswith(".html"):
        html = wrap_lines(html)
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    if index:
        written.append((path, prio))

TOOLS_JS = '<script src="{root}assets/js/tools.js" defer></script>'

# ---- home
write("index.html", page("index.html", "Flex.Work — find, negotiate and thrive in flexible work",
      "Remote, hybrid, part-time, freelance and four-day roles, plus free tools to find them, negotiate them and make them work. Free talent matching for job seekers.",
      H.home(GUIDES), key="", jsonld=[H.faq_ld(), {"@context": "https://schema.org", "@type": "Organization", "name": "Flex.Work", "url": SITE + "/", "logo": SITE + "/assets/img/favicon.svg"}]), "1.0")

# ---- core
core = [
    ("jobs.html", "Explore flexible-friendly roles — remote, hybrid, part-time | Flex.Work", "Filter 50+ careers by remote, hybrid, part-time, freelance and four-day arrangements, and set up free flexible job alerts.", C.jobs, "jobs", '<script src="{root}assets/js/roles.js" defer></script>' + TOOLS_JS, "0.9"),
    ("talent.html", "Join the Flex.Work talent network — free flexible job matching", "Create a free profile and get matched with employers who state their remote, hybrid, part-time or four-day flexibility upfront.", C.talent, "", "", "0.9"),
    ("employers.html", "Hire flexible talent — post remote, hybrid and part-time roles | Flex.Work", "Post flexible roles to candidates who have already chosen that arrangement. Free launch listings, featured roles and hiring partnerships.", C.employers, "employers", "", "0.9"),
    ("support.html", "Support Flex.Work — keep flexible work tools free", "Support independent flexible-work guidance. Contributions fund operations, promotion, fairly paid contributors and contest prizes.", C.support, "support", "", "0.6"),
    ("contests.html", "Contests and prizes | Flex.Work", "Enter free Flex.Work contests — best home office setup, flexible work stories and async tips — and win prizes.", C.contests, "", "", "0.6"),
    ("careers.html", "Work with Flex.Work — remote freelance and part-time roles", "Flex.Work hires remote freelance writers, researchers, developers and community leads. Apply to work flexibly with us.", C.careers, "", "", "0.5"),
    ("advertise.html", "Advertise, sponsor and partner with Flex.Work", "Newsletter, tool and contest sponsorships reaching job seekers, freelancers, managers and HR leaders interested in flexible work.", C.advertise, "", "", "0.6"),
    ("videos.html", "Flexible work video library — remote, hybrid, four-day week | Flex.Work", "Watch talks and explainers on remote work, hybrid teams, four-day weeks and freelancing from researchers and practitioners.", C.videos, "videos", "", "0.7"),
    ("resources.html", "Flexible work statistics and research sources | Flex.Work", "Current statistics on remote, hybrid and four-day-week work with links to every original source — Gallup, BLS, ONS, Pew, Owl Labs and more.", C.resources, "", "", "0.8"),
    ("about.html", "About Flex.Work and our editorial policy", "Flex.Work is an independent guide to flexible work. Learn how we research, how we make money and how we stay independent.", C.about, "", "", "0.5"),
    ("contact.html", "Contact Flex.Work", "Contact Flex.Work with questions, corrections, ideas, press, listings, advertising or partnership inquiries.", C.contact, "", "", "0.5"),
    ("privacy.html", "Privacy and cookie policy | Flex.Work", "How Flex.Work collects, uses and protects information, including cookies and Google AdSense advertising.", C.privacy, "", "", "0.3"),
    ("terms.html", "Terms of use | Flex.Work", "The terms for using Flex.Work, its tools, listings and services.", C.terms, "", "", "0.3"),
    ("disclaimer.html", "Disclaimer | Flex.Work", "Important limits on the information, tools and listings on Flex.Work.", C.disclaimer, "", "", "0.3"),
    ("trademark.html", "Trademark and copyright disclosure | Flex.Work", "Flex.Work is independent and not affiliated with FlexJobs, Flexwork or similarly named companies. Read our trademark and copyright disclosure.", C.trademark, "", "", "0.3"),
]
for path, title, desc, fn, key, scripts, prio in core:
    write(path, page(path, title, desc, fn(), key=key, scripts=scripts), prio)

gbody, gld = C.glossary()
write("glossary.html", page("glossary.html", "Flexible work glossary — terms explained | Flex.Work", "Plain-English definitions of flexible work terms: 9/80, anchor days, async-first, compressed hours, core hours, job-sharing and more.", gbody, jsonld=gld), "0.6")
write("thank-you.html", page("thank-you.html", "Thank you | Flex.Work", "Your submission was received.", C.thanks(), noads=True, noindex=True), index=False)
write("404.html", page("404.html", "Page not found | Flex.Work", "The page you're looking for doesn't exist.", C.notfound(), noads=True, noindex=True, root="/"), index=False)

# ---- tools
for path, title, desc, fn in T.TOOL_PAGES:
    ld = None if path.endswith("index.html") else {"@context": "https://schema.org", "@type": "WebApplication", "name": title.split(" | ")[0].split(" — ")[0], "applicationCategory": "BusinessApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "url": SITE + "/" + path}
    write(path, page(path, title, desc, fn(), key="tools", scripts=TOOLS_JS, jsonld=ld), "0.8")

# ---- guides
def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")

def guide_page(g):
    body = g["body"]
    toc = []
    def add_id(m):
        attrs, text = m.group(1), m.group(2)
        if 'id="' in attrs:
            gid = re.search(r'id="([^"]+)"', attrs).group(1)
        else:
            gid = slugify(re.sub("<[^>]+>", "", text))
            attrs = attrs + f' id="{gid}"'
        toc.append((gid, re.sub("<[^>]+>", "", text)))
        return f"<h2{attrs}>{text}</h2>"
    body = re.sub(r"<h2([^>]*)>(.*?)</h2>", add_id, body)
    # insert one in-article ad zone after the 3rd h2
    parts = body.split("<h2")
    if len(parts) > 4:
        body = "<h2".join(parts[:3]) + "</div>" + ad("inArticle") + '<div class="prose" style="margin-top:0">' + "<h2" + "<h2".join(parts[3:])
    toc_html = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
    related = [x for x in GUIDES if x["slug"] != g["slug"] and x["aud"] == g["aud"]][:3]
    rel = "".join(f'<li><a href="{x["slug"]}.html">{x["title"]}</a></li>' for x in related)
    html = f'''<div class="wrap page-head" style="padding-bottom:24px"><div class="crumbs"><a href="{{root}}index.html">Home</a> / <a href="{{root}}guides/index.html">Guides</a> / {g["aud"]}</div><h1 style="max-width:24ch">{g["title"]}</h1><p class="lede">{g["desc"]}</p><p class="byline">By the Flex.Work editorial team &middot; Updated October 2026 &middot; {g["mins"]} min read</p></div>
<div class="wrap article"><article><div class="prose">{body}</div>
<div class="panel flat soft mt6"><h3>Keep going</h3><ul class="mb0">{rel}</ul></div></article>
<aside><div class="toc"><div class="panel flat"><h3>In this guide</h3><ol>{toc_html}</ol></div>
<div class="panel flat aside-cta" style="background:var(--ink);color:#E9EEF3;border-color:var(--ink)"><h3 style="color:#fff">Get matched with flexible roles</h3><p class="small">Free for job seekers. Choose the flexibility you want.</p><a class="btn mari sm" href="{{root}}talent.html">Join the talent network</a></div>
<div class="panel flat aside-cta"><h3>Hiring flexibly?</h3><p class="small">Post a remote, hybrid or part-time role free during launch.</p><a class="btn ink sm" href="{{root}}employers.html#post">Post a role</a></div></div></aside></div>'''
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"],
          "author": {"@type": "Organization", "name": "Flex.Work editorial team"}, "publisher": {"@type": "Organization", "name": "Flex.Work"},
          "datePublished": "2026-10-30", "dateModified": TODAY, "mainEntityOfPage": f"{SITE}/guides/{g['slug']}.html"}
    return html, ld

for g in GUIDES:
    html, ld = guide_page(g)
    write(f"guides/{g['slug']}.html", page(f"guides/{g['slug']}.html", g["title"] + " | Flex.Work", g["desc"], html, key="guides", jsonld=ld), "0.8")

def grow(g):
    tag = "tag" if g["aud"] == "Workers" else "tag ink"
    return f'<a class="row-link" href="{g["slug"]}.html"><div><span class="{tag}">{g["aud"]}</span><h3 class="mt4">{g["title"]}</h3><p>{g["desc"]}</p></div><span class="meta">{g["mins"]} min read</span></a>'
workers = "".join(grow(g) for g in GUIDES if g["aud"] == "Workers")
emps = "".join(grow(g) for g in GUIDES if g["aud"] == "Employers")
gi = f'''<div class="wrap page-head"><div class="crumbs"><a href="{{root}}index.html">Home</a> / Guides</div><h1>Flexible work guides</h1><p class="lede">Practical, sourced guides for people seeking flexibility and for the teams offering it.</p></div>
<section class="section" style="padding-top:0"><div class="wrap"><h2>For workers and freelancers</h2><div class="rows">{workers}</div></div></section>{ad("inFeed")}
<section class="section white"><div class="wrap"><h2>For managers and employers</h2><div class="rows">{emps}</div></div></section>
<section class="section"><div class="wrap"><p>Looking for a term? Try the <a href="{{root}}glossary.html">flexible work glossary</a>. Want the data? See <a href="{{root}}resources.html">research and resources</a>.</p></div></section>'''
write("guides/index.html", page("guides/index.html", "Flexible work guides for workers and employers | Flex.Work", "Guides to asking for flexible work, remote job searching, avoiding scams, hybrid schedules, four-day weeks, freelancing and managing flexible teams.", gi, key="guides"), "0.9")

# ---- sitemap.html
def title_of(p):
    with open(os.path.join(OUT, p), encoding="utf-8") as f:
        m = re.search(r"<title>(.*?)</title>", f.read())
    return m.group(1).split(" | ")[0] if m else p
groups = {"Main": [], "Tools": [], "Guides": [], "Company and legal": []}
for p, _ in written:
    if p.startswith("tools/"): groups["Tools"].append(p)
    elif p.startswith("guides/"): groups["Guides"].append(p)
    elif p in ("about.html", "contact.html", "privacy.html", "terms.html", "disclaimer.html", "trademark.html", "careers.html", "advertise.html"): groups["Company and legal"].append(p)
    else: groups["Main"].append(p)
sm = '<div class="wrap page-head"><div class="crumbs"><a href="{root}index.html">Home</a> / Sitemap</div><h1>Sitemap</h1><p class="lede">Every page on Flex.Work.</p></div><section class="section" style="padding-top:0"><div class="wrap grid-4">'
for k, v in groups.items():
    sm += f"<div><h2 style='font-size:1.3rem'>{k}</h2><ul>" + "".join(f'<li><a href="{{root}}{p}">{title_of(p)}</a></li>' for p in v) + "</ul></div>"
sm += "</div></section>"
write("sitemap.html", page("sitemap.html", "Sitemap | Flex.Work", "All pages on Flex.Work: tools, guides, role explorer, employer and company pages.", sm), "0.3")

# ---- sitemap.xml / robots / ads.txt / CNAME / manifest / .nojekyll
urls = []
for p, prio in written:
    loc = SITE + "/" + ("" if p == "index.html" else p)
    if loc.endswith("/index.html"): loc = loc[:-10]
    urls.append(f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><priority>{prio}</priority></url>")
open(os.path.join(OUT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /_build/\nDisallow: /thank-you.html\n\nSitemap: {SITE}/sitemap.xml\n")
open(os.path.join(OUT, "ads.txt"), "w").write("google.com, pub-6620975821265271, DIRECT, f08c47fec0942fa0\n")
open(os.path.join(OUT, "CNAME"), "w").write("flex.work\n")
open(os.path.join(OUT, ".nojekyll"), "w").write("")
open(os.path.join(OUT, "site.webmanifest"), "w").write('{"name":"Flex.Work","short_name":"Flex.Work","start_url":"/","display":"standalone","background_color":"#F6F7F2","theme_color":"#1B2A41","icons":[{"src":"/assets/img/favicon.svg","sizes":"any","type":"image/svg+xml"}]}\n')
print(f"Built {len(written)} indexed pages")
