#!/usr/bin/env python3
"""Render non-educator persona creatives (investors, corporate operators) for Squirrel AI Ad Pack 2."""
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


def render(name, w, h, body):
    html = f"<html><head><style>{page_css(w,h)}</style></head><body>{deco(w,h)}{body}</body></html>"
    pdf = f"/tmp/{name}.pdf"
    HTML(string=html).write_pdf(pdf)
    doc = fitz.open(pdf)
    pix = doc[0].get_pixmap(matrix=fitz.Matrix(4/3, 4/3))
    pix.save(os.path.join(OUT, f"{name}.png"))
    print(f"{name}.png  {pix.width}x{pix.height}")


def linkedin(name, eyebrow, headline, chips, cta, hfs=54):
    body = f"""
    <div style="position:absolute; left:64px; top:44px;">{brand(28)}</div>
    <div style="position:absolute; left:64px; top:108px;">
      <span class="eyebrow" style="font-size:15px; padding:8px 18px;">{eyebrow}</span>
      <h1 style="font-size:{hfs}px; width:920px; margin-top:22px;">{headline}</h1>
    </div>
    <div style="position:absolute; left:64px; top:380px;">{chips_html(chips, 218, 30, 14, 18)}</div>
    <div style="position:absolute; left:64px; top:512px;"><span class="cta" style="font-size:20px; padding:14px 34px;">{cta}</span></div>
    <div class="compliance" style="left:64px; right:64px; bottom:16px; font-size:10px;">{COMPLIANCE}</div>
    """
    render(name, 1200, 627, body)


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


# --- LinkedIn 1200x627 ---
linkedin("LI-10_corporate-exit_1200x627",
         "FOR CORPORATE OPERATORS",
         'Stop building someone else&rsquo;s empire. <span class="hl">Start operating your own.</span>',
         [("0", "inventory or<br>supply chain"), ("$250&ndash;350", "monthly recurring<br>subscriptions"), ("&lt;40", "students to<br>break even")],
         "Check Territory Availability &rarr;", hfs=50)

linkedin("LI-11_portfolio_1200x627",
         "FOR MULTI-UNIT INVESTORS",
         'Add education to your portfolio &mdash; <span class="hl">without adding a faculty.</span>',
         [("3,000+", "units operating<br>globally"), ("200", "first-wave U.S.<br>territories"), ("85&ndash;90%", "gross margin<br>per seat")],
         "Download the Item 19 &rarr;", hfs=50)

# --- Square 1080x1080 ---
square("FB-8_no-license_1080x1080",
       "NO EDUCATION BACKGROUND NEEDED",
       'No teaching license.<br>No education degree.<br><span class="hl">No problem.</span>', 76,
       "The AI does the teaching. Your launch includes initial training and a mapped territory.",
       [("0", "certified teachers<br>to recruit"), ("Day 1", "training &amp; territory<br>mapping included"), ("$110K+", "total investment<br>from")],
       "Learn More")

square("FB-9_operator_1080x1080",
       "FOR BUSINESS OPERATORS",
       'You run the business.<br><span class="hl">Software runs the classroom.</span>', 76,
       "Enrollment, community, operations &mdash; the skills you already have. The teaching is handled.",
       [("1,200", "sq. ft. lean<br>footprint"), ("32&ndash;38", "students to<br>break even"), ("$250&ndash;350", "monthly student<br>subscription")],
       "See How the Model Works")

square("IG-8_second-act_1080x1080",
       "LIFE AFTER CORPORATE",
       'Your second act shouldn&rsquo;t come with <span class="hl">a payroll department.</span>', 76,
       "A lean, subscription-based learning center &mdash; no certified-teacher payroll, no inventory.",
       [("3,000+", "centers running<br>worldwide"), ("200", "U.S. territories<br>opening"), ("$110K&ndash;137K", "total<br>investment")],
       "Link in Bio &rarr; Item 19")

# --- Story 1080x1920 ---
story_body = f"""
<div style="position:absolute; left:80px; top:110px;">{brand(34)}</div>
<div style="position:absolute; left:80px; top:330px;">
  <span class="eyebrow" style="font-size:20px; padding:11px 24px;">LEAVING CORPORATE?</span>
  <h1 style="font-size:92px; width:920px; margin-top:44px;">Don&rsquo;t trade a boss for <span class="hl">a staffing problem.</span></h1>
  <p style="font-size:40px; color:rgba(255,255,255,.85); width:880px; line-height:1.45; margin-top:50px;">
    At Squirrel AI Learning, software teaches every K-12 lesson. You operate the business &mdash; no certified-teacher payroll, no inventory.</p>
</div>
<div style="position:absolute; left:80px; top:1230px;">{chips_html([("0","certified teachers<br>on payroll"),("&lt;40","students to<br>break even"),("$110K+","total investment<br>from")], 286, 44, 19, 26)}</div>
<div style="position:absolute; left:80px; top:1560px;"><span class="cta" style="font-size:34px; padding:24px 56px;">IS MY METRO OPEN? &uarr;</span></div>
<div class="compliance" style="left:80px; right:80px; bottom:34px; font-size:13px;">{COMPLIANCE}</div>
"""
render("IG-9_story_corporate-exit_1080x1920", 1080, 1920, story_body)

print("\nDone.")
