#!/usr/bin/env python3
"""Squirrel AI: differentiation-angle ads + franchise one-pager (HTML/CSS -> PDF -> PNG)."""
import os
import fitz
from weasyprint import HTML

OUT = "/home/user/msolomon11.github.io/ad-designs"
DOCS = "/home/user/msolomon11.github.io"
os.makedirs(OUT, exist_ok=True)

ORANGE = "#FF8A3D"
CYAN = "#56D9F2"
INK = "#10163A"

BASE_CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:'Liberation Sans','DejaVu Sans',sans-serif; color:#fff;
       background:linear-gradient(135deg,#10163A 0%,#1B2456 55%,#273480 100%);
       width:__W__px; height:__H__px; position:relative; overflow:hidden; }
.ring { position:absolute; border:3px solid rgba(86,217,242,.18); border-radius:50%; }
.ring2 { position:absolute; border:2px solid rgba(255,138,61,.22); border-radius:50%; }
.glow { position:absolute; background:radial-gradient(circle, rgba(255,138,61,.28) 0%, rgba(255,138,61,0) 70%); border-radius:50%; }
.brand { letter-spacing:1px; }
.brand b { color:#fff; font-weight:bold; }
.brand .sub { color:rgba(255,255,255,.55); font-weight:normal; letter-spacing:3px; }
.eyebrow { display:inline-block; background:rgba(86,217,242,.12); border:1px solid rgba(86,217,242,.5);
           color:__CYAN__; border-radius:999px; letter-spacing:2.5px; font-weight:bold; }
h1 { font-weight:bold; line-height:1.08; }
h1 .hl { color:__ORANGE__; }
.chip { display:inline-block; background:rgba(255,255,255,.07); border:1px solid rgba(255,255,255,.18);
        border-radius:14px; text-align:center; vertical-align:top; }
.chip .num { color:__ORANGE__; font-weight:bold; display:block; }
.chip .lbl { color:rgba(255,255,255,.78); display:block; }
.cta { display:inline-block; background:__ORANGE__; color:__INK__; font-weight:bold; border-radius:999px; }
.compliance { position:absolute; color:rgba(255,255,255,.42); line-height:1.35; }
.panel { display:inline-block; vertical-align:top; border-radius:18px; }
.panel ul { list-style:none; }
.panel li { line-height:1.5; }
"""

COMPLIANCE = ("Figures are estimates per the Franchise Disclosure Document, Item 19. This is not an offer to sell "
              "a franchise. Offers are made only by an FDD in states where registered/permitted.")


def page_css(w, h):
    css = BASE_CSS.replace("__W__", str(w)).replace("__H__", str(h))
    css = css.replace("__ORANGE__", ORANGE).replace("__CYAN__", CYAN).replace("__INK__", INK)
    return f"@page {{ size: {w}px {h}px; margin: 0; }}\n" + css


def brand(size=26):
    return (f'<div class="brand" style="font-size:{size}px;"><b>SQUIRREL</b> <b style="color:{ORANGE}">AI</b>'
            f' <span class="sub" style="font-size:{int(size*0.55)}px;">LEARNING</span></div>')


def chips_html(chips, cw, num_fs, lbl_fs, pad):
    out = '<div>'
    for num, lbl in chips:
        out += (f'<div class="chip" style="width:{cw}px; padding:{pad}px 10px; margin-right:14px;">'
                f'<span class="num" style="font-size:{num_fs}px;">{num}</span>'
                f'<span class="lbl" style="font-size:{lbl_fs}px; margin-top:6px;">{lbl}</span></div>')
    return out + "</div>"


def deco(w, h):
    return (f'<div class="ring" style="width:{int(h*1.1)}px;height:{int(h*1.1)}px;right:-{int(h*0.45)}px;top:-{int(h*0.35)}px;"></div>'
            f'<div class="ring2" style="width:{int(h*0.7)}px;height:{int(h*0.7)}px;right:-{int(h*0.2)}px;bottom:-{int(h*0.3)}px;"></div>'
            f'<div class="glow" style="width:{int(h*0.9)}px;height:{int(h*0.9)}px;right:-{int(h*0.3)}px;top:{int(h*0.1)}px;"></div>')


def render_png(name, w, h, body):
    html = f"<html><head><style>{page_css(w,h)}</style></head><body>{deco(w,h)}{body}</body></html>"
    pdf = f"/tmp/{name}.pdf"
    HTML(string=html).write_pdf(pdf)
    doc = fitz.open(pdf)
    pix = doc[0].get_pixmap(matrix=fitz.Matrix(4/3, 4/3))
    pix.save(os.path.join(OUT, f"{name}.png"))
    print(f"{name}.png  {pix.width}x{pix.height}")


# =========================================================
# AD 1 — LinkedIn 1200x627: side-by-side comparison
# =========================================================
def vs_panel(title, items, good, width, fs):
    color = ORANGE if good else "rgba(255,255,255,.45)"
    mark = "&#10003;" if good else "&#10007;"
    border = f"2px solid {ORANGE}" if good else "1px solid rgba(255,255,255,.18)"
    bg = "rgba(255,138,61,.08)" if good else "rgba(255,255,255,.05)"
    lis = "".join(f'<li style="font-size:{fs}px; margin-bottom:10px;">'
                  f'<span style="color:{color}; font-weight:bold;">{mark}</span>&nbsp; {t}</li>' for t in items)
    tcolor = ORANGE if good else "rgba(255,255,255,.65)"
    return (f'<div class="panel" style="width:{width}px; background:{bg}; border:{border}; padding:22px 26px; margin-right:18px;">'
            f'<div style="font-size:{fs+3}px; font-weight:bold; color:{tcolor}; margin-bottom:14px; letter-spacing:1px;">{title}</div>'
            f'<ul>{lis}</ul></div>')


li12_body = f"""
<div style="position:absolute; left:64px; top:40px;">{brand(28)}</div>
<div style="position:absolute; left:64px; top:100px;">
  <h1 style="font-size:44px; width:1000px;">Tutoring hasn&rsquo;t changed in 40 years. <span class="hl">The technology has.</span></h1>
</div>
<div style="position:absolute; left:64px; top:220px;">
  {vs_panel("TRADITIONAL TUTORING", [
      "Paper worksheets &amp; memorization",
      "Scheduled sessions only",
      "Periodic progress reports"], False, 510, 17)}
  {vs_panel("SQUIRREL AI", [
      "AI pinpoints gaps &mdash; even years back",
      "Adaptive plans adjust in real time, 24/7",
      "Parents see live metrics, anytime"], True, 510, 17)}
</div>
<div style="position:absolute; left:64px; top:512px;"><span class="cta" style="font-size:20px; padding:14px 34px;">Own the Upgrade &mdash; Download the Item 19 &rarr;</span></div>
<div class="compliance" style="left:64px; right:64px; bottom:14px; font-size:10px;">{COMPLIANCE}</div>
"""
render_png("LI-12_vs-traditional_1200x627", 1200, 627, li12_body)

# =========================================================
# AD 2 — LinkedIn 1200x627: parent transparency = retention
# =========================================================
li13_body = f"""
<div style="position:absolute; left:64px; top:44px;">{brand(28)}</div>
<div style="position:absolute; left:64px; top:108px;">
  <span class="eyebrow" style="font-size:15px; padding:8px 18px;">THE PRODUCT SELLS THE SUBSCRIPTION</span>
  <h1 style="font-size:50px; width:920px; margin-top:22px;">Parents don&rsquo;t cancel what they can <span class="hl">see working.</span></h1>
  <p style="font-size:24px; color:rgba(255,255,255,.82); width:880px; margin-top:20px; line-height:1.4;">
    24/7 dashboards show every gap found and closed &mdash; transparency legacy tutoring can&rsquo;t match.</p>
</div>
<div style="position:absolute; left:64px; top:392px;">{chips_html([
    ("24/7", "parent access to<br>live metrics"), ("$250&ndash;350", "monthly recurring<br>subscriptions"), ("3,000+", "centers running<br>worldwide")], 218, 30, 14, 18)}</div>
<div style="position:absolute; left:64px; top:520px;"><span class="cta" style="font-size:20px; padding:14px 34px;">Check Territory Availability &rarr;</span></div>
<div class="compliance" style="left:64px; right:64px; bottom:14px; font-size:10px;">{COMPLIANCE}</div>
"""
render_png("LI-13_parent-transparency_1200x627", 1200, 627, li13_body)

# =========================================================
# AD 3 — Square 1080x1080: 24/7 availability
# =========================================================
fb10_body = f"""
<div style="position:absolute; left:72px; top:60px;">{brand(30)}</div>
<div style="position:absolute; left:72px; top:150px;">
  <span class="eyebrow" style="font-size:17px; padding:9px 20px;">THE DIFFERENTIATED PRODUCT</span>
  <h1 style="font-size:80px; width:920px; margin-top:30px;">The tutor that <span class="hl">never closes.</span></h1>
  <p style="font-size:30px; color:rgba(255,255,255,.82); width:880px; margin-top:26px; line-height:1.4;">
    AI support around the clock, unlimited ways to explain a concept, and award-winning teachers to reinforce the hardest lessons.</p>
</div>
<div style="position:absolute; left:72px; top:700px;">{chips_html([
    ("24/7", "AI learning<br>support"), ("&infin;", "ways to explain<br>a concept"), ("3,000+", "centers<br>worldwide")], 286, 40, 17, 24)}</div>
<div style="position:absolute; left:72px; top:920px;"><span class="cta" style="font-size:26px; padding:18px 44px;">Franchise With the Future</span></div>
<div class="compliance" style="left:72px; right:72px; bottom:20px; font-size:11px;">{COMPLIANCE}</div>
"""
render_png("FB-10_never-closes_1080x1080", 1080, 1080, fb10_body)

# =========================================================
# AD 4 — Square 1080x1080: finds gaps years back
# =========================================================
ig10_body = f"""
<div style="position:absolute; left:72px; top:60px;">{brand(30)}</div>
<div style="position:absolute; left:72px; top:150px;">
  <span class="eyebrow" style="font-size:17px; padding:9px 20px;">WHY PARENTS SWITCH</span>
  <h1 style="font-size:76px; width:920px; margin-top:30px;">A gap from three grades ago? <span class="hl">Found. Fixed.</span></h1>
  <p style="font-size:30px; color:rgba(255,255,255,.82); width:880px; margin-top:26px; line-height:1.4;">
    Worksheets drill what a child already knows. Squirrel AI pinpoints exactly where learning broke down &mdash; and rebuilds from there.</p>
</div>
<div style="position:absolute; left:72px; top:700px;">{chips_html([
    ("Real-time", "progress tracking<br>&amp; plan updates"), ("24/7", "parent metrics<br>dashboard"), ("10,000s", "of students<br>helped")], 286, 36, 17, 26)}</div>
<div style="position:absolute; left:72px; top:920px;"><span class="cta" style="font-size:26px; padding:18px 44px;">Bring It to Your Community</span></div>
<div class="compliance" style="left:72px; right:72px; bottom:20px; font-size:11px;">{COMPLIANCE}</div>
"""
render_png("IG-10_finds-gaps_1080x1080", 1080, 1080, ig10_body)

# =========================================================
# ONE-PAGER — US Letter PDF
# =========================================================
OP_CSS = """
@page { size: 8.5in 11in; margin: 0; }
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:'Liberation Sans','DejaVu Sans',sans-serif; color:#222; font-size:9pt; line-height:1.38; }
.hero { background:linear-gradient(135deg,#10163A 0%,#1B2456 55%,#273480 100%); color:#fff; padding:16pt 40pt 12pt 40pt; }
.hero .brand { font-size:17pt; font-weight:bold; letter-spacing:1px; }
.hero .brand .ai { color:__ORANGE__; }
.hero .brand .sub { color:rgba(255,255,255,.55); font-weight:normal; font-size:9pt; letter-spacing:3px; }
.hero h1 { font-size:18pt; line-height:1.12; margin-top:10pt; font-weight:bold; }
.hero h1 .hl { color:__ORANGE__; }
.hero p { color:rgba(255,255,255,.85); margin-top:5pt; font-size:9pt; width:88%; }
.statband { background:#0C1230; color:#fff; padding:6pt 40pt; }
.statband .stat { display:inline-block; width:31%; vertical-align:top; }
.statband .num { color:__ORANGE__; font-weight:bold; font-size:14pt; display:block; }
.statband .lbl { color:rgba(255,255,255,.75); font-size:7.5pt; }
.wrap { padding:9pt 40pt 0 40pt; }
h2 { font-size:11.5pt; color:#10163A; border-bottom:2pt solid __ORANGE__; padding-bottom:3pt; margin-bottom:6pt; }
.cols2 { width:100%; }
.col { display:inline-block; vertical-align:top; }
table { border-collapse:collapse; width:100%; margin-top:4pt; }
th { background:#10163A; color:#fff; font-size:8pt; padding:3pt 7pt; text-align:left; }
th.sq { background:__ORANGE__; color:#10163A; }
td { border-bottom:0.6pt solid #ddd; padding:3pt 7pt; font-size:8pt; vertical-align:top; }
td.dim { color:#777; }
td.win { font-weight:bold; color:#10163A; }
ul { margin:3pt 0 0 12pt; }
li { margin-bottom:1.5pt; }
.kv { width:100%; margin-top:2pt; }
.kv td { padding:2pt 6pt; }
.kv .k { color:#555; width:58%; }
.kv .v { font-weight:bold; color:#10163A; text-align:right; }
.ctaband { background:__ORANGE__; color:#10163A; padding:7pt 40pt; margin-top:8pt; font-weight:bold; font-size:10pt; }
.footer { padding:7pt 40pt; font-size:6.8pt; color:#888; line-height:1.35; }
"""

ONE_PAGER = f"""
<html><head><style>{OP_CSS.replace("__ORANGE__", ORANGE)}</style></head><body>

<div class="hero">
  <div class="brand">SQUIRREL <span class="ai">AI</span> <span class="sub">LEARNING &nbsp;&middot;&nbsp; FRANCHISE OPPORTUNITY</span></div>
  <h1>The AI-powered learning franchise that&rsquo;s <span class="hl">rebuilding how tutoring works.</span></h1>
  <p>Squirrel AI is a leading education technology company blending an intelligent adaptive learning platform with
     award-winning teaching expertise. Across 3,000+ learning centers worldwide, we&rsquo;ve helped tens of thousands of
     students succeed &mdash; and the first U.S. territories are opening now.</p>
</div>

<div class="statband">
  <div class="stat"><span class="num">3,000+</span><span class="lbl">LEARNING CENTERS WORLDWIDE</span></div>
  <div class="stat"><span class="num">10,000s</span><span class="lbl">OF STUDENTS HELPED TO SUCCESS</span></div>
  <div class="stat"><span class="num">200</span><span class="lbl">FIRST-WAVE U.S. TERRITORIES</span></div>
</div>

<div class="wrap">
  <h2>Why Squirrel AI Wins Where Traditional Tutoring Can&rsquo;t</h2>
  <table>
    <tr><th style="width:30%;">&nbsp;</th><th style="width:33%;">Traditional Tutoring (e.g., Kumon, Mathnasium)</th><th class="sq" style="width:37%;">Squirrel AI</th></tr>
    <tr><td><b>Method</b></td><td class="dim">Paper worksheets, repetition &amp; memorization</td><td class="win">Adaptive AI platform pinpoints the exact concept where learning broke down &mdash; even gaps from years earlier</td></tr>
    <tr><td><b>Learning plan</b></td><td class="dim">One-size-fits-most curriculum levels</td><td class="win">Customized plan per student, adjusted in real time as the AI tracks progress</td></tr>
    <tr><td><b>Availability</b></td><td class="dim">Scheduled sessions only</td><td class="win">24/7 AI support, with unlimited ways to explain a concept until it clicks</td></tr>
    <tr><td><b>Human teaching</b></td><td class="dim">Varies by location and staff</td><td class="win">Award-winning teachers reinforce the most challenging lessons in clear, simple ways</td></tr>
    <tr><td><b>Parent visibility</b></td><td class="dim">Periodic paper reports</td><td class="win">24/7 dashboard with detailed metrics on every gap found and closed</td></tr>
  </table>

  <div style="margin-top:8pt;" class="cols2">
    <div class="col" style="width:48%; margin-right:3%;">
      <h2>The Business Model</h2>
      <table class="kv">
        <tr><td class="k">Total initial investment</td><td class="v">$110,450 &ndash; $137,000</td></tr>
        <tr><td class="k">Revenue model</td><td class="v">$250&ndash;$350/mo subscriptions</td></tr>
        <tr><td class="k">Break-even point</td><td class="v">32&ndash;38 active students</td></tr>
        <tr><td class="k">Center footprint</td><td class="v">1,200 sq. ft.</td></tr>
        <tr><td class="k">Gross margin per seat</td><td class="v">85&ndash;90%</td></tr>
        <tr><td class="k">At 100 students (per Item 19)</td><td class="v">~$30,000 gross / ~$18,250 NOI per mo.</td></tr>
        <tr><td class="k">Formats available</td><td class="v">Single-unit &amp; Area Development</td></tr>
      </table>
      <p style="font-size:7.5pt; color:#777; margin-top:4pt;">No inventory. No complex supply chain. No certified-teacher payroll &mdash; the platform delivers instruction; your team runs enrollment, community, and operations.</p>
    </div>
    <div class="col" style="width:48%;">
      <h2>What You Get as a Franchisee</h2>
      <ul>
        <li><b>State-of-the-art technology</b> &mdash; the proprietary adaptive learning platform, proven across 3,000+ centers</li>
        <li><b>A well-developed curriculum</b> &mdash; award-winning, covering K-12, building academics plus critical thinking and creativity</li>
        <li><b>Comprehensive initial training</b> &mdash; plus territory mapping from day one</li>
        <li><b>Marketing support</b> &mdash; launch and ongoing demand generation built on a trusted name in personalized education</li>
        <li><b>Ongoing guidance</b> &mdash; an experienced team behind you, reducing the risks of starting from scratch</li>
      </ul>
      <p style="margin-top:6pt; font-size:8.5pt;">You focus on growing the business and making an impact in your community &mdash; we provide the tools and systems.</p>
    </div>
  </div>
</div>

<div class="ctaband">Ready to be part of the future of education? &nbsp;&rarr;&nbsp; Request the Item 19 financial disclosures and check territory availability today.</div>

<div class="footer">{COMPLIANCE} Squirrel AI Learning. Kumon&reg; and Mathnasium&reg; are registered trademarks of their respective owners; references are for comparison only and do not imply affiliation or endorsement.</div>

</body></html>
"""

HTML(string=ONE_PAGER).write_pdf(os.path.join(DOCS, "Squirrel_AI_Franchise_One_Pager.pdf"))
print("Squirrel_AI_Franchise_One_Pager.pdf  (US Letter)")
print("\nDone.")
