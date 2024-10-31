import streamlit as st
import time

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

        .reaction {
            font-size: 1.5em;
            margin-top: 20px;
        }
        
        .beaker {
            width: 100px;
            height: 150px;
            border: 2px solid #555;
            border-radius: 10px;
            background: linear-gradient(to top, #f0f0f0, #cfe3f4);
            position: relative;
            margin: auto;
            overflow: hidden;
        }

        .bubbles {
            background-color: white;
            border-radius: 50%;
            position: absolute;
            width: 10px;
            height: 10px;
            animation: bubble-rise 1s linear infinite;
        }

        @keyframes bubble-rise {
            0% { bottom: 0; opacity: 1; }
            100% { bottom: 100%; opacity: 0; }
        }

        .sodium {
            width: 20px;
            height: 20px;
            background-color: white;
            border-radius: 5px;
            margin: auto;
            position: relative;
        }

        .explosion {
            display: none;
            color: red;
            font-size: 3em;
            text-align: center;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            animation: explode 0.5s forwards;
        }

        @keyframes explode {
            0% { transform: scale(1); opacity: 1; }
            100% { transform: scale(3); opacity: 0; }
        }

        .ph-paper {
            width: 40px;
            height: 10px;
            background-color: lightcoral;
            margin: auto;
            display: none;
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

        # Display the beaker with bubbles
        st.markdown('<div class="beaker" id="beaker"><div class="bubbles"></div></div>', unsafe_allow_html=True)
        st.write("Observe the bubbles forming as CO₂ is released!")
        st.write("**Reaction:**")
        st.write("NaHCO₃  + CH₃COOH  → CO₂ + H₂O + NaCH₃COO")

        # Simulating bubbles
        for _ in range(5):  # Simulating multiple bubbles
            st.markdown('<div class="bubbles"></div>', unsafe_allow_html=True)
            time.sleep(0.5)  # Delay for effect

    elif reaction_type == "Exothermic (Warning: Explosive!)":
        st.markdown('<div class="card">Exothermic Reaction</div>', unsafe_allow_html=True)
        st.write("Adding sodium (Na) to water (H₂O)...")
        st.write("**Warning: Explosive Reaction!**")
        st.write("Watch out for sparks and a loud BOOM!")
        
        # Display sodium and water
        sodium_display = st.markdown('<div class="sodium">Na</div>', unsafe_allow_html=True)
        water_display = st.markdown('<div class="beaker" id="water"><div style="background-color: #00f; height: 100%;"></div></div>', unsafe_allow_html=True)
        
        # Simulating explosion
        time.sleep(1)  # Delay before explosion
        explosion_display = st.markdown('<div class="explosion" id="explosion">BOOM!</div>', unsafe_allow_html=True)
        st.write("**Reaction:**")
        st.write("2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g)")
        
        # Make explosion visible
        time.sleep(1)
        st.markdown('<script>document.getElementById("explosion").style.display="block";</script>', unsafe_allow_html=True)

    elif reaction_type == "Indicator":
        st.markdown('<div class="card">Indicator Reaction</div>', unsafe_allow_html=True)
        st.write("Adding pH paper to different solutions...")
        st.write("Observe the color changes according to the pH level of the solutions.")

        # Display pH paper and simulate color change
        for color in ["lightcoral", "lightgreen", "lightblue"]:  # Simulating color changes
            st.markdown(f'<div class="ph-paper" style="background-color: {color};"></div>', unsafe_allow_html=True)
            time.sleep(1)  # Delay for effect
            st.write("Color changed!")

# To run the lab function, uncomment below line
# lab()
