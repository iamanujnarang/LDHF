import streamlit as st
import pandas as pd
import numpy as np

# ==========================================
# 1. PAGE CONFIG
# ==========================================
st.set_page_config(page_title="PSPCL LDHF Calculator", page_icon="⚡", layout="centered")

# Assets Links
PSPCL_LOGO_URL = "https://pspcl.in/assets/images/logo.png"
BEECLUE_LOGO_PNG = "https://beeclue.com/wp-content/uploads/2026/02/b-horizontal-logo-w-2048x506.png"
INSTA_ICON = "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"
FB_ICON = "https://upload.wikimedia.org/wikipedia/commons/1/1b/Facebook_icon.svg"
X_ICON = "https://upload.wikimedia.org/wikipedia/commons/b/b7/X_logo.jpg"
LINKEDIN_ICON = "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"

# ==========================================
# 2. CSS STYLING (Separated to avoid f-string conflicts)
# ==========================================
st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .calc-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.05);
        border: 1px solid #e6e6e6;
        margin-bottom: 20px;
    }
    .result-box {
        background-color: #f7fbff;
        border: 1px solid #dfefff;
        padding: 15px;
        border-radius: 10px;
        margin-top: 15px;
    }
    .footer-container {
        text-align: center;
        margin-top: 50px;
        padding: 40px 20px;
        border-top: 1px solid #eee;
        background-color: #ffffff;
    }
    .social-icon {
        width: 38px;
        margin: 0 15px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        cursor: pointer;
        border-radius: 8px;
    }
    .social-icon:hover {
        transform: scale(1.4) translateY(-8px);
        filter: drop-shadow(0 10px 15px rgba(0,0,0,0.2));
    }
    .beeclue-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 20px 35px;
        border-radius: 15px;
        display: inline-block;
        margin-top: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .beeclue-img { width: 180px; height: auto; }
    .powered-text {
        color: #94a3b8;
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 8px;
        font-weight: 600;
    }
    .made-with-love {
        font-size: 1.1rem;
        color: #334155;
        margin-bottom: 20px; /* Space before social icons */
        font-weight: 500;
    }
    .heart-symbol {
        color: #e63946;
        display: inline-block;
        animation: heartbeat 1.5s infinite;
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    .copyright { color: #94a3b8; font-size: 0.85rem; margin-top: 15px; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. HEADER
# ==========================================
col_l, col_r = st.columns([1, 4])
with col_l:
    st.image(PSPCL_LOGO_URL, width=100)
with col_r:
    st.title("LDHF (L × D × H × F) Calculator")
    st.caption("Standard Assessment Method as per Annexure-7 (PSPCL)[cite: 1]")

# ==========================================
# 4. INPUT SECTION[cite: 1]
# ==========================================
defaults = {
    "Continuous process industry": {"D": 30, "H": 24, "F": 1.00},
    "Non-continuous process industry": {"D": 25, "H": 16, "F": 0.60},
    "Single shift industry": {"D": 30, "H": 8, "F": 0.60},
    "Domestic": {"D": 30, "H": 8, "F": 0.30},
    "Agriculture Supply / AP High Tech": {"D": 30, "H": 12, "F": 1.00},
    "Non-Residential (continuous) – hospitals, hotels": {"D": 30, "H": 20, "F": 0.40},
    "Non-Residential (general)": {"D": 25, "H": 12, "F": 0.40},
    "Bulk Supply": {"D": 30, "H": 8, "F": 0.40},
    "Public lighting": {"D": 30, "H": 8, "F": 0.40},
    "Other / Temporary": {"D": 30, "H": 12, "F": 0.60}
}

with st.container():
    st.markdown('<div class="calc-card">', unsafe_allow_html=True)
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        load_kw = st.number_input("L — Load found / sanctioned (kW)", min_value=0.0, value=10.0, step=0.01)
    with row1_col2:
        cat_choice = st.selectbox("Category (sets default D, H, F)", list(defaults.keys()))
    
    def_d, def_h, def_f = defaults[cat_choice]["D"], defaults[cat_choice]["H"], defaults[cat_choice]["F"]
    
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        days = st.number_input("D — Working days per month", min_value=0, value=def_d, step=1)
    with row2_col2:
        hours = st.number_input("H — Hours of use per day", min_value=0.0, max_value=24.0, value=float(def_h), step=0.1)
        if cat_choice == "Agriculture Supply / AP High Tech":
            st.info("Note: AP feeder = 4 hrs; Urban = 12 hrs.[cite: 1]")
            
    row3_col1, row3_col2 = st.columns([2, 1])
    with row3_col1:
        f_val = st.number_input("F — Demand factor", min_value=0.0, value=float(def_f), step=0.01)
    with row3_col2:
        f_type = st.radio("F Format", ["Decimal", "Percent"], horizontal=True)
    
    u_format = st.selectbox("Units Format", ["kWh (units)", "×10³ kWh"])
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 5. CALCULATION[cite: 1]
# ==========================================
actual_f = f_val / 100 if f_type == "Percent" else f_val
monthly_units = load_kw * days * hours * actual_f

st.markdown('<div class="result-box">', unsafe_allow_html=True)
display_units = monthly_units / 1000 if u_format == "×10³ kWh" else monthly_units
st.subheader(f"Monthly Units: {display_units:,.2f} {u_format.split(' ')[0]}")
st.write(f"**Breakdown:** {load_kw} kW × {days} days × {hours} hrs × {actual_f} = {monthly_units:,.2f} kWh")
st.markdown('</div>', unsafe_allow_html=True)

st.divider()
st.subheader("📅 Proportionate Days Calculator")
prop_days = st.number_input("Enter number of days for proportionate calculation", min_value=1, value=10)
if days > 0:
    prop_units = (prop_days / days) * monthly_units
    st.info(f"Proportionate Units for {prop_days} days: **{prop_units:,.2f} kWh**")

# ==========================================
# 6. FOOTER & BRANDING (Fixed Rendering)
# ==========================================
footer_html = f"""
<div class="footer-container">
    <!-- Made with Love moved UP -->
    <div class="made-with-love">
        Made with <span class="heart-symbol">❤️</span> by <b>Anuj Narang, JE PSPCL</b>
    </div>

    <!-- Social Icons -->
    <div style="margin-bottom: 35px;">
        <a href="https://instagram.com/iamanujnarang" target="_blank"><img src="{INSTA_ICON}" class="social-icon"></a>
        <a href="https://facebook.com/iamanujnarang" target="_blank"><img src="{FB_ICON}" class="social-icon"></a>
        <a href="https://x.com/iamanujnarang" target="_blank"><img src="{X_ICON}" class="social-icon"></a>
        <a href="https://linkedin.com/in/iamanujnarang" target="_blank"><img src="{LINKEDIN_ICON}" class="social-icon"></a>
    </div>

    <!-- Beeclue Box -->
    <div class="beeclue-box">
        <div class="powered-text">In Strategic Collaboration with</div>
        <a href="https://beeclue.com" target="_blank">
            <img src="{BEECLUE_LOGO_PNG}" class="beeclue-img">
        </a>
    </div>

    <div class="copyright">
        © 2026 Official LDHF Calculator as per Supply Code 2024[cite: 1]
    </div>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
