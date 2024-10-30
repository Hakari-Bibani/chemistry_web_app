import streamlit as st

# Load the new CSS file
st.markdown(
    """
    <link href="styles_explanation.css" rel="stylesheet">
    """,
    unsafe_allow_html=True
)

def explanation():
    st.title("Chemistry Concepts & Explanations 📚")
    st.write("Welcome to the explanations section! Here you'll find detailed information about various chemistry concepts.")
    
    topic = st.selectbox("Select a topic to learn about:", ["", "pH", "pOH", "Molarity"])

    if topic == "pH":
        st.subheader("Understanding pH")
        st.write("""
        pH is a measure of the hydrogen ion concentration in a solution. It indicates how acidic or basic a solution is on a scale of 0 to 14.
        
        **The pH Scale:**
        - pH < 7: Acidic
        - pH = 7: Neutral
        - pH > 7: Basic (Alkaline)
        
        **Calculating pH:**
        pH = -log[H⁺] where [H⁺] is the concentration of hydrogen ions in mol/L.
        
        **Common Examples:**
        - Lemon juice: pH 2 (acidic)
        - Pure water: pH 7 (neutral)
        - Baking soda: pH 9 (basic)
        """)
        st.write("**Test Your Knowledge!**")
        st.radio("What pH value represents a neutral solution?", ["0", "7", "14", "3.5"])

    elif topic == "pOH":
        st.subheader("Understanding pOH")
        st.write("""
        pOH is a measure of the hydroxide ion concentration in a solution.
        
        **The pOH Scale:**
        - pOH < 7: Basic (Alkaline)
        - pOH = 7: Neutral
        - pOH > 7: Acidic
        
        **Calculating pOH:**
        pOH = -log[OH⁻] where [OH⁻] is the concentration of hydroxide ions in mol/L.
        
        **Relationship between pH and pOH:**
        pH + pOH = 14
        
        **Common Examples:**
        - Strong base: pOH < 7 (basic)
        - Pure water: pOH = 7 (neutral)
        - Strong acid: pOH > 7 (acidic)
        """)
        st.write("**Test Your Knowledge!**")
        st.radio("What pOH value represents a neutral solution?", ["0", "7", "14", "3.5"])

    elif topic == "Molarity":
        st.subheader("Understanding Molarity")
        st.write("""
        Molarity (M) is the concentration of a solution, measured as moles of solute per liter of solution.
        
        **Calculating Molarity:**
        M = moles of solute / liters of solution
        
        **Applications:**
        - Laboratory solution preparation
        - Chemical analysis
        - Industrial processes
        """)
        st.write("**Test Your Knowledge!**")
        st.radio("If you have 2 moles of NaCl in 0.5 L of solution, what is the molarity?", ["0.5 M", "1.0 M", "2.0 M", "4.0 M"])
