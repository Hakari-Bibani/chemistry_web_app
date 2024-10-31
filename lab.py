import streamlit as st

def lab():
    # CSS for the glowing animated title and reactions
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

        /* Beaker styles */
        .beaker {
            width: 100px;
            height: 200px;
            border: 3px solid #333;
            border-radius: 10px 10px 0 0;
            position: relative;
            overflow: hidden;
            background-color: #e0e0e0;
        }

        .liquid {
            width: 100%;
            height: 50%;
            background-color: #add8e6; /* Color of vinegar */
            position: absolute;
            bottom: 0;
            transition: height 1s;
        }

        .sodium {
            width: 20px;
            height: 20px;
            background-color: white; /* Sodium color */
            position: absolute;
            bottom: 60px; /* Adjust for appearance above the beaker */
            left: 40%;
            transition: transform 0.5s;
        }

        .bubble {
            background-color: #ffffff;
            border-radius: 50%;
            position: absolute;
            animation: rise 1s forwards;
        }

        @keyframes rise {
            0% { transform: translateY(0); opacity: 1; }
            100% { transform: translateY(-100px); opacity: 0; }
        }

        /* pH paper styles */
        .ph-paper {
            width: 10px;
            height: 40px;
            background-color: pink; /* Initial color of pH paper */
            border: 1px solid #000;
            position: relative;
            animation: dive 1s forwards;
        }

        @keyframes dive {
            0% { transform: translateY(0); }
            100% { transform: translateY(200px); }
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

    # Acid-Base Reaction Simulation
    if reaction_type == "Acid-Base (baking soda & vinegar)":
        st.markdown('<div class="card">Acid-Base Reaction</div>', unsafe_allow_html=True)
        st.write("Adding baking soda (NaHCO₃) to vinegar (CH₃COOH)...")
        
        # Display the beaker
        st.markdown('<div class="beaker"><div class="liquid"></div></div>', unsafe_allow_html=True)
        
        # Simulate bubbles rising
        for i in range(5):
            st.markdown(f'<div class="bubble" style="width: {i * 5 + 10}px; height: {i * 5 + 10}px; left: {i * 10 + 10}px;"></div>', unsafe_allow_html=True)
        
        st.write("Observe the bubbles forming as CO₂ is released!")
        st.write("**Reaction:**")
        st.write("NaHCO₃  + CH₃COOH  → CO₂ + H₂O + NaCH₃COO")

    # Exothermic Reaction Simulation
    elif reaction_type == "Exothermic (Warning: Explosive!)":
        st.markdown('<div class="card">Exothermic Reaction</div>', unsafe_allow_html=True)
        st.write("Adding sodium (Na) to water (H₂O)...")
        st.write("**Warning: Explosive Reaction!**")
        
        # Display the beaker with water
        st.markdown('<div class="beaker"><div class="liquid" style="background-color: lightblue;"></div></div>', unsafe_allow_html=True)
        
        # Simulate sodium addition and explosion
        st.markdown('<div class="sodium"></div>', unsafe_allow_html=True)
        st.write("Watch out for sparks and a loud BOOM!")
        st.write("**Reaction:**")
        st.write("2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g)")

        # Placeholder for explosion effect (you can implement your own)
        st.write("BOOM!")  # Placeholder for explosion sound and effect

    # Indicator Reaction Simulation
    elif reaction_type == "Indicator":
        st.markdown('<div class="card">Indicator Reaction</div>', unsafe_allow_html=True)
        st.write("Adding pH paper to different solutions...")
        
        # Display the pH paper diving into solutions
        for solution in ["Acidic", "Neutral", "Basic"]:
            st.markdown(f'<div class="ph-paper" style="background-color: {solution_color(solution)};"></div>', unsafe_allow_html=True)
            st.write(f"{solution} Solution: {solution_color(solution)}")

# Function to determine the color of the pH paper based on the solution type
def solution_color(type):
    if type == "Acidic":
        return "red"
    elif type == "Neutral":
        return "green"
    elif type == "Basic":
        return "blue"
    return "pink"  # Default color for pH paper

# To run the lab function, uncomment below line
# lab()
