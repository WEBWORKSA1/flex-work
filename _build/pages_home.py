from layout import ad, hp
from data import STATS, VIDEOS, video_card, stat_block

ARR = [
    ("Remote", "Work from anywhere approved, with no regular office days.", "guides/what-is-flexible-work.html#remote"),
    ("Hybrid", "A mix of office and home days, often with set anchor days.", "guides/hybrid-schedules-compared.html"),
    ("Flexitime", "Core hours fixed; start and finish times are yours.", "guides/what-is-flexible-work.html#flexitime"),
    ("Compressed hours", "Full-time hours in fewer, longer days — like a 9/80.", "guides/four-day-week-guide.html"),
    ("Four-day week", "Often 100% pay for 80% of the time and 100% output.", "guides/four-day-week-guide.html"),
    ("Part-time", "Fewer contracted hours, chosen to fit life outside work.", "guides/part-time-and-job-sharing.html"),
    ("Job-sharing", "Two people split one full-time role and its pay.", "guides/part-time-and-job-sharing.html"),
    ("Freelance and fractional", "You sell projects or days to several clients.", "guides/freelancing-starter-guide.html"),
]

TOOLS = [
    ("flex-readiness-quiz.html", "Flex readiness quiz", "Twelve questions that show which arrangement suits how you work.", "quiz"),
    ("commute-savings-calculator.html", "Commute savings calculator", "Hours, money and CO₂ you get back from each home day.", "car"),
    ("flexible-work-request-letter.html", "Flexible work request letter", "Draft a persuasive, trial-based request to your manager.", "doc"),
    ("freelance-rate-calculator.html", "Freelance rate calculator", "Work back from the income you need to an hourly and day rate.", "coin"),
    ("four-day-week-calculator.html", "Four-day week calculator", "Compare 100-80-100, compressed, 9/80 and pro-rata models.", "cal"),
    ("hybrid-schedule-planner.html", "Hybrid schedule planner", "Plot your team's week and find the best anchor day.", "grid"),
    ("time-zone-overlap.html", "Time-zone overlap finder", "See the shared working hours across up to four locations.", "globe"),
    ("flex-policy-builder.html", "Flex policy builder", "Generate a complete flexible work policy for your company.", "shield"),
]

ICONS = {
    "quiz": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6V14M12 17.5v.01"/></svg>',
    "car": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 16V11l2-5h10l2 5v5"/><path d="M3 16h18v3H3z"/><circle cx="7.5" cy="13" r=".8"/><circle cx="16.5" cy="13" r=".8"/></svg>',
    "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 13h7M9 17h5"/></svg>',
    "coin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M15 9.5c-.5-1-1.6-1.5-3-1.5-1.7 0-3 .8-3 2s1.3 1.7 3 2 3 .8 3 2-1.3 2-3 2c-1.4 0-2.5-.5-3-1.5M12 6v2M12 16v2"/></svg>',
    "cal": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4M16 15h2"/></svg>',
    "grid": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 10h18M3 15h18M9 4v16M15 4v16"/></svg>',
    "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3l8 3v6c0 4.5-3.4 8-8 9-4.6-1-8-4.5-8-9V6z"/><path d="M9 12l2 2 4-4"/></svg>',
}

def tool_tiles(root_prefix="tools/", feature_first=True):
    out = []
    for i, (h, t, d, ic) in enumerate(TOOLS):
        cls = "tool-tile feature" if (feature_first and i == 0) else "tool-tile"
        out.append(f'<a class="{cls}" href="{{root}}{root_prefix}{h}"><span class="ic">{ICONS[ic]}</span><h3>{t}</h3><p>{d}</p></a>')
    return "".join(out)

ARR_OPTIONS = '''<option value="">Any arrangement</option><option value="r">Remote</option><option value="h">Hybrid</option><option value="p">Part-time</option><option value="f">Freelance</option><option value="d">Four-day / compressed</option><option value="a">Async-first</option>'''

FIELDS = ["Tech and engineering", "Data and analytics", "Design and creative", "Marketing and content", "Sales", "Customer support and success", "Operations and admin", "Finance and accounting", "People and HR", "Education and tutoring", "Healthcare", "Legal", "Frontline and shift work", "Other"]
FIELD_OPTS = "".join(f"<option>{f}</option>" for f in FIELDS)

def arrangement_chips(name="arrangement"):
    items = ["Remote", "Hybrid", "Part-time", "Freelance or contract", "Four-day week", "Compressed hours", "Flexitime", "Job-share"]
    return '<div class="chips">' + "".join(
        f'<label class="chip"><input type="checkbox" name="{name}" value="{x}"><span>{x}</span></label>' for x in items) + "</div>"

QUICK_LEAD = '''<form class="form" data-form="Talent network (quick)" data-redirect="{root}thank-you.html">''' + hp() + '''
 <fieldset><legend>What kind of flexibility do you want?</legend>''' + arrangement_chips() + '''</fieldset>
 <div class="two">
  <label>Your field<select name="field" required><option value="">Choose a field</option>''' + FIELD_OPTS + '''</select></label>
  <label>Role you want<input name="role" required placeholder="e.g. Data analyst"></label>
 </div>
 <div class="two">
  <label>First name<input name="name" required autocomplete="given-name"></label>
  <label>Email<input name="email" type="email" required autocomplete="email"></label>
 </div>
 <label class="check"><input type="checkbox" name="consent" value="Yes" required><span>Email me matched flexible roles and the weekly Flex Brief. Unsubscribe any time. <a href="{root}privacy.html">Privacy</a></span></label>
 <button class="btn" type="submit">Get matched — it&rsquo;s free</button>
 <p class="form-status" aria-live="polite"></p>
</form>'''

FAQ = [
    ("What is flexible work?", "Any arrangement that changes where, when or how much you work compared with a fixed five-day office week: remote and hybrid work, flexitime, compressed hours, four-day weeks, part-time, job-sharing and freelance or fractional work."),
    ("Is Flex.Work a job board?", "Flex.Work is a guide and matching service. The role explorer profiles flexible-friendly careers, and the free talent network matches you with employers who post flexible roles with us. We never charge job seekers."),
    ("How do I ask my employer for flexible work?", "Put it in writing, lead with how the work will get done, and propose a time-limited trial with a review date. Our free request letter generator builds the whole request for you."),
    ("How can I tell if a remote job is a scam?", "Be wary of jobs that pay to chat-only interviews, ask you to buy equipment upfront, request ID or bank details before an offer, or pay unusually well for simple tasks. Our scam guide lists the warning signs and how to verify an employer."),
    ("Do four-day weeks really work?", "Published pilots report that most companies kept the model afterwards. In the UK pilot, 89% of firms were still running a four-day week a year on. Results depend on redesigning work, not just removing a day."),
    ("Is Flex.Work free?", "Yes. All tools, guides and the talent network are free for individuals. The site is funded by advertising, employer listings, sponsorship and reader support."),
]

def faq_html():
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ) + "</div>"

def faq_ld():
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}

def days_html():
    pattern = [("Mon", "office"), ("Tue", "home"), ("Wed", "office"), ("Thu", "home"), ("Fri", "office"), ("Sat", "off"), ("Sun", "off")]
    return "".join(f'<button type="button" class="day" data-day="{d}" data-state="{s}"><span>{d}</span><span class="ico"></span><span class="st"></span></button>' for d, s in pattern)

def home(guides):
    arr = "".join(f'<div class="arr"><h3><a href="{{root}}{h}">{t}</a></h3><p>{d}</p></div>' for t, d, h in ARR)
    stats = "".join(stat_block(s) for s in STATS)
    vids = "".join(video_card(v) for v in VIDEOS[:3])
    grows = "".join(
        f'<a class="row-link" href="{{root}}guides/{g["slug"]}.html"><div><span class="tag{"" if g["aud"]=="Workers" else " ink"}">{g["aud"]}</span><h3 class="mt4">{g["title"]}</h3><p>{g["desc"]}</p></div><span class="meta">{g["mins"]} min read</span></a>'
        for g in guides[:6])
    body = '''
<section class="hero">
 <div class="wrap">
  <div>
   <h1>Work that fits the week you actually have.</h1>
   <p class="lede">Remote, hybrid, part-time, freelance and four-day roles — plus free tools to find them, negotiate them and make them work.</p>
   <form class="hero-search" id="hero-search" role="search" aria-label="Explore flexible roles">
    <label class="hp" for="hs-q">Role or skill</label><input id="hs-q" placeholder="Role or skill" autocomplete="off">
    <label class="hp" for="hs-t">Arrangement</label><select id="hs-t">''' + ARR_OPTIONS + '''</select>
    <button class="btn" type="submit">Explore roles</button>
   </form>
   <div class="hero-links"><a href="{root}talent.html">Get matched with flexible roles</a><a href="{root}employers.html">Hiring? Post a flexible role</a><a href="{root}tools/flexible-work-request-letter.html">Ask your boss for flexibility</a></div>
  </div>
  <div class="week" id="week">
   <h2>Design your week</h2>
   <p class="hint">Tap a day to switch between office, home and off.</p>
   <div class="legend"><span style="--c:var(--ink)">Office</span><span style="--c:var(--fern)">Home</span><span style="--c:var(--mari)">Off</span></div>
   <div class="days">''' + days_html() + '''</div>
   <div class="week-inputs">
    <label for="wk-min">One-way commute (minutes)<input id="wk-min" type="number" min="0" max="240" value="40"></label>
    <label for="wk-cost">Cost per office day ($)<input id="wk-cost" type="number" min="0" max="500" value="25"></label>
   </div>
   <div class="readout" aria-live="polite">
    <div class="k-home"><strong id="wk-hrs">0</strong>hours back a year</div>
    <div class="k-home"><strong id="wk-money">$0</strong>saved a year</div>
    <div><strong id="wk-mix">0/0/0</strong>office / home / off</div>
   </div>
   <p class="small mt4 mb0" id="wk-sum"></p>
   <button class="btn ghost sm mt4" id="wk-go" type="button">Plan this with your team</button>
  </div>
 </div>
</section>

<section class="section white">
 <div class="wrap">
  <div class="sec-head"><h2>Eight ways to work flexibly</h2><p>Flexibility runs from small changes to your hours all the way to working for yourself. Know which one you&rsquo;re asking for before you ask.</p></div>
  <div class="spectrum"><div class="spectrum-bar" aria-hidden="true"></div><div class="spectrum-ends"><span>Small change to when you work</span><span>Full control of where and how much</span></div></div>
  <div class="arr-list">''' + arr + '''</div>
 </div>
</section>
''' + ad("display") + '''
<section class="section ink">
 <div class="wrap">
  <div class="sec-head"><h2>Flexibility is now the default ask</h2><p>Every figure links to its original source, so you can quote it in your own request or policy.</p></div>
  <div class="stats">''' + stats + '''</div>
  <p class="mt6 mb0"><a href="{root}resources.html">More research and data sources</a></p>
 </div>
</section>

<section class="section lead-band" id="match">
 <div class="wrap">
  <div>
   <h2>Get matched with flexible roles</h2>
   <p class="lede">Tell us the flexibility you want. When an employer posts a matching role on Flex.Work, you hear first.</p>
   <ul class="benefits">
    <li>Free for job seekers, always</li>
    <li>Only roles that state their flexibility up front — days in office, hours and location rules</li>
    <li>A weekly Flex Brief with new roles, salary data and negotiation tips</li>
    <li>Employers are checked before their roles reach you</li>
   </ul>
   <p class="small muted">Prefer the full profile? <a href="{root}talent.html">Join the talent network</a> to add skills, availability and pay expectations.</p>
  </div>
  <div class="lead-card">''' + QUICK_LEAD + '''</div>
 </div>
</section>

<section class="section white">
 <div class="wrap">
  <div class="sec-head"><h2>Free tools for flexible work</h2><p>Calculators and generators that do the maths and the writing for you. No sign-up.</p></div>
  <div class="grid-4">''' + tool_tiles() + '''</div>
 </div>
</section>

<section class="section">
 <div class="wrap grid-2" style="align-items:center">
  <div>
   <h2>Hiring? Reach people who want to work this way.</h2>
   <p class="lede">Candidates on Flex.Work choose their arrangement before they apply, so the people who reach you already want the role as you&rsquo;ve designed it.</p>
   <div class="split mt5"><a class="btn ink" href="{root}employers.html#post">Post a flexible role</a><a class="btn ghost" href="{root}tools/flex-policy-builder.html">Build a flex policy</a></div>
  </div>
  <div class="panel">
   <h3>How hiring works</h3>
   <ol class="mb0">
    <li class="mb0"><strong>Tell us the role</strong> and its exact flexibility: days, hours, location rules, pay.</li>
    <li class="mb0 mt4"><strong>We publish and promote it</strong> to matched talent-network members and the Flex Brief.</li>
    <li class="mb0 mt4"><strong>You receive applicants</strong> who have already chosen that arrangement.</li>
   </ol>
  </div>
 </div>
</section>

<section class="section white">
 <div class="wrap">
  <div class="sec-head"><h2>Guides</h2><p>Practical, plain-language guides for people seeking flexibility and the teams offering it.</p></div>
  <div class="rows">''' + grows + '''</div>
  <p class="mt5"><a class="btn ghost" href="{root}guides/index.html">All guides</a></p>
 </div>
</section>
''' + ad("inFeed") + '''
<section class="section">
 <div class="wrap">
  <div class="sec-head"><h2>Watch: the case for flexible work</h2><p>Talks from researchers and practitioners. Videos load only when you press play.</p></div>
  <div class="grid-3">''' + vids + '''</div>
  <p class="mt5"><a href="{root}videos.html">Browse the video library</a></p>
 </div>
</section>

<section class="section white">
 <div class="wrap grid-3">
  <div class="panel flat sun"><h3>Support independent guidance</h3><p>Reader support keeps every tool free and funds promotion, new tools and contest prizes.</p><a class="btn mari sm" href="{root}support.html">Support Flex.Work</a></div>
  <div class="panel flat soft"><h3>Enter a contest</h3><p>Share your best home-office setup or flexible-work story for a chance to win prizes.</p><a class="btn sm" href="{root}contests.html">See current contests</a></div>
  <div class="panel flat"><h3>Write, build or grow with us</h3><p>We hire freelance writers, researchers, developers and community hosts — flexibly, of course.</p><a class="btn ink sm" href="{root}careers.html">Open roles</a></div>
 </div>
</section>

<section class="section">
 <div class="wrap grid-2">
  <div><h2>Questions people ask</h2><p class="muted">Something else? <a href="{root}contact.html">Ask us</a>.</p></div>
  ''' + faq_html() + '''
 </div>
</section>
'''
    return body
