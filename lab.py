import streamlit as st
import time

def lab():
    st.markdown(
        """
        <style>
        /* Base Styles */
        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 20px;
        }

        /* Beaker Styles */
        .beaker {
            width: 150px;
            height: 200px;
            position: relative;
            border: 4px solid #999;
            border-radius: 0 0 20px 20px;
            margin: 20px;
            overflow: hidden;
        }

        .beaker::before {
            content: '';
            position: absolute;
            top: -10px;
            left: -10px;
            right: -10px;
            height: 20px;
            background: #999;
            border-radius: 5px;
        }

        /* Liquid Animation */
        .liquid {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 50%;
            background: repeating-linear-gradient(
                45deg,
                rgba(255,255,255,0.8),
                rgba(255,255,255,0.8) 10px,
                rgba(240,240,240,0.8) 10px,
                rgba(240,240,240,0.8) 20px
            );
            animation: wave 2s infinite linear;
            transform-origin: center bottom;
        }

        @keyframes wave {
            0%, 100% { transform: rotate(-1deg); }
            50% { transform: rotate(1deg); }
        }

        /* Powder Pour Effect */
        .powder-stream {
            position: absolute;
            top: -60px;
            left: 50%;
            width: 10px;
            transform: translateX(-50%);
            height: 60px;
            background: linear-gradient(to bottom, transparent, white);
            opacity: 0;
            animation: pour 3s forwards;
        }

        @keyframes pour {
            0% { opacity: 0; transform: translateX(-50%) rotate(0deg); }
            10% { opacity: 1; transform: translateX(-50%) rotate(5deg); }
            90% { opacity: 1; transform: translateX(-50%) rotate(-5deg); }
            100% { opacity: 0; transform: translateX(-50%) rotate(0deg); }
        }

        /* Enhanced Bubble Animation */
        .bubble {
            position: absolute;
            border-radius: 50%;
            background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.8), rgba(255,255,255,0.4));
            animation: bubbleRise cubic-bezier(0.47, 0, 0.745, 0.715) both;
        }

        @keyframes bubbleRise {
            0% {
                opacity: 0;
                transform: translateY(0) translateX(var(--x-start));
            }
            20% {
                opacity: 1;
            }
            100% {
                opacity: 0;
                transform: translateY(-200px) translateX(var(--x-end));
            }
        }

        /* Sodium Reaction */
        .sodium {
            position: absolute;
            width: 15px;
            height: 15px;
            background: #e0e0e0;
            border-radius: 50%;
            top: -30px;
            left: 50%;
            transform: translateX(-50%);
            animation: sodiumDrop 1s forwards;
        }

        @keyframes sodiumDrop {
            0% { transform: translateX(-50%) translateY(0); }
            100% { transform: translateX(-50%) translateY(130px); }
        }

        /* Enhanced Explosion Effect */
        .explosion {
            position: absolute;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle, #ff6b6b, transparent);
            opacity: 0;
            transform: scale(0.1);
            animation: explode 1s forwards;
        }

        @keyframes explode {
            0% { opacity: 0; transform: scale(0.1); }
            50% { opacity: 1; transform: scale(2); }
            100% { opacity: 0; transform: scale(3); }
        }

        /* Spark Effects */
        .spark {
            position: absolute;
            width: 4px;
            height: 4px;
            background: #ff4400;
            border-radius: 50%;
            filter: blur(1px);
            animation: spark 0.8s ease-out forwards;
        }

        @keyframes spark {
            0% { transform: translate(0, 0) scale(1); opacity: 1; }
            100% { transform: translate(var(--x-end), var(--y-end)) scale(0); opacity: 0; }
        }

        /* pH Strip Animation */
        .ph-strip {
            position: absolute;
            width: 8px;
            height: 100px;
            background: #333;
            left: 50%;
            transform-origin: top center;
            animation: dipStrip 4s ease-in-out forwards;
        }

        @keyframes dipStrip {
            0% { transform: translateX(-50%) translateY(-120%) rotate(0deg); }
            25% { transform: translateX(-50%) translateY(30%) rotate(0deg); }
            75% { transform: translateX(-50%) translateY(30%) rotate(0deg); }
            100% { transform: translateX(-50%) translateY(-120%) rotate(0deg); }
        }

        .ph-strip.acid { animation: dipStripAcid 4s ease-in-out forwards; }
        .ph-strip.neutral { animation: dipStripNeutral 4s ease-in-out forwards; }
        .ph-strip.base { animation: dipStripBase 4s ease-in-out forwards; }

        @keyframes dipStripAcid {
            0% { background: #333; }
            75% { background: #333; }
            100% { background: #ff6b6b; }
        }

        @keyframes dipStripNeutral {
            0% { background: #333; }
            75% { background: #333; }
            100% { background: #51cf66; }
        }

        @keyframes dipStripBase {
            0% { background: #333; }
            75% { background: #333; }
            100% { background: #339af0; }
        }

        /* Dynamic Liquid Motion */
        .reaction-liquid {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 50%;
            animation: reactionMotion 2s infinite ease-in-out;
        }

        @keyframes reactionMotion {
            0%, 100% {
                transform: translate(-2px, 2px) rotate(-1deg);
                height: 50%;
            }
            50% {
                transform: translate(2px, -2px) rotate(1deg);
                height: 52%;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 style="text-align: center;">Interactive Chemistry Lab 🧪</h1>', unsafe_allow_html=True)

    reaction_type = st.selectbox("Select Reaction:", [
        "", 
        "Acid-Base (Baking Soda + Vinegar)", 
        "Sodium + Water (Explosive!)", 
        "pH Paper Test"
    ])

    if reaction_type == "Acid-Base (Baking Soda + Vinegar)":
        st.markdown("""
            <div class="container">
                <div class="beaker">
                    <div class="reaction-liquid" style="background: rgba(255,255,255,0.8);">
                        <div class="wave"></div>
                    </div>
                    <div class="powder-stream"></div>
                    <div class="bubbles" id="bubble-container"></div>
                </div>
            </div>
            <script>
                function createBubbles() {
                    const container = document.getElementById('bubble-container');
                    for(let i = 0; i < 20; i++) {
                        const bubble = document.createElement('div');
                        bubble.className = 'bubble';
                        bubble.style.left = Math.random() * 100 + '%';
                        bubble.style.width = Math.random() * 10 + 5 + 'px';
                        bubble.style.height = bubble.style.width;
                        bubble.style.animationDelay = Math.random() * 2 + 's';
                        bubble.style.animationDuration = Math.random() * 2 + 2 + 's';
                        container.appendChild(bubble);
                    }
                }
                createBubbles();
            </script>
        """, unsafe_allow_html=True)
        
    elif reaction_type == "Sodium + Water (Explosive!)":
        st.markdown("""
            <div class="container">
                <div class="beaker">
                    <div class="reaction-liquid" style="background: rgba(255,255,255,0.9);">
                        <div class="wave"></div>
                    </div>
                    <div class="sodium"></div>
                    <div class="explosion"></div>
                    <div class="sparks">
                        <div class="spark" style="--x-end: 100px; --y-end: -80px;"></div>
                        <div class="spark" style="--x-end: -80px; --y-end: -100px;"></div>
                        <div class="spark" style="--x-end: 60px; --y-end: -120px;"></div>
                        <div class="spark" style="--x-end: -120px; --y-end: -90px;"></div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    elif reaction_type == "pH Paper Test":
        st.markdown("""
            <div class="container">
                <div class="beaker">
                    <div class="reaction-liquid" style="background: rgba(255,200,200,0.3);">
                        <div class="wave"></div>
                    </div>
                    <div class="ph-strip acid"></div>
                </div>
                <div class="beaker">
                    <div class="reaction-liquid" style="background: rgba(200,255,200,0.3);">
                        <div class="wave"></div>
                    </div>
                    <div class="ph-strip neutral"></div>
                </div>
                <div class="beaker">
                    <div class="reaction-liquid" style="background: rgba(200,200,255,0.3);">
                        <div class="wave"></div>
                    </div>
                    <div class="ph-strip base"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    lab()
