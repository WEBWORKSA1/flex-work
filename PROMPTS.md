# Flex.Work — idea, revenue model and phase-wise build prompt

## 1. The idea

**Flex.Work = the flexible-work hub.** It's a guide, toolkit and matching service for every kind of flexible work: remote, hybrid, flexitime, compressed hours, four-day weeks, part-time, job-sharing, and freelance or fractional work. It serves two audiences on one domain:

- **Workers** find flexible-friendly roles, negotiate flexibility and avoid scams.
- **Employers** post flexible roles, design policies and plan hybrid teams.

### Why this idea wins on this domain

| Factor | Reasoning |
|---|---|
| Exact-match meaning | "Flex work" is the everyday phrase for this whole category, and the `.work` TLD reads as the category itself. |
| Search demand | People search all year for remote jobs, hybrid policy, four-day week, freelance rates, work-from-home scams and flexible working requests. Many of these are tool queries (calculators, generators, letters), which bring repeat visits and backlinks. |
| AdSense value | Careers, HR software, payroll/EOR, freelancing, insurance and education are among the higher-CPC ad verticals. |
| Lead value | Job-seeker profiles (talent network), employer job posts and HR-software intent are all leads that can be sold or monetized. |
| Gap in the market | No competitor covers *all* arrangement types in one filter. 4dayweek.io only covers four-day-week variants, and the Flex Index consumer site has wound down. A Flex Employer Index is an open position. |
| Trademark safety | Original brand "Flex.Work" (with the dot). It's not "FlexJobs" or "Flexwork". A disclosure page and footer notice are included. |

### Revenue streams (built in)

1. **Google AdSense.** Auto ads, plus reserved, labelled zones that can take manual units later.
2. **Employer job listings:** free launch listing, $149 Featured, custom Hiring Partner.
3. **Talent network leads:** matched introductions to employers, and later recruiter or partner referrals.
4. **Sponsorships:** newsletter, "presented by" tool placements, contest prizes, labelled sponsored guides.
5. **Reader support:** one-off, monthly or yearly pledges. A secure payment link is sent by email, so no card data touches the site.
6. **Future:** affiliate links (HR/payroll software, résumé tools, home-office gear), a paid Flex Employer Index profile, and a newsletter with paid tiers.

### Back-of-envelope revenue model (assumptions — validate with real data)

| Monthly traffic | AdSense (RPM $6–15, careers/HR, Tier-1 heavy) | Featured posts (5–20 × $149) | Sponsorship | Total range |
|---|---|---|---|---|
| 20k pageviews | $120–300 | $745–1,490 | $0–300 | ~$0.9k–2.1k |
| 100k pageviews | $600–1,500 | $1,490–2,980 | $500–2,000 | ~$2.6k–6.5k |
| 300k pageviews | $1.8k–4.5k | $2,980+ | $2k–6k | ~$6.8k–13.5k |

Ads alone won't make this site pay. Employer listings and sponsorship are where the money is. That's why the employer funnel and the talent network sit in the main navigation.

---

## 2. Phase-wise build prompt

Use these prompts in order. Each phase is self-contained and can be handed to a builder (human or AI).

### Phase 0 — Strategy and constraints
> Build **Flex.Work**, an independent flexible-work hub for workers and employers, as a static website (HTML, CSS, vanilla JS) hosted free on GitHub Pages from the `main` branch with custom domain `flex.work`.
>
> Hard constraints:
> - Every page shows a top bar: "Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership", linked to `https://web.works/contact`.
> - Every form posts to one inbox through a relay. The address is assembled in JavaScript at runtime and never appears in HTML, text or visible source strings.
> - AdSense publisher `ca-pub-6620975821265271`: the script goes in `<head>` of every content page; add `ads.txt`.
> - Avoid "FlexJobs"/"Flexwork" trademarks. Include a trademark and copyright disclosure.
> - Fully responsive, accessible (WCAG AA contrast, keyboard focus, reduced motion) and fast (no frameworks).

### Phase 1 — Design system
> Create a distinct visual identity rooted in "the working week".
> - **Palette:** ink `#1B2A41`, paper `#F6F7F2`, fern `#2F6B4F`, marigold `#E9B949`, sky `#DCE8F0`, line `#D8DCD3`.
> - **Colour meaning everywhere:** office = ink, home = fern, off = marigold.
> - **Type:** Bricolage Grotesque (display, condensed to about 88% width) and Hanken Grotesk (body), both from Google Fonts under the OFL.
> - **Components:** buttons (fern, ink, marigold, ghost), panels, list rows (avoid identical card grids), chips, multi-step forms with a progress bar, pricing tiers, result panels, click-to-load video cards, FAQ accordions, a consent notice, and labelled ad zones.

### Phase 2 — Global layout
> Shared header with sticky nav (Find roles, Tools, Guides, For employers, Videos, Support, and a "Join the talent network" CTA), a mobile menu, the owner bar, and a five-column footer. The footer holds a newsletter form, link columns and an independence/trademark line. Add JSON-LD (WebSite, Organization, FAQPage, Article, WebApplication, DefinedTermSet), canonical URLs, Open Graph tags and the social image. Generate pages from one Python build script so the header and footer stay consistent across 40+ pages.

### Phase 3 — Home page
> - **Hero:** headline, a search that routes to the role explorer, and an interactive **"Design your week" widget**. Tapping days cycles Office, Home and Off, with a live readout of hours and money saved per year.
> - Then: an eight-arrangement spectrum; a cited stats band (Gallup, Flex Index, BLS, Owl Labs, Pew, Upwork, 4-day-week pilots); the talent-network lead band with an inline form; a tools grid; the employer funnel; latest guides; three videos; support/contest/careers panels; FAQ.

### Phase 4 — Lead generation (highest priority)
> 1. **Talent network** (`talent.html`): a three-step form covering arrangement chips, field, role and max office days; then experience, country, skills, hours, availability and pay; then name, email, URL and consent.
> 2. **Quick match form** on the home page (one step).
> 3. **Job alerts** on the role explorer.
> 4. **Employer role posting**: a three-step form covering company, role (arrangement, office days, location eligibility, pay, timeline) and contact plus plan. Sits next to pricing tiers.
> 5. **Flex Employer Index submission** (lead magnet for employers).
> 6. **Newsletter** in every footer.
>
> All forms: honeypot, validation, AJAX relay, redirect to `thank-you.html?f=<form>`, and a hidden mailto fallback on error.

### Phase 5 — Tools (traffic and backlinks)
> Build eight client-side tools, each on its own page with explanation content and a CTA:
> 1. Flex readiness quiz (12 questions, 5 dimensions)
> 2. Commute savings calculator (time, money, CO₂)
> 3. Flexible work request letter generator (copy, download, print)
> 4. Freelance rate calculator
> 5. Four-day week calculator (100-80-100, compressed, 9/80, pro-rata)
> 6. Hybrid schedule planner (team grid, anchor day)
> 7. Time-zone overlap finder (4 locations, 24-hour grid)
> 8. Flex policy builder (12-section policy, copy and download)

### Phase 6 — Content (AdSense approval depends on this)
> Write 14+ original guides of 700–1,200 words. Each gets a table of contents, an in-article ad zone after the third section, related links and sidebar CTAs.
> - **Workers:** what flexible work is, how to ask, remote job scams, job-search strategy, interview tips, home office setup, part-time and job-share, freelancing, digital nomad basics.
> - **Employers:** hybrid schedules compared, four-day week, managing flexible teams, writing a policy, async communication.
>
> Also build: a 50+ role explorer (editorial ratings, not fake job postings), a glossary, a research page listing every stat with its source, and a video library of verified YouTube embeds (privacy-enhanced, click-to-load).

### Phase 7 — Monetization pages
> - **support.html:** four funding purposes (operations, promotion and marketing, hiring talent, contests and prizes), three tiers, and a pledge form. A payment link is emailed; no card data on site.
> - **contests.html:** three contests, prizes, an official-rules summary (no purchase necessary, 18+, void where prohibited) and an entry form.
> - **careers.html:** five flexible contributor roles and an application form.
> - **advertise.html:** newsletter, tool and contest sponsorships, an inquiry form, and a domain/acquisition panel linking to `web.works/contact`.

### Phase 8 — AdSense compliance and legal
> - Pages: About (with editorial policy), Contact, Privacy and cookies (Google advertising-cookie wording plus opt-out links), Terms, Disclaimer, Trademark and copyright.
> - Cookie notice; sitemap.html and sitemap.xml; robots.txt; ads.txt; 404.
> - No ads on the thank-you or 404 pages. Ad zones are labelled "Advertisement" and placed away from buttons. No fake listings, no paywalls, no countdown timers.

### Phase 9 — QA
> - Check every internal link.
> - Zero console errors across all pages.
> - No horizontal scroll at 390px.
> - Test form submissions with the relay mocked.
> - Grep the repo to confirm the inbox address appears nowhere in plain text.
> - Check every tool against hand-worked examples.
> - Take screenshots on desktop and mobile.

### Phase 10 — Deploy
> Push to `WEBWORKSA1/flex-work` on `main`, then enable Pages (Settings → Pages → Deploy from branch → `main` / root). Add custom domain `flex.work` and turn on Enforce HTTPS. Set these DNS records at the registrar:
> - Apex A records: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
> - AAAA records (optional)
> - `www` CNAME → `webworksa1.github.io`
>
> Then submit the sitemap in Search Console and apply for AdSense.

### Phase 11 — Growth roadmap (expansion)
> 1. Fill the Flex Employer Index from submissions and turn it into a searchable directory.
> 2. Publish live employer listings in the role explorer (a JSON feed in the repo).
> 3. Programmatic pages: "remote [role] jobs", "[country] flexible work rights", "[city] coworking".
> 4. Annual "State of Flex" survey of talent-network members (an original-data backlink magnet).
> 5. More tools: an office-vs-home cost calculator, a résumé remote-readiness checker, a salary-by-arrangement explorer.
> 6. A newsletter with sponsor slots; an affiliate layer for HR/payroll, résumé and home-office products.
> 7. Localise to the UK, Canada, India and Australia (high flexible-work search volume).
