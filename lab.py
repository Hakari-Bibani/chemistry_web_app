import streamlit as st
import time

# Page settings
st.set_page_config(layout="centered")
st.markdown("<h2 style='text-align: center;'>Litmus Test Simulation</h2>", unsafe_allow_html=True)

# Custom CSS for animation and styling
animation_css = """
<style>
.container {
    display: flex;
    justify-content: space-around;
    align-items: flex-start;
    margin-top: 20px;
}

.beaker {
    width: 100px;
    height: 150px;
    border: 2px solid #333;
    border-radius: 5px;
    overflow: hidden;
    position: relative;
    text-align: center;
    font-weight: bold;
}

.solution {
    position: absolute;
    width: 100%;
    height: 50%;
    bottom: 0;
    transition: background-color 0.5s;
}

#acid {
    background-color: lightgray;
}

#base {
    background-color: lightgray;
}

#neutral {
    background-color: #add8e6; /* Pale blue for water */
}

.litmus-paper {
    width: 20px;
    height: 50px;
    background-color: yellow;
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    animation: dip 3s infinite;
    transition: background-color 0.5s;
}

#acid-paper {
    animation-delay: 0s;
}

#base-paper {
    animation-delay: 1s;
}

#neutral-paper {
    animation-delay: 2s;
}

@keyframes dip {
    0%, 100% {
        top: -50px;
        background-color: yellow;
    }
    30% {
        top: 50px;
        background-color: yellow;
    }
    60% {
        top: 50px;
    }
    90% {
        top: -50px;
    }
}

/* Color transitions for acid, base, and neutral */
@keyframes acidColorChange {
    60% { background-color: red; }
}

@keyframes baseColorChange {
    60% { background-color: blue; }
}

@keyframes neutralColorChange {
    60% { background-color: lightgreen; }
}

#acid-paper {
    animation-name: dip, acidColorChange;
}

#base-paper {
    animation-name: dip, baseColorChange;
}

#neutral-paper {
    animation-name: dip, neutralColorChange;
}
</style>
"""

# Inject CSS into Streamlit
st.markdown(animation_css, unsafe_allow_html=True)

# HTML structure for beakers and litmus papers
html_structure = """
<div class="container">
    <!-- Acid Beaker -->
    <div class="beaker">
        HCl
        <div id="acid" class="solution"></div>
        <div id="acid-paper" class="litmus-paper"></div>
    </div>

    <!-- Base Beaker -->
    <div class="beaker">
        NaOH
        <div id="base" class="solution"></div>
        <div id="base-paper" class="litmus-paper"></div>
    </div>

    <!-- Neutral Beaker -->
    <div class="beaker">
        H₂O
        <div id="neutral" class="solution"></div>
        <div id="neutral-paper" class="litmus-paper"></div>
    </div>
</div>
"""

# Inject HTML structure into Streamlit
st.markdown(html_structure, unsafe_allow_html=True)
