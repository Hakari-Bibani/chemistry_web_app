import streamlit as st

def explanations():
    st.title("Chemistry Concepts & Explanations 📚")
    st.write("""
        Welcome to the explanations section! Here you'll find detailed information about various chemistry concepts.
        Select a topic to learn about:
    """)

    # Topic selection dropdown
    topic = st.selectbox("Choose a topic:", ["", "pH", "pOH", "Molarity"])

    if topic == "pH":
        st.subheader("Understanding pH")
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
        
        st.markdown("---")
        st.subheader("Test Your Knowledge! 📝")
        answer = st.radio(
            "What pH value represents a neutral solution?",
            ("0", "7", "14", "3.5")
        )
        if answer == "7":
            st.success("Correct! A neutral solution has a pH of 7.")
        else:
            st.error("That's incorrect. The correct answer is 7.")

    elif topic == "pOH":
        st.subheader("Understanding pOH")
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
            In any aqueous solution at 25°C, the following relationship holds:
            pH + pOH = 14

            **Common Examples:**
            - Strong base (like sodium hydroxide): pOH < 7 (basic)
            - Pure water: pOH = 7 (neutral)
            - Strong acid (like hydrochloric acid): pOH > 7 (acidic)
        """)
        
        st.markdown("---")
        st.subheader("Test Your Knowledge! 📝")
        answer = st.radio(
            "What pOH value represents a neutral solution?",
            ("0", "7", "14", "3.5")
        )
        if answer == "7":
            st.success("Correct! A neutral solution has a pOH of 7.")
        else:
            st.error("That's incorrect. The correct answer is 7.")

    elif topic == "Molarity":
        st.subheader("Understanding Molarity")
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
        
        st.markdown("---")
        st.subheader("Test Your Knowledge! 📝")
        answer = st.radio(
            "If you have 2 moles of NaCl in 0.5 L of solution, what is the molarity?",
            ("0.5 M", "1.0 M", "2.0 M", "4.0 M")
        )
        if answer == "4.0 M":
            st.success("Correct! The molarity is 4.0 M.")
        else:
            st.error("That's incorrect. The correct answer is 4.0 M.")

# Run the explanations function when this script is executed
if __name__ == "__main__":
    explanations()
