import streamlit as st

def lab():
    st.markdown(
        """
        <style>
        /* Neon glowing title animation */
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

        /* Baking soda and vinegar reaction */
        .vinegar-beaker {
            display: inline-block;
            width: 140px;
            height: 200px;
            position: relative;
            margin: 20px;
            overflow: hidden;
            background: #ffcccc;
            border-radius: 0 0 20px 20px;
            animation: wave 3s infinite;
        }

        .baking-soda {
            width: 40px;
            height: 60px;
            background: #fff;
            border: 2px solid #ddd;
            position: absolute;
            top: -40px;
            left: 50%;
            transform: translateX(-50%);
            animation: pour-baking-soda 3s forwards;
        }

        @keyframes pour-baking-soda {
            0% { top: -40px; }
            100% { top: 80px; }
        }

        .bubbles {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 100%;
            opacity: 0;
            animation: show-bubbles 4s forwards;
        }

        @keyframes show-bubbles {
            0% { opacity: 0; }
            50% { opacity: 0.6; }
            100% { opacity: 1; }
        }

        .bubble {
            position: absolute;
            bottom: 0;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: rise 2s infinite;
        }

        @keyframes rise {
            0% { transform: translateY(0); opacity: 1; }
            100% { transform: translateY(-120px); opacity: 0; }
        }

        /* Sodium and water reaction */
        .water-beaker {
            display: inline-block;
            width: 140px;
            height: 200px;
            background: #cceeff;
            position: relative;
            margin: 20px;
            overflow: hidden;
            border-radius: 0 0 20px 20px;
            animation: wave 3s infinite;
        }

        .sodium {
            width: 30px;
            height: 30px;
            background: #bbb;
            border-radius: 50%;
            position: absolute;
            top: -50px;
            left: 50%;
            transform: translateX(-50%);
            animation: pour-sodium 2s forwards;
        }

        @keyframes pour-sodium {
            0% { top: -50px; }
            100% { top: 70px; }
        }

        .explosion {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 300px;
            height: 300px;
            opacity: 0;
            animation: explode 2s forwards;
            animation-delay: 2s;
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

        /* Solution wave for indicator */
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
            <div class='vinegar-beaker'>
                <div class='baking-soda'></div>
                <div class='bubbles'>
                    <div class='bubble' style='width: 10px; height: 10px; left: 20%;'></div>
                    <div class='bubble' style='width: 15px; height: 15px; left: 40%;'></div>
                    <div class='bubble' style='width: 12px; height: 12px; left: 60%;'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    elif reaction_type == "Exothermic (sodium & water)":
        st.markdown("""
            <div class='water-beaker'>
                <div class='sodium'></div>
                <div class='explosion'></div>
                <div class='fire'></div>
            </div>
        """, unsafe_allow_html=True)

    elif reaction_type == "Indicator":
        st.markdown("""
            <div class='water-beaker indicator-wave'>
                <div class='liquid' style='background: rgba(255,255,255,0.9);'></div>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    lab()
