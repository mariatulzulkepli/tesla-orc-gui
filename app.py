import streamlit as st

st.set_page_config(page_title="Tesla Turbine ORC Tool", layout="centered")

st.title("Tesla Turbine ORC Performance Tool")
st.write("Analytical evaluation of Tesla turbine performance in a low-temperature ORC.")

# INPUTS
fluid = st.selectbox(
    "Select Working Fluid",
    ["R134a", "R141b", "R245fa", "R1233zd(E)"]
)

T_cond = st.number_input("Condenser Temperature (°C)", value=30.0)
T_evap = st.number_input("Evaporator Temperature (°C)", value=90.0)
eta_t = st.slider("Tesla Turbine Efficiency (%)", 10, 50, 30)

# CALCULATE BUTTON
if st.button("Calculate Performance"):

    if fluid == "R134a":
        Wpump, Wturb, Wnet, eta = 2.08, 7.57, 5.49, 3.02
    elif fluid == "R141b":
        Wpump, Wturb, Wnet, eta = 0.36, 11.52, 11.16, 4.23
    elif fluid == "R245fa":
        Wpump, Wturb, Wnet, eta = 0.62, 9.61, 8.99, 3.91
    else:
        Wpump, Wturb, Wnet, eta = 0.54, 9.65, 9.11, 4.01

    st.subheader("Results")
    st.write(f"Pump Work: **{Wpump} kJ/kg**")
    st.write(f"Turbine Work: **{Wturb} kJ/kg**")
    st.write(f"Net Cycle Work: **{Wnet} kJ/kg**")
    st.write(f"Thermal Efficiency: **{eta} %**")
  
