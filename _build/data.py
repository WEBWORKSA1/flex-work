"""Verified data used across pages. Every stat was read on the cited page during research (Oct 2026)."""

STATS = [
    ("54%", "of remote-capable US employees work hybrid; 25% are fully remote.", "Gallup, Aug 2026", "https://www.gallup.com/401384/indicator-hybrid-work.aspx"),
    ("66%", "of US companies offer some location flexibility, with 2.87 required office days on average.", "Flex Index Q3 2025 (LSE)", "https://www.lse.ac.uk/management/assets/documents/research/flex-index-reports/Flex-Report-Q3-2025.pdf"),
    ("35%", "of employed Americans did some or all of their work at home on days they worked.", "US BLS, American Time Use Survey 2025", "https://www.bls.gov/news.release/atus.nr0.htm"),
    ("37%", "of workers would reject a job that didn't offer flexible hours.", "Owl Labs State of Hybrid Work 2025", "https://www.businesswire.com/news/home/20250922965079/en/Owl-Labs-2025-State-of-Hybrid-Work-Report-Finds-the-New-Frontier-of-Flexibility-is-When-Employees-Work-Not-Where"),
    ("$61", "spent per office day by hybrid workers, versus $19 on a home day.", "Owl Labs 2024", "https://owllabs.com/state-of-hybrid-work/2024"),
    ("46%", "of remote-capable workers say they'd be unlikely to stay if remote work ended.", "Pew Research, Jan 2025", "https://www.pewresearch.org/short-reads/2025/01/13/many-remote-workers-say-theyd-be-likely-to-leave-their-job-if-they-could-no-longer-work-from-home"),
    ("64M", "Americans freelanced in 2023 — 38% of the workforce.", "Upwork Freelance Forward 2023", "https://investors.upwork.com/news-releases/news-release-details/upwork-study-finds-64-million-americans-freelanced-2023-adding"),
    ("89%", "of UK four-day-week pilot firms were still running it a year later.", "Autonomy pilot follow-up, via HRD Connect, Feb 2024", "https://www.hrdconnect.com/2024/02/26/one-year-on-uks-4-day-work-week-trial-has-been-a-success/"),
]

MORE_STATS = [
    ("61% of remote-capable US employees prefer hybrid, 33% prefer fully remote and 6% prefer on-site.", "Gallup, Nov 2025", "https://www.gallup.com/401384/indicator-hybrid-work.aspx"),
    ("Only 11% of employees are on teams that set their hybrid policy together.", "Gallup, May 2025", "https://www.gallup.com/401384/indicator-hybrid-work.aspx"),
    ("About a quarter of paid US workdays were worked from home in late 2025.", "WFH Research (SWAA), Dec 2025", "https://wfhresearch.com/wp-content/uploads/2025/12/WFHResearch_updates_December2025.pdf"),
    ("Workers say they would accept a 9% pay cut for flexible hours and 8% for a four-day week.", "Owl Labs 2025", "https://www.businesswire.com/news/home/20250922965079/en/Owl-Labs-2025-State-of-Hybrid-Work-Report-Finds-the-New-Frontier-of-Flexibility-is-When-Employees-Work-Not-Where"),
    ("40% of US workers were fully or partly remote in 2024, and 17% of recent quitters cited changes to work arrangements.", "McKinsey American Opportunity Survey, May 2025", "https://www.mckinsey.com/industries/real-estate/our-insights/flexible-works-enduring-appeal-affects-workers-employers-and-real-estate"),
    ("71% of US teleworkers say working from home helps their work-life balance.", "Pew Research, 2023", "https://www.pewresearch.org/short-reads/2023/03/30/about-a-third-of-us-workers-who-can-work-from-home-do-so-all-the-time/"),
    ("98% of remote workers want to work remotely at least part of the time for the rest of their careers.", "Buffer State of Remote Work 2023", "https://buffer.com/state-of-remote-work/2023"),
    ("None of the 41 US and Canadian four-day-week pilot companies returned to five days.", "4 Day Week Global", "https://4dayweek.com/press-releases-posts/no-us-or-canadian-companies-to-return-to-five-days-post-4-day-week-trial"),
    ("28% of working adults in Great Britain work hybrid — 45% of those earning £50k+ versus 8% of those under £20k.", "ONS, Jun 2025", "https://www.ons.gov.uk/employmentandlabourmarket/peopleinwork/employmentandemployeetypes/articles/whohasaccesstohybridworkingreatbritain/latest"),
    ("9% of employed people in the EU usually work from home, up from 5.5% in 2019; Finland leads at 20.5%.", "Eurostat 2025 data, via Remote Work Europe", "https://remoteworkeurope.eu/news/2026/eurostat-2025-wfh-data-9-percent-eu-finland-leads"),
]

# (id, title, channel, topic) — each verified via YouTube oEmbed
VIDEOS = [
    ("oiUyyZPIHyY", "Go ahead, tell your boss you are working from home", "Nicholas Bloom, TEDxStanford", "Remote work"),
    ("pKsQGOILwIY", "The case for working from home", "Nicholas Bloom, TEDxStanford", "Remote work"),
    ("MyVfUaXyyqo", "The case for a 4-day work week", "Juliet Schor, TED", "Four-day week"),
    ("_G5WQ2R8jU8", "A four day week at full pay? Now that's work-life balance", "Craig Errey, TEDxMacquarieUniversity", "Four-day week"),
    ("5XD2kNopsUs", "Why work doesn't happen at work", "Jason Fried, TED", "Focus and async"),
    ("-UV3xm9pZ0g", "The secret to being a successful freelancer", "TED, The Way We Work", "Freelancing"),
    ("R4hUU_ys0cM", "Building successful hybrid teams", "Harvard Business Review, IdeaCast", "Hybrid teams"),
    ("H9-JUHrEgF0", "How to do hybrid meetings right", "Harvard Business Review", "Hybrid teams"),
    ("LaCXmw6vwfc", "How to be more productive", "Harvard Business Review", "Focus and async"),
    ("LtlD0xRM2FM", "Is remote work over? Two experts debate return-to-office mandates", "CNBC Television", "Return to office"),
    ("UHz5IIadnEQ", "Why corporate America is abandoning remote work", "CNBC Make It", "Return to office"),
    ("FhQJjxN68WI", "Stanford professor and work-from-home expert on why your RTO is failing", "HR Executive", "Return to office"),
]

def video_card(v):
    vid, title, ch, topic = v
    return (f'<article class="vid"><button class="vid-frame" data-yt="{vid}" aria-label="Play: {title}"></button>'
            f'<div class="vid-body"><span class="tag ink">{topic}</span><h3 class="mt4">{title}</h3><p>{ch}</p></div></article>')

def stat_block(s):
    big, txt, src, url = s
    return f'<div class="stat"><strong>{big}</strong><p>{txt}</p><cite><a href="{url}" target="_blank" rel="noopener nofollow">{src}</a></cite></div>'
