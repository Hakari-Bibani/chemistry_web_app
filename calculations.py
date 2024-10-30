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

    # Existing code for calculation logic
    calc_type = st.selectbox("Select calculation type:", ["", "pH", "Molarity"])

   if calculation_type == "pH":
        st.subheader("pH Calculation")
        st.write("Provide either the value of [H₃O⁺] to find pH or the value of pH to find [H₃O⁺].")
        
        # Input boxes for either [H3O+] or pH
        h3o_concentration = st.number_input("Enter [H₃O⁺] (in mol/L)", min_value=0.0, format="%.5f", step=0.00001)
        ph_value = st.number_input("Enter pH", min_value=0.0, max_value=14.0, format="%.2f", step=0.01)

        if h3o_concentration:
            # Calculate pH from [H3O+]
            pH = -math.log10(h3o_concentration)
            st.write("**Calculation Steps:**")
            st.latex(r"pH = -\log [H_3O^+]")
            st.write(f"pH = -log({h3o_concentration}) = {pH:.2f}")
            st.success(f"The calculated pH is {pH:.2f}")

        elif ph_value:
            # Calculate [H3O+] from pH
            h3o_concentration = 10 ** (-ph_value)
            st.write("**Calculation Steps:**")
            st.latex(r"[H_3O^+] = 10^{-pH}")
            st.write(f"[H₃O⁺] = 10^(-{ph_value}) = {h3o_concentration:.5f} mol/L")
            st.success(f"The calculated [H₃O⁺] concentration is {h3o_concentration:.5f} mol/L")

    # Molarity Calculation Section
    elif calculation_type == "Molarity":
        st.subheader("Molarity Calculation")
        st.write("Provide two values to calculate the third one (Molarity, Moles, or Volume).")
        
        # Input boxes for Moles, Volume, and Molarity
        moles = st.number_input("Enter moles of solute", min_value=0.0, format="%.4f", step=0.0001)
        volume = st.number_input("Enter volume of solution (in L)", min_value=0.0, format="%.4f", step=0.0001)
        molarity = st.number_input("Enter molarity (M)", min_value=0.0, format="%.4f", step=0.0001)

        if moles and volume:
            # Calculate Molarity from Moles and Volume
            molarity = moles / volume
            st.write("**Calculation Steps:**")
            st.latex(r"M = \frac{\text{moles of solute}}{\text{volume of solution (L)}}")
            st.write(f"M = {moles} / {volume} = {molarity:.4f} M")
            st.success(f"The calculated molarity is {molarity:.4f} M")

        elif volume and molarity:
            # Calculate Moles from Volume and Molarity
            moles = molarity * volume
            st.write("**Calculation Steps:**")
            st.latex(r"\text{Moles of solute} = M \times \text{volume of solution (L)}")
            st.write(f"Moles = {molarity} * {volume} = {moles:.4f}")
            st.success(f"The calculated moles of solute is {moles:.4f} moles")

        elif moles and molarity:
            # Calculate Volume from Moles and Molarity
            volume = moles / molarity
            st.write("**Calculation Steps:**")
            st.latex(r"\text{Volume of solution (L)} = \frac{\text{moles of solute}}{M}")
            st.write(f"Volume = {moles} / {molarity} = {volume:.4f} L")
            st.success(f"The calculated volume is {volume:.4f} L")

# Run the calculations function when this script is executed
if __name__ == "__main__":
    calculations()
