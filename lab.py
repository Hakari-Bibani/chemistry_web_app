import streamlit as st
import time

def lab():
    st.markdown(
        """
        <style>
        @keyframes text-glow {
            0%, 100% { color: #fff; text-shadow: 0 0 5px #ff69b4, 0 0 10px #ff69b4, 0 0 20px #ff69b4; }
            50% { color: #ff69b4; text-shadow: 0 0 20px #ff69b4, 0 0 30px #ff69b4, 0 0 40px #ff69b4; }
        }

        h1 {
            font-size: 3em;
            text-align: center;
            margin-bottom: 2em;
            animation: text-glow 3s ease-in-out infinite;
        }

        .beaker {
            display: inline-block;
            width: 140px;
            height: 200px;
            border: 5px solid #ddd;
            border-radius: 0 0 20px 20px;
            position: relative;
            margin: 40px;
            overflow: hidden;
            box-shadow: inset 0 0 20px rgba(255,255,255,0.2);
            background: transparent;
        }

        .beaker .liquid {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 50%;
            background: rgba(0, 128, 255, 0.3);
            transition: all 0.5s;
        }

        /* Baking soda pour and bubbles */
        .pour-container {
            position: absolute;
            top: -60px;
            left: 50%;
            transform: translateX(-50%) rotate(-10deg);
            width: 40px;
            height: 40px;
            background: #fff;
            border: 2px solid #999;
            animation: pour 3s forwards;
            transform-origin: bottom right;
        }

        @keyframes pour {
            0% { transform: translateX(-50%) rotate(-10deg); }
            30% { transform: translateX(-50%) rotate(45deg); }
            100% { transform: translateX(-50%) rotate(-10deg); }
        }

        .bubbles {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 100%;
            opacity: 0;
            animation: show-bubbles 4s forwards;
            animation-delay: 2s;
        }

        .bubble {
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: rise 2s infinite;
        }

        @keyframes rise {
            0% { transform: translateY(0); opacity: 0.9; }
            100% { transform: translateY(-120px); opacity: 0; }
        }

        /* Explosion effect */
        .explosion {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 300px;
            height: 300px;
            transform: translate(-50%, -50%);
            opacity: 0;
            animation: explode 2s forwards;
            animation-delay: 3s;
        }

        @keyframes explode {
            0% { transform: scale(0); opacity: 0; background: radial-gradient(circle, #ff4400 0%, transparent 70%); }
            50% { transform: scale(2); opacity: 1; background: radial-gradient(circle, #ff8800 0%, #ff4400 30%, transparent 70%); }
            100% { transform: scale(3); opacity: 0; background: radial-gradient(circle, #ffbb00 0%, #ff8800 30%, transparent 70%); }
        }

        .fire {
            position: absolute;
            bottom: 50%;
            width: 100%;
            height: 60px;
            animation: burn 2s infinite;
            background: linear-gradient(to top, #ff4400, #ff8800, transparent);
            filter: blur(2px);
        }

        @keyframes burn {
            0%, 100% { transform: scaleY(1); opacity: 0.8; }
            50% { transform: scaleY(1.2); opacity: 1; }
        }

        /* Solution wave */
        .indicator-wave {
            animation: wave 1.5s ease-in-out infinite;
        }

        @keyframes wave {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(5px); }
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown('<h1>Virtual Chemistry Lab 🧪</h1>', unsafe_allow_html=True)
    st.subheader("Choose your reaction type:")
    reaction_type = st.selectbox("", ["", "Acid-Base (baking soda & vinegar)", "Exothermic (sodium & water)", "Indicator"])

    if reaction_type == "Acid-Base (baking soda & vinegar)":
        st.markdown("""
            <div class='beaker'>
                <div class='liquid' style='background: rgba(255,0,0,0.4);'></div>
                <div class='pour-container'></div>
                <div class='bubbles'>
                    <div class='bubble' style='--size: 10px;'></div>
                    <div class='bubble' style='--size: 15px;'></div>
                    <div class='bubble' style='--size: 12px;'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.write("Step 1: Pouring baking soda into the vinegar...")
        st.write("Step 2: Vigorous bubbling reaction observed!")
        st.write("NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")

    elif reaction_type == "Exothermic (sodium & water)":
        st.markdown("""
            <div class='beaker'>
                <div class='liquid' style='background: rgba(0,128,255,0.3);'></div>
                <div class='explosion'></div>
                <div class='fire'></div>
            </div>
        """, unsafe_allow_html=True)
        st.write("Step 1: Carefully adding sodium to water...")
        st.write("Step 2: Violent explosion observed!")
        st.write("2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g) + Energy")

    elif reaction_type == "Indicator":
        st.markdown("""
            <div class='beaker indicator-wave'>
                <div class='liquid' style='background: rgba(255,255,255,0.9);'></div>
            </div>
        """, unsafe_allow_html=True)
        st.write("Step: Dipping pH strip in solution and observing color change.")
        st.write("Acidic: Red, Neutral: Green, Basic: Blue")

if __name__ == "__main__":
    lab()
