import streamlit as st

def lab():
    # CSS for the glowing animated title and animations
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

        .reaction-container {
            display: flex;
            justify-content: space-around;
            margin: 20px;
        }

        .beaker {
            width: 100px;
            height: 200px;
            border: 2px solid #444;
            border-radius: 10px 10px 0 0;
            position: relative;
            background-color: rgba(173, 216, 230, 0.7);
        }

        .baking-soda {
            position: absolute;
            width: 20px;
            height: 20px;
            background-color: white;
            animation: drop-baking-soda 2s forwards;
        }

        @keyframes drop-baking-soda {
            0% { top: -20px; opacity: 1; }
            100% { top: 160px; opacity: 0; }
        }

        .bubbles {
            position: absolute;
            bottom: 50px;
            width: 15px;
            height: 15px;
            background-color: white;
            border-radius: 50%;
            animation: bubble-rise 1s infinite;
            opacity: 0.8;
        }

        @keyframes bubble-rise {
            0% { transform: translateY(0); opacity: 1; }
            100% { transform: translateY(-150px); opacity: 0; }
        }

        .explosion {
            position: relative;
            width: 100px;
            height: 200px;
            border: 2px solid #444;
            border-radius: 10px 10px 0 0;
            background-color: rgba(173, 216, 230, 0.7);
            animation: shake 0.5s infinite alternate;
        }

        @keyframes shake {
            0% { transform: translateX(0); }
            100% { transform: translateX(-10px); }
        }

        .sparks {
            position: absolute;
            width: 5px;
            height: 5px;
            background-color: red;
            border-radius: 50%;
            animation: spark 1s infinite;
        }

        @keyframes spark {
            0% { opacity: 1; transform: translateY(0); }
            50% { opacity: 1; transform: translateY(-20px); }
            100% { opacity: 0; transform: translateY(-40px); }
        }

        .indicator {
            width: 50px;
            height: 10px;
            background-color: lightblue;
            position: absolute;
            bottom: 0;
            animation: dip 2s forwards;
        }

        @keyframes dip {
            0% { transform: translateY(0); }
            100% { transform: translateY(-100px); }
        }

        .acid-solution { background-color: lightcoral; }
        .neutral-solution { background-color: lightgreen; }
        .base-solution { background-color: lightblue; }

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
        st.markdown('<div class="beaker" style="position: relative;">'
                    '<div class="baking-soda"></div>'
                    '<div class="bubbles" style="animation-delay: 0s;"></div>'
                    '<div class="bubbles" style="animation-delay: 0.2s;"></div>'
                    '<div class="bubbles" style="animation-delay: 0.4s;"></div>'
                    '<div class="bubbles" style="animation-delay: 0.6s;"></div>'
                    '<div class="bubbles" style="animation-delay: 0.8s;"></div>'
                    '</div>', unsafe_allow_html=True)
        
        st.write("Adding baking soda (NaHCO₃) to vinegar (CH₃COOH)...")
        st.write("Observe the bubbles forming as CO₂ is released!")
        st.write("**Reaction:**")
        st.write("NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")

    elif reaction_type == "Exothermic (Warning: Explosive!)":
        st.markdown('<div class="explosion"></div>', unsafe_allow_html=True)
        st.write("Adding sodium (Na) to water (H₂O)...")
        st.write("**Warning: Explosive Reaction!**")
        st.write("Watch out for sparks and a loud BOOM!")
        st.write("**Reaction:**")
        st.write("2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g)")

        # Displaying sparks
        for i in range(5):
            st.markdown(f'<div class="sparks" style="animation-delay: {i * 0.2}s; left: {i * 20}px;"></div>', unsafe_allow_html=True)

    elif reaction_type == "Indicator":
        st.markdown('<div style="position: relative; width: 100%; height: 300px;">'
                    '<div class="indicator" style="animation-delay: 0s;"></div>'
                    '<div class="beaker acid-solution" style="position: absolute; left: 10%;"></div>'
                    '<div class="beaker neutral-solution" style="position: absolute; left: 45%;"></div>'
                    '<div class="beaker base-solution" style="position: absolute; left: 80%;"></div>'
                    '</div>', unsafe_allow_html=True)
        
        st.write("Adding pH paper to different solutions...")
        st.write("Observe the color changes according to the pH level of the solutions:")
        st.write("- Acidic Solution: Red")
        st.write("- Neutral Solution: Green")
        st.write("- Basic Solution: Blue")

# To run the lab function, uncomment below line
# lab()
