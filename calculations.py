import streamlit as st

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
    if st.button("pH"):
        st.write("You selected pH. Please enter the required values to calculate.")
            if calc_type == "pH":
        st.subheader("pH Calculations")
        value_type = st.selectbox("Calculate based on:", ["", "Hydronium Ion Concentration [H3O+]", "pH"])

        if value_type == "Hydronium Ion Concentration [H3O+]":
            h3o_concentration = st.number_input("Enter [H3O+] in mol/L:", min_value=0.0, step=0.01)
            if h3o_concentration > 0:
                ph = -math.log10(h3o_concentration)
                st.write(f"pH = -log([H3O+]) = {ph:.2f}")

        elif value_type == "pH":
            ph_value = st.number_input("Enter pH value:", min_value=0.0, step=0.01)
            if ph_value >= 0:
                h3o_concentration = 10 ** (-ph_value)
                st.write(f"[H3O+] = 10^(-pH) = {h3o_concentration:.2e} mol/L")

    if st.button("Molarity"):
        st.write("You selected Molarity. Please enter the required values to calculate.")
    elif calc_type == "Molarity":
        st.subheader("Molarity Calculations")
        knowns = st.multiselect("Select known values:", ["Mole", "Volume", "Molarity"])

        if "Mole" in knowns and "Volume" in knowns:
            mole = st.number_input("Enter moles of solute:")
            volume = st.number_input("Enter volume in liters:")
            if volume > 0:
                molarity = mole / volume
                st.write(f"Molarity (M) = {molarity:.2f} mol/L")
    st.markdown('</div>', unsafe_allow_html=True)
