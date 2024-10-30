import streamlit as st
import time

def lab():
    st.title("Virtual Chemistry Lab 🧪")
    st.write("Welcome to the virtual lab! Here you can simulate different chemical reactions and observe their outcomes.")
    
    # Select Reaction Type
    reaction_type = st.selectbox("Select Reaction Type:", ["", "Acid-Base (baking soda & vinegar)", "Exothermic (Warning: Explosive!)", "Indicator"])

    # Acid-Base Reaction: Baking Soda and Vinegar
    if reaction_type == "Acid-Base (baking soda & vinegar)":
        st.subheader("Acid-Base Reaction: Baking Soda & Vinegar")
        st.write("Add baking soda (white powder) to vinegar (clear liquid) and observe the reaction.")

        # Simulate the addition of baking soda to vinegar with button click
        if st.button("Add Baking Soda to Vinegar"):
            st.write("**Baking soda is added to vinegar!**")
            
            # Simulate bubbling effect
            for _ in range(5):
                st.write("💧 *Bubbles forming...*")
                time.sleep(0.5)
            
            # Display chemical reaction equation
            st.write("### Reaction:")
            st.latex(r"NaHCO_3 + CH_3COOH \rightarrow CO_2 + H_2O + NaCH_3COO")
            st.success("Reaction complete! Carbon dioxide bubbles have been released.")

    # Exothermic Reaction: Sodium and Water (Explosion)
    elif reaction_type == "Exothermic (Warning: Explosive!)":
        st.subheader("Exothermic Reaction: Sodium & Water (Warning: Explosive!)")
        st.write("Add sodium to water and observe the explosive reaction!")

        # Simulate the addition of sodium to water with button click
        if st.button("Add Sodium to Water"):
            st.write("**Sodium is added to water!**")

            # Simulate explosion with red flashing effect
            for _ in range(5):
                st.markdown("<span style='color:red;'>💥 Explosion! 💥</span>", unsafe_allow_html=True)
                time.sleep(0.5)
            
            # Display chemical reaction equation
            st.write("### Reaction:")
            st.latex(r"2Na(s) + 2H_2O(l) \rightarrow 2NaOH(aq) + H_2(g)")
            st.warning("Reaction complete! Sodium hydroxide and hydrogen gas were produced.")

    # Indicator Reaction: pH Indicator with Acid and Base Solutions
    elif reaction_type == "Indicator":
        st.subheader("Indicator Reaction: pH Paper with Acid and Base Solutions")
        st.write("Add pH paper to various acid and base solutions and observe the color change.")

        # Create a selection for solution type
        solution = st.selectbox("Choose a solution to test:", ["", "Strong Acid", "Weak Acid", "Neutral", "Weak Base", "Strong Base"])
        
        # Color change simulation based on pH
        if solution:
            st.write(f"**Testing pH of {solution} solution...**")
            time.sleep(1)  # Simulate testing time

            # Show color change based on solution type
            if solution == "Strong Acid":
                st.markdown("<span style='color:red;'>pH Paper Color: Red (pH ≈ 1)</span>", unsafe_allow_html=True)
            elif solution == "Weak Acid":
                st.markdown("<span style='color:orange;'>pH Paper Color: Orange (pH ≈ 5)</span>", unsafe_allow_html=True)
            elif solution == "Neutral":
                st.markdown("<span style='color:green;'>pH Paper Color: Green (pH ≈ 7)</span>", unsafe_allow_html=True)
            elif solution == "Weak Base":
                st.markdown("<span style='color:blue;'>pH Paper Color: Light Blue (pH ≈ 9)</span>", unsafe_allow_html=True)
            elif solution == "Strong Base":
                st.markdown("<span style='color:purple;'>pH Paper Color: Purple (pH ≈ 13)</span>", unsafe_allow_html=True)
                
            st.success(f"The pH paper color has changed to indicate the pH level of the {solution} solution.")

# Run the lab function when this script is executed
if __name__ == "__main__":
    lab()
