import streamlit as st

def lab():
    # Insert all the HTML/CSS from above into this markdown block
    st.markdown("""
        [Insert the entire HTML/CSS code from above here]
    """, unsafe_allow_html=True)

    st.title("Virtual Chemistry Lab 🧪")
    
    reaction_type = st.selectbox("Select Reaction Type:", 
                               ["", "Acid-Base (baking soda & vinegar)", 
                                "Exothermic (Warning: Explosive!)", 
                                "Indicator"])

    if reaction_type == "Acid-Base (baking soda & vinegar)":
        st.write("### Acid-Base Reaction: Baking Soda & Vinegar")
        if st.button("Start Reaction"):
            st.markdown("""
                <div class="beaker acid-base">
                    <div class="vinegar"></div>
                    <div class="powder"></div>
                    <div class="bubble" style="left: 30%; width: 10px; height: 10px;"></div>
                    <div class="bubble" style="left: 50%; width: 15px; height: 15px; animation-delay: 0.5s;"></div>
                    <div class="bubble" style="left: 70%; width: 12px; height: 12px; animation-delay: 1s;"></div>
                </div>
            """, unsafe_allow_html=True)
            st.latex(r"NaHCO_3 + CH_3COOH \rightarrow CO_2 + H_2O + NaCH_3COO")

    elif reaction_type == "Exothermic (Warning: Explosive!)":
        st.write("### Exothermic Reaction: Sodium & Water")
        if st.button("Start Reaction"):
            st.markdown("""
                <div class="beaker sodium">
                    <div class="water"></div>
                    <div class="sodium-piece"></div>
                    <div class="explosion">
                        <script>createSparks();</script>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.latex(r"2Na(s) + 2H_2O(l) \rightarrow 2NaOH(aq) + H_2(g)")

    elif reaction_type == "Indicator":
        st.write("### pH Indicator Test")
        if st.button("Test Solutions"):
            st.markdown("""
                <div class="ph-container">
                    <div class="test-beaker acid-solution">
                        <div class="ph-strip acid-strip"></div>
                    </div>
                    <div class="test-beaker neutral-solution">
                        <div class="ph-strip neutral-strip"></div>
                    </div>
                    <div class="test-beaker base-solution">
                        <div class="ph-strip base-strip"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.write("Results:")
            st.write("🔴 Acidic solution: pH < 7")
            st.write("🟢 Neutral solution: pH = 7")
            st.write("🔵 Basic solution: pH > 7")

if __name__ == "__main__":
    lab()
