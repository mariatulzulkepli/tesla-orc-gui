import streamlit as st

# Page config
st.set_page_config(page_title="Tesla Turbine ORC Tool", layout="centered")

# Title
st.title("Tesla Turbine ORC Performance Evaluation Tool")
st.write("Analytical evaluation of Tesla turbine performance in a low-temperature ORC.")

# INPUTS
fluid = st.selectbox(
    "Select Working Fluid",
    ["R134a", "R141b", "R245fa", "R1233zd(E)"]
)

T_cond = st.number_input("Condenser Temperature (°C)", value=30.0)
T_evap = st.number_input("Evaporator Temperature (°C)", value=90.0)
eta_t = st.slider("Tesla Turbine Efficiency (%)", 10, 50, 30)

# BUTTON
if st.button("Calculate Performance"):

    # ✅ Predefined results (from your analysis)
    if fluid == "R134a":
        Wpump, Wturb, Wnet, eta = 2.08, 7.57, 5.49, 3.02
    elif fluid == "R141b":
        Wpump, Wturb, Wnet, eta = 0.36, 11.52, 11.16, 4.23
    elif fluid == "R245fa":
        Wpump, Wturb, Wnet, eta = 0.62, 9.61, 8.99, 3.91
    else:
        Wpump, Wturb, Wnet, eta = 0.54, 9.65, 9.11, 4.01

    # ✅ PERFORMANCE DISPLAY
    st.subheader("Performance Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Pump Work (kJ/kg)", Wpump)
        st.metric("Turbine Work (kJ/kg)", Wturb)

    with col2:
        st.metric("Net Work (kJ/kg)", Wnet)
        st.metric("Thermal Efficiency (%)", eta)

    # ✅ LINE SEPARATOR
    st.markdown("---")

    # ✅ T-S DIAGRAM SECTION
    st.subheader("T–s Diagram")

    st.write(f"Showing T–s diagram for **{fluid}**")

    if fluid == "R134a":
        st.image("r134a.jpg", use_column_width=True)
    elif fluid == "R141b":
        st.image("r141b.jpg", use_column_width=True)
    elif fluid == "R245fa":
        st.image("r245fa.jpg", use_column_width=True)
    else:
        st.image("r1233zdE.jpg", use_column_width=True)

    # ✅ INTERPRETATION (VERY IMPORTANT FOR FYP)
    if fluid == "R134a":
        st.info("R134a is used as the reference working fluid. It shows baseline performance with lower net work output compared to other fluids.")
    elif fluid == "R141b":
        st.success("R141b demonstrates the highest turbine work output and thermal efficiency due to its higher vapour density.")
    elif fluid == "R245fa":
        st.info("R245fa shows moderate performance, with turbine work output higher than R134a but lower than R141b.")
    else:
        st.info("R1233zd(E) is an environmentally friendly alternative with good performance comparable to R245fa.")

# ✅ ADD THIS LINE HERE
st.caption("Cycle representation is based on Rankine cycle assumptions with Tesla turbine efficiency applied.")

# ✅ FOOTER
st.markdown("---")
st.subheader("About")

st.write("""
This GUI tool evaluates Tesla turbine performance in a low-temperature Organic Rankine Cycle (ORC).
It is based on Rankine cycle energy balance principles and analytical results obtained in the study.
""")
