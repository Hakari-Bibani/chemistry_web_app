import streamlit as st
import time

def lab():
    # CSS for the glowing animated title and cards
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

        .reaction {
            font-size: 1.5em;
            margin-top: 20px;
        }

        .beaker {
            display: inline-block;
            width: 100px;
            height: 150px;
            border: 2px solid #999;
            border-radius: 5px;
            position: relative;
            margin: 0 20px;
            background-color: #e0e0e0;
            overflow: hidden;
        }

        .bubbles {
            position: absolute;
            bottom: 10px;
            left: 10px;
            width: 80%;
            height: 30px;
            background: rgba(255, 255, 255, 0.5);
            border-radius: 50%;
            animation: bubble-rise 1.5s infinite;
        }

        @keyframes bubble-rise {
            0% { transform: translateY(20px); opacity: 1; }
            50% { opacity: 0.7; }
            100% { transform: translateY(-30px); opacity: 0; }
        }

        .sodium {
            display: inline-block;
            width: 30px;
            height: 30px;
            background-color: white;
            border: 2px solid #999;
            border-radius: 50%;
            position: absolute;
            top: 10%;
            left: 50%;
            transform: translateX(-50%);
        }

        .explosion {
            display: none;
            color: red;
            font-size: 2em;
            text-align: center;
            animation: explode 1s forwards;
        }

        @keyframes explode {
            from { opacity: 0; }
            to { opacity: 1; transform: scale(2); }
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

        # Show the beaker and add baking soda
        st.markdown('<div class="beaker"><div class="bubbles"></div></div>', unsafe_allow_html=True)
        st.write("Baking soda is being added...")
        time.sleep(2)  # Simulate the time for adding baking soda
        st.write("Bubbles are rising up!")

    elif reaction_type == "Exothermic (Warning: Explosive!)":
        st.markdown('<div class="card">Exothermic Reaction</div>', unsafe_allow_html=True)
        st.write("Adding sodium (Na) to water (H₂O)...")
        st.write("**Warning: Explosive Reaction!**")
        st.write("Watch out for sparks and a loud BOOM!")
        st.write("**Reaction:**")
        st.write("2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g)")

        # Show the sodium being added
        st.markdown('<div class="beaker"><div class="sodium"></div></div>', unsafe_allow_html=True)
        st.write("Sodium is being added...")
        time.sleep(2)  # Simulate the time for adding sodium
        st.markdown('<div class="explosion">BOOM!</div>', unsafe_allow_html=True)
        time.sleep(1)  # Pause before the next line
        st.write("An explosion occurs!")

    elif reaction_type == "Indicator":
        st.markdown('<div class="card">Indicator Reaction</div>', unsafe_allow_html=True)
        st.write("Adding pH paper to different solutions...")
        st.write("Observe the color changes according to the pH level of the solutions.")

        # Show the pH paper diving into solutions
        st.write("The pH paper is being added to the solutions...")
        time.sleep(2)  # Simulate the time for adding the pH paper
        st.write("Acidic Solution: Red")
        st.write("Neutral Solution: Green")
        st.write("Basic Solution: Blue")
        st.write("The pH paper changes color based on the solution it is in!")

# To run the lab function, uncomment below line
# lab()
