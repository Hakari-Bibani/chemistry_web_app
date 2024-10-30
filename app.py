import streamlit as st
from home import home  # Import the home page function
from explanation import explanation  # Import the explanation page function

# Create a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Explanation", "Calculation", "Lab"])

# Display the selected page
if page == "Home":
    home()
elif page == "Explanation":
    explanation()  # Call the explanation function when selected
elif page == "Calculation":
    # Placeholder for the calculation page function
    st.write("This is the Calculation page. (Function not implemented yet)")
elif page == "Lab":
    # Placeholder for the lab page function
    st.write("This is the Lab page. (Function not implemented yet)")
