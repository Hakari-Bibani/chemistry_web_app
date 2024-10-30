import streamlit as st

def calculations():
    # Glowing Animated Title
    st.markdown(
        """
        <h1 class="glowing-title">Welcome to the Calculation section!</h1>
        """,
        unsafe_allow_html=True
    )

    # Instruction
    st.write("Select calculation type:")

    # Styled Cards for Options
    st.markdown(
        """
        <div class="calculation-cards">
            <div class="card" id="ph-card">
                <h2>pH</h2>
            </div>
            <div class="card" id="molarity-card">
                <h2>Molarity</h2>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Logic for handling selections will go here
    # You may need to implement functionality to react to clicks on the cards

# CSS Styles for Calculation Page
st.markdown(
    """
    <style>
    /* Glowing Title with Movement */
    .glowing-title {
        font-size: 2.5em;
        text-align: center;
        color: black; /* Text color */
        text-shadow: 0 0 10px #add8e6, 0 0 20px #add8e6, 0 0 30px #add8e6, 0 0 40px #add8e6; /* Light blue shadow */
        animation: text-glow 1.5s infinite alternate, move-title 2s infinite alternate; /* Added movement */
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

    /* Calculation Cards */
    .calculation-cards {
        display: flex;
        justify-content: space-around;
        margin-top: 2em;
    }

    .calculation-cards .card {
        background: #e3f2fd;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        width: 30%;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
        transition: transform 0.3s;
    }

    .calculation-cards .card:hover {
        transform: translateY(-10px);
    }
    </style>
    """,
    unsafe_allow_html=True
)
