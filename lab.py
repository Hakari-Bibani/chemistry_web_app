import streamlit as st
import time

def lab():
    st.markdown("""
        <style>
        /* Base styles from your original CSS */
        .glowing-title {
            font-size: 2.5em;
            color: black;
            text-align: center;
            text-shadow: 0 0 10px #add8e6, 0 0 20px #add8e6, 0 0 30px #add8e6, 0 0 40px #add8e6;
            animation: text-glow 1.5s infinite alternate, move-title 2s infinite alternate;
        }
        
        @keyframes text-glow {
            from { text-shadow: 0 0 5px #add8e6, 0 0 10px #add8e6; }
            to { text-shadow: 0 0 20px #add8e6, 0 0 30px #add8e6; }
        }

        @keyframes move-title {
            0% { transform: translateX(0); }
            50% { transform: translateX(-10px); }
            100% { transform: translateX(0); }
        }

        /* Enhanced beaker and reaction animations */
        .beaker {
            width: 120px;
            height: 150px;
            background: rgba(255, 255, 255, 0.9);
            border: 3px solid #666;
            border-radius: 0 0 10px 10px;
            position: relative;
            margin: 20px auto;
            overflow: hidden;
        }

        .liquid {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 80%;
            background: rgba(255, 255, 255, 0.8);
            transition: all 0.5s;
        }

        .powder {
            position: absolute;
            top: -20px;
            left: 50%;
            width: 20px;
            height: 20px;
            background: white;
            border-radius: 50%;
            animation: fall 2s linear forwards;
        }

        @keyframes fall {
            0% { transform: translateY(0) translateX(-50%) rotate(0deg); }
            100% { transform: translateY(170px) translateX(-50%) rotate(360deg); }
        }

        .bubbles {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 100%;
            animation: bubble-rise 2s infinite;
        }

        .bubble {
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: float-up 3s infinite;
        }

        @keyframes float-up {
            0% { transform: translateY(100%) scale(1); opacity: 1; }
            100% { transform: translateY(-100%) scale(0); opacity: 0; }
        }

        .explosion-effect {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 200px;
            height: 200px;
            background: radial-gradient(circle, #ff4444, transparent);
            border-radius: 50%;
            animation: explode 1s forwards;
        }

        @keyframes explode {
            0% { transform: translate(-50%, -50%) scale(0); opacity: 0; }
            50% { transform: translate(-50%, -50%) scale(1.5); opacity: 1; }
            100% { transform: translate(-50%, -50%) scale(2); opacity: 0; }
        }

        /* pH Paper styles */
        .ph-container {
            display: flex;
            justify-content: space-around;
            margin: 20px 0;
        }

        .ph-beaker {
            width: 80px;
            height: 100px;
            position: relative;
            border: 2px solid #666;
            border-radius: 0 0 10px 10px;
        }

        .ph-paper {
            width: 10px;
            height: 40px;
            background: #fff;
            position: absolute;
            top: -50px;
            left: 50%;
            transform: translateX(-50%);
            animation: dip-paper 4s forwards;
        }

        @keyframes dip-paper {
            0% { top: -50px; }
            40% { top: 20px; }
            60% { top: 20px; }
            100% { top: -50px; }
        }

        .acid-solution { background: rgba(255, 0, 0, 0.2); }
        .neutral-solution { background: rgba(0, 255, 0, 0.2); }
        .base-solution { background: rgba(0, 0, 255, 0.2); }

        .paper-acid { background: #ff6666; }
        .paper-neutral { background: #66ff66; }
        .paper-base { background: #6666ff; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="glowing-title">Virtual Chemistry Lab 🧪</h1>', unsafe_allow_html=True)
    
    reaction_type = st.selectbox("Select Reaction Type:", 
                               ["", "Acid-Base (baking soda & vinegar)", 
                                "Exothermic (Warning: Explosive!)", 
                                "Indicator"])

    if reaction_type == "Acid-Base (baking soda & vinegar)":
        st.write("### Acid-Base Reaction: Baking Soda & Vinegar")
        if st.button("Start Reaction"):
            st.markdown("""
                <div class="beaker">
                    <div class="liquid"></div>
                    <div class="powder"></div>
                    <div class="bubbles">
                        <div class="bubble" style="left: 20%; animation-delay: 0s;"></div>
                        <div class="bubble" style="left: 40%; animation-delay: 0.5s;"></div>
                        <div class="bubble" style="left: 60%; animation-delay: 1s;"></div>
                        <div class="bubble" style="left: 80%; animation-delay: 1.5s;"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.latex(r"NaHCO_3 + CH_3COOH \rightarrow CO_2 + H_2O + NaCH_3COO")

    elif reaction_type == "Exothermic (Warning: Explosive!)":
        st.write("### Exothermic Reaction: Sodium & Water")
        if st.button("Start Reaction"):
            st.markdown("""
                <div class="beaker">
                    <div class="liquid"></div>
                    <div class="powder"></div>
                    <div class="explosion-effect"></div>
                </div>
            """, unsafe_allow_html=True)
            st.markdown('<h2 style="color: red; text-align: center; animation: text-glow 0.5s infinite;">💥 BOOM! 💥</h2>', 
                       unsafe_allow_html=True)
            st.latex(r"2Na(s) + 2H_2O(l) \rightarrow 2NaOH(aq) + H_2(g)")

    elif reaction_type == "Indicator":
        st.write("### pH Indicator Test")
        if st.button("Test Solutions"):
            st.markdown("""
                <div class="ph-container">
                    <div class="ph-beaker acid-solution">
                        <div class="ph-paper" style="animation-delay: 0s;"></div>
                        <div class="liquid"></div>
                    </div>
                    <div class="ph-beaker neutral-solution">
                        <div class="ph-paper" style="animation-delay: 2s;"></div>
                        <div class="liquid"></div>
                    </div>
                    <div class="ph-beaker base-solution">
                        <div class="ph-paper" style="animation-delay: 4s;"></div>
                        <div class="liquid"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.write("Results:")
            st.write("🔴 Acidic solution: pH < 7")
            st.write("🟢 Neutral solution: pH = 7")
            st.write("🔵 Basic solution: pH > 7")

if __name__ == "__main__":
    lab()
