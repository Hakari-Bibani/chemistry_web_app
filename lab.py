import streamlit as st

def lab():
    st.markdown(
        """
        <style>
        @keyframes text-glow {
            0% { text-shadow: 0 0 10px #f0f, 0 0 20px #f0f, 0 0 30px #f0f, 0 0 40px #ff00ff, 0 0 70px #ff00ff, 0 0 80px #ff00ff, 0 0 100px #ff00ff; }
            100% { text-shadow: 0 0 20px #ff00ff, 0 0 30px #ff00ff, 0 0 40px #ff00ff, 0 0 50px #ff00ff, 0 0 70px #ff00ff, 0 0 90px #ff00ff, 0 0 120px #ff00ff; }
        }

        h1 {
            text-align: center;
            margin-bottom: 2em;
            font-size: 2.5em;
            color: #ff00ff;
            animation: text-glow 2s ease-in-out infinite alternate;
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
        }

        .liquid {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 50%;
            transition: all 0.5s;
        }

        .liquid-acid { background: rgba(255, 200, 200, 0.9); }
        .liquid-water { background: rgba(200, 230, 255, 0.9); }

        .bubbles { /* Acid-base bubbles animation */
            position: absolute;
            bottom: 0;
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
            animation: rise 1.5s infinite;
        }

        @keyframes show-bubbles {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }

        @keyframes rise {
            0% { transform: translateY(0) translateX(var(--x-start)); opacity: 0.8; width: var(--size); height: var(--size); }
            100% { transform: translateY(-120px) translateX(var(--x-end)); opacity: 0; width: calc(var(--size) * 2); height: calc(var(--size) * 2); }
        }

        .explosion { /* Exothermic explosion animation */
            position: absolute;
            top: 50%;
            left: 50%;
            width: 300px;
            height: 300px;
            transform: translate(-50%, -50%);
            opacity: 0;
            animation: explode 2s forwards;
            animation-delay: 3s;
            pointer-events: none;
        }

        @keyframes explode {
            0% { transform: translate(-50%, -50%) scale(0); opacity: 0; background: radial-gradient(circle, #ff4400 0%, transparent 70%); }
            50% { transform: translate(-50%, -50%) scale(2); opacity: 1; background: radial-gradient(circle, #ff8800 0%, #ff4400 30%, transparent 70%); }
            100% { transform: translate(-50%, -50%) scale(3); opacity: 0; background: radial-gradient(circle, #ffbb00 0%, #ff8800 30%, transparent 70%); }
        }

        .fire { /* Fire spark animation */
            position: absolute;
            bottom: 50%;
            left: 0;
            width: 100%;
            height: 60px;
            opacity: 0;
            animation: burn 2s infinite;
            animation-delay: 3s;
            filter: blur(2px);
            transform-origin: center bottom;
        }

        @keyframes burn {
            0%, 100% { transform: scaleY(1); opacity: 0.8; background: linear-gradient(to top, #ff4400, #ff8800, transparent); }
            50% { transform: scaleY(1.2); opacity: 1; background: linear-gradient(to top, #ff8800, #ffbb00, transparent); }
        }

        .ph-strip { /* pH strip animation for indicator */
            position: absolute;
            width: 12px;
            height: 100px;
            background: #333;
            left: 50%;
            transform-origin: bottom center;
            animation: dip 6s forwards;
        }

        .ph-strip.acid { animation: dip-acid 6s forwards; }
        .ph-strip.neutral { animation: dip-neutral 6s forwards; }
        .ph-strip.base { animation: dip-base 6s forwards; }

        @keyframes dip-acid {
            0% { transform: translateX(-50%) translateY(-120%); background: #333; }
            80% { transform: translateX(-50%) translateY(30%); background: #ff6b6b; }
            100% { transform: translateX(-50%) translateY(-120%); background: #ff6b6b; }
        }
        /* Additional animations for neutral and base strips */
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
                <div class='liquid liquid-acid'></div>
                <div class='bubbles'>
                    <div class='bubble' style='--x-start: 10px; --x-end: 20px; --size: 10px; animation-delay: 0s;'></div>
                    <div class='bubble' style='--x-start: -15px; --x-end: -25px; --size: 15px; animation-delay: 0.5s;'></div>
                    <div class='bubble' style='--x-start: 5px; --x-end: -10px; --size: 12px; animation-delay: 1s;'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    elif reaction_type == "Exothermic (Warning: Explosive!)":
        st.markdown("""
            <div class='beaker'>
                <div class='liquid liquid-water'></div>
                <div class='explosion'></div>
                <div class='fire'></div>
            </div>
        """, unsafe_allow_html=True)

    elif reaction_type == "Indicator":
        st.markdown("""
            <div style='display: flex; justify-content: center;'>
                <div class='beaker'>
                    <div class='liquid' style='background: rgba(255,255,255,0.95);'></div>
                    <div class='ph-strip acid'></div>
                </div>
                <div class='beaker'>
                    <div class='liquid' style='background: rgba(255,255,255,0.95);'></div>
                    <div class='ph-strip neutral'></div>
                </div>
                <div class='beaker'>
                    <div class='liquid' style='background: rgba(255,255,255,0.95);'></div>
                    <div class='ph-strip base'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    lab()
