"""Generates the static pages. Run: python build.py"""
import os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
NAME = "Melvin Jackson"
LINKEDIN = "https://www.linkedin.com/in/melvin-jackson/"
GITHUB = "https://github.com/mj65825"
EMAIL = "melvin11jackson@gmail.com"
REPO = GITHUB + "/cybersecurity-portfolio"

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


def page(fname, title, desc, active, body, depth=0):
    p = "../" * depth
    nav = ""
    for key, label, href in NAV:
        cls = "sidebar__link" + (" is-active" if key == active else "")
        dl = " download" if href.endswith(".pdf") else ""
        nav += f'<a href="{p}{href}" class="{cls}"{dl}><svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICONS[key]}</svg>{label}</a>\n'
    social = (f'<a class="icon-btn" href="{LINKEDIN}" aria-label="LinkedIn" target="_blank" rel="noopener">{LI}</a>'
              f'<a class="icon-btn" href="{GITHUB}" aria-label="GitHub" target="_blank" rel="noopener">{GH}</a>'
              f'<a class="icon-btn" href="mailto:{EMAIL}" aria-label="Email">{MAIL}</a>')
    fsocial = social.replace("icon-btn", "").replace('class=" "', "")
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
<link rel="stylesheet" href="{p}styles.css" />
<script>try{{var d=document.documentElement,t=localStorage.getItem('theme'),c=localStorage.getItem('color');if(t)d.dataset.theme=t;if(c)d.dataset.color=c}}catch(e){{}}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<button class="menu-toggle" id="menuToggle" aria-label="Open menu" aria-controls="sidebar"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg></button>
<aside class="sidebar" id="sidebar" aria-label="Primary">
  <div class="sidebar__brand"><span class="sidebar__name">{NAME}</span></div>
  <nav class="sidebar__nav">
{nav}  </nav>
  <div class="sidebar__foot">{social}</div>
</aside>
<div class="utility">
  <button class="util-btn" id="themeToggle" aria-label="Toggle light/dark"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg></button>
  <button class="util-btn" id="paletteToggle" aria-label="Theme color"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c1 0 1.5-.7 1.5-1.5 0-.4-.2-.8-.5-1-.3-.3-.5-.6-.5-1 0-.8.7-1.5 1.5-1.5H16c3.3 0 6-2.7 6-6 0-4.7-4.5-8.5-10-8.5z"/></svg></button>
  <div class="color-picker" id="colorPicker" role="group" aria-label="Accent color"><span class="color-picker__label">Theme</span>{swatches}</div>
</div>
<main id="main">
  <div class="wrap">
{body}
    <footer class="foot">
      <span>&copy; 2026 {NAME}</span>
      <div class="foot__social">{fsocial}</div>
    </footer>
  </div>
</main>
<button class="to-top" id="toTop" aria-label="Back to top"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 15l7-7 7 7"/></svg></button>
<script src="{p}main.js"></script>
</body>
</html>
'''
    path = os.path.join(ROOT, fname)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(out)


def head(eyebrow, title, lead=""):
    l = f'<p class="hero__lead" style="margin-top:14px;">{lead}</p>' if lead else ""
    return f'<div class="h-block"><div class="h-eyebrow">// {eyebrow}</div><h1 class="h-title">{title}</h1><div class="h-rule"></div>{l}</div>'


# ---------------------------------------------------------------- home
home = f'''
    <section class="hero" style="position:relative;">
      <div class="hero-bg" aria-hidden="true"><div class="hero-bg__glow"></div><div class="hero-bg__glow hero-bg__glow--2"></div></div>
      <div class="hero-flow">
        <div class="status"><span class="status__dot"></span>ACTIVE &middot; Threat Research Lab, KnowBe4</div>
        <div class="prompt" aria-hidden="true">$ <span id="typed" data-text="whoami &rarr; melvin.jackson"></span><span class="caret"></span></div>
        <h1 class="hero__hello">Hi, I&rsquo;m <span class="hero__name-script">{NAME}!</span></h1>
        <h2 class="hero__role">I&rsquo;m a <span class="accent">Cybersecurity Analyst</span></h2>
        <p class="hero__lead">I research phishing and malware as a Threat Researcher at KnowBe4. I also have hands-on experience in vulnerability assessment, mobile application security, and AI risk and governance. This site shows my projects and what I learned from each one.</p>
        <div class="badges"><span class="badge"><b>CompTIA</b> Security+</span><span class="badge"><b>AWS</b> Cloud Practitioner</span><span class="badge"><b>GMU</b> B.S. IT &middot; 3.7 GPA</span></div>
        <div class="hero__ctas">
          <a class="btn btn--primary" href="projects.html">View Projects {ARROW}</a>
          <a class="btn btn--ghost" href="MelvinJackson_Cybersecurity_Resume.pdf" download>Resume {DOWN}</a>
          <a class="btn btn--ghost" href="contact.html">Contact</a>
        </div>
      </div>
      <div class="portrait-wrap reveal"><div class="portrait"><img class="portrait__img" src="assets/headshot.jpg" alt="Portrait of {NAME}" /></div><div class="portrait-tag">ID &middot; MJ-2026 &middot; CLEARED FOR HIRE</div></div>
    </section>'''
page("index.html", f"{NAME} — Cybersecurity Analyst",
     f"{NAME}: cybersecurity analyst and threat researcher at KnowBe4. Security+ and AWS Certified Cloud Practitioner. Projects and resume.", "home", home)

# ---------------------------------------------------------------- about
about = head("About me", "About", "Cybersecurity associate focused on threat research, vulnerability assessment, and clear communication.") + f'''
    <section class="reveal prose">
      <p>I&rsquo;m a cybersecurity analyst and a recent <strong>George Mason University</strong> graduate (B.S. in Information Technology, Cybersecurity concentration, 3.7 GPA). I&rsquo;m a Threat Researcher at <strong>KnowBe4</strong>, where I investigate phishing emails, analyze malware, and track threat campaigns.</p>
      <p>Before that I completed internships in mobile application security at <strong>NowSecure</strong>, AI risk and governance at <strong>InterSec</strong>, and enterprise vulnerability assessment with the <strong>Department of Homeland Security</strong>.</p>
      <p>I like turning technical findings into something both engineers and non-technical readers can act on. Outside work I keep learning through labs, workshops, and personal projects, and I write about them on LinkedIn.</p>
      <h2 class="sec">Certifications</h2>
      <div class="meta"><span class="chip">CompTIA Security+</span><span class="chip">AWS Certified Cloud Practitioner</span></div>
      <h2 class="sec">Education</h2>
      <p><strong>George Mason University</strong><br>B.S. Information Technology, Concentration in Cybersecurity &middot; May 2026 &middot; GPA 3.7</p>
      <h2 class="sec">Skills</h2>
    </section>
    <div class="skills reveal">
      <div class="skillbox"><h3>Security</h3><span class="chip">Threat Hunting</span><span class="chip">Email Security</span><span class="chip">Vulnerability Management</span><span class="chip">Application Security</span><span class="chip">Network Security</span><span class="chip">Digital Forensics</span><span class="chip">Cloud Security</span></div>
      <div class="skillbox"><h3>Frameworks</h3><span class="chip">NIST</span><span class="chip">MITRE ATT&amp;CK</span><span class="chip">FedRAMP</span><span class="chip">Zero Trust</span><span class="chip">ISO 27001</span></div>
      <div class="skillbox"><h3>Tools</h3><span class="chip">Nmap</span><span class="chip">OpenVAS</span><span class="chip">Tenable / Nessus</span><span class="chip">Wireshark</span><span class="chip">SIEM</span></div>
      <div class="skillbox"><h3>Languages and systems</h3><span class="chip">Python</span><span class="chip">SQL</span><span class="chip">MongoDB</span><span class="chip">Windows</span><span class="chip">macOS</span><span class="chip">Linux</span></div>
    </div>'''
page("about.html", f"About — {NAME}", f"About {NAME}: threat researcher, GMU graduate, Security+ and AWS Cloud Practitioner.", "about", about)

# ---------------------------------------------------------------- experience
def tl(date, role, org, bullets):
    li = "".join(f"<li>{b}</li>" for b in bullets)
    return f'<div class="tl__item"><div class="tl__date">{date}</div><div class="tl__role">{role}</div><div class="tl__org">{org}</div><ul class="list">{li}</ul></div>'

exp = head("Where I&rsquo;ve worked", "Experience") + '<div class="tl reveal">' + "".join([
    tl("Jul 2026 &ndash; Present", "Cybersecurity Threat Researcher", "KnowBe4 &middot; Arlington, VA", [
        "Investigate phishing emails, analyze malware, and track threat campaigns in the KnowBe4 Threat Research Lab.",
        "Label and classify thousands of emails daily to refine detection logic, contributing to a 30%+ reduction in false positives and false negatives.",
        "Analyze large datasets to establish threat patterns across regions, industries, and business segments.",
        "Deploy and configure endpoint, email, web, and network protection to support threat research and detection workflows.",
        "Triage and respond to alerts from the email platform and contribute to external-facing Threat Labs research content."]),
    tl("Jan 2026 &ndash; Apr 2026", "Mobile Application Security Intern", "NowSecure &middot; Vienna, VA", [
        "Static and dynamic analysis of Android and iOS applications to find vulnerabilities, malicious behaviors, and security risks.",
        "Guided mobile application testing on the NowSecure platform, and research comparing open-source, commercial, and traditional AI pentesting tools."]),
    tl("Oct 2025 &ndash; Dec 2025", "Commonwealth Cybersecurity Initiative Intern", "InterSec &middot; Leesburg, VA", [
        "Led a multi-phase AI risk and cybersecurity initiative evaluating governance controls, data management, and control effectiveness.",
        "Produced compliance findings and policy recommendations for senior leadership."]),
    tl("Jun 2025 &ndash; Sep 2025", "Vulnerability Assessment Team Intern", "Dept. of Homeland Security &middot; Ashburn, VA", [
        "Ran enterprise vulnerability assessments with Nmap, OpenVAS, and Tenable, finding exposed services, misconfigurations, and high-risk vulnerabilities.",
        "Analyzed CVE and CVSS data to build risk-prioritized remediation queues.",
        "Evaluated AI-enabled vulnerability management platforms and delivered recommendations that saved 100+ analyst hours."]),
    tl("Aug 2025 &ndash; May 2026", "IT Consulting Capstone, Team Lead", "ATCAP Home Healthcare Solutions &middot; George Mason University", [
        "Led a five-person team delivering three IT solutions for a healthcare client. <a class=\"accent\" href=\"projects/atcap-capstone.html\">Read the case study</a>."]),
]) + "</div>"
page("experience.html", f"Experience — {NAME}", f"Work and internship experience of {NAME}: KnowBe4, NowSecure, InterSec, DHS.", "exp", exp)

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

# ---------------------------------------------------------------- projects index
cards = ""
for p in PROJECTS:
    kind, val = p["thumb"]
    if kind == "img":
        th = f'<div class="card__thumb"><img src="{val}" alt="" loading="lazy"></div>'
    else:
        th = f'<div class="card__thumb card__thumb--code" aria-hidden="true"><div><div style="opacity:.55;">{val[0]}</div><div style="margin-top:6px;color:#C3E88D;">{val[1]}</div><div style="margin-top:2px;color:#C3E88D;">{val[2]}</div></div></div>'
    cards += f'''
        <a class="card reveal" href="projects/{p["slug"]}.html" data-tags="{p["tags"]}" aria-label="{html.escape(p["title"])}">
          {th}
          <div class="card__body">
            <span class="card__tag">{p["tag"]}</span>
            <h3 class="card__title">{p["title"]}</h3>
            <p class="card__desc">{p["desc"]}</p>
            <div class="card__foot"><span>{p["foot"]}</span><span class="card__cta">Open &rarr;</span></div>
          </div>
        </a>'''
proj = head("My recent projects", "Portfolio", "Five projects across vulnerability management, network analysis, AI-assisted development, and team leadership. Filter by focus area.") + f'''
    <section>
      <div class="filter" role="tablist" aria-label="Filter projects">
        <button class="filter__btn is-active" data-filter="all" role="tab" aria-selected="true">All</button>
        <button class="filter__btn" data-filter="vuln" role="tab" aria-selected="false">Vulnerability Management</button>
        <button class="filter__btn" data-filter="detection" role="tab" aria-selected="false">Detection</button>
        <button class="filter__btn" data-filter="ai" role="tab" aria-selected="false">AI &amp; Development</button>
        <button class="filter__btn" data-filter="leadership" role="tab" aria-selected="false">Leadership</button>
      </div>
      <div class="grid" id="proj-grid">{cards}
      </div>
      <div class="callout" style="margin-top:32px;"><b>More on GitHub.</b> Write-ups live in my <a href="{REPO}">cybersecurity-portfolio</a> repository and the chatbot has <a href="{GITHUB}/ai-chatbot">its own repo</a>.</div>
    </section>'''
page("projects.html", f"Projects — {NAME}", "Cybersecurity projects: vulnerability assessment labs, Wireshark analysis, AI chatbot, AWS Kiro dashboard, and the ATCAP capstone.", "projects", proj)

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
    body = f'''<a class="back" href="../projects.html">&larr; All projects</a>
    <section>
      {head(p["tag"], p["title"], p["desc"])}
      <div class="meta">{chips}</div>
      <div class="hero__ctas" style="margin-top:16px;">{btns}</div>{BODY[p["slug"]]}
    </section>'''
    page(f'projects/{p["slug"]}.html', f'{p["title"]} — {NAME}', p["desc"], "projects", body, depth=1)

# ---------------------------------------------------------------- contact
contact = head("Get in touch", "Contact", "I&rsquo;m open to cybersecurity roles and happy to talk about threat research, vulnerability management, and security projects.") + f'''
    <div class="contact-grid reveal">
      <a class="contact-card" href="mailto:{EMAIL}"><small>Email</small><span>{EMAIL}</span></a>
      <a class="contact-card" href="{LINKEDIN}" target="_blank" rel="noopener"><small>LinkedIn</small><span>linkedin.com/in/melvin-jackson</span></a>
      <a class="contact-card" href="{GITHUB}" target="_blank" rel="noopener"><small>GitHub</small><span>github.com/mj65825</span></a>
      <a class="contact-card" href="MelvinJackson_Cybersecurity_Resume.pdf" download><small>Resume</small><span>Download PDF</span></a>
    </div>'''
page("contact.html", f"Contact — {NAME}", f"Contact {NAME} by email, LinkedIn, or GitHub.", "contact", contact)
print("built")
