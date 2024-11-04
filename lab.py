import streamlit as st
import time

# Set up page title and description
st.title("Test the pH of Different Solutions Using Litmus Paper!")
st.write("Place litmus papers into the beakers to see how they react with different solutions.")

# Define initial colors and states
solution_colors = {
    "HCl": "lightgray",       # Hydrochloric acid
    "NaOH": "lightgray",      # Sodium hydroxide
    "H₂O": "paleturquoise"    # Neutral water
}

litmus_colors = {
    "HCl": "red",             # Turns red for acid
    "NaOH": "blue",           # Turns blue for base
    "H₂O": "lightgreen"       # Turns green for neutral
}

# Set up a placeholder for the simulation
beaker1, beaker2, beaker3 = st.columns(3)
solutions = ["HCl", "NaOH", "H₂O"]

# Display each beaker with a solution
with beaker1:
    st.write("**Hydrochloric Acid (HCl)**")
    st.markdown(f'<div style="background-color:{solution_colors["HCl"]}; width:100%; height:150px; border-radius:10px;"></div>', unsafe_allow_html=True)
    if st.button("Test HCl"):
        st.markdown(f'<div style="background-color:{litmus_colors["HCl"]}; width:30px; height:100px; margin:auto; border-radius:5px;"></div>', unsafe_allow_html=True)
        time.sleep(1)  # Simulate delay for dipping
        st.write("**Litmus Paper Turns Red**")

with beaker2:
    st.write("**Sodium Hydroxide (NaOH)**")
    st.markdown(f'<div style="background-color:{solution_colors["NaOH"]}; width:100%; height:150px; border-radius:10px;"></div>', unsafe_allow_html=True)
    if st.button("Test NaOH"):
        st.markdown(f'<div style="background-color:{litmus_colors["NaOH"]}; width:30px; height:100px; margin:auto; border-radius:5px;"></div>', unsafe_allow_html=True)
        time.sleep(1)  # Simulate delay for dipping
        st.write("**Litmus Paper Turns Blue**")

with beaker3:
    st.write("**Neutral Water (H₂O)**")
    st.markdown(f'<div style="background-color:{solution_colors["H₂O"]}; width:100%; height:150px; border-radius:10px;"></div>', unsafe_allow_html=True)
    if st.button("Test H₂O"):
        st.markdown(f'<div style="background-color:{litmus_colors["H₂O"]}; width:30px; height:100px; margin:auto; border-radius:5px;"></div>', unsafe_allow_html=True)
        time.sleep(1)  # Simulate delay for dipping
        st.write("**Litmus Paper Turns Light Green**")

# Add some spacing and instructions
st.write("---")
st.write("**Instructions:** Click on the 'Test' button for each solution to simulate dipping the litmus paper. Observe the color change after a second to determine the solution's pH.")
