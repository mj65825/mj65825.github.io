"""Generates the static pages. Run: python build.py"""
import os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
NAME = "Melvin Jackson"
LINKEDIN = "https://www.linkedin.com/in/melvin-jackson/"
GITHUB = "https://github.com/mj65825"
EMAIL = "melvin11jackson@gmail.com"
REPO = GITHUB + "/cybersecurity-portfolio"
RESUME = "MelvinJackson_Cybersecurity_Resume.pdf"

ICONS = {
    "home": '<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/>',
    "about": '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-7 8-7s8 3 8 7"/>',
    "exp": '<path d="M3 7h18v13H3z"/><path d="M8 7V4h8v3"/><path d="M3 13h18"/>',
    "projects": '<path d="M3 4h6v6H3zM15 4h6v6h-6zM3 14h6v6H3zM15 14h6v6h-6z"/>',
    "resume": '<path d="M14 3H6v18h12V7z"/><path d="M14 3v4h4"/><path d="M9 13h6M9 17h6"/>',
    "contact": '<path d="M21 15a2 2 0 0 1-2 2H8l-5 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
}
NAV = [("home", "Home", "index.html"), ("about", "About", "about.html"), ("exp", "Experience", "experience.html"),
       ("projects", "Projects", "projects.html"), ("resume", "Resume", "MelvinJackson_Cybersecurity_Resume.pdf"), ("contact", "Contact", "contact.html")]

LI = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5A2.5 2.5 0 1 1 5 8.5a2.5 2.5 0 0 1-.02-5zM3 9.5h4v11H3zm7 0h3.8v1.6h.06c.53-.9 1.83-1.9 3.77-1.9C21.3 9.2 22 11.5 22 14.3V20.5h-4v-5.5c0-1.32-.02-3-1.83-3-1.83 0-2.11 1.43-2.11 2.9v5.6h-4z"/></svg>'
GH = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5a11.5 11.5 0 0 0-3.64 22.42c.58.11.79-.25.79-.56v-2c-3.2.7-3.87-1.36-3.87-1.36-.53-1.34-1.3-1.7-1.3-1.7-1.05-.72.08-.7.08-.7 1.17.08 1.78 1.2 1.78 1.2 1.04 1.77 2.72 1.26 3.38.96.1-.75.4-1.26.73-1.55-2.55-.29-5.24-1.28-5.24-5.68 0-1.25.45-2.28 1.19-3.08-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.18 1.18a11 11 0 0 1 5.79 0c2.2-1.49 3.17-1.18 3.17-1.18.64 1.59.24 2.76.12 3.05.74.8 1.19 1.83 1.19 3.08 0 4.41-2.7 5.38-5.27 5.67.41.35.77 1.04.77 2.1v3.11c0 .31.21.68.8.56A11.5 11.5 0 0 0 12 .5z"/></svg>'
MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>'
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 5l7 7-7 7"/></svg>'
DOWN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v12M6 10l6 6 6-6M4 20h16"/></svg>'
FAV = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.85em' font-size='90' font-family='monospace' fill='%231E88E5'%3EM%3C/text%3E%3C/svg%3E"


def page(fname, title, desc, body, depth=0):
    p = "../" * depth
    home = p + "index.html"
    secs = [("about", "About"), ("projects", "Projects"), ("experience", "Experience"), ("skills", "Skills"), ("contact", "Contact")]
    links = "".join(f'<a class="nav__link" data-sec="{k}" href="{home if depth else ""}#{k}">{v}</a>' for k, v in secs)
    links += f'<a class="nav__link nav__link--cv" href="{p}cv/">Recruiter view</a>'
    social = (f'<a href="{LINKEDIN}" aria-label="LinkedIn" target="_blank" rel="noopener">{LI}</a>'
              f'<a href="{GITHUB}" aria-label="GitHub" target="_blank" rel="noopener">{GH}</a>'
              f'<a href="mailto:{EMAIL}" aria-label="Email">{MAIL}</a>')
    swatches = "".join(f'<span class="swatch" data-color="{c}" role="button" tabindex="0" aria-label="{c.title()}"></span>' for c in ["gold", "blue", "teal", "violet", "rose", "amber"])
    out = f'''<!doctype html>
<html lang="en" data-theme="dark" data-color="gold">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}" />
<meta property="og:title" content="{html.escape(title)}" />
<meta property="og:description" content="{html.escape(desc)}" />
<link rel="icon" href="{FAV}" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=IBM+Plex+Mono:wght@400;500;600&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="{p}styles.css?v=7" />
<script>try{{var d=document.documentElement,t=localStorage.getItem('theme'),c=localStorage.getItem('color');if(t)d.dataset.theme=t;if(c)d.dataset.color=c}}catch(e){{}}</script>
</head>
<body id="top">
<a class="skip" href="#main">Skip to content</a>
<header class="nav" role="banner">
  <a class="nav__brand" href="{home}" aria-label="Home">Melvin</a>
  <nav class="nav__links" id="navLinks" aria-label="Primary">{links}</nav>
  <a class="nav__resume" href="{p}{RESUME}" download aria-label="Download resume">{DOWN}<span>Resume</span></a>
  <div class="nav__tools">
    <button class="tool nav__menu" id="menuBtn" aria-label="Open menu" aria-expanded="false" aria-controls="navLinks"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
    <button class="tool" id="themeToggle" aria-label="Toggle light/dark"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg></button>
    <button class="tool" id="paletteToggle" aria-label="Theme color"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c1 0 1.5-.7 1.5-1.5 0-.4-.2-.8-.5-1-.3-.3-.5-.6-.5-1 0-.8.7-1.5 1.5-1.5H16c3.3 0 6-2.7 6-6 0-4.7-4.5-8.5-10-8.5z"/></svg></button>
  </div>
  <div class="color-picker" id="colorPicker" role="group" aria-label="Accent color"><span class="color-picker__label">Theme</span>{swatches}</div>
</header>
<main id="main">
{body}
  <div class="wrap">
    <footer class="foot">
      <span>&copy; 2026 {NAME}</span>
      <div class="foot__social">{social}</div>
    </footer>
  </div>
</main>
<button class="to-top" id="toTop" aria-label="Back to top"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 15l7-7 7 7"/></svg></button>
<script src="{p}main.js?v=6"></script>
</body>
</html>
'''
    path = os.path.join(ROOT, fname)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(out)


def head(eyebrow, title, lead=""):
    l = f'<p class="d-lead">{lead}</p>' if lead else ""
    return f'<div class="eyebrow">{eyebrow}</div><h1 class="d-title">{title}</h1>{l}'



# ---------------------------------------------------------------- projects data
PROJECTS = [
    dict(slug="atcap-capstone", title="ATCAP Senior Capstone", tag="Leadership &middot; IT Consulting", tags="leadership",
         desc="Led a five-person team delivering a reliable website, structured job application form, and automated review script for a home healthcare client.",
         foot="2025&ndash;2026", thumb=("code", ["// website uptime", "{ before: ~25%, after: ~99.9% }", "&darr; $248.33/mo &rarr; $23.00/mo"]),
         chips=["Team lead", "Python", "Squarespace", "Business analysis"], links=[("Live site", "https://www.atcaphomehealthcare.com/")],
         src="Projects/ATCAP-Capstone"),
    dict(slug="vuln-labs", title="Vulnerability Assessment Labs", tag="Vulnerability Management", tags="vuln",
         desc="Hands-on scanning with Nmap, Nessus, and OpenVAS. Compared scanner results, found an unpatched CVE, and wrote a report with CVSS scores and remediation steps.",
         foot="LABS &middot; 2026", thumb=("img", "assets/nessus-localhost-scan.jpg"),
         chips=["Nmap", "Nessus", "OpenVAS", "Hack The Box"], links=[], src="Projects/Vulnerability-Assessment-Labs"),
    dict(slug="wireshark", title="Wireshark Traffic Analysis", tag="Detection &middot; Networking", tags="detection",
         desc="SIEM lab analyzing real traffic: Teams calls, DNS, TLS handshakes, and ARP, and what metadata reveals even when traffic is encrypted.",
         foot="LAB &middot; 2026", thumb=("code", ["// capture.filter", "tls.handshake.type == 1", "&rarr; Client Hello &middot; SNI &middot; DNS &middot; ARP"]),
         chips=["Wireshark", "SIEM", "Packet analysis"], links=[], src="Projects/Wireshark-Traffic-Analysis"),
    dict(slug="kiro-dashboard", title="Productivity Dashboard with Amazon Kiro", tag="AWS &middot; AI-assisted dev", tags="ai",
         desc="Built at an AWS workshop with AI-assisted development: Pomodoro timer, task tracker, and live weather.",
         foot="WORKSHOP &middot; 2026", thumb=("img", "assets/dashboard-pomodoro.jpg"),
         chips=["Amazon Kiro", "AWS", "Weather API"], links=[], src="Projects/AWS-Kiro-Dashboard"),
    dict(slug="ai-chatbot", title="Free AI Chatbot", tag="Python &middot; AI", tags="ai",
         desc="Browser-based chatbot with three bot personalities, memory, streaming replies, and save/load. Runs on the free Gemini tier or fully offline with Ollama.",
         foot="PYTHON &middot; MIT &middot; 20 TESTS", thumb=("code", ["$ python app.py", "{ provider: \"gemini\" | \"ollama\", tests: 20 }", "&rarr; streaming &middot; memory &middot; save/load"]),
         chips=["Python", "Gradio", "Gemini API", "Ollama", "pytest"], links=[], src="Projects/AI-Chatbot"),
]

# ---------------------------------------------------------------- project details
def shots(*items):
    return '<div class="shots">' + "".join(f'<img src="../{s}" alt="{a}" loading="lazy">' for s, a in items) + "</div>"

def ul(*items):
    return '<ul class="list">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

BODY = {}
BODY["vuln-labs"] = f'''
      <h2 class="sec">Lab 1: Scanning my own system</h2>
      <p>I ran a full Nmap and Nessus scan of my own machine, reviewed the open ports, and went through the findings. I also read up on real-world vulnerabilities, including Log4Shell and SMB exploits, to see how these issues are used in attacks.</p>
      {shots(("assets/nmap-open-ports.jpg", "Nmap output showing open ports"), ("assets/nessus-localhost-scan.jpg", "Nessus localhost scan results"))}
      {ul("Open ports such as SMB and RPC can be real entry points if they are not secured.", "Even &ldquo;low severity&rdquo; and informational findings show how much information a system gives away.", "Vulnerabilities are not always obvious, and attackers only need one weak spot.")}
      <h2 class="sec">Lab 2: Two scanners on a Windows target</h2>
      <p>On a Hack The Box Academy target I ran Nessus (on Windows) and OpenVAS (on Ubuntu). Each tool found things the other missed, which is a good reminder that relying on a single scanner in a real engagement can leave gaps. I found an unpatched CVE that could have gone unnoticed without a careful read, then wrote a full report covering severity ratings, CVSS scores, and remediation recommendations.</p>
      <div class="callout">Both labs were run only against my own machine or an authorized lab target.</div>'''
BODY["wireshark"] = f'''
      <h2 class="sec">What I did</h2>
      <p>In a SIEM lab I analyzed real network traffic with Wireshark. I tracked a Teams call, web browsing, DNS requests, and secure HTTPS sessions, and picked out specific events: TLS handshakes for secure sessions, ARP traffic showing devices talking on the network, and the DNS lookups behind a Teams call.</p>
      <h2 class="sec">Takeaways</h2>
      {ul("Everyday actions like browsing or video calls leave clear patterns in network traffic.", "Even with encryption, metadata such as IP addresses and timing still gives useful insight.", "Packet analysis is key to understanding how systems communicate and where risks can exist.")}
      <div class="callout">Screenshots are left out because they show a home network&rsquo;s addresses.</div>'''
BODY["kiro-dashboard"] = f'''
      <h2 class="sec">What it does</h2>
      <p>I built this dashboard at an AWS workshop (hosted with GMU NSBE and GMU ColorStack) using Amazon Kiro, an AI-assisted development environment.</p>
      {ul("Pomodoro timer with work, short break, and long break modes", "Task tracker", "Daily motivational quote and a break-time cat fact button", "Real-time weather integration")}
      {shots(("assets/dashboard-pomodoro.jpg", "Dashboard with quote, weather and task tracker"), ("assets/dashboard-tasks.jpg", "Dashboard with Pomodoro timer and task tracker"))}
      <h2 class="sec">Takeaways</h2>
      {ul("Describing what you want in plain language can turn an idea into a working app quickly, but you still need to understand the logic to build and secure it properly.", "Integrating an API like weather makes an application instantly more practical.", "Understanding how these systems are built matters just as much when thinking about their security.")}'''
BODY["ai-chatbot"] = f'''
      <h2 class="sec">What it does</h2>
      <p>A browser-based AI chatbot built from scratch in Python. It costs nothing to run: it uses Google&rsquo;s free Gemini API tier, or a local model through Ollama that never sends data off the machine.</p>
      {ul("<strong>Three switchable bots:</strong> Helpful Assistant, Coding Buddy, and Sarcastic Pirate, each defined by a system prompt.", "<strong>Conversation memory:</strong> the full history is sent with every request.", "<strong>Streaming replies</strong>, a model picker, and save/load of chats as JSON.", "<strong>Plain-English errors</strong> for bad keys, rate limits, and wrong model names.")}
      <h2 class="sec">Security decisions</h2>
      {ul("The API key is read from a gitignored <code>.env</code> file at runtime and is never in the source.", "A small provider interface keeps the app independent of any one AI vendor.", "With Ollama, prompts and replies stay on the local machine.", "Known limits are documented: no login, rate limiting, or prompt-injection filtering, so it is not meant for the public internet.")}
      <h2 class="sec">Testing</h2>
      <p>20 pytest tests run offline with a fake AI backend. They cover message handling, memory across turns, a Gradio 6 message-format bug I tracked down, error messages, bot switching, and save/load.</p>'''
BODY["atcap-capstone"] = f'''
      <div class="callout"><b>Client:</b> ATCAP Home Healthcare Solutions, a home health agency in Woodbridge, VA with 31 employees. <b>Team:</b> M&amp;T Solutions, five people. <b>My role:</b> Team Lead.</div>
      <h2 class="sec">The business problems</h2>
      <table class="t"><tr><th>Area</th><th>Before</th></tr>
        <tr><td>Website</td><td>The WordPress site often returned a fatal error (about 25% uptime). Visitors had to call the office to learn more, costing the receptionist up to about 60 minutes.</td></tr>
        <tr><td>Job applications</td><td>Applicants emailed a resume or walked in. There was no structured way to apply.</td></tr>
        <tr><td>Application review</td><td>The owner reviewed applications by hand, one email at a time, which was repetitive and made it easy to miss new talent.</td></tr></table>
      <h2 class="sec">What we delivered</h2>
      {ul("<strong>A reliable website</strong> on Squarespace.", "<strong>A structured application form</strong> so every application arrives in the same format.", "<strong>An automated review process:</strong> a Python script pulls applicant data from Google Sheets, sorts it by position, and generates structured documents for the owner to review.")}
      <h2 class="sec">How it helped the business</h2>
      <table class="t"><tr><th>Measure</th><th>Before</th><th>After</th></tr>
        <tr><td>Website uptime</td><td>~25%</td><td>~99.9%</td></tr>
        <tr><td>Website monthly cost</td><td>$248.33</td><td>$23.00</td></tr>
        <tr><td>Time on website-error calls</td><td>up to ~60 min</td><td>none</td></tr>
        <tr><td>Application intake</td><td>~1 min, unstructured email</td><td>~0.5 min, structured form</td></tr>
        <tr><td>Application review</td><td>~35 min</td><td>~30 min (estimate from two applications)</td></tr></table>
      <h2 class="sec">Security and testing</h2>
      {ul("Input validation, HTTPS with SSL certificate verification, user authentication, and multi-factor authentication.", "Alpha, Beta, and user acceptance testing. A link failure found in Alpha was fixed and retested, and a script failure found in UAT (Python had to be installed on the office computer) was resolved and confirmed by the sponsor.", "A training session and training materials so the owner can run the process independently.")}
      <h2 class="sec">My role as Team Lead</h2>
      {ul("Led the team across two semesters, including pivots in scope and approach.", "Was the main point of contact with the sponsor and kept her needs at the center of the work.", "Presented the original business process analysis: how the website, application, and review processes worked and what they cost in time and money.", "Defined the areas for improvement and presented the overview of the three technical solutions.")}'''

for p in PROJECTS:
    chips = "".join(f'<span class="chip">{c}</span>' for c in p["chips"])
    btns = "".join(f'<a class="btn btn--primary" href="{u}" target="_blank" rel="noopener">{l} {ARROW}</a>' for l, u in p["links"])
    btns += f'<a class="btn btn--ghost" href="{GITHUB + '/ai-chatbot' if p['slug'] == 'ai-chatbot' else REPO + '/tree/main/' + p['src']}" target="_blank" rel="noopener">View on GitHub</a>'
    body = f'''<section class="wrap detail"><div class="body"><a class="back" href="../index.html#projects">&larr; All projects</a>
      {head(p["tag"], p["title"], p["desc"])}
      <div class="meta">{chips}</div>
      <div class="hero__ctas" style="margin-top:16px;">{btns}</div>{BODY[p["slug"]]}
    </div></section>'''
    page(f'projects/{p["slug"]}.html', f'{p["title"]} — {NAME}', p["desc"], body, depth=1)


# ---------------------------------------------------------------- one-page home
def sec_head(num, title, sub=""):
    s = f'<p class="sec-sub">{sub}</p>' if sub else ""
    return f'<div class="sec-head"><span class="sec-num">{num}</span><div><h2 class="sec-title">{title}</h2>{s}</div></div>'


def xp(date, role, org, bullets):
    li = "".join(f"<li>{b}</li>" for b in bullets)
    return f'<article class="xp"><div class="xp__date">{date}</div><h3 class="xp__role">{role}</h3><div class="xp__org">{org}</div><ul>{li}</ul></article>'


cards = ""
for p in PROJECTS:
    kind, val = p["thumb"]
    if kind == "img":
        th = f'<div class="pcard__thumb"><img src="{val}" alt="" loading="lazy"></div>'
    else:
        th = f'<div class="pcard__thumb pcard__thumb--code" aria-hidden="true"><div><div style="opacity:.55;">{val[0]}</div><div class="ln">{val[1]}</div><div class="ln">{val[2]}</div></div></div>'
    cards += f'''
        <a class="pcard reveal" href="projects/{p["slug"]}.html" data-tags="{p["tags"]}" aria-label="{html.escape(p["title"])}">
          {th}
          <div class="pcard__body">
            <span class="pcard__tag">{p["tag"]}</span>
            <h3 class="pcard__title">{p["title"]}</h3>
            <p class="pcard__desc">{p["desc"]}</p>
            <div class="pcard__foot"><span>{p["foot"]}</span><b>Open &rarr;</b></div>
          </div>
        </a>'''

skills_marquee = ["Threat Hunting", "Email Security", "Malware Analysis", "Vulnerability Management", "Nmap", "OpenVAS", "Tenable", "Wireshark",
                  "MITRE ATT&amp;CK", "NIST", "FedRAMP", "Zero Trust", "ISO 27001", "Python", "SQL", "Cloud Security"]
mq = "".join(f"<span>{s}</span>" for s in skills_marquee)

index = f'''
  <section class="wrap hero" id="home">
    <div class="hero__text">
      <div class="eyebrow">Cybersecurity &middot; Northern Virginia</div>
      <p class="hero__hello">Hi, I&rsquo;m</p>
      <h1 class="hero__name">{NAME}!</h1>
      <h2 class="hero__role">I&rsquo;m a <span class="accent">Cybersecurity Analyst</span></h2>
      <p class="hero__lead">I research phishing and malware as a Threat Researcher at KnowBe4. I also have hands-on experience in vulnerability assessment, mobile application security, and AI risk and governance. This site shows my projects and what I learned from each one.</p>
      <div class="ctas">
        <a class="btn btn--primary" href="#projects">View Projects {ARROW}</a>
        <a class="btn btn--ghost" href="{RESUME}" download>Resume {DOWN}</a>
        <a class="btn btn--ghost" href="cv/">Recruiter view</a>
      </div>
    </div>
    <div class="arch reveal">
      <div class="arch__ring"></div>
      <img class="arch__img" src="assets/headshot.jpg" alt="Portrait of {NAME}" />
      <div class="arch__dot" aria-hidden="true">MJ</div>
    </div>
  </section>

  <div class="marquee" aria-hidden="true"><div class="marquee__track">{mq}{mq}</div></div>

  <section class="wrap section" id="about">
    {sec_head("01", "About me", "Cybersecurity associate focused on threat research, vulnerability assessment, and clear communication.")}
    <div class="bento">
      <div class="tile span2 row2 reveal">
        <div class="tile__label">Who I am</div>
        <h3>Threat Researcher at KnowBe4</h3>
        <p>I investigate phishing emails, analyze malware, and track threat campaigns. Before that I completed internships in mobile application security at NowSecure, AI risk and governance at InterSec, and enterprise vulnerability assessment with the Department of Homeland Security.</p>
        <p style="margin-top:12px;">I like turning technical findings into something both engineers and non-technical readers can act on, and I keep learning through labs, workshops, and personal projects.</p>
      </div>
      <div class="tile reveal"><div class="stat">30%+</div><p>fewer false positives and false negatives from email classification work at KnowBe4</p></div>
      <div class="tile reveal"><div class="stat">100+</div><p>analyst hours saved by recommendations from a DHS vulnerability platform evaluation</p></div>
      <div class="tile tile--gold reveal"><div class="tile__label">Education</div><h3>George Mason University</h3><p>B.S. Information Technology, Cybersecurity &middot; May 2026 &middot; GPA 3.7</p></div>
      <div class="tile reveal"><div class="tile__label">Certifications</div><div class="certs"><span class="chip">CompTIA Security+</span><span class="chip">AWS Certified Cloud Practitioner</span><span class="chip chip--wip">CompTIA CySA+ &middot; in progress</span></div></div>
    </div>
  </section>

  <section class="wrap section" id="projects">
    {sec_head("02", "Projects", "Five projects across vulnerability management, network analysis, AI-assisted development, and team leadership.")}
    <div class="filter" role="tablist" aria-label="Filter projects">
      <button class="filter__btn is-active" data-filter="all" role="tab" aria-selected="true">All</button>
      <button class="filter__btn" data-filter="vuln" role="tab" aria-selected="false">Vulnerability Management</button>
      <button class="filter__btn" data-filter="detection" role="tab" aria-selected="false">Detection</button>
      <button class="filter__btn" data-filter="ai" role="tab" aria-selected="false">AI &amp; Development</button>
      <button class="filter__btn" data-filter="leadership" role="tab" aria-selected="false">Leadership</button>
    </div>
    <div class="pgrid" id="proj-grid">{cards}
    </div>
    <div class="callout" style="margin-top:26px;"><b>More on GitHub.</b> Write-ups live in my <a href="{REPO}">cybersecurity-portfolio</a> repository and the chatbot has <a href="{GITHUB}/ai-chatbot">its own repo</a>.</div>
  </section>

  <section class="wrap section" id="experience">
    {sec_head("03", "Experience", "Where I&rsquo;ve worked and interned.")}
    <div class="scroller">
      {xp("Jul 2026 &ndash; Present", "Cybersecurity Threat Researcher", "KnowBe4 &middot; Arlington, VA", [
          "Investigate phishing emails, analyze malware, and track threat campaigns in the Threat Research Lab.",
          "Label and classify thousands of emails daily to refine detection logic, contributing to a 30%+ reduction in false positives and false negatives.",
          "Analyze large datasets to establish threat patterns across regions, industries, and business segments.",
          "Deploy and configure endpoint, email, web, and network protection to support threat research.",
          "Triage alerts and contribute to external-facing Threat Labs research content."])}
      {xp("Jan 2026 &ndash; Apr 2026", "Mobile Application Security Intern", "NowSecure &middot; Vienna, VA", [
          "Static and dynamic analysis of Android and iOS applications to find vulnerabilities and malicious behaviors.",
          "Guided mobile app testing on the NowSecure platform, plus research comparing open-source, commercial, and traditional AI pentesting tools."])}
      {xp("Oct 2025 &ndash; Dec 2025", "Commonwealth Cybersecurity Initiative Intern", "InterSec &middot; Leesburg, VA", [
          "Led a multi-phase AI risk and cybersecurity initiative evaluating governance controls, data management, and control effectiveness.",
          "Produced compliance findings and policy recommendations for senior leadership."])}
      {xp("Jun 2025 &ndash; Sep 2025", "Vulnerability Assessment Team Intern", "Dept. of Homeland Security &middot; Ashburn, VA", [
          "Ran enterprise vulnerability assessments with Nmap, OpenVAS, and Tenable.",
          "Analyzed CVE and CVSS data to build risk-prioritized remediation queues.",
          "Evaluated AI-enabled vulnerability management platforms and saved 100+ analyst hours."])}
      {xp("Aug 2025 &ndash; May 2026", "IT Consulting Capstone, Team Lead", "ATCAP Home Healthcare Solutions &middot; GMU", [
          "Led a five-person team delivering three IT solutions for a healthcare client.",
          'Website uptime went from about 25% to about 99.9%. <a href="projects/atcap-capstone.html">Read the case study</a>.'])}
    </div>
    <p class="hint">Swipe or scroll &rarr;</p>
  </section>

  <section class="wrap section" id="skills">
    {sec_head("04", "Skills", "Tools, frameworks, and languages I work with.")}
    <div class="bento">
      <div class="tile reveal"><div class="tile__label">Security</div><span class="chip">Threat Hunting</span><span class="chip">Email Security</span><span class="chip">Vulnerability Management</span><span class="chip">Application Security</span><span class="chip">Network Security</span><span class="chip">Digital Forensics</span><span class="chip">Cloud Security</span></div>
      <div class="tile reveal"><div class="tile__label">Frameworks</div><span class="chip">NIST</span><span class="chip">MITRE ATT&amp;CK</span><span class="chip">FedRAMP</span><span class="chip">Zero Trust</span><span class="chip">ISO 27001</span></div>
      <div class="tile reveal"><div class="tile__label">Tools</div><span class="chip">Nmap</span><span class="chip">OpenVAS</span><span class="chip">Tenable / Nessus</span><span class="chip">Wireshark</span><span class="chip">SIEM</span></div>
      <div class="tile reveal"><div class="tile__label">Languages &amp; systems</div><span class="chip">Python</span><span class="chip">SQL</span><span class="chip">MongoDB</span><span class="chip">Windows</span><span class="chip">macOS</span><span class="chip">Linux</span></div>
    </div>
  </section>

  <section class="wrap section" id="contact">
    {sec_head("05", "Contact", "Open to cybersecurity roles. Happy to talk about threat research, vulnerability management, and security projects.")}
    <div class="contact">
      <div class="tile tile--gold reveal"><div class="tile__label">Let&rsquo;s talk</div><div class="contact__big">Let&rsquo;s build something secure.</div>
        <div class="ctas"><a class="btn" style="background:#0a0a0b;color:#fff;border-color:#0a0a0b;" href="{RESUME}" download>Download resume {DOWN}</a></div></div>
      <div class="clinks reveal">
        <a class="clink" href="mailto:{EMAIL}"><div><small>Email</small><span>{EMAIL}</span></div>{ARROW}</a>
        <a class="clink" href="{LINKEDIN}" target="_blank" rel="noopener"><div><small>LinkedIn</small><span>linkedin.com/in/melvin-jackson</span></div>{ARROW}</a>
        <a class="clink" href="{GITHUB}" target="_blank" rel="noopener"><div><small>GitHub</small><span>github.com/mj65825</span></div>{ARROW}</a>
        <a class="clink" href="cv/"><div><small>Recruiter view</small><span>Plain, fast, printable r&eacute;sum&eacute;</span></div>{ARROW}</a>
      </div>
    </div>
  </section>'''
page("index.html", f"{NAME} — Cybersecurity Analyst",
     f"{NAME}: cybersecurity analyst and threat researcher at KnowBe4. Security+ and AWS Certified Cloud Practitioner. Projects and resume.", index)
print("built")


# ---------------------------------------------------------------- recruiter view (plain, fast, printable)
import json

SITE = "https://mj65825.github.io/"
PHONE = "(703) 469-7026"

CV_EXP = [
    ("Cybersecurity Threat Researcher", "KnowBe4 &middot; Arlington, VA", "Jul 2026 &ndash; Present", [
        "Investigate phishing emails, analyze malware, and track threat campaigns within the KnowBe4 Threat Research Lab to identify emerging attack patterns and techniques.",
        "Label and classify thousands of emails daily to refine detection logic, contributing to a 30%+ reduction in false positives and false negatives.",
        "Analyze trends across large datasets to establish threat patterns across regions, industries, and business segments.",
        "Deploy and configure endpoint, email, web, and network protection to support threat research and detection workflows.",
        "Triage, investigate, and respond to alerts from the email platform and contribute to external-facing Threat Labs research content."]),
    ("Mobile Application Security Intern", "NowSecure &middot; Vienna, VA", "Jan 2026 &ndash; Apr 2026", [
        "Conducted static and dynamic analysis of Android and iOS applications to identify vulnerabilities, malicious behaviors, and security risks.",
        "Performed guided mobile application testing and researched AI pentesting tools, comparing open-source, commercial, and traditional options."]),
    ("Commonwealth Cybersecurity Initiative Intern", "InterSec &middot; Leesburg, VA", "Oct 2025 &ndash; Dec 2025", [
        "Led a multi-phase AI risk and cybersecurity initiative evaluating governance controls, data management, and control effectiveness.",
        "Produced compliance findings and policy recommendations for senior leadership."]),
    ("Vulnerability Assessment Team Intern", "U.S. Department of Homeland Security &middot; Ashburn, VA", "Jun 2025 &ndash; Sep 2025", [
        "Conducted enterprise vulnerability assessments using Nmap, OpenVAS, and Tenable, identifying exposed services, misconfigurations, and high-risk vulnerabilities.",
        "Analyzed CVE and CVSS data to build risk-prioritized remediation queues supporting continuous monitoring and incident triage.",
        "Evaluated AI-enabled vulnerability management platforms; recommendations improved remediation workflows and saved 100+ analyst hours."]),
]
CV_PROJ = [
    ("IT Consulting Capstone, Team Lead &middot; ATCAP Home Healthcare Solutions", "Aug 2025 &ndash; May 2026",
     "Led a five-person team delivering a website, a structured job application form, and a Python application-review script. Website uptime improved from about 25% to about 99.9%.", "projects/atcap-capstone.html"),
    ("Vulnerability Assessment Labs", "2026",
     "Scanned my own system and a Hack The Box target with Nmap, Nessus, and OpenVAS; compared scanner findings and wrote a CVSS-scored remediation report.", "projects/vuln-labs.html"),
    ("Wireshark Traffic Analysis", "2026",
     "Analyzed real captures (DNS, TLS handshakes, ARP, Teams traffic) in a SIEM lab and documented what encrypted traffic metadata reveals.", "projects/wireshark.html"),
    ("Free AI Chatbot", "2026",
     "Python chatbot with Gemini and local Ollama providers, memory, streaming, and 20 offline pytest tests; secrets kept out of source.", "projects/ai-chatbot.html"),
]
CV_SKILLS = [
    ("Security", "Threat hunting, email security, malware analysis, vulnerability management, application security, network security, digital forensics, cloud security"),
    ("Frameworks", "NIST, MITRE ATT&amp;CK, FedRAMP, Zero Trust Architecture, ISO 27001"),
    ("Tools", "Nmap, OpenVAS, Tenable / Nessus, Wireshark, SIEM"),
    ("Languages and systems", "Python, SQL, MongoDB; Windows, macOS, Linux"),
    ("Networking", "TCP/IP, DNS, encryption, firewalls, authentication, perimeter protection"),
]

exp_html = "".join(
    f'<article class="item"><header><h3>{r}</h3><p class="meta"><span>{o}</span><time>{d}</time></p></header><ul>' + "".join(f"<li>{b}</li>" for b in bl) + "</ul></article>"
    for r, o, d, bl in CV_EXP)
proj_html = "".join(
    f'<article class="item"><header><h3>{t}</h3><p class="meta"><span></span><time>{d}</time></p></header><p>{x} <a href="../{u}">Details</a></p></article>'
    for t, d, x, u in CV_PROJ)
skills_html = "".join(f"<p><strong>{k}:</strong> {v}</p>" for k, v in CV_SKILLS)

ld = json.dumps({
    "@context": "https://schema.org", "@type": "Person", "name": NAME, "jobTitle": "Cybersecurity Analyst",
    "worksFor": {"@type": "Organization", "name": "KnowBe4"}, "url": SITE, "email": EMAIL,
    "sameAs": [LINKEDIN, GITHUB], "address": {"@type": "PostalAddress", "addressLocality": "Alexandria", "addressRegion": "VA", "addressCountry": "US"},
    "alumniOf": {"@type": "CollegeOrUniversity", "name": "George Mason University"},
    "hasCredential": ["CompTIA Security+", "AWS Certified Cloud Practitioner"],
})

cv = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{NAME} · Cybersecurity Analyst · R&eacute;sum&eacute;</title>
<meta name="description" content="{NAME}, Cybersecurity Analyst and Threat Researcher at KnowBe4. Security+, AWS Cloud Practitioner. Experience, projects, skills, and contact." />
<link rel="icon" href="{FAV}" />
<link rel="stylesheet" href="cv.css?v=1" />
<script type="application/ld+json">{ld}</script>
</head>
<body>
<a class="skip" href="#cv">Skip to r&eacute;sum&eacute;</a>
<main id="cv" class="cv">
  <header class="cv-head">
    <div>
      <p class="eyebrow">Open to cybersecurity roles</p>
      <h1>{NAME}</h1>
      <p class="role">Cybersecurity Analyst &middot; Threat Researcher at KnowBe4 &middot; Alexandria, VA</p>
    </div>
    <nav class="cv-actions" aria-label="R&eacute;sum&eacute; actions">
      <a class="btn btn-solid" href="../{RESUME}" download>Download PDF</a>
      <a class="btn" href="../">Open the full portfolio</a>
    </nav>
  </header>
  <ul class="contact" aria-label="Contact">
    <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
    <li><a href="tel:+17034697026">{PHONE}</a></li>
    <li><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></li>
    <li><a href="{GITHUB}" target="_blank" rel="noopener">GitHub</a></li>
  </ul>
  <section aria-labelledby="s-sum"><h2 id="s-sum">Summary</h2>
    <p>Cybersecurity associate with hands-on experience in vulnerability assessment, threat detection, security monitoring, and compliance across enterprise environments. Skilled at identifying and prioritizing risk, conducting static and dynamic analysis, and communicating technical findings to technical and non-technical audiences. U.S. citizen.</p></section>
  <section aria-labelledby="s-exp"><h2 id="s-exp">Experience</h2>{exp_html}</section>
  <section aria-labelledby="s-proj"><h2 id="s-proj">Projects</h2>{proj_html}</section>
  <section aria-labelledby="s-skills"><h2 id="s-skills">Skills</h2>{skills_html}</section>
  <section aria-labelledby="s-edu"><h2 id="s-edu">Education and certifications</h2>
    <article class="item"><header><h3>B.S. Information Technology, Cybersecurity concentration</h3><p class="meta"><span>George Mason University &middot; GPA 3.7</span><time>May 2026</time></p></header></article>
    <p><strong>Certifications:</strong> CompTIA Security+, AWS Certified Cloud Practitioner. <strong>In progress:</strong> CompTIA CySA+</p></section>
  <footer class="cv-foot">&copy; 2026 {NAME} &middot; <a href="../">Portfolio</a></footer>
</main>
</body>
</html>
'''
os.makedirs(os.path.join(ROOT, "cv"), exist_ok=True)
with open(os.path.join(ROOT, "cv", "index.html"), "w", encoding="utf-8", newline="\n") as f:
    f.write(cv)
print("cv built")
