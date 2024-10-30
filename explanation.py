# Define topics and details
topics = {
    "pH": {
        "detail": """Understanding pH: 
        pH is a measure of the hydrogen ion concentration in a solution. It indicates how acidic or basic a solution is on a scale of 0 to 14.
        The pH Scale:
        • pH < 7: Acidic
        • pH = 7: Neutral
        • pH > 7: Basic (Alkaline)
        Common Examples:
        • Lemon juice: pH 2 (acidic)
        • Pure water: pH 7 (neutral)
        • Baking soda: pH 9 (basic)""",
        "question": "What pH value represents a neutral solution?",
        "options": ["0", "7", "14", "3.5"],
        "correct": "7"
    },
    "pOH": {
        "detail": """Understanding pOH: 
        pOH is a measure of the hydroxide ion concentration in a solution. It's a scale similar to pH that indicates how acidic or basic a solution is.
        The pOH Scale:
        • pOH < 7: Basic (Alkaline)
        • pOH = 7: Neutral
        • pOH > 7: Acidic
        Relationship between pH and pOH:
        pH + pOH = 14""",
        "question": "What pOH value represents a neutral solution?",
        "options": ["0", "7", "14", "3.5"],
        "correct": "7"
    },
    "Molarity": {
        "detail": """Understanding Molarity: 
        Molarity (M) is a measure of the concentration of a solution, expressed as the number of moles of solute per liter of solution.
        Applications:
        • Laboratory solution preparation
        • Chemical analysis
        • Industrial processes""",
        "question": "If you have 2 moles of NaCl in 0.5 L of solution, what is the molarity?",
        "options": ["0.5 M", "1.0 M", "2.0 M", "4.0 M"],
        "correct": "4"
    }
}

# Display topics as cards
for topic in topics:
    if st.button(topic):
        st.markdown(f"<div class='card'>{topics[topic]['detail']}</div>", unsafe_allow_html=True)
        # Question display
        st.markdown(f"**{topics[topic]['question']}**")
        user_answer = st.radio("Choose your answer:", topics[topic]['options'])
        if st.button("Submit"):
            if user_answer == topics[topic]['correct']:
                st.success("Correct!")
            else:
                st.error(f"Incorrect! The correct answer is {topics[topic]['correct']}.")
