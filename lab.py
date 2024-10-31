import streamlit as st
import time

def lab():
    st.markdown(
        """
        <style>
        /* Glowing Animated Title */
        @keyframes text-glow {
            0%, 100% { color: #00e5ff; text-shadow: 0 0 5px #00e5ff, 0 0 10px #00e5ff, 0 0 15px #00e5ff, 0 0 20px #00e5ff; }
            50% { color: #fff; text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff, 0 0 30px #ff00ff, 0 0 40px #ff00ff; }
        }

        h1 { 
            font-size: 2.5em;
            text-align: center;
            margin-bottom: 1em;
            animation: text-glow 2s infinite;
        }

        /* Basic beaker and liquid setup */
        .beaker {
            display: inline-block;
            width: 140px;
            height: 200px;
            border: 5px solid #ddd;
            border-radius: 0 0 20px 20px;
            position: relative;
            margin: 40px;
            background: transparent;
            overflow: hidden;
        }

        /* Baking Soda & Vinegar Reaction */
        .vinegar { background: rgba(255, 100, 100, 0.8); }
        
        .powder-container, .powder-stream {
            position: absolute;
            animation: pour 2s forwards;
        }

        @keyframes pour {
            0% { transform: translateY(-40px) rotate(0); }
            50% { transform: translateY(0) rotate(30deg); }
            100% { transform: translateY(-40px) rotate(0); }
        }

        .bubbles {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 100%;
            opacity: 0;
            animation: bubble-rise 3s forwards 1s;
        }

        @keyframes bubble-rise {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }

        .bubble {
            position: absolute;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.8);
            animation: float 2s infinite;
        }

        /* Sodium & Water Explosion */
        .explosion {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            animation: explode 1s ease-out 1.5s forwards;
        }

        @keyframes explode {
            0% { transform: scale(0); opacity: 1; }
            50% { transform: scale(1.5); opacity: 1; background: #ff8800; }
            100% { transform: scale(2); opacity: 0; }
        }

        .spark {
            position: absolute;
            width: 6px;
            height: 6px;
            background: yellow;
            animation: spark-move 1s ease-out infinite;
        }

        @keyframes spark-move {
            from { transform: translate(0, 0); opacity: 1; }
            to { transform: translate(var(--x), var(--y)); opacity: 0; }
        }

        /* Indicator Reaction */
        .liquid { background: rgba(255, 255, 255, 0.95); animation: wave 3s ease-in-out infinite; }

        @keyframes wave {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(5px); }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1>Virtual Chemistry Lab 🧪</h1>', unsafe_allow_html=True)

    st.subheader("Choose your reaction type:")
    reaction_type = st.selectbox("", ["", "Acid-Base (baking soda & vinegar)", "Exothermic (Warning: Explosive!)", "Indicator"])

    if reaction_type == "Acid-Base (baking soda & vinegar)":
        st.markdown("""
            <div class='beaker'>
                <div class='liquid vinegar'></div>
                <div class='powder-container'></div>
                <div class='powder-stream'></div>
                <div class='bubbles'>
                    <div class='bubble' style='--x-start: 10px; --size: 10px;'></div>
                    <div class='bubble' style='--x-start: -15px; --size: 15px;'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    elif reaction_type == "Exothermic (Warning: Explosive!)":
        st.markdown("""
            <div class='beaker'>
                <div class='liquid' style='background: rgba(173, 216, 230, 0.8);'></div>
                <div class='explosion'></div>
                <div class='spark' style='--x: 100px; --y: -120px;'></div>
                <div class='spark' style='--x: -80px; --y: -100px;'></div>
            </div>
        """, unsafe_allow_html=True)
        
    elif reaction_type == "Indicator":
        st.markdown("""
            <div style='display: flex; justify-content: center;'>
                <div class='beaker'>
                    <div class='liquid' style='background: rgba(255, 99, 71, 0.7);'></div>
                </div>
                <div class='beaker'>
                    <div class='liquid' style='background: rgba(60, 179, 113, 0.7);'></div>
                </div>
                <div class='beaker'>
                    <div class='liquid' style='background: rgba(70, 130, 180, 0.7);'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    lab()
