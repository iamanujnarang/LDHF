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
# 2. CSS STYLING (No F-string here to avoid errors)
# ==========================================
st.markdown("""
<style>
    .top-logo-container { display: flex; justify-content: center; margin-bottom: 10px; }
    .top-logo { width: 140px; }
    
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
# 3. TOP LOGO & HEADER
# ==========================================
st.markdown(f'<div class="top-logo-container"><img src="{PSPCL_LOGO_URL}" class="top-logo"></div>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>LDHF Calculator</h1>", unsafe_allow_html=True)

# ... (Yahan aapka calculator wala logic code aayega) ...
st.info("Calculator Logic Placeholder - Calculation goes here.")

# ==========================================
# 4. FINAL FOOTER (Split from CSS to ensure rendering)
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
