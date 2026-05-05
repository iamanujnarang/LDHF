import streamlit as st
import pandas as pd
import numpy as np

# ==========================================
# 1. PAGE CONFIG & STYLING
# ==========================================
st.set_page_config(page_title="PSPCL LDHF Calculator", page_icon="⚡", layout="centered")

# Updated Assets Links
PSPCL_LOGO_URL = "https://pspcl.in/assets/images/logo.png"
# Use the direct PNG link for Beeclue
BEECLUE_LOGO_PNG = "https://beeclue.com/wp-content/uploads/2026/02/b-horizontal-logo-w-2048x506.png"
INSTA_ICON = "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"
FB_ICON = "https://upload.wikimedia.org/wikipedia/commons/1/1b/Facebook_icon.svg"
X_ICON = "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" # Updated to LinkedIn Icon
LINKEDIN_ICON = "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"

# Custom CSS for UI/UX and Branding
st.markdown(f"""
<style>
    .main {{ background-color: #f8f9fa; }}
    
    /* Center the Logo */
    .logo-container {{
        display: flex;
        justify-content: center;
        margin-bottom: 10px;
    }}
    
    .title-container {{
        text-align: center;
        margin-bottom: 30px;
    }}

    /* Card Style */
    .calc-card {{
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.05);
        border: 1px solid #e6e6e6;
        margin-bottom: 20px;
    }}
    
    /* Results Box */
    .result-box {{
        background-color: #f7fbff;
        border: 1px solid #dfefff;
        padding: 15px;
        border-radius: 10px;
        margin-top: 15px;
        text-align: center;
    }}
    
    /* Footer Container */
    .footer-container {{
        text-align: center;
        margin-top: 50px;
        padding: 40px 20px;
        border-top: 1px solid #eee;
        background-color: #ffffff;
    }}

    /* Social Icons Styling */
    .social-icon {{
        width: 32px;
        margin: 0 10px;
        transition: transform 0.3s ease;
        display: inline-block;
    }}
    .social-icon:hover {{
        transform: scale(1.2);
    }}

    /* Beeclue Tech Box */
    .beeclue-box {{
        background: #0f172a;
        padding: 15px 25px;
        border-radius: 12px;
        display: inline-block;
        margin-top: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }}
    .beeclue-img {{
        width: 160px;
        height: auto;
        display: block;
        margin: 0 auto;
    }}
    .powered-text {{
        color: #94a3b8;
        font-size: 0.65rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }}

    .made-with-love {{
        font-size: 1rem;
        color: #334155;
        margin-top: 20px;
    }}
    .heart-symbol {{
        color: #e63946;
    }}
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
    "Non-Residential (continuous) – hospitals, hotels": {"D": 30, "H": 20, "F": 0.40},
    "Non-Residential (general)": {"D": 25, "H": 12, "F": 0.40},
    "Bulk Supply": {"D": 30, "H": 8, "F": 0.40},
    "Public lighting": {"D": 30, "H": 8, "F": 0.40},
    "Other / Temporary": {"D": 30, "H": 12, "F": 0.60}
}

# ==========================================
# 3. HEADER (Centered Logo & Clean Title)
# ==========================================
st.markdown(f"""
<div class="logo-container">
    <img src="{PSPCL_LOGO_URL}" width="100">
</div>
<div class="title-container">
    <h1 style="margin-bottom:0;">LDHF Calculator</h1>
    <p style="color: #6b7280;">Official Assessment Method (PSPCL)</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 4. INPUT SECTION
# ==========================================
with st.container():
    st.markdown('<div class="calc-card">', unsafe_allow_html=True)
    
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        load_kw = st.number_input("L — Load found / sanctioned (kW)", min_value=0.0, value=10.0, step=0.01)
    with row1_col2:
        cat_choice = st.selectbox("Category (sets default D, H, F)", list(defaults.keys()))
    
    def_d = defaults[cat_choice]["D"]
    def_h = defaults[cat_choice]["H"]
    def_f = defaults[cat_choice]["F"]
    
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        days = st.number_input("D — Working days per month", min_value=0, value=def_d, step=1)
    with row2_col2:
        hours = st.number_input("H — Hours of use per day", min_value=0.0, max_value=24.0, value=float(def_h), step=0.1)
        if cat_choice == "Agriculture Supply / AP High Tech":
            st.info("Note: AP feeder = 4 hrs; Urban = 12 hrs.")
            
    row3_col1, row3_col2 = st.columns([2, 1])
    with row3_col1:
        f_val = st.number_input("F — Demand factor", min_value=0.0, value=float(def_f), step=0.01)
    with row3_col2:
        f_type = st.radio("F Format", ["Decimal", "Percent"], horizontal=True)
    
    u_format = st.selectbox("Units Format", ["kWh (units)", "×10³ kWh"])
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 5. CALCULATION
# ==========================================
actual_f = f_val / 100 if f_type == "Percent" else f_val
monthly_units = load_kw * days * hours * actual_f

st.markdown('<div class="result-box">', unsafe_allow_html=True)
display_units = monthly_units / 1000 if u_format == "×10³ kWh" else monthly_units
st.subheader(f"Monthly Units: {display_units:,.2f} {u_format.split(' ')[0]}")
st.write(f"**Breakdown:** {load_kw}L × {days}D × {hours}H × {actual_f}F")
st.markdown('</div>', unsafe_allow_html=True)

# Proportionate Calculator
st.divider()
st.subheader("📅 Proportionate Days Calculator")
prop_days = st.number_input("Enter number of days", min_value=1, value=10)
if days > 0:
    prop_units = (prop_days / days) * monthly_units
    st.success(f"Proportionate Units for {prop_days} days: **{prop_units:,.2f} kWh**")

# ==========================================
# 6. FOOTER & BRANDING
# ==========================================
st.markdown(f"""
<div class="footer-container">
    <div style="margin-bottom: 25px;">
        <a href="https://instagram.com/iamanujnarang" target="_blank"><img src="{INSTA_ICON}" class="social-icon"></a>
        <a href="https://facebook.com/iamanujnarang" target="_blank"><img src="{FB_ICON}" class="social-icon"></a>
        <a href="https://linkedin.com/in/iamanujnarang" target="_blank"><img src="{LINKEDIN_ICON}" class="social-icon"></a>
    </div>

    <div class="beeclue-box">
        <div class="powered-text">In Strategic Collaboration with</div>
        <a href="https://beeclue.com" target="_blank">
            <img src="{BEECLUE_LOGO_PNG}" class="beeclue-img">
        </a>
    </div>

    <div class="made-with-love">
        Made with <span class="heart-symbol">❤️</span> by <b>Anuj Narang, JE PSPCL</b>
    </div>

    <div style="color: #94a3b8; font-size: 0.8rem; margin-top: 10px;">
        © 2026 | Supply Code 2024 Guidelines
    </div>
</div>
""", unsafe_allow_html=True)
