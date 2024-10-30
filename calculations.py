import streamlit as st
import math

def calculations():
    # CSS for glowing title and styled option cards
    st.markdown("""
        <style>
        /* Glowing Title with Movement */
        .glowing-title {
            font-size: 2.5em;
            color: black; /* Text color */
            text-align: center;
            margin-top: 20px;
            text-shadow: 0 0 10px #00f0ff, 0 0 20px #00f0ff, 0 0 30px #00f0ff, 0 0 40px #00f0ff;
            animation: text-glow 1.5s infinite alternate, move-title 2s infinite alternate;
        }

        @keyframes text-glow {
            from {
                text-shadow: 0 0 5px #00f0ff, 0 0 10px #00f0ff;
            }
            to {
                text-shadow: 0 0 20px #00f0ff, 0 0 30px #00f0ff;
            }
        }

        @keyframes move-title {
            0% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0); }
        }

        /* Option Cards */
        .option-cards {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 2em;
        }

        .option-card {
            background: #e3f2fd;
            padding: 20px;
            width: 150px;
            text-align: center;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
            transition: transform 0.3s;
        }

        .option-card:hover {
            transform: translateY(-10px);
        }
        </style>
    """, unsafe_allow_html=True)

    # Display the glowing title
    st.markdown('<div class="glowing-title">Welcome to the Calculation section!</div>', unsafe_allow_html=True)

    # Display the calculation options as styled cards
    st.markdown('<div class="option-cards">', unsafe_allow_html=True)
    
    # pH calculation logic
    if st.button("pH"):
        st.write("## pH Calculation")
        h3o_concentration = st.number_input("Enter [H₃O⁺] concentration (mol/L)", min_value=0.0, format="%.8f")
        if h3o_concentration > 0:
            pH_value = -math.log10(h3o_concentration)
            st.write(f"**pH**: {pH_value:.2f}")
            st.write("### Calculation Steps:")
            st.write("1. Take the negative logarithm of the [H₃O⁺] concentration.")
            st.write("2. The formula is: **pH = -log([H₃O⁺])**")
            st.write(f"3. With [H₃O⁺] = {h3o_concentration}, pH = -log({h3o_concentration}) = {pH_value:.2f}")
        else:
            st.write("Please enter a valid [H₃O⁺] concentration greater than 0.")

    # Molarity calculation logic
    if st.button("Molarity"):
        st.write("## Molarity Calculation")
        moles = st.number_input("Enter moles of solute", min_value=0.0, format="%.2f")
        volume = st.number_input("Enter volume of solution (L)", min_value=0.0, format="%.2f")
        if moles > 0 and volume > 0:
            molarity = moles / volume
            st.write(f"**Molarity**: {molarity:.2f} M")
            st.write("### Calculation Steps:")
            st.write("1. Divide the number of moles by the volume of the solution in liters.")
            st.write("2. The formula is: **M = moles / liters**")
            st.write(f"3. With {moles} moles and {volume} liters, M = {moles} / {volume} = {molarity:.2f} M")
        else:
            st.write("Please enter valid values for both moles and volume greater than 0.")
    
    st.markdown('</div>', unsafe_allow_html=True)
