import streamlit as st
import pandas as pd

# ==========================================
# 1. PAGE CONFIG & STYLING
# ==========================================
st.set_page_config(page_title="PSPCL LDHF Calculator", page_icon="⚡", layout="centered")

# Assets Links
PSPCL_LOGO = "https://upload.wikimedia.org/wikipedia/en/3/3a/Punjab_State_Power_Corporation_Limited_logo.png"
INSTA_ICON = "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"
FB_ICON = "https://upload.wikimedia.org/wikipedia/commons/1/1b/Facebook_icon.svg"
X_ICON = "https://upload.wikimedia.org/wikipedia/commons/b/b7/X_logo.jpg"
LINKEDIN_ICON = "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"
BEECLUE_LOGO_WHITE = "https://beeclue.com/wp-content/uploads/2026/02/b-horizontal-logo-w-2048x506.png"

# Custom CSS for effects and layout
st.markdown(f"""
<style>
    /* Main Background */
    .main {{ background-color: #f8f9fa; }}
    
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
    }}
    
    /* Footer & Social Icons */
    .footer-container {{
        text-align: center;
        margin-top: 50px;
        padding: 40px 10px;
        border-top: 1px solid #eee;
    }}
    .social-icon {{
        width: 35px;
        margin: 0 12px;
        transition: transform 0.3s ease, filter 0.3s ease;
        cursor: pointer;
        border-radius: 5px;
    }}
    .social-icon:hover {{
        transform: scale(1.3) translateY(-5px);
        filter: brightness(1.2);
    }}
    
    /* Beeclue Branding Box */
    .beeclue-box {{
        background: linear-gradient(135deg, #001c3d 0%, #003066 100%);
        padding: 15px 25px;
        border-radius: 12px;
        display: inline-block;
        margin-top: 20px;
        transition: 0.3s;
        border: 1px solid rgba(255,255,255,0.1);
    }}
    .beeclue-box:hover {{ transform: scale(1.05); box-shadow: 0 10px 20px rgba(0,0,0,0.2); }}
    .beeclue-img {{ width: 150px; height: auto; }}
    .powered-text {{ color: #aaa; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; }}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. DATA & LOGIC
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
# 3. HEADER
# ==========================================
col_l, col_r = st.columns([1, 4])
with col_l:
    st.image(PSPCL_LOGO, width=100)
with col_r:
    st.title("LDHF (L × D × H × F) Calculator")
    st.caption("Standard Assessment Method as per Annexure-7 (PSPCL)")

# ==========================================
# 4. INPUT CARD
# ==========================================
with st.container():
    st.markdown('<div class="calc-card">', unsafe_allow_html=True)
    
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        load_kw = st.number_input("L — Load found / sanctioned (kW)", min_value=0.0, value=10.0, step=0.01)
    with row1_col2:
        cat_choice = st.selectbox("Category (sets default D, H, F)", list(defaults.keys()))
    
    # Get defaults based on category
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
    
    # Unit Format Toggle
    u_format = st.selectbox("Units Format", ["kWh (units)", "×10³ kWh"])
    
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 5. CALCULATION & RESULTS
# ==========================================
actual_f = f_val / 100 if f_type == "Percent" else f_val
monthly_units = load_kw * days * hours * actual_f

st.markdown('<div class="result-box">', unsafe_allow_html=True)
display_units = monthly_units / 1000 if u_format == "×10³ kWh" else monthly_units
st.subheader(f"Monthly Units: {display_units:,.2f} {u_format.split(' ')[0]}")
st.write(f"**Breakdown:** {load_kw} kW × {days} days × {hours} hrs × {actual_f} = {monthly_units:,.2f} kWh")
st.markdown('</div>', unsafe_allow_html=True)

# Proportionate Calculator Section
st.divider()
st.subheader("📅 Proportionate Days Calculator")
prop_days = st.number_input("Enter number of days for proportionate calculation", min_value=1, value=10)
if days > 0:
    prop_units = (prop_days / days) * monthly_units
    st.info(f"Proportionate Units for {prop_days} days: **{prop_units:,.2f} kWh**")

# ==========================================
# 6. FOOTER & BRANDING
# ==========================================
st.markdown(f"""
<div class="footer-container">
    <p style="font-size: 1.2rem; font-weight: 600; margin-bottom: 5px;">Made with ❤️ by <b>Anuj Narang</b></p>
    <p style="color: #666; margin-bottom: 25px;">Junior Engineer (Electrical) | PSPCL</p>
    
    <div style="margin-bottom: 30px;">
        <a href="https://instagram.com/iamanujnarang" target="_blank"><img src="{INSTA_ICON}" class="social-icon"></a>
        <a href="https://facebook.com/iamanujnarang" target="_blank"><img src="{FB_ICON}" class="social-icon"></a>
        <a href="https://x.com/iamanujnarang" target="_blank"><img src="{X_ICON}" class="social-icon"></a>
        <a href="https://linkedin.com/in/iamanujnarang" target="_blank"><img src="{LINKEDIN_ICON}" class="social-icon"></a>
    </div>
    
    <div class="beeclue-box">
        <div class="powered-text">Powered by</div>
        <a href="https://beeclue.com" target="_blank">
            <img src="{BEECLUE_LOGO_WHITE}" class="beeclue-img">
        </a>
    </div>
    
    <p style="color: #bbb; font-size: 0.8rem; margin-top: 30px;">© 2026 Anuj Narang. Official Annexure-7 Implementation.</p>
</div>
""", unsafe_allow_html=True)
