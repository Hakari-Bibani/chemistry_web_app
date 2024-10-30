import streamlit as st
import math

def calculations():
    # CSS for the glowing animated title
    st.markdown(
        """
        <style>
        .glowing-title {
            font-size: 2.5em;
            color: black;
            text-align: center;
            text-shadow: 0 0 10px #add8e6, 0 0 20px #add8e6, 0 0 30px #add8e6, 0 0 40px #add8e6;
            animation: text-glow 1.5s infinite alternate, move-title 2s infinite alternate;
        }
        
        @keyframes text-glow {
            from {
                text-shadow: 0 0 5px #add8e6, 0 0 10px #add8e6;
            }
            to {
                text-shadow: 0 0 20px #add8e6, 0 0 30px #add8e6;
            }
        }

        @keyframes move-title {
            0% { transform: translateX(0); }
            50% { transform: translateX(-10px); }
            100% { transform: translateX(0); }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display the title with the CSS class
    st.markdown('<h1 class="glowing-title">Welcome to the Calculation section!</h1>', unsafe_allow_html=True)

    # Calculation logic
    calc_type = st.selectbox("Select calculation type:", ["", "pH", "Molarity"])

    if calc_type == "pH":
        st.subheader("pH Calculations")
        value_type = st.selectbox("Calculate based on:", ["", "Hydronium Ion Concentration [H3O+]", "pH"])

        if value_type == "Hydronium Ion Concentration [H3O+]":
            h3o_concentration = st.number_input("Enter [H3O+] in mol/L:", min_value=0.0, step=0.01)
            if h3o_concentration > 0:
                ph = -math.log10(h3o_concentration)
                st.write(f"**Calculation Steps:**")
                st.write(f"1. pH = -log([H3O+])")
                st.write(f"2. pH = -log({h3o_concentration})")
                st.write(f"3. pH = {ph:.2f}")
        
        elif value_type == "pH":
            ph_value = st.number_input("Enter pH value:", min_value=0.0, step=0.01)
            if ph_value >= 0:
                h3o_concentration = 10 ** (-ph_value)
                st.write(f"**Calculation Steps:**")
                st.write(f"1. [H3O+] = 10^(-pH)")
                st.write(f"2. [H3O+] = 10^(-{ph_value})")
                st.write(f"3. [H3O+] = {h3o_concentration:.2e} mol/L")

    elif calc_type == "Molarity":
        st.subheader("Molarity Calculations")
        knowns = st.multiselect("Select known values:", ["Mole", "Volume", "Molarity"])

        if "Mole" in knowns and "Volume" in knowns:
            mole = st.number_input("Enter moles of solute:")
            volume = st.number_input("Enter volume in liters:")
            if volume > 0:
                molarity = mole / volume
                st.write(f"**Calculation Steps:**")
                st.write(f"1. Molarity (M) = moles of solute / liters of solution")
                st.write(f"2. Molarity (M) = {mole} moles / {volume} L")
                st.write(f"3. Molarity (M) = {molarity:.2f} mol/L")

        elif "Volume" in knowns and "Molarity" in knowns:
            volume = st.number_input("Enter volume in liters:")
            molarity = st.number_input("Enter molarity (M):")
            if molarity > 0:
                mole = molarity * volume
                st.write(f"**Calculation Steps:**")
                st.write(f"1. Moles of solute = Molarity (M) × Volume (L)")
                st.write(f"2. Moles of solute = {molarity} mol/L × {volume} L")
                st.write(f"3. Moles of solute = {mole:.2f} moles")

        elif "Mole" in knowns and "Molarity" in knowns:
            mole = st.number_input("Enter moles of solute:")
            molarity = st.number_input("Enter molarity (M):")
            if molarity > 0:
                volume = mole / molarity
                st.write(f"**Calculation Steps:**")
                st.write(f"1. Volume (L) = Moles of solute / Molarity (M)")
                st.write(f"2. Volume (L) = {mole} moles / {molarity} mol/L")
                st.write(f"3. Volume (L) = {volume:.2f} L")
