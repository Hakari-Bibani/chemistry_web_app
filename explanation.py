# explanation.py
import streamlit as st

def explanation_page():
    # Glowing Animated Title
    st.markdown("""
    <style>
    .glowing-title {
        font-size: 2.5em;
        text-align: center;
        color: #add8e6;
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

    # Display topic details and Test Your Knowledge section
    if selected_topic == "pH":
        st.markdown("""
        <div class="st-card">
            <h3>Understanding pH</h3>
            <p>- pH is a measure of the hydrogen ion concentration.</p>
            <p>- The pH Scale:</p>
            <ul>
                <li>pH < 7: Acidic</li>
                <li>pH = 7: Neutral</li>
                <li>pH > 7: Basic (Alkaline)</li>
            </ul>
            <p>- Calculating pH: pH = -log[H⁺]</p>
        </div>
        """, unsafe_allow_html=True)

        # Test Your Knowledge - pH
        st.write("### Test Your Knowledge on pH")
        answer = st.radio("What pH value represents a neutral solution?", ["0", "7", "14", "3.5"])
        if st.button("Submit Answer"):
            if answer == "7":
                st.success("Correct!")
            else:
                st.error("Incorrect. The correct answer is 7.")

    elif selected_topic == "pOH":
        st.markdown("""
        <div class="st-card">
            <h3>Understanding pOH</h3>
            <p>- pOH is a measure of hydroxide ion concentration.</p>
            <p>- The pOH Scale:</p>
            <ul>
                <li>pOH < 7: Basic</li>
                <li>pOH = 7: Neutral</li>
                <li>pOH > 7: Acidic</li>
            </ul>
            <p>- Relationship with pH: pH + pOH = 14</p>
        </div>
        """, unsafe_allow_html=True)

        # Test Your Knowledge - pOH
        st.write("### Test Your Knowledge on pOH")
        answer = st.radio("What pOH value represents a neutral solution?", ["0", "7", "14", "3.5"])
        if st.button("Submit Answer"):
            if answer == "7":
                st.success("Correct!")
            else:
                st.error("Incorrect. The correct answer is 7.")

    elif selected_topic == "Molarity":
        st.markdown("""
        <div class="st-card">
            <h3>Understanding Molarity</h3>
            <p>- Molarity (M) is the concentration of a solution.</p>
            <p>- Calculating Molarity: M = moles of solute / liters of solution</p>
        </div>
        """, unsafe_allow_html=True)

        # Test Your Knowledge - Molarity
        st.write("### Test Your Knowledge on Molarity")
        answer = st.radio("If you have 2 moles of NaCl in 0.5 L of solution, what is the molarity?", ["0.5 M", "1.0 M", "2.0 M", "4.0 M"])
        if st.button("Submit Answer"):
            if answer == "4.0 M":
                st.success("Correct!")
            else:
                st.error("Incorrect. The correct answer is 4.0 M.")

# CSS styling for cards
st.markdown("""
<style>
.st-card {
    background: #f0f8ff;
    border-radius: 10px;
    padding: 15px;
    margin: 10px 0;
    text-align: left;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    transition: 0.3s;
}
.st-card:hover {
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}
</style>
""", unsafe_allow_html=True)
