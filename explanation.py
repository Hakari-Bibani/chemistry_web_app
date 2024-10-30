import streamlit as st
from streamlit_extras import st_card, show_hide, st_glow_title  # Assuming these custom modules handle certain effects or custom styles

def explanation_page():
    # Glowing Animated Title
    st.markdown("""
    <style>
    .glowing-title {
        font-size: 2.5em;
        text-align: center;
        color: #add8e6;  /* Light blue glow */
        text-shadow: 0 0 10px #add8e6, 0 0 20px #add8e6, 0 0 30px #add8e6, 0 0 40px #add8e6;
        animation: text-glow 1.5s infinite alternate;
    }
    @keyframes text-glow {
        from { text-shadow: 0 0 5px #add8e6, 0 0 10px #add8e6; }
        to { text-shadow: 0 0 20px #add8e6, 0 0 30px #add8e6; }
    }
    </style>
    <h1 class="glowing-title">📚 Chemistry Concepts & Explanation</h1>
    """, unsafe_allow_html=True)
    
    # Styled Topic Cards
    st.markdown("### Select a topic to learn about:")
    topics = ["pH", "pOH", "Molarity"]
    selected_topic = st.selectbox("Choose a topic", topics)
    
    if selected_topic == "pH":
        st_card("Understanding pH", """
            - pH is a measure of the hydrogen ion concentration.
            - The pH Scale:
              * pH < 7: Acidic
              * pH = 7: Neutral
              * pH > 7: Basic (Alkaline)
            - Calculating pH: pH = -log[H⁺]
            """, icon="⚛️", key="ph_card")
        # Test Your Knowledge - pH
        if st.button("Test Your Knowledge on pH"):
            st.write("What pH value represents a neutral solution?")
            answer = st.radio("Select your answer:", ("0", "7", "14", "3.5"))
            if answer == "7":
                st.success("Correct!")
            else:
                st.error("Incorrect. The correct answer is 7.")

    elif selected_topic == "pOH":
        st_card("Understanding pOH", """
            - pOH is a measure of hydroxide ion concentration.
            - The pOH Scale:
              * pOH < 7: Basic
              * pOH = 7: Neutral
              * pOH > 7: Acidic
            - Relationship with pH: pH + pOH = 14
            """, icon="⚛️", key="poh_card")
        # Test Your Knowledge - pOH
        if st.button("Test Your Knowledge on pOH"):
            st.write("What pOH value represents a neutral solution?")
            answer = st.radio("Select your answer:", ("0", "7", "14", "3.5"))
            if answer == "7":
                st.success("Correct!")
            else:
                st.error("Incorrect. The correct answer is 7.")

    elif selected_topic == "Molarity":
        st_card("Understanding Molarity", """
            - Molarity (M) is the concentration of a solution.
            - Calculating Molarity: M = moles of solute / liters of solution
            """, icon="⚛️", key="molarity_card")
        # Test Your Knowledge - Molarity
        if st.button("Test Your Knowledge on Molarity"):
            st.write("If you have 2 moles of NaCl in 0.5 L of solution, what is the molarity?")
            answer = st.radio("Select your answer:", ("0.5 M", "1.0 M", "2.0 M", "4.0 M"))
            if answer == "4.0 M":
                st.success("Correct!")
            else:
                st.error("Incorrect. The correct answer is 4.0 M.")
