import streamlit as st

# Set the title of the app
st.title("Chemistry Learning App")

# Create a sidebar for navigation
st.sidebar.title("Navigation")

# Create a sidebar button for the home page
if st.sidebar.button("Home"):
    st.subheader("Welcome to your virtual chemistry learning environment!")
    st.markdown("""
        📚 What you can do here:
        - Perform chemical calculations
        - Watch simulated reactions
        - Learn chemistry concepts

        🔬 Getting Started:
        1. Select a section on the left side
        2. Follow the instructions
        3. Experiment and learn!
    """)

# Set up a session state to control sidebar visibility
if "show_home" not in st.session_state:
    st.session_state.show_home = True

# Show only the home page initially
if st.session_state.show_home:
    # Display the home page content
    st.subheader("Welcome to your virtual chemistry learning environment!")
    st.markdown("""
        📚 What you can do here:
        - Perform chemical calculations
        - Watch simulated reactions
        - Learn chemistry concepts

        🔬 Getting Started:
        1. Select a section on the left side
        2. Follow the instructions
        3. Experiment and learn!
    """)

    # Button to allow navigation to other pages (optional)
    if st.button("Go to Explanation Section"):
        st.session_state.show_home = False
        # You can set the state for other pages similarly as needed

# Add your explanation, calculation, and lab sections here, but wrap them in
# conditions that check if `show_home` is False to only show when needed.
