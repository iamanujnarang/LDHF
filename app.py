import streamlit as st

# ==========================================
# 1. PAGE CONFIG & ASSETS
# ==========================================
st.set_page_config(page_title="PSPCL LDHF Calculator", page_icon="⚡", layout="centered")

PSPCL_LOGO_URL = "https://pspcl.in/assets/images/logo.png"
BEECLUE_LOGO_PNG = "https://beeclue.com/wp-content/uploads/2026/02/b-horizontal-logo-w-2048x506.png"
INSTA_ICON = "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"
FB_ICON = "https://upload.wikimedia.org/wikipedia/commons/1/1b/Facebook_icon.svg"
X_ICON = "https://upload.wikimedia.org/wikipedia/commons/b/b7/X_logo.jpg"
LINKEDIN_ICON = "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"

# ==========================================
# 2. CSS STYLING (Brackets separate to avoid F-string conflict)
# ==========================================
st.markdown("""
<style>
    .top-logo-container { display: flex; justify-content: center; margin-bottom: 10px; }
    .top-logo { width: 140px; }
    .calc-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.05);
        border: 1px solid #e6e6e6;
    }
    .result-box {
        background-color: #f0f7ff;
        border: 1px solid #cce3ff;
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
        text-align: center;
    }
    .footer-container { text-align: center; margin-top: 60px; padding: 40px 10px; border-top: 1px solid #eee; }
    .made-with-love { font-size: 1.2rem; color: #334155; margin-bottom: 20px; font-weight: 600; }
    .heart-symbol { color: #e63946; display: inline-block; animation: heartbeat 1.5s infinite; }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    .social-icon { width: 38px; margin: 0 10px; transition: transform 0.3s ease; }
    .social-icon:hover { transform: scale(1.3) translateY(-5px); }
    .beeclue-box { 
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); 
        padding: 25px 40px; 
        border-radius: 15px; 
        display: inline-block; 
        margin-top: 30px; 
        border: 1px solid rgba(255, 255, 255, 0.1); 
    }
    .beeclue-img { width: 200px; height: auto; }
    .powered-text { color: #94a3b8; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 12px; }
    .copyright { color: #94a3b8; font-size: 0.8rem; margin-top: 20px; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. HEADER & CALCULATION LOGIC[cite: 1]
# ==========================================
st.markdown(f'<div class="top-logo-container"><img src="{PSPCL_LOGO_URL}" class="top-logo"></div>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>LDHF Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Standard Assessment Method (Annexure-7)</p>", unsafe_allow_html=True)

# Table for Annexure-7 defaults[cite: 1]
defaults = {
    "Continuous process industry": {"D": 30, "H": 24, "F": 1.00},
    "Non-continuous process industry": {"D": 25, "H": 16, "F": 0.60},
    "Single shift industry": {"D": 30, "H": 8, "F": 0.60},
    "Domestic": {"D": 30, "H": 8, "F": 0.30},
    "Agriculture Supply": {"D": 30, "H": 12, "F": 1.00},
    "Non-Residential (continuous)": {"D": 30, "H": 20, "F": 0.40},
    "Non-Residential (general)": {"D": 25, "H": 12, "F": 0.40},
    "Bulk Supply": {"D": 30, "H": 8, "F": 0.40}
}

with st.container():
    st.markdown('<div class="calc-card">', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        load = st.number_input("L — Connected Load (kW)", min_value=0.0, value=10.0, step=0.5)
    with c2:
        cat = st.selectbox("Category", list(defaults.keys()))
    
    c3, c4 = st.columns(2)
    with c3:
        days = st.number_input("D — Working Days", value=defaults[cat]["D"])
    with c4:
        hours = st.number_input("H — Hours of Use/Day", value=float(defaults[cat]["H"]))
    
    factor = st.number_input("F — Demand Factor", value=float(defaults[cat]["F"]), step=0.01)
    st.markdown('</div>', unsafe_allow_html=True)

# Final Formula: L * D * H * F[cite: 1]
monthly_units = load * days * hours * factor

st.markdown(f"""
<div class="result-box">
    <h2 style="margin:0; color:#0b79d0;">{monthly_units:,.2f} Units (kWh)</h2>
    <p style="color:#666; margin-top:5px;">Estimated Monthly Assessment</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 4. FINAL FOOTER
# ==========================================
footer_html = f"""
<div class="footer-container">
    <div class="made-with-love">
        Made with <span class="heart-symbol">❤️</span> by <b>Anuj Narang, JE PSPCL</b>
    </div>
    
    <div style="margin-bottom: 25px;">
        <a href="https://instagram.com/iamanujnarang" target="_blank"><img src="{INSTA_ICON}" class="social-icon"></a>
        <a href="https://facebook.com/iamanujnarang" target="_blank"><img src="{FB_ICON}" class="social-icon"></a>
        <a href="https://x.com/iamanujnarang" target="_blank"><img src="{X_ICON}" class="social-icon"></a>
        <a href="https://linkedin.com/in/iamanujnarang" target="_blank"><img src="{LINKEDIN_ICON}" class="social-icon"></a>
    </div>

    <div class="beeclue-box">
        <div class="powered-text">In Strategic Collaboration with</div>
        <a href="https://beeclue.com" target="_blank">
            <img src="{BEECLUE_LOGO_PNG}" class="beeclue-img">
        </a>
    </div>

    <div class="copyright">
        © 2026 Official Annexure-7 Standard Implementation[cite: 1]
    </div>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
