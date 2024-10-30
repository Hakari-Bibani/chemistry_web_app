import streamlit as st

def explanation():
    st.title("Chemistry Concepts & Explanations 📚")
    # Add the content for your explanation page here

# Add CSS file for explanation page
st.markdown('<link rel="stylesheet" href="styles.css">', unsafe_allow_html=True)

# Glowing Title
st.markdown('<h1 class="glowing-title">📚 Chemistry Concepts & Explanation</h1>', unsafe_allow_html=True)

# Options for Learning Topics
st.markdown('<h2>Select a topic to learn about:</h2>', unsafe_allow_html=True)

# Create styled cards for each option
options = ["pH", "pOH", "Molarity"]
selected_option = st.selectbox("Choose a topic:", options)

# Show content based on selection
if selected_option == "pH":
    st.markdown("""
    ## Understanding pH
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

elif selected_option == "pOH":
    st.markdown("""
    ## Understanding pOH
    **What is pOH?**
    pOH is a measure of the hydroxide ion concentration in a solution. It's a scale similar to pH that indicates how acidic or basic a solution is.
    **The pOH Scale:**
    - pOH < 7: Basic (Alkaline)
    - pOH = 7: Neutral
    - pOH > 7: Acidic
    **Calculating pOH:**
    pOH = -log[OH⁻] where [OH⁻] is the concentration of hydroxide ions in mol/L
    **Relationship between pH and pOH:**
    In any aqueous solution at 25°C, the following relationship holds:
    pH + pOH = 14
    **Common Examples:**
    - Strong base (like sodium hydroxide): pOH < 7 (basic)
    - Pure water: pOH = 7 (neutral)
    - Strong acid (like hydrochloric acid): pOH > 7 (acidic)
    """)

elif selected_option == "Molarity":
    st.markdown("""
    ## Understanding Molarity
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

# Test Your Knowledge Section
st.markdown('<div class="test-knowledge">', unsafe_allow_html=True)
st.markdown("<h3>Test Your Knowledge! 📝</h3>", unsafe_allow_html=True)
answer = st.selectbox("What pH value represents a neutral solution?", ['0', '7', '14', '3.5'])

if st.button("Submit Answer"):
    if answer == '7':
        st.success("Correct! The pH value that represents a neutral solution is 7.")
    else:
        st.error("Incorrect. The correct answer is 7.")
st.markdown('</div>', unsafe_allow_html=True)
