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

        .simulation {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }

        .beaker {
            width: 100px;
            height: 200px;
            border: 2px solid #aaa;
            border-radius: 10px;
            position: relative;
            background-color: #f0f0f0;
            overflow: hidden;
        }

        .baking-soda {
            width: 80%;
            height: 20px;
            background-color: white;
            position: absolute;
            bottom: 40%;
            left: 10%;
        }

        .vinegar {
            width: 80%;
            height: 150px;
            background-color: rgba(173, 216, 230, 0.5);
            position: absolute;
            bottom: 0;
            left: 10%;
        }

        .bubbles {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background-color: white;
            position: absolute;
            bottom: 50%;
            animation: bubble-rise 1s infinite;
        }

        @keyframes bubble-rise {
            0% { transform: translateY(0); opacity: 1; }
            100% { transform: translateY(-150px); opacity: 0; }
        }

        .sodium {
            width: 30px;
            height: 30px;
            background-color: white;
            border-radius: 5px;
            position: relative;
            display: inline-block;
            margin: 0 10px;
        }

        .explosion {
            display: none;
            width: 300px;
            height: 200px;
            position: absolute;
            background: radial-gradient(circle, red, orange);
            border-radius: 50%;
            animation: explode 0.5s forwards;
        }

        @keyframes explode {
            0% { transform: scale(0); opacity: 1; }
            100% { transform: scale(3); opacity: 0; }
        }

        .pH-paper {
            width: 10px;
            height: 50px;
            background-color: white;
            border-radius: 5px;
            position: relative;
            margin: 0 5px;
            display: inline-block;
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

        # Beaker simulation
        st.markdown("""
        <div class="simulation">
            <div class="beaker">
                <div class="vinegar"></div>
                <div class="baking-soda"></div>
                <div class="bubbles" style="left: 20%; animation-delay: 0s;"></div>
                <div class="bubbles" style="left: 40%; animation-delay: 0.2s;"></div>
                <div class="bubbles" style="left: 60%; animation-delay: 0.4s;"></div>
                <div class="bubbles" style="left: 80%; animation-delay: 0.6s;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("**Reaction:**")
        st.write("NaHCO₃  + CH₃COOH  → CO₂ + H₂O + NaCH₃COO")

    elif reaction_type == "Exothermic (Warning: Explosive!)":
        st.markdown('<div class="card">Exothermic Reaction</div>', unsafe_allow_html=True)
        st.write("Adding sodium (Na) to water (H₂O)...")
        st.write("**Warning: Explosive Reaction!**")
        st.write("Watch out for sparks and a loud BOOM!")

        # Sodium and explosion simulation
        st.markdown("""
        <div class="simulation" style="position: relative;">
            <div class="sodium"></div>
            <div class="explosion" id="explosion"></div>
        </div>
        """, unsafe_allow_html=True)

        st.write("**Reaction:**")
        st.write("2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g)")

        # Trigger explosion (placeholder)
        st.write("BOOM!")  # Placeholder for explosion sound and effect
        st.markdown("""
        <script>
        setTimeout(() => {
            const explosion = document.getElementById('explosion');
            explosion.style.display = 'block';
        }, 1000);
        </script>
        """, unsafe_allow_html=True)

    elif reaction_type == "Indicator":
        st.markdown('<div class="card">Indicator Reaction</div>', unsafe_allow_html=True)
        st.write("Adding pH paper to different solutions...")

        # pH paper simulation
        st.write("Observe the color changes according to the pH level of the solutions.")

        # Simulating pH paper color changes
        st.markdown("""
        <div class="simulation">
            <div class="pH-paper" style="background-color: red;"></div>
            <div class="pH-paper" style="background-color: green;"></div>
            <div class="pH-paper" style="background-color: blue;"></div>
            <div class="pH-paper" style="background-color: yellow;"></div>
            <div class="pH-paper" style="background-color: orange;"></div>
            <div class="pH-paper" style="background-color: purple;"></div>
        </div>
        """, unsafe_allow_html=True)

        st.write("**Color Changes:**")
        st.write("Acidic Solution: Red")
        st.write("Neutral Solution: Green")
        st.write("Basic Solution: Blue")
        st.write("Other Solutions: Yellow, Orange, Purple")

# To run the lab function, uncomment below line
# lab()
