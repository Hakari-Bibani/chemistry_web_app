import streamlit as st

# Title with Glowing Animation
st.markdown('<h1 class="explanation-title">📚 Chemistry Concepts & Explanation</h1>', unsafe_allow_html=True)

st.write("Welcome to the explanations section! Here you'll find detailed information about various chemistry concepts.")
st.write("Select a topic to learn about:")

# Topic Options as Styled Cards
topics = {
    "pH": {
        "title": "Understanding pH",
        "content": """**What is pH?**
                      pH is a measure of the hydrogen ion concentration in a solution. It indicates how acidic or basic a solution is on a scale of 0 to 14.""",
        "quiz_question": "What pH value represents a neutral solution?",
        "quiz_options": ["0", "7", "14", "3.5"],
        "correct_answer": "7"
    },
    "pOH": {
        "title": "Understanding pOH",
        "content": """**What is pOH?**
                      pOH is a measure of the hydroxide ion concentration in a solution.""",
        "quiz_question": "What pOH value represents a neutral solution?",
        "quiz_options": ["0", "7", "14", "3.5"],
        "correct_answer": "7"
    },
    "Molarity": {
        "title": "Understanding Molarity",
        "content": """**What is Molarity?**
                      Molarity (M) is a measure of the concentration of a solution.""",
        "quiz_question": "If you have 2 moles of NaCl in 0.5 L of solution, what is the molarity?",
        "quiz_options": ["0.5 M", "1.0 M", "2.0 M", "4.0 M"],
        "correct_answer": "4.0 M"
    }
}

# Display topics as cards
col1, col2, col3 = st.columns(3)
for i, (key, topic) in enumerate(topics.items()):
    with [col1, col2, col3][i]:
        if st.button(key):
            st.subheader(topic["title"])
            st.write(topic["content"])

            # Quiz Section
            st.markdown("---")
            st.write("**Test Your Knowledge! 📝**")
            selected_option = st.radio(topic["quiz_question"], topic["quiz_options"], index=0)

            # Check the answer
            if st.button("Check Answer"):
                if selected_option == topic["correct_answer"]:
                    st.success("Correct!")
                else:
                    st.error(f"Incorrect. The correct answer is {topic['correct_answer']}.")
