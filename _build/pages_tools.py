from layout import ad
from pages_home import tool_tiles

def head(title, lede, crumb):
    return f'''<div class="wrap page-head"><div class="crumbs"><a href="{{root}}index.html">Home</a> / <a href="{{root}}tools/index.html">Tools</a> / {crumb}</div><h1>{title}</h1><p class="lede">{lede}</p></div>'''

def explain(html):
    return f'<section class="section white"><div class="wrap"><div class="prose">{html}</div></div></section>'

CTA = '''<section class="section"><div class="wrap grid-2" style="align-items:center"><div><h2>Ready for a role that works this way?</h2><p class="lede">Join the free talent network and we&rsquo;ll match you with employers who state their flexibility upfront.</p></div><div class="split"><a class="btn" href="{root}talent.html">Join the talent network</a><a class="btn ghost" href="{root}tools/index.html">More tools</a></div></div></section>'''

_QN = [0]
def q(dim, text, opts):
    _QN[0] += 1
    name = "q" + str(_QN[0])
    o = "".join(f'<label class="chip"><input type="radio" name="{name}" value="{v}" required><span>{t}</span></label>' for t, v in opts)
    return f'<fieldset data-dim="{dim}" class="panel flat"><legend>{text}</legend><div class="chips">{o}</div></fieldset>'

FREQ = [("Rarely", 0), ("Sometimes", 1), ("Usually", 2), ("Always", 3)]

def quiz():
    qs = [
        ("focus", "I start work without anyone checking on me.", FREQ),
        ("focus", "I can keep my attention on one task for an hour or more.", FREQ),
        ("focus", "I hit deadlines that nobody reminds me about.", FREQ),
        ("comms", "I explain problems clearly in writing.", FREQ),
        ("comms", "I ask for help early when I'm blocked.", FREQ),
        ("setup", "I have a quiet place to work where I won't be interrupted.", [("No", 0), ("Shared space", 1), ("Mostly", 2), ("Yes, dedicated", 3)]),
        ("setup", "My internet is reliable enough for video calls.", [("No", 0), ("Patchy", 1), ("Mostly", 2), ("Always", 3)]),
        ("social", "I feel fine going a whole day without seeing colleagues in person.", FREQ),
        ("social", "I have people outside work I see regularly.", FREQ),
        ("routine", "I stop work at a set time.", FREQ),
        ("routine", "I keep a regular daily routine on non-office days.", FREQ),
        ("routine", "I can switch off notifications without anxiety.", FREQ),
    ]
    _QN[0] = 0
    fields = "".join(q(*x) for x in qs)
    return head("Flex readiness quiz", "Twelve quick questions that show which flexible arrangement suits the way you work — and what to improve first.", "Flex readiness quiz") + f'''
<div class="wrap tool-ui" style="padding-bottom:48px">
 <form id="quiz" class="form">{fields}<button class="btn" type="submit">See my result</button><p class="form-status err" id="quiz-msg" aria-live="polite"></p></form>
 <div class="toc"><div class="result" id="quiz-result" hidden aria-live="polite">
  <h3>Your flex readiness</h3><div class="big" id="quiz-score">0%</div><div class="meter"><i></i></div>
  <h3 id="quiz-band" class="mt4"></h3><p id="quiz-text"></p><dl id="quiz-dims"></dl>
  <a class="btn mari sm mt5" href="{{root}}talent.html">Find roles that fit</a>
 </div><div class="panel flat mt5"><h3>How it&rsquo;s scored</h3><p class="mb0 small">Each answer scores 0–3 across five areas that research and remote-first companies consistently link to success in flexible work: focus, written communication, home setup, social energy and routines. Your answers stay in your browser.</p></div></div>
</div>''' + ad("display") + explain('''<h2>What your score means</h2>
<p><strong>80% and above — fully remote ready.</strong> You have the habits remote-first employers screen for. Say so explicitly in applications and interviews, with examples.</p>
<p><strong>60–79% — hybrid sweet spot.</strong> Two or three home days with a predictable anchor day suits you. Work on your lowest area before going fully remote.</p>
<p><strong>40–59% — flex-curious.</strong> Start with a trial: one home day, flexitime or a compressed fortnight. Build routines first.</p>
<p><strong>Below 40% — structure first.</strong> You get energy from in-person structure. Part-time, shift choice or compressed hours may suit you better than remote work.</p>
<h2>Improve your weakest area</h2>
<ul><li><strong>Focus:</strong> time-block your calendar and close chat during focus blocks.</li><li><strong>Communication:</strong> end every message with the ask and the deadline.</li><li><strong>Setup:</strong> see our <a href="../guides/home-office-setup.html">home office guide</a>.</li><li><strong>Social:</strong> schedule regular coworking or meetups.</li><li><strong>Routine:</strong> use a fixed start and shutdown ritual.</li></ul>''') + CTA

def commute():
    return head("Commute savings calculator", "See how many hours, how much money and how much CO₂ you get back for every day you don&rsquo;t commute.", "Commute savings") + '''
<div class="wrap tool-ui" id="commute" style="padding-bottom:48px">
 <div class="panel"><div class="form">
  <div class="two"><label>One-way commute (minutes)<input id="cm-min" type="number" min="0" value="40"></label><label>Home days per week<input id="cm-days" type="number" min="0" max="7" step="0.5" value="2"></label></div>
  <div class="two"><label>Working weeks a year<input id="cm-weeks" type="number" min="1" max="52" value="46"></label><label>How you commute<select id="cm-mode"><option value="car">Petrol or diesel car</option><option value="ev">Electric car</option><option value="motorbike">Motorbike</option><option value="transit">Bus or train</option><option value="bike">Bike or walk</option></select></label></div>
  <div class="two"><label>One-way distance (km)<input id="cm-km" type="number" min="0" value="20"></label><label>Travel cost per km ($)<input id="cm-cpk" type="number" min="0" step="0.01" value="0.30"></label></div>
  <div class="two"><label>Other costs per office day ($)<input id="cm-other" type="number" min="0" value="15"></label><label>Value of your time ($/hour)<input id="cm-wage" type="number" min="0" value="30"></label></div>
  <p class="small muted mb0">&ldquo;Other costs&rdquo; covers parking, lunch and coffee. Use a transit fare by setting cost per km to the fare &divide; distance.</p>
 </div></div>
 <div class="result" aria-live="polite"><h3>Every year you get back</h3><div class="big" id="cm-hours">0 h</div><p>That&rsquo;s <strong id="cm-days-back">0</strong> eight-hour days.</p>
  <dl><dt>Travel and day costs saved</dt><dd id="cm-cost">$0</dd><dt>Value of time saved</dt><dd id="cm-value">$0</dd><dt>CO₂ avoided</dt><dd id="cm-co2">0 kg</dd><dt>Total value</dt><dd id="cm-total">$0</dd></dl>
  <a class="btn mari sm mt5" href="{root}tools/flexible-work-request-letter.html">Use this in a request</a></div>
</div>''' + ad("display") + explain('''<h2>How the numbers work</h2>
<p>Hours saved = round-trip minutes &times; home days per week &times; working weeks &divide; 60. Costs saved = (round-trip distance &times; cost per km + other daily costs) &times; home days a year. The time value multiplies hours saved by the hourly value you enter.</p>
<p>CO₂ uses approximate per-km factors: 0.17 kg for a petrol or diesel car, 0.11 kg for a motorbike, 0.05 kg for an electric car (varies with the power grid), 0.04 kg for public transport and zero for cycling or walking. Treat results as estimates.</p>
<h2>Why it matters</h2>
<p>Owl Labs&rsquo; 2024 research found hybrid workers spend about $61 on an office day versus $19 at home. Two home days a week can add up to thousands of dollars and more than a working week of time each year — useful evidence in a <a href="../guides/how-to-ask-for-flexible-work.html">flexible-work request</a>.</p>''') + CTA

def rate():
    return head("Freelance rate calculator", "Work back from the income you need to the minimum hourly and day rate you should charge.", "Freelance rate") + '''
<div class="wrap tool-ui" id="rate" style="padding-bottom:48px">
 <div class="panel"><div class="form">
  <div class="two"><label>Take-home income you want per year ($)<input id="rt-income" type="number" min="0" value="70000"></label><label>Business expenses per year ($)<input id="rt-exp" type="number" min="0" value="8000"></label></div>
  <div class="two"><label>Tax and social contributions (%)<input id="rt-tax" type="number" min="0" max="70" value="28"></label><label>Profit buffer (%)<input id="rt-profit" type="number" min="0" max="100" value="10"></label></div>
  <div class="two"><label>Weeks off (holidays, sickness, gaps)<input id="rt-off" type="number" min="0" max="40" value="8"></label><label>Working hours per week<input id="rt-hours" type="number" min="1" max="80" value="40"></label></div>
  <label>Billable share of your hours (%)<input id="rt-bill" type="number" min="5" max="100" value="60"></label>
  <p class="small muted mb0">Expenses include software, equipment, insurance, accounting, coworking and pension contributions.</p>
 </div></div>
 <div class="result" aria-live="polite"><h3>Minimum hourly rate</h3><div class="big" id="rt-hourly">$0</div>
  <dl><dt>Day rate (8 hours)</dt><dd id="rt-day">$0</dd><dt>40-hour project</dt><dd id="rt-proj">$0</dd><dt>Revenue needed per year</dt><dd id="rt-gross">$0</dd><dt>Revenue needed per month</dt><dd id="rt-month">$0</dd><dt>Billable hours per year</dt><dd id="rt-billable">0 h</dd></dl>
  <a class="btn mari sm mt5" href="{root}guides/freelancing-starter-guide.html">Read the freelancing guide</a></div>
</div>''' + ad("display") + explain('''<h2>How it works</h2>
<p>Revenue needed = (take-home income + expenses) &divide; (1 &minus; tax rate), plus your profit buffer. Billable hours = (52 &minus; weeks off) &times; weekly hours &times; billable share. Your minimum hourly rate is revenue needed &divide; billable hours.</p>
<h2>Why freelancers undercharge</h2>
<p>Most people compare a freelance rate with their old salary divided by 2,080 hours. That ignores unpaid holidays, sick days, admin and sales time, and the taxes and benefits an employer used to pay. A 60% billable share is typical for established freelancers; new ones are often lower.</p>
<p>This is a planning tool, not tax advice. Check your actual tax rate with a local accountant.</p>''') + CTA

def fourday():
    return head("Four-day week calculator", "Compare four-day week models and see your daily hours, effective hourly pay and extra days off a year.", "Four-day week") + '''
<div class="wrap tool-ui" id="fourday" style="padding-bottom:48px">
 <div class="panel"><div class="form">
  <label>Model<select id="fd-model"><option value="100">100-80-100 (full pay, fewer hours)</option><option value="compressed">Compressed (same hours, four days)</option><option value="nineeighty">9/80 (every other Friday off)</option><option value="pro">Pro-rata four days (80% hours, 80% pay)</option></select></label>
  <div class="two"><label>Current hours per week<input id="fd-hours" type="number" min="1" max="80" value="40"></label><label>Current salary per year ($)<input id="fd-salary" type="number" min="0" value="60000"></label></div>
  <label>Day off<select id="fd-start"><option value="4">Friday</option><option value="0">Monday</option><option value="2">Wednesday</option></select></label>
  <p class="small muted mb0" id="fd-desc"></p>
 </div>
 <div class="days mt5" id="fd-week" style="grid-template-columns:repeat(7,1fr)"></div></div>
 <div class="result" aria-live="polite"><h3>Your new week</h3><div class="big" id="fd-weekly">0 h</div><p>hours per week, <strong id="fd-perday">0 h</strong> per working day</p>
  <dl><dt>Salary</dt><dd id="fd-pay">$0</dd><dt>Effective hourly pay</dt><dd id="fd-hourly">$0</dd></dl><p class="mt4 mb0" id="fd-daysoff"></p>
  <a class="btn mari sm mt5" href="{root}guides/four-day-week-guide.html">Read the four-day week guide</a></div>
</div>''' + ad("display") + explain('''<h2>Which model is right?</h2>
<p><strong>100-80-100</strong> is what most published pilots tested: same pay, about 80% of the time, the same output. It depends on cutting low-value work. <strong>Compressed hours</strong> keeps the same total hours over four days — easy to approve, but long days. <strong>9/80</strong> spreads 80 hours over nine days, a gentle middle ground. <strong>Pro-rata</strong> trades 20% of pay for 20% of time.</p>
<p>In the UK pilot, 89% of participating firms were still running a four-day week a year later. Read the full <a href="../guides/four-day-week-guide.html">four-day week guide</a> for a pilot plan.</p>''') + CTA

def planner():
    return head("Hybrid schedule planner", "Map your team&rsquo;s week, see who is in the office each day and find your best anchor day.", "Hybrid planner") + '''
<div class="wrap" id="planner" style="padding-bottom:48px">
 <div class="panel"><p class="small muted">Click a cell to cycle Office, Home and Off. Edit names directly.</p>
  <div class="planner"><table><thead><tr><th>Person</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th></th></tr></thead><tbody></tbody></table></div>
  <div class="split mt5"><button class="btn ghost sm" id="pl-add" type="button">Add person</button><button class="btn ink sm" id="pl-copy" type="button">Copy schedule</button></div>
 </div>
 <div class="tool-ui mt5"><div class="result" aria-live="polite"><h3>Best anchor day</h3><div class="big" id="pl-anchor">—</div><p id="pl-note"></p></div>
 <div class="panel"><h3>Office attendance by day</h3><dl id="pl-sum" style="display:grid;grid-template-columns:1fr auto;gap:8px 16px;margin:0"></dl></div></div>
</div>''' + ad("display") + explain('''<h2>Choosing an anchor day</h2>
<p>An anchor day is when the whole team is in the office together. Put planning, workshops, one-to-ones and social time there, and leave focus work for home days. Most teams settle on one or two anchor days mid-week.</p>
<p>Gallup found in 2025 that only 11% of employees are on teams that set their hybrid policy together. Planning the schedule as a team — with this tool — is a simple way to fix that. Compare models in <a href="../guides/hybrid-schedules-compared.html">hybrid schedules compared</a>.</p>''') + CTA

def letter():
    return head("Flexible work request letter generator", "Answer a few questions and get a clear, trial-based request your manager can say yes to.", "Request letter") + '''
<div class="wrap tool-ui" id="letter" style="padding-bottom:48px">
 <div class="panel no-print"><div class="form">
  <div class="two"><label>Your name<input id="lt-name" autocomplete="name"></label><label>Manager&rsquo;s name<input id="lt-mgr"></label></div>
  <div class="two"><label>Your role<input id="lt-role" placeholder="e.g. Senior accountant"></label><label>Arrangement<select id="lt-type"><option value="hybrid">Hybrid</option><option value="remote">Fully remote</option><option value="compressed">Compressed hours</option><option value="fourday">Four-day week</option><option value="parttime">Part-time hours</option><option value="flexi">Flexitime</option><option value="jobshare">Job-share</option></select></label></div>
  <label>Proposed schedule<input id="lt-detail" placeholder="e.g. home on Monday and Friday, office Tuesday to Thursday"></label>
  <div class="two"><label>Start date<input id="lt-start" placeholder="e.g. 1 December"></label><label>Trial period<select id="lt-trial"><option>eight-week</option><option>four-week</option><option>twelve-week</option><option value="none">No trial</option></select></label></div>
  <label>Why it works for the team<textarea id="lt-why" placeholder="e.g. Fewer interruptions on home days would let me finish month-end reports faster."></textarea></label>
  <label>How work will be covered (optional)<textarea id="lt-cover" placeholder="e.g. I'll keep 9:30–16:00 core hours and attend every client meeting in person."></textarea></label>
  <label>Tone<select id="lt-tone"><option value="friendly">Friendly</option><option value="formal">Formal</option></select></label>
 </div></div>
 <div><div class="output-doc" id="lt-out" aria-live="polite"></div>
 <div class="split mt4 no-print"><button class="btn" id="lt-copy" type="button">Copy letter</button><button class="btn ghost" id="lt-dl" type="button">Download .txt</button><button class="btn ghost" id="lt-print" type="button">Print</button></div></div>
</div>''' + ad("display") + explain('''<h2>Why this structure works</h2>
<p>Managers approve requests when they can see the risk is handled. This letter leads with the arrangement and start date, explains the benefit to the team, shows how work and meetings will be covered, and proposes a reversible trial with a review. Read the full method in <a href="../guides/how-to-ask-for-flexible-work.html">how to ask for flexible work</a>.</p>
<p>Strengthen your case with numbers from the <a href="commute-savings-calculator.html">commute savings calculator</a> and published research on our <a href="../resources.html">resources page</a>. Everything you type stays in your browser.</p>''') + CTA

def tz():
    sel = "".join(f'<label>Location {i+1}<select class="tz-sel"></select></label>' for i in range(4))
    return head("Time-zone overlap finder", "See the working hours your distributed team shares — and plan meetings and handoffs around them.", "Time-zone overlap") + f'''
<div class="wrap" id="tz" style="padding-bottom:48px">
 <div class="panel"><div class="form"><div class="grid-4">{sel}</div><div class="two" style="max-width:420px"><label>Workday starts<input id="tz-start" type="number" min="0" max="23" value="9"></label><label>Workday ends<input id="tz-end" type="number" min="1" max="24" value="17"></label></div></div></div>
 <div class="tool-ui mt5"><div class="result" aria-live="polite"><h3>Shared working hours</h3><div class="big" id="tz-hours">0 h</div><p id="tz-msg" class="mb0"></p></div>
 <div class="panel"><h3>Reading the grid</h3><p class="small mb0">Each row is a location; each column is one hour in Location 1&rsquo;s time. Dark green cells are working hours, light green are one hour either side, and outlined cells are overlap for everyone. Hover a cell for local time.</p></div></div>
 <div class="panel mt5 tz-grid" id="tz-grid"></div>
</div>''' + ad("display") + explain('''<h2>Making little overlap work</h2>
<p>Two to three shared hours is enough for most teams if you use them only for live discussion. Move status updates, reviews and decisions into writing — see our <a href="../guides/async-communication.html">async communication guide</a>. When there is no overlap at all, rotate meeting times so the same people aren&rsquo;t always up early or late.</p>''') + CTA

def policy():
    types = ["Remote work", "Hybrid work", "Flexitime around core hours", "Compressed hours", "Four-day week", "Part-time hours", "Job-sharing", "Temporary remote work for caring or relocation"]
    chips = "".join(f'<label class="chip"><input type="checkbox" name="pb-types" value="{t}" {"checked" if i < 3 else ""}><span>{t}</span></label>' for i, t in enumerate(types))
    return head("Flex policy builder", "Generate a complete, twelve-section flexible work policy for your company in a few clicks.", "Policy builder") + f'''
<div class="wrap tool-ui" id="policy" style="padding-bottom:48px">
 <div class="panel no-print"><div class="form">
  <div class="two"><label>Company name<input id="pb-org"></label><label>Effective date<input id="pb-date" placeholder="e.g. 1 January 2027"></label></div>
  <label>Working model<select id="pb-model"><option value="hybrid">Structured hybrid</option><option value="remote">Remote-first</option><option value="flexible">Team-led flexibility</option><option value="office">Office-based with options</option></select></label>
  <div class="two"><label>Anchor days (optional)<input id="pb-anchor" placeholder="e.g. Tuesday and Thursday"></label><label>Core hours<input id="pb-core" value="10:00–15:00"></label></div>
  <fieldset><legend>Arrangements offered</legend><div class="chips">{chips}</div></fieldset>
  <div class="two"><label>Location rule<select id="pb-loc"><option value="country">Within country of contract</option><option value="region">Within state or province</option><option value="anywhere">Anywhere approved</option></select></label><label>Equipment<select id="pb-equip"><option value="stipend">Laptop plus stipend</option><option value="provided">Company provides equipment</option><option value="byod">Bring your own device</option></select></label></div>
  <div class="two"><label>Stipend amount (optional)<input id="pb-stipend" placeholder="e.g. $500 one-off"></label><label>Trial length<select id="pb-review"><option>three-month</option><option>six-week</option><option>six-month</option></select></label></div>
 </div></div>
 <div><div class="output-doc" id="pb-out" aria-live="polite"></div><div class="split mt4 no-print"><button class="btn" id="pb-copy" type="button">Copy policy</button><button class="btn ghost" id="pb-dl" type="button">Download .txt</button><a class="btn ink" href="{{root}}employers.html#post">Hire for this policy</a></div></div>
</div>''' + ad("display") + explain('''<h2>What a good policy does</h2>
<p>It makes flexibility consistent across managers, clear for employees and defensible for the company. Read <a href="../guides/writing-a-flexible-work-policy.html">how to write a flexible work policy</a> for the reasoning behind each section and the most common mistakes.</p>
<p>This template is general information, not legal advice. Employment law differs by country, state and province, so have your final policy reviewed locally.</p>''')

def index():
    return '''<div class="wrap page-head"><div class="crumbs"><a href="{root}index.html">Home</a> / Tools</div><h1>Free flexible work tools</h1><p class="lede">Calculators and generators for job seekers, freelancers, managers and HR teams. No sign-up, and your inputs stay in your browser.</p></div>
<section class="section" style="padding-top:0"><div class="wrap"><div class="grid-4">''' + tool_tiles("tools/") + '''</div></div></section>''' + ad("display") + CTA

TOOL_PAGES = [
    ("tools/index.html", "Free flexible work tools — calculators and generators | Flex.Work", "Free tools for flexible work: readiness quiz, commute savings, freelance rate, four-day week, hybrid planner, time-zone overlap, request letter and policy builder.", index),
    ("tools/flex-readiness-quiz.html", "Flex readiness quiz: is remote or hybrid work right for you? | Flex.Work", "Take the free 12-question flex readiness quiz to see whether remote, hybrid or another flexible arrangement suits how you work.", quiz),
    ("tools/commute-savings-calculator.html", "Commute savings calculator — time, money and CO2 | Flex.Work", "Calculate the hours, money and CO2 you save each year by working from home on some days.", commute),
    ("tools/freelance-rate-calculator.html", "Freelance rate calculator — hourly and day rate | Flex.Work", "Work out the minimum hourly and day rate you need to charge as a freelancer to hit your income goal.", rate),
    ("tools/four-day-week-calculator.html", "Four-day week calculator — 100-80-100, compressed and 9/80 | Flex.Work", "Compare four-day week models and see daily hours, effective hourly pay and extra days off.", fourday),
    ("tools/hybrid-schedule-planner.html", "Hybrid schedule planner — find your team's anchor day | Flex.Work", "Plan your team's hybrid week, see office attendance by day and find the best anchor day.", planner),
    ("tools/flexible-work-request-letter.html", "Flexible work request letter generator | Flex.Work", "Generate a clear, persuasive flexible working request letter with a trial period, ready to send to your manager.", letter),
    ("tools/time-zone-overlap.html", "Time-zone overlap finder for remote teams | Flex.Work", "Find shared working hours across up to four time zones for distributed and remote teams.", tz),
    ("tools/flex-policy-builder.html", "Flexible work policy builder — free template | Flex.Work", "Build a complete flexible work policy for your company: model, arrangements, core hours, location, equipment and fairness.", policy),
]
