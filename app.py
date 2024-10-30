import streamlit as st

# Custom CSS to style the home page
st.markdown(
    """
    <style>
    .home-page {
        background-image: url('chemistry_lab');
        background-size: cover;
        background-repeat: no-repeat;
        color: white; /* Change text color for better visibility */
        padding: 50px; /* Add padding for spacing */
        text-align: center; /* Center align text */
    }
    .header {
        font-size: 40px;
        font-weight: bold;
    }
    .subheader {
        font-size: 24px;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Home page content
st.container()
st.markdown('<div class="home-page">', unsafe_allow_html=True)
st.markdown('<div class="header">Welcome to your virtual chemistry learning environment!</div>', unsafe_allow_html=True)

st.markdown('<div class="subheader">📚 What you can do here:</div>', unsafe_allow_html=True)
st.markdown('• Perform chemical calculations<br/>• Watch simulated reactions<br/>• Learn chemistry concepts', unsafe_allow_html=True)

st.markdown('<div class="subheader">🔬 Getting Started:</div>', unsafe_allow_html=True)
st.markdown('1. Select a section on the left side<br/>2. Follow the instructions<br/>3. Experiment and learn!', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close home page div
