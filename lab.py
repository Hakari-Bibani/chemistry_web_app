import streamlit as st

def lab():
    # Glowing animated title
    st.markdown(
        """
        <h1 style="text-align: center; color: black; font-size: 36px; animation: text-glow 1s infinite alternate;">
            <span style="text-shadow: 0 0 20px lightblue, 0 0 30px lightblue;">Virtual Chemistry Lab 🧪</span>
        </h1>
        <style>
            @keyframes text-glow {
                0% { text-shadow: 0 0 10px lightblue, 0 0 20px lightblue; }
                100% { text-shadow: 0 0 20px lightblue, 0 0 30px lightblue; }
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Styled cards for reaction selection
    st.markdown(
        """
        <div style="display: flex; justify-content: center; margin: 20px;">
            <div class="card" onclick="selectReaction('acid-base')">
                <h3>Acid-Base (baking soda & vinegar)</h3>
            </div>
            <div class="card" onclick="selectReaction('exothermic')">
                <h3>Exothermic (Warning: Explosive!)</h3>
            </div>
            <div class="card" onclick="selectReaction('indicator')">
                <h3>Indicator</h3>
            </div>
        </div>
        <style>
            .card {
                border: 1px solid lightblue;
                border-radius: 10px;
                padding: 20px;
                margin: 10px;
                text-align: center;
                cursor: pointer;
                transition: transform 0.2s, box-shadow 0.2s;
                animation: glow 1.5s infinite alternate;
            }
            .card:hover {
                transform: scale(1.05);
                box-shadow: 0 0 20px lightblue;
            }
            @keyframes glow {
                0% { box-shadow: 0 0 10px lightblue; }
                100% { box-shadow: 0 0 20px lightblue; }
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Reaction selection handling
    reaction = st.selectbox("Select a reaction type:", ["", "Acid-Base", "Exothermic", "Indicator"])

    if reaction == "Acid-Base":
        st.write("Add baking soda to vinegar:")
        add_acid_base()
    elif reaction == "Exothermic":
        st.write("Add sodium to water:")
        add_exothermic()
    elif reaction == "Indicator":
        st.write("Add pH paper to solutions:")
        add_indicator()

def add_acid_base():
    if st.button("Add Baking Soda"):
        # Simulation of bubbles
        st.write("Adding baking soda to vinegar...")
        st.markdown(
            """
            <div style="position: relative; height: 200px; overflow: hidden;">
                <div class="bubbles"></div>
            </div>
            <style>
                .bubbles {
                    position: absolute;
                    bottom: 0;
                    left: 50%;
                    transform: translateX(-50%);
                    width: 20px;
                    height: 20px;
                    border-radius: 50%;
                    background: white;
                    opacity: 0.7;
                    animation: bubble-up 1s infinite;
                }
                @keyframes bubble-up {
                    0% { transform: translateY(0); opacity: 0.7; }
                    100% { transform: translateY(-150px); opacity: 0; }
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.write("NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")

def add_exothermic():
    if st.button("Add Sodium"):
        # Show explosion simulation
        st.markdown(
            """
            <h3 style="color: red;">BOOM!</h3>
            <div style="color: orange;">2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g)</div>
            <style>
                @keyframes explode {
                    0% { transform: scale(1); }
                    50% { transform: scale(1.5); color: red; }
                    100% { transform: scale(1); color: black; }
                }
                h3 {
                    animation: explode 1s infinite;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

def add_indicator():
    st.write("Choose a solution to test:")
    solutions = ["Solution 1 (Acid)", "Solution 2 (Base)", "Solution 3 (Neutral)", "Solution 4 (Acid)", "Solution 5 (Base)", "Solution 6 (Neutral)"]
    selected_solution = st.selectbox("Select a solution:", solutions)

    if st.button("Add pH Paper"):
        color_change(selected_solution)

def color_change(solution):
    color_map = {
        "Solution 1 (Acid)": "red",
        "Solution 2 (Base)": "blue",
        "Solution 3 (Neutral)": "green",
        "Solution 4 (Acid)": "red",
        "Solution 5 (Base)": "blue",
        "Solution 6 (Neutral)": "green",
    }
    color = color_map.get(solution, "gray")
    st.markdown(f"<h3 style='color: {color};'>pH Paper Color: {color}</h3>", unsafe_allow_html=True)
