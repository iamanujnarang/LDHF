import streamlit as st
import pandas as pd
import numpy as np

# ==========================================
# 1. PAGE CONFIG & STYLING
# ==========================================
st.set_page_config(page_title="PSPCL LDHF Calculator", page_icon="⚡", layout="centered")

# Assets Links
PSPCL_LOGO_URL = "https://pspcl.in/assets/images/logo.png"
BEECLUE_LOGO_PNG = "https://beeclue.com/wp-content/uploads/2026/02/b-horizontal-logo-w-2048x506.png"
INSTA_ICON = "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"
FB_ICON = "https://upload.wikimedia.org/wikipedia/commons/1/1b/Facebook_icon.svg"
X_ICON = "https://upload.wikimedia.org/wikipedia/commons/5/53/X_logo_2023_original.svg"
LINKEDIN_ICON = "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"

# Custom CSS (Sab ek line mein ya zero indentation ke saath taaki code box na bane)
st.markdown(f"""
<style>
.main {{ background-color: #f8f9fa; }}
.logo-container {{ display: flex; justify-content: center; margin-bottom: 10px; }}
.title-container {{ text-align: center; margin-bottom: 30px; }}
.calc-card {{ background: white; padding: 25px; border-radius: 15px; box-shadow: 0 6px 18px rgba(0,0,0,0.05); border: 1px solid #e6e6e6; margin-bottom: 20px; }}
.result-box {{ background-color: #f7fbff; border: 1px solid #dfefff; padding: 15px; border-radius: 10px; margin-top: 15px; text-align: center; }}
.footer-container {{ text-align: center; margin-top: 50px; padding: 40px 20px; border-top: 1px solid #eee; }}
.social-icon {{ width: 28px; margin: 0 12px; transition: transform 0.3s ease; display: inline-block; vertical-align: middle; }}
.social-icon:hover {{ transform: scale(1.2); }}
.beeclue-box {{ background: #0f172a; padding: 20px 30px; border-radius: 12px; display: inline-block; margin-top: 25px; border: 1px solid rgba(255, 255, 255, 0.1); }}
.beeclue-img {{ width: 170px; height: auto; display: block; margin: 0 auto; }}
.powered-text {{ color: #94a3b8; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 10px; font-weight: 600; }}
.made-with-love {{ font-size: 1.1rem; color: #1e293b; margin-bottom: 15px; font-weight: 500; }}
.heart-symbol {{ color: #e63946; }}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LOGIC & DEFAULTS
# ==========================================
defaults = {
    "Continuous process industry": {"D": 30, "H": 24, "F": 1.00},
    "Non-continuous process industry": {"D": 25, "H": 16, "F": 0.60},
    "Single shift industry": {"D": 30, "H": 8, "F": 0.60},
    "Domestic": {"D": 30, "H": 8, "F": 0.30},
    "Agriculture Supply / AP High Tech": {"D": 30, "H": 12, "F": 1.00},
    "Non-Residential (continuous)": {"D": 30, "H": 20, "F": 0.40},
    "Non-Residential (general)": {"D": 25, "H": 12, "F": 0.40},
    "Bulk Supply": {"D": 30, "H": 8, "F": 0.40},
    "Public lighting": {"D": 30, "H": 8, "F": 0.40},
    "Other / Temporary": {"D": 30, "H": 12, "F": 0.60}
}

# ==========================================
# 3. HEADER
# ==========================================
st.markdown(f'<div class="logo-container"><img src="{PSPCL_LOGO_URL}" width="100"></div>', unsafe_allow_html=True)
st.markdown('<div class="title-container"><h1 style="margin-bottom:0;">LDHF Calculator</h1><p style="color: #64748b;">Official Assessment Method (PSPCL)</p></div>', unsafe_allow_html=True)

# ==========================================
# 4. INPUT SECTION
# ==========================================
with st.container():
    st.markdown('<div class="calc-card">', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    load_kw = c1.number_input("L — Load found / sanctioned (kW)", min_value=0.0, value=10.0, step=0.01)
    cat_choice = c2.selectbox("Category (sets default D, H, F)", list(defaults.keys()))
    
    def_d, def_h, def_f = defaults[cat_choice]["D"], defaults[cat_choice]["H"], defaults[cat_choice]["F"]
    
    c3, c4 = st.columns(2)
    days = c3.number_input("D — Working days per month", min_value=0, value=def_d)
    hours = c4.number_input("H — Hours of use per day", min_value=0.0, max_value=24.0, value=float(def_h))
    
    # Agriculture Note restoration
    if cat_choice == "Agriculture Supply / AP High Tech":
        st.info("Note: AP feeder = 4 hrs; Urban = 12 hrs.")
    
    c5, c6 = st.columns([2, 1])
    f_val = c5.number_input("F — Demand factor", min_value=0.0, value=float(def_f), step=0.01)
    f_type = c6.radio("F Format", ["Decimal", "Percent"], horizontal=True)
    u_format = st.selectbox("Units Format", ["kWh (units)", "×10³ kWh"])
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 5. CALCULATION
# ==========================================
actual_f = f_val / 100 if f_type == "Percent" else f_val
monthly_units = load_kw * days * hours * actual_f
display_units = monthly_units / 1000 if u_format == "×10³ kWh" else monthly_units

st.markdown(f'<div class="result-box"><h3>Monthly Units: {display_units:,.2f} {u_format.split(" ")[0]}</h3><p><b>Formula:</b> {load_kw}L × {days}D × {hours}H × {actual_f}F</p></div>', unsafe_allow_html=True)

st.divider()
st.subheader("📅 Proportionate Days Calculator")
prop_days = st.number_input("Enter number of days", min_value=1, value=10)
if days > 0:
    prop_units = (prop_days / days) * monthly_units
    st.success(f"Proportionate Units for {prop_days} days: **{prop_units:,.2f} kWh**")

# ==========================================
# 6. FOOTER & BRANDING (Strictly No Indentation)
# ==========================================
footer_html = f"""
<div class="made-with-love">Made with <span class="heart-symbol">❤️</span> by <b>Anuj Narang, JE PSPCL</b></div> <div style="margin-bottom: 25px;"> <a href="https://instagram.com/iamanujnarang" target="_blank"><img src="{INSTA_ICON}" class="social-icon"></a> <a href="https://facebook.com/iamanujnarang" target="_blank"><img src="{FB_ICON}" class="social-icon"></a> <a href="https://x.com/iamanujnarang" target="_blank"><img src="{X_ICON}" class="social-icon"></a> <a href="https://linkedin.com/in/iamanujnarang" target="_blank"><img src="{LINKEDIN_ICON}" class="social-icon"></a> </div> <div class="beeclue-box"> <div class="powered-text">In Strategic Collaboration with</div> <a href="https://beeclue.com" target="_blank"> <img src="{BEECLUE_LOGO_PNG}" class="beeclue-img"> </a> </div> <div style="color: #94a3b8; font-size: 0.85rem; margin-top: 20px;">© 2026 | Supply Code 2024 Guidelines</div> </div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
