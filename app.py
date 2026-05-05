import streamlit as st

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
# 2. CSS STYLING (Fixed for Streamlit)
# ==========================================
st.markdown("""
<style>
    /* Top Logo Centering */
    .top-logo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .top-logo {
        width: 120px;
    }

    /* Card & UI */
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

    /* Footer Layout */
    .footer-container {
        text-align: center;
        margin-top: 50px;
        padding: 40px 20px;
        border-top: 1px solid #eee;
    }

    /* Made with Love */
    .made-with-love {
        font-size: 1.2rem;
        color: #334155;
        margin-bottom: 20px;
        font-weight: 600;
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

    /* Social Icons */
    .social-icon {
        width: 38px;
        margin: 0 12px;
        transition: all 0.4s ease;
    }
    .social-icon:hover {
        transform: scale(1.3) translateY(-5px);
        filter: drop-shadow(0 5px 10px rgba(0,0,0,0.2));
    }

    /* Beeclue Box */
    .beeclue-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 20px 40px;
        border-radius: 15px;
        display: inline-block;
        margin-top: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .beeclue-img {
        width: 180px;
        height: auto;
    }
    .powered-text {
        color: #94a3b8;
        font-size: 0.7rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 10px;
    }
    .copyright {
        color: #94a3b8;
        font-size: 0.8rem;
        margin-top: 15px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. TOP LOGO
# ==========================================
st.markdown(f"""
<div class="top-logo-container">
    <img src="{PSPCL_LOGO_URL}" class="top-logo">
</div>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>LDHF Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Standard Assessment Method (Annexure-7)[cite: 1]</p>", unsafe_allow_html=True)

# ==========================================
# 4. CALCULATOR LOGIC
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

with st.container():
    st.markdown('<div class="calc-card">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        load_kw = st.number_input("L — Load (kW)", min_value=0.0, value=10.0)
    with col2:
        cat = st.selectbox("Category", list(defaults.keys()))

    col3, col4 = st.columns(2)
    with col3:
        days = st.number_input("D — Working Days", value=defaults[cat]["D"])
    with col4:
        hours = st.number_input("H — Hours/Day", value=float(defaults[cat]["H"]))

    f_val = st.number_input("F — Demand Factor", value=float(defaults[cat]["F"]))
    st.markdown('</div>', unsafe_allow_html=True)

# Result
monthly_units = load_kw * days * hours * f_val
st.markdown(f"""
<div class="result-box">
    <h3>Monthly Units: {monthly_units:,.2f} kWh</h3>
    <small>Calculation: {load_kw} * {days} * {hours} * {f_val}</small>
</div>
""", unsafe_allow_html=True)

# ==========================================
# 5. FOOTER (Branding Fixed)
# ==========================================
st.markdown(f"""
<div class="footer-container">
    
    <!-- 1. Made with Love (Now at Top) -->
    <div class="made-with-love">
        Made with <span class="heart-symbol">❤️</span> by <b>Anuj Narang, JE PSPCL</b>
    </div>

    <!-- 2. Social Icons -->
    <div style="margin-bottom: 20px;">
        <a href="https://instagram.com/iamanujnarang" target="_blank"><img src="{INSTA_ICON}" class="social-icon"></a>
        <a href="https://facebook.com/iamanujnarang" target="_blank"><img src="{FB_ICON}" class="social-icon"></a>
        <a href="https://x.com/iamanujnarang" target="_blank"><img src="{X_ICON}" class="social-icon"></a>
        <a href="https://linkedin.com/in/iamanujnarang" target="_blank"><img src="{LINKEDIN_ICON}" class="social-icon"></a>
    </div>

    <!-- 3. Beeclue Box -->
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
""", unsafe_allow_html=True)
