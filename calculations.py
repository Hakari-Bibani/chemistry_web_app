import streamlit as st
import math

# CSS for glowing title, styled option cards with movement
st.markdown(
    """
    <style>
    /* Glowing Title with Movement */
    .glowing-title {
        font-size: 2.5em;
        text-align: center;
        color: black;
        text-shadow: 0 0 10px #add8e6, 0 0 20px #add8e6, 0 0 30px #add8e6;
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
        0% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0); }
    }

    /* Styled Option Cards with Movement */
    .option-cards {
        display: flex;
        justify-content: space-around;
        margin-top: 2em;
    }

    .option-card {
        background: #e3f2fd;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        width: 45%;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
        transition: transform 0.3s;
    }

    .option-card:hover {
        transform: translateY(-10px);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Glowing animated title for the calculation section
st.markdown('<div class="glowing-title">Welcome to the Calculation section!</div>', unsafe_allow_html=True)

# Options displayed as styled cards
st.markdown('<div class="option-cards">', unsafe_allow_html=True)
if st.button("pH"):
    st.markdown(
        """
        <div class="option-card">
            <h4>pH Calculation</h4>
            <p>Input [H3O+] or pH value to calculate</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    h3o_concentration = st.number_input("Enter [H3O+] concentration (mol/L):", min_value=0.0, step=0.01, format="%.4f")
    if h3o_concentration > 0:
        pH_value = -math.log10(h3o_concentration)
        st.write(f"Calculated pH: {pH_value:.2f}")
    else:
        pH_value = st.number_input("Enter pH value:", min_value=0.0, step=0.01, format="%.2f")
        h3o_concentration = 10 ** (-pH_value)
        st.write(f"Calculated [H3O+]: {h3o_concentration:.4f} mol/L")

if st.button("Molarity"):
    st.markdown(
        """
        <div class="option-card">
            <h4>Molarity Calculation</h4>
            <p>Input values to find Molarity, Moles, or Volume</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    moles = st.number_input("Enter moles of solute:", min_value=0.0, step=0.01, format="%.4f")
    volume = st.number_input("Enter volume of solution (L):", min_value=0.0, step=0.01, format="%.4f")
    if moles > 0 and volume > 0:
        molarity = moles / volume
        st.write(f"Calculated Molarity: {molarity:.2f} M")
    else:
        molarity = st.number_input("Enter Molarity (M):", min_value=0.0, step=0.01, format="%.2f")
        if moles == 0:
            st.write(f"Required moles: {molarity * volume:.4f} moles")
        else:
            st.write(f"Required volume: {moles / molarity:.4f} L")

st.markdown('</div>', unsafe_allow_html=True)
