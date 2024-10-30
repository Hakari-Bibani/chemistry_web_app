import streamlit as st

def show_explanation_section():
    st.markdown("<h1 class='glowing-title'>📚 Chemistry Concepts & Explanations</h1>", unsafe_allow_html=True)
    
    st.write("Welcome to the explanations section! Here you'll find detailed information about various chemistry concepts.")
    st.write("Select a topic to learn about:")
    
    topics = {
        "pH": """
        Understanding pH:
        - pH is a measure of the hydrogen ion concentration in a solution. It indicates how acidic or basic a solution is on a scale of 0 to 14.
        
        The pH Scale:
        - pH < 7: Acidic
        - pH = 7: Neutral
        - pH > 7: Basic (Alkaline)
        
        Common Examples:
        - Lemon juice: pH 2 (acidic)
        - Pure water: pH 7 (neutral)
        - Baking soda: pH 9 (basic)
        """,
        "pOH": """
        Understanding pOH:
        - pOH is a measure of the hydroxide ion concentration in a solution. It indicates how acidic or basic a solution is.
        
        The pOH Scale:
        - pOH < 7: Basic (Alkaline)
        - pOH = 7: Neutral
        - pOH > 7: Acidic
        
        Relationship between pH and pOH:
        - pH + pOH = 14
        """,
        "Molarity": """
        Understanding Molarity:
        - Molarity (M) is a measure of the concentration of a solution, expressed as the number of moles of solute per liter of solution.
        """,
    }

    # Display topic cards
    for topic in topics.keys():
        if st.button(topic):
            st.markdown(f"<div class='details'>{topics[topic]}</div>", unsafe_allow_html=True)
    
    # Test Your Knowledge Section
    st.markdown("<h2>Test Your Knowledge! 📝</h2>", unsafe_allow_html=True)

    # pH Question
    st.write("What pH value represents a neutral solution?")
    pH_options = [0, 7, 14, 3.5]
    pH_answer = st.selectbox("Choose your answer:", pH_options)

    if st.button("Submit pH Answer"):
        if pH_answer == 7:
            st.success("Correct! The pH value that represents a neutral solution is 7.")
        else:
            st.error(f"Incorrect! The correct answer is 7.")

    # pOH Question
    st.write("What pOH value represents a neutral solution?")
    pOH_options = [0, 7, 14, 3.5]
    pOH_answer = st.selectbox("Choose your answer:", pOH_options)

    if st.button("Submit pOH Answer"):
        if pOH_answer == 7:
            st.success("Correct! The pOH value that represents a neutral solution is 7.")
        else:
            st.error(f"Incorrect! The correct answer is 7.")

    # Molarity Question
    st.write("If you have 2 moles of NaCl in 0.5 L of solution, what is the molarity?")
    molarity_options = [0.5, 1.0, 2.0, 4.0]
    molarity_answer = st.selectbox("Choose your answer:", molarity_options)

    if st.button("Submit Molarity Answer"):
        if molarity_answer == 4.0:
            st.success("Correct! The molarity is 4.0 M.")
        else:
            st.error("Incorrect! The correct answer is 4.0 M.")
