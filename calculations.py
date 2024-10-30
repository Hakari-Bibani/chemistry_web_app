import streamlit as st
import streamlit.components.v1 as components

def calculations():
    # CSS Styles
    st.markdown(
        """
        <style>
        /* Glowing Animated Title */
        .glowing-title {
            font-size: 2.5em;
            color: black; /* Text color */
            text-align: center;
            text-shadow: 0 0 10px #add8e6, 0 0 20px #add8e6, 0 0 30px #add8e6, 0 0 40px #add8e6; /* Light blue shadow */
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

        /* Styled Cards for Options */
        .options-row {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
        }

        .option-card {
            background: #e3f2fd;
            padding: 20px;
            border-radius: 10px;
            width: 150px;
            text-align: center;
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

    # Title with glowing effect
    st.markdown("<div class='glowing-title'>Welcome to the Calculation section!</div>", unsafe_allow_html=True)

    # Option Cards in a horizontal row
    st.markdown("<div class='options-row'>", unsafe_allow_html=True)
    if st.button("pH"):
        st.write("pH Calculation section loaded.")
    if st.button("Molarity"):
        st.write("Molarity Calculation section loaded.")
    st.markdown("</div>", unsafe_allow_html=True)
