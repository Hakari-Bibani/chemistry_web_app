import streamlit as st

def main():
    st.title("📚 Chemistry Concepts & Explanation")
    st.markdown('<h1 class="glowing-title">📚 Chemistry Concepts & Explanation</h1>', unsafe_allow_html=True)

    # Options for the topics
    topics = ["pH", "pOH", "Molarity"]
    selected_topic = st.selectbox("Select a topic to learn about:", topics)

    # Create styled cards for options
    st.markdown("""
    <style>
    .card-container {
        display: flex;
        justify-content: space-around;
        margin-top: 2em;
    }
    .card {
        background-color: #e6e6fa; /* Light purple */
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        width: 30%;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s;
    }
    .card:hover {
        transform: translateY(-10px);
    }
    </style>
    """, unsafe_allow_html=True)

    if selected_topic == "pH":
        display_ph_info()
    elif selected_topic == "pOH":
        display_pOH_info()
    elif selected_topic == "Molarity":
        display_molarity_info()

def display_ph_info():
    st.markdown("""
    ### Understanding pH
    **What is pH?**
    pH is a measure of the hydrogen ion concentration in a solution, indicating how acidic or basic it is on a scale of 0 to 14.
    **The pH Scale:**
    - pH < 7: Acidic
    - pH = 7: Neutral
    - pH > 7: Basic (Alkaline)

    **Common Examples:**
    - Lemon juice: pH 2 (acidic)
    - Pure water: pH 7 (neutral)
    - Baking soda: pH 9 (basic)

    **Test Your Knowledge! 📝**
    What pH value represents a neutral solution?
    """)
    
    options = ["0", "7", "14", "3.5"]
    answer = st.radio("Select your answer:", options)
    if st.button("Submit"):
        if answer == "7":
            st.success("Correct! The pH value that represents a neutral solution is 7.")
        else:
            st.error("Incorrect. The correct answer is 7.")

def display_pOH_info():
    st.markdown("""
    ### Understanding pOH
    **What is pOH?**
    pOH is a measure of the hydroxide ion concentration in a solution. It's a scale similar to pH that indicates how acidic or basic a solution is.
    
    **The pOH Scale:**
    - pOH < 7: Basic (Alkaline)
    - pOH = 7: Neutral
    - pOH > 7: Acidic

    **Common Examples:**
    - Strong base (like sodium hydroxide): pOH < 7 (basic)
    - Pure water: pOH = 7 (neutral)
    - Strong acid (like hydrochloric acid): pOH > 7 (acidic)

    **Test Your Knowledge! 📝**
    What pOH value represents a neutral solution?
    """)
    
    options = ["0", "7", "14", "3.5"]
    answer = st.radio("Select your answer:", options)
    if st.button("Submit"):
        if answer == "7":
            st.success("Correct! The pOH value that represents a neutral solution is 7.")
        else:
            st.error("Incorrect. The correct answer is 7.")

def display_molarity_info():
    st.markdown("""
    ### Understanding Molarity
    **What is Molarity?**
    Molarity (M) is a measure of the concentration of a solution, expressed as the number of moles of solute per liter of solution.

    **Applications:**
    - Laboratory solution preparation
    - Chemical analysis
    - Industrial processes

    **Test Your Knowledge! 📝**
    If you have 2 moles of NaCl in 0.5 L of solution, what is the molarity?
    """)
    
    options = ["0.5 M", "1.0 M", "2.0 M", "4.0 M"]
    answer = st.radio("Select your answer:", options)
    if st.button("Submit"):
        if answer == "4.0 M":
            st.success("Correct! The molarity is 4.0 M.")
        else:
            st.error("Incorrect. The correct answer is 4.0 M.")

if __name__ == "__main__":
    main()
