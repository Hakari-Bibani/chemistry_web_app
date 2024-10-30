import streamlit as st

# Set the title of the page
st.title("Welcome to Your Virtual Chemistry Learning Environment!")

# Add the custom CSS for styling
st.markdown(
    """
    <style>
        .custom-background {
            background-image: url('chemistry_lab');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: white; /* Change text color for better visibility */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Apply the custom background to the container
with st.container():
    st.markdown('<div class="custom-background">', unsafe_allow_html=True)
    st.header("📚 What you can do here:")
    st.write("• Perform chemical calculations")
    st.write("• Watch simulated reactions")
    st.write("• Learn chemistry concepts")
    st.subheader("🔬 Getting Started:")
    st.write("1. Select a section on the left side")
    st.write("2. Follow the instructions")
    st.write("3. Experiment and learn!")
    st.markdown('</div>', unsafe_allow_html=True)
