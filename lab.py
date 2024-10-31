import streamlit as st

def lab():
    # CSS for the glowing animated title
    st.markdown(
        """
        <style>
        .glowing-title {
            font-size: 2.5em;
            color: black;
            text-align: center;
            text-shadow: 0 0 10px #add8e6, 0 0 20px #add8e6, 0 0 30px #add8e6, 0 0 40px #add8e6;
            animation: text-glow 1.5s infinite alternate, move-title 2s infinite alternate;
        }
        
        @keyframes text-glow {
            from {
                text-shadow: 0 0 5px #add8e6, 0 0 10px #add8e6;
            }
            to {
                text-shadow: 0 0 20px #add8e6, 0 0 30px #add8e6;
            }
        }

        @keyframes move-title {
            0% { transform: translateX(0); }
            50% { transform: translateX(-10px); }
            100% { transform: translateX(0); }
        }

        .card {
            display: inline-block;
            background-color: #f0f0f0;
            border-radius: 10px;
            padding: 20px;
            margin: 10px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            transition: transform 0.2s;
            animation: move-card 1.5s infinite alternate;
        }

        @keyframes move-card {
            0% { transform: translateY(0); }
            50% { transform: translateY(-5px); }
            100% { transform: translateY(0); }
        }

        .card:hover {
            transform: scale(1.05);
        }

        .reaction {
            font-size: 1.5em;
            margin-top: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display the title with the CSS class
    st.markdown('<h1 class="glowing-title">Virtual Chemistry Lab 🧪</h1>', unsafe_allow_html=True)

    # Selection for reaction type
    st.subheader("Choose your reaction type:")
    reaction_type = st.selectbox("", ["", "Acid-Base (baking soda & vinegar)", "Exothermic (Warning: Explosive!)", "Indicator"])

    # Reaction simulation
    if reaction_type == "Acid-Base (baking soda & vinegar)":
        st.markdown('<div class="card">Acid-Base Reaction</div>', unsafe_allow_html=True)
        st.write("Adding baking soda (NaHCO₃) to vinegar (CH₃COOH)...")
        st.write("Observe the bubbles forming as CO₂ is released!")
        st.write("**Reaction:**")
        st.write("NaHCO₃  + CH₃COOH  → CO₂ + H₂O + NaCH₃COO")
        
        # Here you would implement a simple animation or visualization code
        st.balloons()  # Placeholder for bubbles

    elif reaction_type == "Exothermic (Warning: Explosive!)":
        st.markdown('<div class="card">Exothermic Reaction</div>', unsafe_allow_html=True)
        st.write("Adding sodium (Na) to water (H₂O)...")
        st.write("**Warning: Explosive Reaction!**")
        st.write("Watch out for sparks and a loud BOOM!")
        st.write("**Reaction:**")
        st.write("2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g)")
        
        # Here you would implement an explosion effect
        st.write("BOOM!")  # Placeholder for explosion sound and effect

    elif reaction_type == "Indicator":
        st.markdown('<div class="card">Indicator Reaction</div>', unsafe_allow_html=True)
        st.write("Adding pH paper to different solutions...")
        st.write("Observe the color changes according to the pH level of the solutions.")
        
        # Placeholder for the pH paper and solutions
        st.write("Acidic Solution: Red")
        st.write("Neutral Solution: Green")
        st.write("Basic Solution: Blue")

# To run the lab function, uncomment below line
# lab()
