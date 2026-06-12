#!/usr/bin/env python3
"""Render Squirrel AI Ad Pack 2 static creatives: HTML/CSS -> PDF (WeasyPrint) -> PNG (PyMuPDF)."""
import os
import fitz
from weasyprint import HTML

OUT = "/home/user/msolomon11.github.io/ad-designs"
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
.brand .dot { color:__ORANGE__; }
.brand .sub { color:rgba(255,255,255,.55); font-weight:normal; letter-spacing:3px; }
.eyebrow { display:inline-block; background:rgba(86,217,242,.12); border:1px solid rgba(86,217,242,.5);
           color:__CYAN__; border-radius:999px; letter-spacing:2.5px; font-weight:bold; }
h1 { font-weight:bold; line-height:1.08; }
h1 .hl { color:__ORANGE__; }
.chips { }
.chip { display:inline-block; background:rgba(255,255,255,.07); border:1px solid rgba(255,255,255,.18);
        border-radius:14px; text-align:center; vertical-align:top; }
.chip .num { color:__ORANGE__; font-weight:bold; display:block; }
.chip .lbl { color:rgba(255,255,255,.78); display:block; }
.cta { display:inline-block; background:__ORANGE__; color:__INK__; font-weight:bold; border-radius:999px; }
.compliance { position:absolute; color:rgba(255,255,255,.42); line-height:1.35; }
"""

COMPLIANCE = ("Figures are estimates per the Franchise Disclosure Document, Item 19. This is not an offer to sell "
              "a franchise. Offers are made only by an FDD in states where registered/permitted.")


def page_css(w, h):
    css = BASE_CSS.replace("__W__", str(w)).replace("__H__", str(h))
    css = css.replace("__ORANGE__", ORANGE).replace("__CYAN__", CYAN).replace("__INK__", INK)
    return f"@page {{ size: {w}px {h}px; margin: 0; }}\n" + css


def brand(size=26, sub=True):
    s = f'<div class="brand" style="font-size:{size}px;"><b>SQUIRREL</b> <b style="color:{ORANGE}">AI</b>'
    if sub:
        s += f' <span class="sub" style="font-size:{int(size*0.55)}px;">LEARNING</span>'
    return s + "</div>"


def chips_html(chips, cw, num_fs, lbl_fs, pad):
    out = '<div class="chips">'
    for num, lbl in chips:
        out += (f'<div class="chip" style="width:{cw}px; padding:{pad}px 10px; margin-right:14px;">'
                f'<span class="num" style="font-size:{num_fs}px;">{num}</span>'
                f'<span class="lbl" style="font-size:{lbl_fs}px; margin-top:6px;">{lbl}</span></div>')
    return out + "</div>"


def deco(w, h):
    return (f'<div class="ring" style="width:{int(h*1.1)}px;height:{int(h*1.1)}px;right:-{int(h*0.45)}px;top:-{int(h*0.35)}px;"></div>'
            f'<div class="ring2" style="width:{int(h*0.7)}px;height:{int(h*0.7)}px;right:-{int(h*0.2)}px;bottom:-{int(h*0.3)}px;"></div>'
            f'<div class="glow" style="width:{int(h*0.9)}px;height:{int(h*0.9)}px;right:-{int(h*0.3)}px;top:{int(h*0.1)}px;"></div>')


def render(name, w, h, body):
    html = f"<html><head><style>{page_css(w,h)}</style></head><body>{deco(w,h)}{body}</body></html>"
    pdf = f"/tmp/{name}.pdf"
    HTML(string=html).write_pdf(pdf)
    doc = fitz.open(pdf)
    pix = doc[0].get_pixmap(matrix=fitz.Matrix(4/3, 4/3))
    png = os.path.join(OUT, f"{name}.png")
    pix.save(png)
    print(f"{name}.png  {pix.width}x{pix.height}")


# ---------- LinkedIn 1200x627 ----------
def linkedin(name, eyebrow, headline, chips, cta):
    body = f"""
    <div style="position:absolute; left:64px; top:44px;">{brand(28)}</div>
    <div style="position:absolute; left:64px; top:108px;">
      <span class="eyebrow" style="font-size:15px; padding:8px 18px;">{eyebrow}</span>
      <h1 style="font-size:54px; width:880px; margin-top:22px;">{headline}</h1>
    </div>
    <div style="position:absolute; left:64px; top:380px;">{chips_html(chips, 218, 30, 14, 18)}</div>
    <div style="position:absolute; left:64px; top:512px;"><span class="cta" style="font-size:20px; padding:14px 34px;">{cta}</span></div>
    <div class="compliance" style="left:64px; right:64px; bottom:16px; font-size:10px;">{COMPLIANCE}</div>
    """
    render(name, 1200, 627, body)


linkedin("LI-5_educator_1200x627",
         "FOR FORMER EDUCATORS",
         'You left the classroom.<br>You don&rsquo;t have to <span class="hl">leave education.</span>',
         [("0", "certified teachers<br>on payroll"), ("32&ndash;38", "students to<br>break even"), ("$110K+", "total investment<br>from")],
         "Download the Item 19 &rarr;")

linkedin("LI-6_early-window_1200x627",
         "MULTI-UNIT &amp; AREA DEVELOPMENT",
         'Every franchise category has<br>an early window. <span class="hl">This is one.</span>',
         [("3,000+", "units operating<br>globally"), ("200", "first-wave U.S.<br>territories"), ("85&ndash;90%", "gross margin<br>per seat")],
         "Check Territory Availability &rarr;")

# ---------- Square 1080x1080 (FB/IG) ----------
def square(name, eyebrow, headline, hfs, sub, chips, cta):
    sub_html = f'<p style="font-size:30px; color:rgba(255,255,255,.82); width:880px; margin-top:26px; line-height:1.4;">{sub}</p>' if sub else ""
    body = f"""
    <div style="position:absolute; left:72px; top:60px;">{brand(30)}</div>
    <div style="position:absolute; left:72px; top:150px;">
      <span class="eyebrow" style="font-size:17px; padding:9px 20px;">{eyebrow}</span>
      <h1 style="font-size:{hfs}px; width:920px; margin-top:30px;">{headline}</h1>
      {sub_html}
    </div>
    <div style="position:absolute; left:72px; top:700px;">{chips_html(chips, 286, 40, 17, 24)}</div>
    <div style="position:absolute; left:72px; top:920px;"><span class="cta" style="font-size:26px; padding:18px 44px;">{cta}</span></div>
    <div class="compliance" style="left:72px; right:72px; bottom:20px; font-size:11px;">{COMPLIANCE}</div>
    """
    render(name, 1080, 1080, body)


square("FB-4_educator_1080x1080",
       "FOR FORMER EDUCATORS",
       'Stay in education.<br><span class="hl">Own the center.</span>', 84,
       "The AI teaches, grades, and plans every lesson. You build enrollment and community.",
       [("0", "lesson plans<br>to write"), ("32&ndash;38", "students to<br>break even"), ("$110K+", "total investment<br>from")],
       "Learn More")

square("FB-6_no-teachers_1080x1080",
       "THE CONTRARIAN MODEL",
       'The most important hire here isn&rsquo;t a teacher. <span class="hl">There isn&rsquo;t one.</span>', 72,
       "A Level 5 adaptive engine delivers all K-12 instruction on smart tablets.",
       [("3,000+", "centers running<br>worldwide"), ("1,200", "sq. ft. lean<br>footprint"), ("$250&ndash;350", "monthly student<br>subscription")],
       "See the Item 19 Numbers")

square("IG-4_zero-in-your-city_1080x1080",
       "FIRST 200 U.S. TERRITORIES",
       '3,000 centers worldwide.<br><span class="hl">Zero in your city &mdash; for now.</span>', 76,
       "The AI-powered learning franchise opens its first U.S. wave, one metro at a time.",
       [("200", "first-wave U.S.<br>territories"), ("32&ndash;38", "students to<br>break even"), ("$110K&ndash;137K", "total<br>investment")],
       "Link in Bio &rarr; Item 19 + Map")

# ---------- IG Carousel 5 slides 1080x1080 ----------
def slide(name, idx, kicker, headline, hfs, body_txt, cta=None, chips=None):
    chips_block = f'<div style="margin-top:48px;">{chips_html(chips, 286, 38, 17, 22)}</div>' if chips else ""
    body_block = f'<p style="font-size:34px; color:rgba(255,255,255,.85); width:900px; line-height:1.45; margin-top:34px;">{body_txt}</p>' if body_txt else ""
    cta_block = f'<div style="margin-top:54px;"><span class="cta" style="font-size:26px; padding:18px 44px;">{cta}</span></div>' if cta else ""
    arrow = '' if cta else f'<div style="position:absolute; right:72px; bottom:88px; color:{ORANGE}; font-size:40px; font-weight:bold;">&rarr;</div>'
    body = f"""
    <div style="position:absolute; left:72px; top:60px;">{brand(30)}</div>
    <div style="position:absolute; right:72px; top:60px; color:rgba(255,255,255,.5); font-size:24px; font-weight:bold;">{idx}/5</div>
    <div style="position:absolute; left:72px; top:200px;">
      <span class="eyebrow" style="font-size:17px; padding:9px 20px;">{kicker}</span>
      <h1 style="font-size:{hfs}px; width:920px; margin-top:34px;">{headline}</h1>
      {body_block}{chips_block}{cta_block}
    </div>
    {arrow}
    <div class="compliance" style="left:72px; right:72px; bottom:20px; font-size:11px;">{COMPLIANCE}</div>
    """
    render(name, 1080, 1080, body)


slide("IG-5_carousel_1of5", 1, "FOR FORMER EDUCATORS",
      'For everyone who left teaching but never stopped <span class="hl">loving education.</span>', 72,
      "Swipe for the ownership model that doesn&rsquo;t need a faculty.")

slide("IG-5_carousel_2of5", 2, "THE OLD WAY BACK IN",
      'Open a tutoring center. Then spend your life <span class="hl">recruiting teachers</span> in a shortage.', 64,
      "More students = more certified teachers = more payroll. Margins shrink as you grow.")

slide("IG-5_carousel_3of5", 3, "THE SQUIRREL AI WAY",
      'A Level 5 AI engine teaches, grades, and plans <span class="hl">every lesson.</span>', 68,
      "Students learn on smart tablets. You build enrollment and community.")

slide("IG-5_carousel_4of5", 4, "THE NUMBERS",
      'Unit economics a faculty <span class="hl">can&rsquo;t match.</span>', 72, "",
      chips=[("$110&ndash;137K", "total<br>investment"), ("$250&ndash;350", "monthly student<br>subscription"), ("32&ndash;38", "students to<br>break even")])

slide("IG-5_carousel_5of5", 5, "200 U.S. TERRITORIES",
      'Training and territory mapping included <span class="hl">from day one.</span>', 68,
      "3,000+ units globally. The first U.S. wave is open now.",
      cta="Link in Bio &rarr; Item 19")

# ---------- IG Story 1080x1920 ----------
story_body = f"""
<div style="position:absolute; left:80px; top:110px;">{brand(34)}</div>
<div style="position:absolute; left:80px; top:330px;">
  <span class="eyebrow" style="font-size:20px; padding:11px 24px;">FRANCHISE OPPORTUNITY</span>
  <h1 style="font-size:96px; width:920px; margin-top:44px;">This franchise&rsquo;s best employee isn&rsquo;t on payroll.<br><span class="hl">It&rsquo;s software.</span></h1>
  <p style="font-size:40px; color:rgba(255,255,255,.85); width:880px; line-height:1.45; margin-top:50px;">
    AI teaches every K-12 lesson on smart tablets. Owners run the center.</p>
</div>
<div style="position:absolute; left:80px; top:1230px;">{chips_html([("3,000+","centers<br>worldwide"),("200","U.S. territories<br>opening"),("32&ndash;38","students to<br>break even")], 286, 44, 19, 26)}</div>
<div style="position:absolute; left:80px; top:1560px;"><span class="cta" style="font-size:34px; padding:24px 56px;">IS MY METRO OPEN? &uarr;</span></div>
<div class="compliance" style="left:80px; right:80px; bottom:34px; font-size:13px;">{COMPLIANCE}</div>
"""
render("IG-6_story_1080x1920", 1080, 1920, story_body)

print("\nAll renders complete:", len(os.listdir(OUT)), "files in", OUT)
