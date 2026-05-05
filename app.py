import streamlit as st

# ==========================================
# 1. PAGE CONFIG
# ==========================================
st.set_page_config(page_title="PSPCL LDHF Calculator", page_icon="⚡", layout="centered")

# Assets
PSPCL_LOGO_URL = "https://pspcl.in/assets/images/logo.png"
BEECLUE_LOGO_PNG = "https://beeclue.com/wp-content/uploads/2026/02/b-horizontal-logo-w-2048x506.png"
INSTA_ICON = "https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png"
FB_ICON = "https://upload.wikimedia.org/wikipedia/commons/1/1b/Facebook_icon.svg"
X_ICON = "https://upload.wikimedia.org/wikipedia/commons/b/b7/X_logo.jpg"
LINKEDIN_ICON = "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"

# ==========================================
# 2. CSS
# ==========================================
st.markdown("""
<style>

/* Center Logo */
.top-logo {
    display: flex;
    justify-content: center;
    margin-top: -20px;
}
.top-logo img {
    width: 140px;
}

/* Card */
.calc-card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.05);
    border: 1px solid #e6e6e6;
    margin-bottom: 20px;
}

/* Result */
.result-box {
    background-color: #f7fbff;
    border: 1px solid #dfefff;
    padding: 15px;
    border-radius: 10px;
    margin-top: 15px;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 50px;
    padding: 40px 10px;
    border-top: 1px solid #eee;
}

/* Social Icons */
.social-icon {
    width: 38px;
    margin: 0 12px;
    transition: all 0.3s ease;
}
.social-icon:hover {
    transform: scale(1.3) translateY(-6px);
}

/* Made with love */
.made {
    font-size: 1.1rem;
    margin-bottom: 15px;
}
.heart {
    color: red;
    animation: beat 1.5s infinite;
}
@keyframes beat {
    0% {transform: scale(1);}
    50% {transform: scale(1.2);}
    100% {transform: scale(1);}
}

/* Beeclue box */
.beeclue-box {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    padding: 20px;
    border-radius: 15px;
    display: inline-block;
    margin-top: 25px;
    transition: 0.3s;
}
.beeclue-box:hover {
    transform: translateY(-5px);
}
.beeclue-box img {
    width: 180px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. HEADER (CENTER LOGO FIX)
# ==========================================
st.markdown(f"""
<div class="top-logo">
    <img src="{PSPCL_LOGO_URL}">
</div>
""", unsafe_allow_html=True)

st.title("LDHF (L × D × H × F) Calculator")
st.caption("Standard Assessment Method (Annexure-7)")

# ==========================================
# 4. INPUT
# ==========================================
defaults = {
    "Domestic": {"D": 30, "H": 8, "F": 0.30},
    "Industry": {"D": 25, "H": 16, "F": 0.60},
}

st.markdown('<div class="calc-card">', unsafe_allow_html=True)

l = st.number_input("Load (kW)", value=10.0)
cat = st.selectbox("Category", list(defaults.keys()))

d = st.number_input("Days", value=defaults[cat]["D"])
h = st.number_input("Hours", value=float(defaults[cat]["H"]))
f = st.number_input("Factor", value=float(defaults[cat]["F"]))

st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 5. RESULT
# ==========================================
units = l * d * h * f

st.markdown('<div class="result-box">', unsafe_allow_html=True)
st.subheader(f"Units: {units:.2f} kWh")
st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 6. FOOTER (FIXED ORDER)
# ==========================================
st.markdown(f"""
<div class="footer">

    <div class="made">
        Made with <span class="heart">❤️</span> by <b>Anuj Narang</b>
    </div>

    <div>
        <a href="https://instagram.com/iamanujnarang" target="_blank">
            <img src="{INSTA_ICON}" class="social-icon">
        </a>
        <a href="https://facebook.com/iamanujnarang" target="_blank">
            <img src="{FB_ICON}" class="social-icon">
        </a>
        <a href="https://x.com/iamanujnarang" target="_blank">
            <img src="{X_ICON}" class="social-icon">
        </a>
        <a href="https://linkedin.com/in/iamanujnarang" target="_blank">
            <img src="{LINKEDIN_ICON}" class="social-icon">
        </a>
    </div>

    <div class="beeclue-box">
        <a href="https://beeclue.com" target="_blank">
            <img src="{BEECLUE_LOGO_PNG}">
        </a>
    </div>

</div>
""", unsafe_allow_html=True)
