import streamlit as st

# Load CSS styles
def load_css():
    with open("explanation_styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()

st.title("📚 Chemistry Concepts & Explanation")
st.markdown('<h1 class="glowing-title">Chemistry Concepts & Explanations</h1>', unsafe_allow_html=True)
st.write("Welcome to the explanations section! Here you'll find detailed information about various chemistry concepts.")
st.write("Select a topic to learn about:")

# Options for topics
options = ["pH", "pOH", "Molarity"]
selected_option = st.selectbox("Choose a topic:", options)

if selected_option:
    st.markdown(f"## Understanding {selected_option}")

    if selected_option == "pH":
        st.write("""
        **What is pH?**
        pH is a measure of the hydrogen ion concentration in a solution. It indicates how acidic or basic a solution is on a scale of 0 to 14.

        **The pH Scale:**
        - pH < 7: Acidic
        - pH = 7: Neutral
        - pH > 7: Basic (Alkaline)

        **Calculating pH:**
        pH = -log[H⁺] where [H⁺] is the concentration of hydrogen ions in mol/L

        **Common Examples:**
        - Lemon juice: pH 2 (acidic)
        - Pure water: pH 7 (neutral)
        - Baking soda: pH 9 (basic)
        """)

        # Test Your Knowledge!
        st.markdown("## Test Your Knowledge! 📝")
        answer = st.radio("What pH value represents a neutral solution?", ("0", "7", "14", "3.5"))
        if st.button("Submit"):
            if answer == "7":
                st.markdown('<p class="correct-answer">Correct! The neutral pH is 7.</p>', unsafe_allow_html=True)
            else:
                st.markdown('<p class="correct-answer">Incorrect. The correct answer is 7.</p>', unsafe_allow_html=True)

    elif selected_option == "pOH":
        st.write("""
        **What is pOH?**
        pOH is a measure of the hydroxide ion concentration in a solution. It's a scale similar to pH that indicates how acidic or basic a solution is.

        **The pOH Scale:**
        - pOH < 7: Basic (Alkaline)
        - pOH = 7: Neutral
        - pOH > 7: Acidic

        **Calculating pOH:**
        pOH = -log[OH⁻] where [OH⁻] is the concentration of hydroxide ions in mol/L

        **Relationship between pH and pOH:**
        In any aqueous solution at 25°C, the following relationship holds: pH + pOH = 14
        """)

        # Test Your Knowledge!
        st.markdown("## Test Your Knowledge! 📝")
        answer = st.radio("What pOH value represents a neutral solution?", ("0", "7", "14", "3.5"))
        if st.button("Submit"):
            if answer == "7":
                st.markdown('<p class="correct-answer">Correct! The neutral pOH is 7.</p>', unsafe_allow_html=True)
            else:
                st.markdown('<p class="correct-answer">Incorrect. The correct answer is 7.</p>', unsafe_allow_html=True)

    elif selected_option == "Molarity":
        st.write("""
        **What is Molarity?**
        Molarity (M) is a measure of the concentration of a solution, expressed as the number of moles of solute per liter of solution.

        **Calculating Molarity:**
        M = moles of solute / liters of solution

        **Important Concepts:**
        1. Standard solutions
        2. Dilution calculations
        3. Solution preparation

        **Applications:**
        - Laboratory solution preparation
        - Chemical analysis
        - Industrial processes
        """)

        # Test Your Knowledge!
        st.markdown("## Test Your Knowledge! 📝")
        answer = st.radio("If you have 2 moles of NaCl in 0.5 L of solution, what is the molarity?", ("0.5 M", "1.0 M", "2.0 M", "4.0 M"))
        if st.button("Submit"):
            if answer == "4.0 M":
                st.markdown('<p class="correct-answer">Correct! The molarity is 4.0 M.</p>', unsafe_allow_html=True)
            else:
                st.markdown('<p class="correct-answer">Incorrect. The correct answer is 4.0 M.</p>', unsafe_allow_html=True)
