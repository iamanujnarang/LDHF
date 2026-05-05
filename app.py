import streamlit as st

st.set_page_config(page_title="LDHF Calculator", page_icon="⚡", layout="centered")

# ---------------- STYLE ----------------
st.markdown("""
<style>
.footer {text-align:center; margin-top:50px; color:#94a3b8;}
.made {font-size:1.4rem; margin:20px 0;}
</style>
""", unsafe_allow_html=True)

st.title("⚡ LDHF (L × D × H × F) Calculator")
st.markdown("Calculate assessed energy consumption as per PSPCL Annexure-7")

# ---------------- DEFAULT DATA ----------------
defaults = {
    "Continuous Process Industry": (30, 24, 1.00),
    "Non-Continuous Industry": (25, 16, 0.60),
    "Single Shift Industry": (30, 8, 0.60),
    "Domestic": (30, 8, 0.30),
    "Agriculture / AP High Tech": (30, 12, 1.00),
    "Non-Residential Continuous": (30, 20, 0.40),
    "Non-Residential General": (25, 12, 0.40),
    "Bulk Supply": (30, 8, 0.40),
    "Public Lighting": (30, 8, 0.40),
    "Other": (30, 12, 0.60)
}

# ---------------- INPUT ----------------
col1, col2 = st.columns(2)

with col1:
    load = st.number_input("Load (kW)", value=10.0)

    category = st.selectbox("Category", list(defaults.keys()))

    D, H, F_default = defaults[category]

    days = st.number_input("Working Days (D)", value=float(D))
    hours = st.number_input("Hours per Day (H)", value=float(H))

with col2:
    df_type = st.selectbox("Demand Factor Type", ["Decimal", "Percent"])
    demand_factor = st.number_input("Demand Factor (F)", value=float(F_default))

    unit_format = st.selectbox("Unit Format", ["kWh", "×10³ kWh"])

# ---------------- CALCULATION ----------------
if st.button("Calculate Monthly Units"):

    F = demand_factor / 100 if df_type == "Percent" else demand_factor

    units = load * days * hours * F

    display_units = units / 1000 if unit_format == "×10³ kWh" else units

    st.success(f"Monthly Units = {display_units:,.2f} {unit_format}")

    st.info(f"Formula: {load} × {days} × {hours} × {round(F,3)} = {units:,.2f} kWh")

    # Store for proportionate
    st.session_state["monthly_units"] = units
    st.session_state["monthly_days"] = days

# ---------------- PROPORTIONATE ----------------
if "monthly_units" in st.session_state:

    st.subheader("📅 Proportionate Days Calculator")

    prop_days = st.number_input("Enter Days", value=10)

    if st.button("Calculate Proportionate Units"):

        prop_units = (prop_days / st.session_state["monthly_days"]) * st.session_state["monthly_units"]

        st.success(f"Proportionate Units = {prop_units:,.2f} kWh")

# ---------------- FOOTER ----------------
st.markdown("---")

st.markdown("""
<div class="footer">
    <div class="made">
        Made with ❤️ by <strong>@iamanujnarang</strong>
    </div>
    <p>
        <a href="https://facebook.com/iamanujnarang" target="_blank">Facebook</a> |
        <a href="https://instagram.com/iamanujnarang" target="_blank">Instagram</a> |
        <a href="https://x.com/iamanujnarang" target="_blank">X</a> |
        <a href="https://linkedin.com/in/iamanujnarang" target="_blank">LinkedIn</a>
    </p>
    <p>
        Powered by <a href="https://beeclue.com/" target="_blank">Beeclue Tech</a>
    </p>
</div>
""", unsafe_allow_html=True)
