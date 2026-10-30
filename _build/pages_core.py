from layout import ad, hp, OWNER
from data import VIDEOS, MORE_STATS, STATS, video_card
from pages_home import arrangement_chips, FIELD_OPTS, ARR_OPTIONS

def ph(title, lede, crumb=None):
    c = f'<div class="crumbs"><a href="{{root}}index.html">Home</a> / {crumb}</div>' if crumb else ""
    return f'<div class="wrap page-head">{c}<h1>{title}</h1><p class="lede">{lede}</p></div>'

CONSENT = '<label class="check"><input type="checkbox" name="consent" value="Yes" required><span>I agree to be contacted about this request and accept the <a href="{root}privacy.html">privacy policy</a>.</span></label>'

# ---------------------------------------------------------------- jobs / explorer
def jobs():
    return ph("Explore flexible-friendly roles", "Fifty-plus careers rated for how often they come with remote, hybrid, part-time, freelance or four-day arrangements. Filter by what you want, then get matched.", "Find roles") + '''
<section class="section" style="padding-top:0"><div class="wrap" id="explorer">
 <div class="filters panel flat">
  <label>Search<input id="ex-q" placeholder="Role, skill or keyword"></label>
  <label>Field<select id="ex-cat"><option value="">All fields</option></select></label>
  <label>Arrangement<select id="ex-arr">''' + ARR_OPTIONS + '''</select></label>
  <label>Minimum flexibility<select id="ex-min"><option value="1">Any</option><option value="3">3 of 5 or more</option><option value="4">4 of 5 or more</option><option value="5">5 of 5 only</option></select></label>
 </div>
 <p class="small muted"><strong id="ex-count"></strong>. Profiles are Flex.Work editorial assessments to guide your search, not job postings. Flexibility ratings reflect how commonly each role is offered flexibly.</p>
 <div class="role-list" id="ex-out" aria-live="polite"></div>
</div></section>''' + ad("inFeed") + '''
<section class="section white" id="alerts"><div class="wrap grid-2" style="align-items:start">
 <div><h2>Get flexible job alerts</h2><p class="lede">Choose a field and an arrangement. When employers post matching roles on Flex.Work, we email you — at most once a week.</p><p class="small muted">Want full matching with skills and pay? <a href="{root}talent.html">Join the talent network</a>.</p></div>
 <div class="panel"><form class="form" data-form="Job alert" data-redirect="{root}thank-you.html">''' + hp() + '''
  <div class="two"><label>Field<select name="field" required><option value="">Choose a field</option>''' + FIELD_OPTS + '''</select></label>
  <label>Arrangement<select name="arrangement" required><option value="">Choose one</option><option>Remote</option><option>Hybrid</option><option>Part-time</option><option>Freelance or contract</option><option>Four-day week or compressed</option><option>Any flexible</option></select></label></div>
  <div class="two"><label>Country you can work in<input name="country" required autocomplete="country-name"></label><label>Email<input name="email" type="email" required autocomplete="email"></label></div>
  <label class="check"><input type="checkbox" name="consent" value="Yes" required><span>Send me matching flexible job alerts. Unsubscribe any time.</span></label>
  <button class="btn" type="submit">Create job alert</button><p class="form-status" aria-live="polite"></p>
 </form></div>
</div></section>'''

# ---------------------------------------------------------------- talent network (primary lead gen)
def talent():
    return '''<section class="section lead-band" style="padding-top:56px"><div class="wrap">
 <div>
  <div class="crumbs"><a href="{root}index.html">Home</a> / Talent network</div>
  <h1 style="font-size:clamp(2.2rem,4.4vw,3.4rem)">Join the Flex.Work talent network</h1>
  <p class="lede">One free profile. Matched to employers who state their flexibility, location rules and pay before you apply.</p>
  <ul class="benefits">
   <li>Never pay to find work — free for job seekers, always</li>
   <li>Matches only when an employer&rsquo;s arrangement fits yours</li>
   <li>Employers are checked before their roles reach you</li>
   <li>Weekly Flex Brief: new roles, pay data and negotiation tips</li>
   <li>Delete your profile any time with one email</li>
  </ul>
  <div class="panel flat soft"><h3>How matching works</h3><ol class="mb0"><li>Tell us the flexibility, field and pay you want (two minutes).</li><li>Employers post roles with exact days, hours and location rules.</li><li>We introduce you only when both sides fit.</li></ol></div>
 </div>
 <div class="lead-card">
  <form class="form" data-form="Talent network profile" data-steps data-redirect="{root}thank-you.html">''' + hp() + '''
   <div class="stepper" aria-hidden="true"><i></i><i></i><i></i></div><p class="step-count"></p>
   <div class="step">
    <h3 class="mb0">What you&rsquo;re looking for</h3>
    <fieldset><legend>Arrangements you want</legend>''' + arrangement_chips() + '''</fieldset>
    <div class="two"><label>Field<select name="field" required><option value="">Choose a field</option>''' + FIELD_OPTS + '''</select></label>
    <label>Target role<input name="role" required placeholder="e.g. Customer success manager"></label></div>
    <label>Maximum office days per week<select name="max_office_days"><option>0 — fully remote</option><option>1</option><option>2</option><option>3</option><option>4 or more is fine</option></select></label>
    <div class="step-nav"><span></span><button class="btn" type="button" data-next>Continue</button></div>
   </div>
   <div class="step">
    <h3 class="mb0">Your experience</h3>
    <div class="two"><label>Experience<select name="experience" required><option value="">Choose</option><option>Entry level / student</option><option>1–3 years</option><option>3–7 years</option><option>7–15 years</option><option>15+ years</option></select></label>
    <label>Country you live in<input name="country" required autocomplete="country-name"></label></div>
    <label>Top skills<input name="skills" required placeholder="e.g. SQL, stakeholder reporting, Tableau"></label>
    <div class="two"><label>Hours per week<select name="hours"><option>Full-time</option><option>30–35</option><option>20–29</option><option>10–19</option><option>Under 10</option></select></label>
    <label>Available from<select name="available"><option>Immediately</option><option>Within a month</option><option>1–3 months</option><option>Just exploring</option></select></label></div>
    <label>Pay expectation (optional)<input name="pay" placeholder="e.g. $70k/year or $45/hour"></label>
    <div class="step-nav"><button class="btn ghost" type="button" data-prev>Back</button><button class="btn" type="button" data-next>Continue</button></div>
   </div>
   <div class="step">
    <h3 class="mb0">How to reach you</h3>
    <div class="two"><label>Full name<input name="name" required autocomplete="name"></label><label>Email<input name="email" type="email" required autocomplete="email"></label></div>
    <label>LinkedIn or portfolio URL (optional)<input name="profile_url" type="url" placeholder="https://"></label>
    <label class="check"><input type="checkbox" name="consent" value="Yes" required><span>Match me with flexible roles and email me about them. I accept the <a href="{root}privacy.html">privacy policy</a>.</span></label>
    <label class="check"><input type="checkbox" name="newsletter" value="Yes" checked><span>Also send the weekly Flex Brief.</span></label>
    <div class="step-nav"><button class="btn ghost" type="button" data-prev>Back</button><button class="btn" type="submit">Join the network</button></div>
    <p class="form-status" aria-live="polite"></p>
   </div>
  </form>
  <div class="trust"><span>Free</span><span>No spam</span><span>Unsubscribe any time</span></div>
 </div>
</div></section>
<section class="section white"><div class="wrap grid-3">
 <div><h3>Before you join</h3><p>Read <a href="{root}guides/remote-job-search-strategy.html">a remote job search strategy that beats mass-applying</a>.</p></div>
 <div><h3>Stay safe</h3><p>Flex.Work will never ask you for money, bank details or ID documents. Learn the <a href="{root}guides/remote-job-scams.html">warning signs of job scams</a>.</p></div>
 <div><h3>Not sure what to ask for?</h3><p>Take the <a href="{root}tools/flex-readiness-quiz.html">flex readiness quiz</a> to find the arrangement that fits.</p></div>
</div></section>'''

# ---------------------------------------------------------------- employers
def employers():
    return ph("Hire people who want to work the way you do", "Post remote, hybrid, part-time, four-day and freelance roles to candidates who have already chosen that arrangement.", "For employers") + '''
<section class="section" style="padding-top:0"><div class="wrap">
 <div class="tiers">
  <div class="tier"><h3>Launch listing</h3><div class="price">Free <small>30 days</small></div><p class="muted">For employers posting during our launch period.</p><ul><li>One flexible role, 30 days</li><li>Arrangement and pay badges</li><li>Matched to talent-network members</li></ul><a class="btn ghost" href="#post">Post free</a></div>
  <div class="tier pick"><span class="tag sun">Most chosen</span><h3>Featured</h3><div class="price">$149 <small>per role</small></div><p class="muted">For roles you need to fill quickly.</p><ul><li>Everything in Launch, for 60 days</li><li>Pinned in the role explorer and alerts</li><li>Included in the weekly Flex Brief</li><li>Social promotion</li></ul><a class="btn" href="#post">Choose Featured</a></div>
  <div class="tier"><h3>Hiring partner</h3><div class="price">Custom</div><p class="muted">For ongoing or volume flexible hiring.</p><ul><li>Unlimited roles</li><li>Shortlists from the talent network</li><li>Employer profile and sponsored guide</li><li>Flex policy review</li></ul><a class="btn ink" href="#post">Talk to us</a></div>
 </div>
 <p class="small muted mt4">Prices in USD. We confirm details and send a secure payment link before anything is charged.</p>
</div></section>
<section class="section lead-band" id="post" style="background:var(--ink);color:#E9EEF3"><div class="wrap">
 <div><h2 style="color:#fff">Post a flexible role</h2><p class="lede" style="color:#C7D0DA">Three short steps. We review every role within one business day and confirm before it goes live.</p>
  <ul class="benefits"><li>State the exact flexibility: office days, core hours, location rules</li><li>Reach candidates who have chosen that arrangement</li><li>Show pay to get more qualified applicants</li><li>Free during launch; upgrade any time</li></ul>
 </div>
 <div class="lead-card"><form class="form" data-form="Employer role posting" data-steps data-redirect="{root}thank-you.html">''' + hp() + '''
  <div class="stepper" aria-hidden="true"><i></i><i></i><i></i></div><p class="step-count"></p>
  <div class="step"><h3 class="mb0">Your company</h3>
   <div class="two"><label>Company name<input name="company" required autocomplete="organization"></label><label>Website<input name="website" type="url" required placeholder="https://"></label></div>
   <div class="two"><label>Company size<select name="size" required><option value="">Choose</option><option>1–10</option><option>11–50</option><option>51–200</option><option>201–1,000</option><option>1,000+</option></select></label><label>Industry<input name="industry" required></label></div>
   <div class="step-nav"><span></span><button class="btn" type="button" data-next>Continue</button></div></div>
  <div class="step"><h3 class="mb0">The role</h3>
   <div class="two"><label>Job title<input name="job_title" required></label><label>Arrangement<select name="arrangement" required><option value="">Choose</option><option>Fully remote</option><option>Hybrid</option><option>Part-time</option><option>Four-day week</option><option>Compressed hours</option><option>Freelance / contract</option><option>Job-share</option></select></label></div>
   <div class="two"><label>Office days per week<select name="office_days"><option>0</option><option>1</option><option>2</option><option>3</option><option>4+</option><option>Not applicable</option></select></label><label>Location eligibility<input name="location" required placeholder="e.g. Remote, Canada only"></label></div>
   <div class="two"><label>Pay range<input name="pay_range" placeholder="e.g. $65k–$80k"></label><label>Hiring timeline<select name="timeline"><option>As soon as possible</option><option>Within 30 days</option><option>1–3 months</option><option>Ongoing</option></select></label></div>
   <label>Short description or link to the posting<textarea name="description" required></textarea></label>
   <div class="step-nav"><button class="btn ghost" type="button" data-prev>Back</button><button class="btn" type="button" data-next>Continue</button></div></div>
  <div class="step"><h3 class="mb0">Your details</h3>
   <div class="two"><label>Your name<input name="name" required autocomplete="name"></label><label>Work email<input name="email" type="email" required autocomplete="email"></label></div>
   <div class="two"><label>Phone (optional)<input name="phone" type="tel" autocomplete="tel"></label><label>Plan<select name="plan"><option>Launch listing (free)</option><option>Featured ($149)</option><option>Hiring partner (custom)</option><option>Not sure yet</option></select></label></div>
   ''' + CONSENT + '''
   <div class="step-nav"><button class="btn ghost" type="button" data-prev>Back</button><button class="btn" type="submit">Submit role</button></div>
   <p class="form-status" aria-live="polite"></p></div>
 </form></div>
</div></section>
<section class="section white" id="index"><div class="wrap grid-2" style="align-items:start">
 <div><h2>Get listed in the Flex Employer Index</h2><p class="lede">We&rsquo;re building a public directory of employers and their real flexibility: office days, core hours, location rules and four-day-week status. Listing is free.</p><p>Research by the Flex Index found 66% of US companies offer some location flexibility. Candidates want to know which ones — being listed puts your policy in front of them.</p></div>
 <div class="panel"><form class="form" data-form="Flex Employer Index submission" data-redirect="{root}thank-you.html">''' + hp() + '''
  <div class="two"><label>Company<input name="company" required></label><label>Careers page URL<input name="careers_url" type="url" required placeholder="https://"></label></div>
  <div class="two"><label>Policy<select name="policy" required><option value="">Choose</option><option>Fully flexible / remote-first</option><option>Structured hybrid</option><option>Team-led</option><option>Office-based with options</option></select></label><label>Required office days<select name="office_days"><option>0</option><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option></select></label></div>
  <label>Other flexibility (four-day week, flexitime, job-share…)<input name="other"></label>
  <div class="two"><label>Your name<input name="name" required></label><label>Work email<input name="email" type="email" required></label></div>
  ''' + CONSENT + '''<button class="btn ink" type="submit">Submit for the index</button><p class="form-status" aria-live="polite"></p>
 </form></div>
</div></section>
<section class="section"><div class="wrap"><div class="sec-head"><h2>Employer resources</h2></div><div class="rows">
 <a class="row-link" href="{root}tools/flex-policy-builder.html"><div><h3>Flex policy builder</h3><p>Generate a twelve-section flexible work policy.</p></div><span class="meta">Tool</span></a>
 <a class="row-link" href="{root}guides/managing-flexible-teams.html"><div><h3>Managing flexible teams</h3><p>Outcomes, meeting rhythm and avoiding proximity bias.</p></div><span class="meta">Guide</span></a>
 <a class="row-link" href="{root}guides/hybrid-schedules-compared.html"><div><h3>Hybrid schedules compared</h3><p>Five models and how to choose.</p></div><span class="meta">Guide</span></a>
 <a class="row-link" href="{root}guides/four-day-week-guide.html"><div><h3>The four-day week</h3><p>Evidence, models and a six-step pilot plan.</p></div><span class="meta">Guide</span></a>
</div></div></section>'''

# ---------------------------------------------------------------- support / donations
def support():
    uses = [("Operations", "Hosting, tools, data and keeping every calculator free."), ("Promotion and marketing", "Reaching more people looking for flexible work."), ("Hiring talent", "Paying freelance writers, researchers and developers fairly."), ("Contests and prizes", "Funding prizes for our community contests.")]
    u = "".join(f'<div class="arr"><h3>{a}</h3><p>{b}</p></div>' for a, b in uses)
    amts = "".join(f'<label class="chip"><input type="radio" name="amount" value="{v}" {"checked" if v=="$25" else ""}><span>{v}</span></label>' for v in ["$5", "$10", "$25", "$50", "$100", "$250", "$500", "Other"])
    return ph("Support Flex.Work", "Flex.Work is independent and free. Reader support keeps it that way and funds new tools, promotion, fairly paid contributors and contest prizes.", "Support") + '''
<section class="section" style="padding-top:0"><div class="wrap"><div class="arr-list" style="grid-template-columns:repeat(4,minmax(0,1fr))">''' + u + '''</div></div></section>
<section class="section white"><div class="wrap grid-2" style="align-items:start">
 <div><h2>Make a contribution</h2><p class="lede">Choose an amount and how often. We&rsquo;ll email you a secure payment link — we never collect card details on this site.</p>
  <div class="tiers" style="grid-template-columns:1fr;gap:12px">
   <div class="panel flat"><h3>Coffee supporter</h3><p class="mb0">$5 a month. Your name on the supporters page, if you&rsquo;d like.</p></div>
   <div class="panel flat soft"><h3>Flex champion</h3><p class="mb0">$25 a month. Early access to new tools and a say in what we build next.</p></div>
   <div class="panel flat sun"><h3>Patron</h3><p class="mb0">$100+ a month or one-off. Recognition on the site and a quarterly call with the editor.</p></div>
  </div>
 </div>
 <div class="panel"><form class="form" data-form="Support pledge" data-redirect="{root}thank-you.html">''' + hp() + '''
  <fieldset><legend>Amount (USD)</legend><div class="amounts">''' + amts + '''</div></fieldset>
  <label>Other amount (optional)<input name="other_amount" placeholder="e.g. $75"></label>
  <fieldset><legend>How often</legend><div class="chips"><label class="chip"><input type="radio" name="frequency" value="One-off" checked><span>One-off</span></label><label class="chip"><input type="radio" name="frequency" value="Monthly"><span>Monthly</span></label><label class="chip"><input type="radio" name="frequency" value="Yearly"><span>Yearly</span></label></div></fieldset>
  <label>Put it towards<select name="purpose"><option>Wherever it&rsquo;s needed most</option><option>Operations</option><option>Promotion and marketing</option><option>Hiring talent</option><option>Contests and prizes</option></select></label>
  <div class="two"><label>Name<input name="name" required autocomplete="name"></label><label>Email<input name="email" type="email" required autocomplete="email"></label></div>
  <label class="check"><input type="checkbox" name="public_credit" value="Yes"><span>List my name on the supporters page.</span></label>
  ''' + CONSENT + '''<button class="btn mari" type="submit">Send me a payment link</button><p class="form-status" aria-live="polite"></p>
 </form></div>
</div></section>
<section class="section"><div class="wrap grid-3">
 <div><h3>Other ways to help</h3><p>Share a tool with a colleague, link to a guide, or suggest a feature through <a href="{root}contact.html">contact</a>.</p></div>
 <div><h3>Sponsor a contest</h3><p>Businesses can fund prizes in exchange for recognition. <a href="{root}advertise.html">See sponsorship</a>.</p></div>
 <div><h3>Transparency</h3><p>Contributions support Flex.Work as a business; they are not charitable donations and are not tax-deductible.</p></div>
</div></section>'''

# ---------------------------------------------------------------- contests
def contests():
    cs = [
        ("Best home office setup", "Share a photo of your workspace and one change that made the biggest difference.", "Workspace upgrade voucher worth $300", "Runner-up prizes: ergonomic accessories"),
        ("My flexible work story", "In 300–800 words, tell us how a flexible arrangement changed your work or life.", "$250 prize and publication on Flex.Work", "Two runners-up: $50 each"),
        ("Best async tip", "Share one habit or template that saves your team a meeting.", "Annual subscription to a productivity tool of your choice, up to $150", "Featured in the Flex Brief"),
    ]
    cards = "".join(f'<div class="tier"><span class="tag">Open</span><h3>{t}</h3><p>{d}</p><p class="mb0"><strong>Prize:</strong> {p}</p><p class="small muted">{r}</p><a class="btn" href="#enter">Enter</a></div>' for t, d, p, r in cs)
    opts = "".join(f"<option>{c[0]}</option>" for c in cs)
    return ph("Contests and prizes", "Share what makes flexible work work for you. Free to enter, judged on merit, with prizes funded by readers and sponsors.", "Contests") + '''
<section class="section" style="padding-top:0"><div class="wrap"><div class="tiers">''' + cards + '''</div></div></section>
<section class="section white" id="enter"><div class="wrap grid-2" style="align-items:start">
 <div><h2>Enter a contest</h2><p class="lede">Send your entry using the form. For photos, include a link to the image on any file-sharing service.</p>
 <h3>Official rules summary</h3><ul class="small"><li>No purchase or payment necessary. Purchasing does not improve your chance of winning.</li><li>Open to individuals aged 18 or over where contests are legal. Void where prohibited.</li><li>One entry per person per contest. Entries must be your own original work.</li><li>Entries are judged by the Flex.Work editorial team on originality, usefulness and clarity.</li><li>Winners are notified by email and announced on this page. Prizes may be substituted with an equal-value alternative.</li><li>By entering you grant Flex.Work a non-exclusive licence to publish your entry with credit. You keep the copyright.</li><li>Entry dates and closing dates are announced in the Flex Brief and on this page.</li></ul></div>
 <div class="panel"><form class="form" data-form="Contest entry" data-redirect="{root}thank-you.html">''' + hp() + '''
  <label>Contest<select name="contest" required>''' + opts + '''</select></label>
  <div class="two"><label>Name<input name="name" required autocomplete="name"></label><label>Email<input name="email" type="email" required autocomplete="email"></label></div>
  <label>Country<input name="country" required autocomplete="country-name"></label>
  <label>Your entry, or a link to it<textarea name="entry" required></textarea></label>
  <label class="check"><input type="checkbox" name="rules" value="Accepted" required><span>I confirm I&rsquo;m 18 or over, the entry is my own work, and I accept the rules.</span></label>
  <button class="btn" type="submit">Submit entry</button><p class="form-status" aria-live="polite"></p>
 </form></div>
</div></section>
<section class="section"><div class="wrap grid-2" style="align-items:center"><div><h2>Sponsor a prize</h2><p class="lede">Put your brand in front of people who care about how they work. Sponsors fund prizes and receive recognition across the contest.</p></div><div class="split"><a class="btn ink" href="{root}advertise.html#sponsor">Sponsorship options</a></div></div></section>'''

# ---------------------------------------------------------------- careers / hiring talent
def careers():
    roles = [
        ("Freelance writer — flexible work and careers", "Remote, freelance", "Write practical, well-sourced guides for workers and employers. Paid per article."),
        ("Data researcher", "Remote, part-time contract", "Track public flexibility policies for the Flex Employer Index and verify sources."),
        ("Front-end developer", "Remote, project-based", "Build new tools and calculators in plain HTML, CSS and JavaScript."),
        ("Community and partnerships lead", "Remote, fractional", "Grow the talent network, run contests and manage employer relationships."),
        ("Video creator", "Remote, freelance", "Produce short explainers on flexible work for YouTube and social."),
    ]
    rows = "".join(f'<div class="row-link" style="cursor:default"><div><h3>{t}</h3><p>{d}</p></div><span class="meta">{a}</span></div>' for t, a, d in roles)
    opts = "".join(f"<option>{r[0]}</option>" for r in roles)
    return ph("Work with Flex.Work", "We practise what we publish: every role here is remote and flexible. We hire freelancers and part-time contributors as we grow.", "Work with us") + '''
<section class="section" style="padding-top:0"><div class="wrap"><div class="rows">''' + rows + '''</div></div></section>
<section class="section white" id="apply"><div class="wrap grid-2" style="align-items:start">
 <div><h2>Apply</h2><p class="lede">Tell us about yourself and send examples of your work. We reply to every applicant.</p><h3>How we work</h3><ul><li>Async first, with one optional weekly call</li><li>Paid on time, every time</li><li>You choose your hours</li><li>Credit on everything you publish</li></ul></div>
 <div class="panel"><form class="form" data-form="Careers application" data-redirect="{root}thank-you.html">''' + hp() + '''
  <label>Role<select name="role" required>''' + opts + '''<option>Something else</option></select></label>
  <div class="two"><label>Name<input name="name" required autocomplete="name"></label><label>Email<input name="email" type="email" required autocomplete="email"></label></div>
  <div class="two"><label>Portfolio or LinkedIn<input name="portfolio" type="url" required placeholder="https://"></label><label>Hours per week available<select name="hours"><option>Under 10</option><option>10–20</option><option>20–30</option><option>30+</option></select></label></div>
  <label>Why you, in a few sentences<textarea name="message" required></textarea></label>
  ''' + CONSENT + '''<button class="btn" type="submit">Send application</button><p class="form-status" aria-live="polite"></p>
 </form></div>
</div></section>'''

# ---------------------------------------------------------------- advertise
def advertise():
    return ph("Advertise, sponsor and partner", "Reach job seekers, freelancers, managers and HR leaders at the moment they&rsquo;re deciding how to work.", "Advertise") + '''
<section class="section" style="padding-top:0"><div class="wrap">
 <div class="panel sun" style="margin-bottom:32px"><h3>Interested in this website or the Flex.Work domain?</h3><p class="mb0">For acquisition, domain, sponsorship, advertising or partnership inquiries, <a href="''' + OWNER + '''" target="_blank" rel="noopener">contact the owner directly</a>.</p></div>
 <div class="tiers" id="sponsor">
  <div class="tier"><h3>Newsletter sponsor</h3><p>A dedicated placement in the weekly Flex Brief.</p><ul><li>Logo, 60-word message and link</li><li>Sent to talent-network members</li></ul></div>
  <div class="tier pick"><h3>Tool sponsor</h3><p>&ldquo;Presented by&rdquo; placement on one of our free tools.</p><ul><li>Logo and short message on the tool page</li><li>Mention in related guides</li><li>Minimum three months</li></ul></div>
  <div class="tier"><h3>Contest and content partner</h3><p>Fund a contest prize or co-create a research guide.</p><ul><li>Recognition across the contest</li><li>Clearly labelled sponsored content</li></ul></div>
 </div>
 <p class="small muted mt4">All sponsored content is labelled. We don&rsquo;t sell reader data and we don&rsquo;t accept advertising for jobs that charge applicants.</p>
</div></section>
<section class="section white"><div class="wrap grid-2" style="align-items:start">
 <div><h2>Tell us what you have in mind</h2><p class="lede">We reply within two business days with availability and a media kit.</p><p>Good fits include HR and payroll software, coworking spaces, home-office and ergonomics brands, productivity tools, training providers, insurance for freelancers and flexible employers.</p></div>
 <div class="panel"><form class="form" data-form="Advertising and partnership inquiry" data-redirect="{root}thank-you.html">''' + hp() + '''
  <div class="two"><label>Name<input name="name" required autocomplete="name"></label><label>Work email<input name="email" type="email" required autocomplete="email"></label></div>
  <div class="two"><label>Company<input name="company" required autocomplete="organization"></label><label>Website<input name="website" type="url" placeholder="https://"></label></div>
  <div class="two"><label>Interest<select name="interest" required><option>Newsletter sponsor</option><option>Tool sponsor</option><option>Contest sponsor</option><option>Sponsored content</option><option>Partnership</option><option>Website or domain acquisition</option><option>Other</option></select></label><label>Monthly budget<select name="budget"><option>Under $500</option><option>$500–$2,000</option><option>$2,000–$10,000</option><option>$10,000+</option><option>Not sure</option></select></label></div>
  <label>Message<textarea name="message" required></textarea></label>
  ''' + CONSENT + '''<button class="btn ink" type="submit">Send inquiry</button><p class="form-status" aria-live="polite"></p>
 </form></div>
</div></section>'''

# ---------------------------------------------------------------- videos
def videos():
    return ph("Flexible work video library", "Talks and explainers on remote work, hybrid teams, four-day weeks and freelancing from researchers and practitioners.", "Videos") + '''
<section class="section" style="padding-top:0"><div class="wrap"><div class="grid-3">''' + "".join(video_card(v) for v in VIDEOS[:6]) + '''</div></div></section>''' + ad("inFeed") + '''
<section class="section" style="padding-top:0"><div class="wrap"><div class="grid-3">''' + "".join(video_card(v) for v in VIDEOS[6:]) + '''</div>
<p class="small muted mt5">Videos are embedded from YouTube in privacy-enhanced mode and load only when you press play. They belong to their creators; Flex.Work is not affiliated with them. Suggest a video through <a href="{root}contact.html">contact</a>.</p></div></section>'''

# ---------------------------------------------------------------- resources
def resources():
    allstats = [(t, s, u) for _, t, s, u in STATS] + MORE_STATS
    rows = "".join(f'<tr><td>{t}</td><td><a href="{u}" target="_blank" rel="noopener nofollow">{s}</a></td></tr>' for t, s, u in allstats)
    orgs = [
        ("Gallup — hybrid work indicator", "https://www.gallup.com/401384/indicator-hybrid-work.aspx", "Quarterly US data on where remote-capable employees work and want to work."),
        ("WFH Research", "https://wfhresearch.com/", "Survey of Working Arrangements and Attitudes from Stanford and partner universities."),
        ("US Bureau of Labor Statistics — American Time Use Survey", "https://www.bls.gov/news.release/atus.nr0.htm", "Official US data on where and when people work."),
        ("Office for National Statistics — hybrid working", "https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/articles/whohasaccesstohybridworkingreatbritain/latest", "Who can work hybrid in Great Britain."),
        ("4 Day Week Global", "https://4dayweek.com/", "Pilot results and resources on the four-day week."),
        ("Owl Labs — State of Hybrid Work", "https://owllabs.com/state-of-hybrid-work/2024", "Annual survey on hybrid work costs and preferences."),
        ("Buffer — State of Remote Work", "https://buffer.com/state-of-remote-work/2023", "Annual survey of remote workers."),
        ("GitLab — all-remote guide", "https://handbook.gitlab.com/handbook/company/culture/all-remote/guide/", "One of the most detailed public handbooks on running a remote company."),
        ("Pew Research Center — remote work", "https://www.pewresearch.org/short-reads/2025/01/13/many-remote-workers-say-theyd-be-likely-to-leave-their-job-if-they-could-no-longer-work-from-home", "Surveys of US workers on teleworking."),
    ]
    o = "".join(f'<a class="row-link" href="{u}" target="_blank" rel="noopener nofollow"><div><h3>{t}</h3><p>{d}</p></div><span class="meta">External</span></a>' for t, u, d in orgs)
    return ph("Flexible work research and resources", "The data behind flexible work, with links to every original source — free to cite in your own request, report or policy.", "Resources") + '''
<section class="section" style="padding-top:0"><div class="wrap"><div class="prose" style="max-width:none"><table><thead><tr><th>Finding</th><th>Source</th></tr></thead><tbody>''' + rows + '''</tbody></table></div>
<p class="small muted">Figures were checked against the original pages in October 2026. Where the original was unavailable, the secondary source is named. Spotted something out of date? <a href="{root}contact.html">Let us know</a>.</p></div></section>''' + ad("display") + '''
<section class="section white"><div class="wrap"><div class="sec-head"><h2>Organisations worth following</h2></div><div class="rows">''' + o + '''</div></div></section>'''

# ---------------------------------------------------------------- glossary
GLOSS = [
    ("9/80 schedule", "Eighty hours worked over nine days in a two-week period, giving every other Friday (or another day) off."),
    ("100-80-100", "A four-day week model: 100% of pay for 80% of the time, in exchange for 100% of agreed output."),
    ("Anchor day", "A day when a whole team is expected in the office together."),
    ("Async-first", "A way of working where written, non-real-time communication is the default and meetings are the exception."),
    ("Compressed hours", "Working full-time hours over fewer, longer days."),
    ("Core hours", "The hours when everyone must be available, with flexible time around them."),
    ("Coworking space", "A shared workspace rented by the day or month."),
    ("Digital nomad", "Someone who works remotely while travelling between locations."),
    ("Employer of record (EOR)", "A company that legally employs someone on another company&rsquo;s behalf, often in another country."),
    ("Flexitime", "Choosing your start and finish times around core hours."),
    ("Four-day week", "A working week of four days, usually with reduced hours and unchanged pay."),
    ("Fractional work", "Senior professionals working part-time for several companies, such as a fractional CFO."),
    ("Hot-desking", "Office desks that aren&rsquo;t assigned to anyone and are used first-come, first-served or by booking."),
    ("Hybrid work", "Splitting work between an office and another location, usually home."),
    ("Job-sharing", "Two people sharing one full-time role, its responsibilities and its pay."),
    ("Location eligibility", "The countries, states or time zones a remote employee is allowed to work from."),
    ("Part-time", "A contract with fewer hours than the full-time standard, with pro-rata pay and benefits."),
    ("Proximity bias", "The tendency to favour people who are physically near you, which can disadvantage remote workers."),
    ("Remote-first", "A company where remote work is the default and processes are built for distributed teams."),
    ("Return to office (RTO)", "Employer policies requiring more in-office days."),
    ("Staggered hours", "Different start and finish times for different employees."),
    ("Workcation", "A trip combining remote work with leisure."),
]
def glossary():
    items = "".join(f'<div class="arr" id="{t.lower().replace(" ", "-").replace("/", "").replace("(", "").replace(")", "")}"><h3>{t}</h3><p>{d}</p></div>' for t, d in GLOSS)
    ld = {"@context": "https://schema.org", "@type": "DefinedTermSet", "name": "Flex.Work flexible work glossary",
          "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t, "description": d.replace("&rsquo;", "'")} for t, d in GLOSS]}
    return ph("Flexible work glossary", "Plain-English definitions of the terms you&rsquo;ll meet in flexible job ads, policies and negotiations.", "Glossary") + '''
<section class="section" style="padding-top:0"><div class="wrap"><div class="arr-list" style="grid-template-columns:repeat(3,minmax(0,1fr))">''' + items + '''</div></div></section>''', ld

# ---------------------------------------------------------------- about
def about():
    return ph("About Flex.Work", "An independent guide to flexible work for the people seeking it and the teams offering it.", "About") + '''
<section class="section" style="padding-top:0"><div class="wrap article"><div class="prose">
<h2>What we do</h2><p>Flex.Work helps people find, negotiate and succeed in flexible work — remote, hybrid, flexitime, compressed hours, four-day weeks, part-time, job-sharing and freelance. We publish practical guides, build free tools, profile flexible-friendly careers, and connect job seekers with employers who state their flexibility upfront.</p>
<h2>Who it&rsquo;s for</h2><ul><li><strong>Workers</strong> who want more control over where, when or how much they work.</li><li><strong>Freelancers</strong> pricing their work and finding clients.</li><li><strong>Managers and HR teams</strong> designing policies and leading distributed teams.</li></ul>
<h2 id="editorial">Editorial policy</h2><p>Our guides are written to be useful first. We:</p><ul><li>Link every statistic to its original source, and name the secondary source when the original is unavailable.</li><li>Review guides regularly and update them when evidence or rules change.</li><li>Keep advertising, sponsorship and editorial separate. Sponsored content is always labelled.</li><li>Never accept payment to change a role rating or an assessment.</li><li>Correct errors promptly — tell us through <a href="{root}contact.html">contact</a>.</li></ul>
<p>Our guides are general information. They are not legal, tax, immigration or financial advice.</p>
<h2>How we make money</h2><p>Flex.Work is free for individuals. We are funded by display advertising through Google AdSense, employer job listings, sponsorship, and reader support. We never charge job seekers and never sell personal data.</p>
<h2>Independence</h2><p>Flex.Work is an independent publication. It is not affiliated with FlexJobs, Flexwork or any company with a similar name. See our <a href="{root}trademark.html">trademark and copyright disclosure</a>.</p>
</div><aside><div class="panel flat soft"><h3>Get in touch</h3><p>Questions, corrections or ideas.</p><a class="btn sm" href="{root}contact.html">Contact us</a></div><div class="panel flat sun mt5"><h3>Website or domain</h3><p>Interested in this site, the domain, sponsorship or partnership?</p><a class="btn mari sm" href="''' + OWNER + '''" target="_blank" rel="noopener">Contact the owner</a></div></aside></div></section>'''

# ---------------------------------------------------------------- contact
def contact():
    return ph("Contact Flex.Work", "Questions, corrections, tool ideas, press or partnerships. We reply within two business days.", "Contact") + '''
<section class="section" style="padding-top:0"><div class="wrap grid-2" style="align-items:start">
 <div class="panel"><form class="form" data-form="Contact message" data-redirect="{root}thank-you.html">''' + hp() + '''
  <div class="two"><label>Name<input name="name" required autocomplete="name"></label><label>Email<input name="email" type="email" required autocomplete="email"></label></div>
  <label>Topic<select name="topic"><option>General question</option><option>Correction or feedback</option><option>Tool or guide idea</option><option>Talent network or my data</option><option>Employer listing</option><option>Press</option><option>Advertising, sponsorship or partnership</option><option>Website or domain inquiry</option></select></label>
  <label>Message<textarea name="message" required></textarea></label>
  ''' + CONSENT + '''<button class="btn" type="submit">Send message</button><p class="form-status" aria-live="polite"></p>
 </form></div>
 <div>
  <div class="panel sun"><h3>Website, domain, sponsorship or partnership</h3><p class="mb0">For interest in this website, the Flex.Work domain name, sponsorship, advertising or partnership, <a href="''' + OWNER + '''" target="_blank" rel="noopener">contact the owner directly</a>.</p></div>
  <div class="panel mt5"><h3>Prefer email?</h3><p><a href="#" data-mail="Flex.Work inquiry">Email the Flex.Work team</a> — the link opens your email app.</p><h3>Quick links</h3><ul class="mb0"><li><a href="{root}employers.html#post">Post a flexible role</a></li><li><a href="{root}talent.html">Join the talent network</a></li><li><a href="{root}advertise.html">Advertising and sponsorship</a></li><li><a href="{root}support.html">Support the site</a></li></ul></div>
 </div>
</div></section>'''

# ---------------------------------------------------------------- legal
def legal_wrap(title, lede, crumb, html):
    return ph(title, lede, crumb) + f'<section class="section" style="padding-top:0"><div class="wrap"><div class="prose">{html}</div></div></section>'

def privacy():
    return legal_wrap("Privacy and cookie policy", "How Flex.Work collects, uses and protects information. Last updated October 2026.", "Privacy", '''
<h2>Who we are</h2><p>Flex.Work (&ldquo;we&rdquo;) operates the website flex.work. You can reach us through our <a href="{root}contact.html">contact page</a>.</p>
<h2>Information we collect</h2><ul><li><strong>Information you give us</strong> through forms: name, email, and the details you choose to share (for example arrangement preferences, skills, company and role details, contest entries).</li><li><strong>Information collected automatically</strong>: standard server logs and, through third-party services such as Google AdSense, cookies and similar technologies that record device and usage information.</li><li><strong>Tool inputs</strong>: calculators and generators run in your browser. We do not receive what you type into them.</li></ul>
<h2>How we use it</h2><ul><li>To reply to messages and process listings, pledges, applications and contest entries.</li><li>To match talent-network members with relevant roles, with consent.</li><li>To send newsletters and alerts you&rsquo;ve asked for. Every email includes a way to unsubscribe.</li><li>To keep the site secure and improve it.</li><li>To show advertising that funds the site.</li></ul>
<h2>Form processing</h2><p>Form submissions are delivered to us by a third-party form-relay service (FormSubmit), which processes the data only to deliver it.</p>
<h2 id="cookies">Cookies and advertising</h2><p>We use Google AdSense to show ads. Third-party vendors, including Google, use cookies to serve ads based on your previous visits to this and other websites. Google&rsquo;s use of advertising cookies enables it and its partners to serve ads based on your visits to this site and other sites on the internet.</p><p>You can opt out of personalised advertising by visiting <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a>, or opt out of some third-party vendors&rsquo; use of cookies at <a href="https://www.aboutads.info/choices/" target="_blank" rel="noopener">aboutads.info</a>. Learn more in <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">how Google uses information from sites that use its services</a>.</p><p>Visitors in the European Economic Area, the UK and Switzerland are shown a consent message, provided through Google&rsquo;s certified consent management, before personalised ads are used. Our own cookie notice stores your choice in your browser.</p>
<h2>Embedded videos</h2><p>Videos are embedded from YouTube in privacy-enhanced mode and load only when you press play. YouTube may then set cookies under Google&rsquo;s policies.</p>
<h2>Sharing</h2><p>We don&rsquo;t sell personal data. With a talent-network member&rsquo;s consent, we share relevant profile details with a matched employer. We use service providers (hosting, form relay, email) who process data on our behalf.</p>
<h2>Retention</h2><p>We keep personal data only as long as needed for the purposes above, then delete it. Talent-network profiles are deleted on request.</p>
<h2>Your rights</h2><p>Depending on where you live, you may have rights to access, correct, delete or export your data, object to processing, or withdraw consent. Contact us to exercise them. You may also complain to your local data-protection authority.</p>
<h2>Children</h2><p>Flex.Work is intended for adults and is not directed at children under 16.</p>
<h2>Changes</h2><p>We&rsquo;ll update this page if our practices change.</p>''')

def terms():
    return legal_wrap("Terms of use", "The rules for using Flex.Work. Last updated October 2026.", "Terms", '''
<h2>Using the site</h2><p>By using Flex.Work you agree to these terms. If you don&rsquo;t agree, please don&rsquo;t use the site.</p>
<h2>Information, not advice</h2><p>Content and tools are general information. They are not legal, tax, financial, immigration or employment advice. Calculator results are estimates. Check with a qualified professional before acting.</p>
<h2>Role profiles and listings</h2><p>Role profiles in the explorer are editorial assessments, not job offers. Employer listings are provided by employers, who are responsible for their accuracy and legality. We review listings but cannot guarantee any employer, role or outcome.</p>
<h2>Your submissions</h2><p>You confirm that information you submit is accurate and that you have the right to share it. You grant us permission to use it to provide the service you requested. For contest entries, see the contest rules.</p>
<h2>Acceptable use</h2><p>Don&rsquo;t misuse the site: no spam, scraping that harms performance, attempts to break security, fraudulent listings, or listings that charge applicants.</p>
<h2>Payments</h2><p>Paid listings, sponsorships and contributions are confirmed individually by email before payment, through a secure third-party payment provider. Contributions support Flex.Work as a business and are not charitable donations.</p>
<h2>Intellectual property</h2><p>Flex.Work&rsquo;s original text, design, tools and code are protected by copyright. You may quote short extracts with a link. Third-party trademarks belong to their owners. See the <a href="{root}trademark.html">trademark and copyright disclosure</a>.</p>
<h2>External links</h2><p>We link to other websites for reference. We aren&rsquo;t responsible for their content or practices.</p>
<h2>Liability</h2><p>The site is provided &ldquo;as is.&rdquo; To the extent permitted by law, we are not liable for losses arising from use of the site, its tools or third-party listings.</p>
<h2>Changes</h2><p>We may update these terms. Continued use means you accept the updated terms.</p>''')

def disclaimer():
    return legal_wrap("Disclaimer", "Important limits on the information and tools on Flex.Work.", "Disclaimer", '''
<p>Flex.Work publishes general information about flexible work. It is not a substitute for advice from a qualified lawyer, accountant, financial adviser, immigration adviser or HR professional.</p>
<h2>Tools and calculators</h2><p>Results from our tools are estimates based on the numbers you enter and simplified assumptions. They don&rsquo;t account for every personal, legal or tax circumstance.</p>
<h2>Statistics</h2><p>We link every statistic to its source and check figures at the time of writing. Data can change after publication.</p>
<h2>Employers and roles</h2><p>We don&rsquo;t endorse any employer and can&rsquo;t guarantee employment. Always verify an employer independently — see our <a href="{root}guides/remote-job-scams.html">scam guide</a>.</p>
<h2>Advertising</h2><p>Ads are served by Google AdSense and labelled where we place them. An ad appearing on Flex.Work is not an endorsement.</p>
<h2>Videos and external links</h2><p>Embedded videos and linked sites belong to their creators. We don&rsquo;t control or endorse their content.</p>''')

def trademark():
    return legal_wrap("Trademark and copyright disclosure", "How Flex.Work relates to other brands, and who owns what on this site.", "Trademark and copyright", '''
<h2>Independence from similarly named companies</h2><p>Flex.Work is an independent publication operating at the domain flex.work. It is <strong>not affiliated with, endorsed by, sponsored by or connected to</strong> FlexJobs, Flexwork, FlexWork, Flex Work or any other company, product or service with a similar name. Any similarity of name is coincidental and descriptive: &ldquo;flex work&rdquo; is a common phrase describing flexible working arrangements.</p>
<p>We use the name &ldquo;Flex.Work&rdquo; — written with the dot, as our domain name — to identify this website. We do not claim rights in the generic phrase &ldquo;flexible work&rdquo; or &ldquo;flex work,&rdquo; and we do not intend to cause confusion with any registered trademark. If you believe any content on this site infringes your trademark, contact us and we will review it promptly.</p>
<h2>Third-party names and trademarks</h2><p>Company, product and organisation names mentioned on this site — including those of research organisations, video channels, software and job platforms — are trademarks of their respective owners. They are used only to identify those organisations and their work, for reference and commentary. Their mention does not imply endorsement or affiliation.</p>
<h2>Copyright in this site</h2><p>&copy; Flex.Work. The original text, guides, role profiles, tools, calculators, code, layout and graphics on this site are original works protected by copyright. You may share links and quote short passages with attribution and a link to the source page. Please don&rsquo;t republish whole guides or copy the tools without permission.</p>
<h2>Third-party content</h2><ul><li><strong>Statistics</strong> are summarised in our own words with links to the original publishers, who own the underlying research.</li><li><strong>Videos</strong> are embedded through YouTube&rsquo;s official embed player and remain the property of their creators and channels.</li><li><strong>Fonts</strong> (Bricolage Grotesque and Hanken Grotesk) are used under the SIL Open Font License, served by Google Fonts.</li></ul>
<h2>Reporting a concern</h2><p>If you believe material on Flex.Work infringes your copyright or trademark, send us the details through the <a href="{root}contact.html">contact page</a>, including the page address and the work concerned. We will respond promptly and remove material where appropriate.</p>''')

def thanks():
    return '''<section class="section"><div class="wrap measure"><h1>Thank you — it&rsquo;s on its way</h1><p class="lede">We received your <strong id="ty-form">submission</strong> and will reply within two business days.</p><p>While you wait:</p><ul><li><a href="{root}tools/index.html">Try the free tools</a></li><li><a href="{root}guides/index.html">Read the guides</a></li><li><a href="{root}jobs.html">Explore flexible roles</a></li></ul><a class="btn mt5" href="{root}index.html">Back to home</a></div></section>'''

def notfound():
    return '''<section class="section"><div class="wrap measure"><h1>This page took a flexible day off</h1><p class="lede">The page you&rsquo;re looking for doesn&rsquo;t exist or has moved.</p><div class="split"><a class="btn" href="/index.html">Go to home</a><a class="btn ghost" href="/tools/index.html">Browse tools</a><a class="btn ghost" href="/guides/index.html">Read guides</a></div></div></section>'''
