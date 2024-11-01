import streamlit as st
import time

def lab():
    st.markdown(
        """
        <style>
        /* Styles for the beaker, liquid, and bubbles */
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
            box-shadow: inset 0 0 20px rgba(255,255,255,0.2);
        }

        .beaker::before {
            content: '';
            position: absolute;
            top: -12px;
            left: -15px;
            right: -15px;
            height: 25px;
            background: #ddd;
            border-radius: 5px;
        }

        .liquid {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 50%;
            background: rgba(255, 99, 99, 0.7);
            transition: height 0.5s ease;
            animation: wave 2s infinite alternate;
        }

        @keyframes wave {
            0% { transform: translateY(0); }
            100% { transform: translateY(-5px); }
        }

        .spoon {
            position: absolute;
            top: -60px;
            left: 50%;
            width: 50px;
            height: 20px;
            background: #ddd;
            border-radius: 10px;
            transform: translateX(-50%) rotate(-20deg);
            animation: tilt-pour 3s forwards;
            transform-origin: bottom center;
            display: none;
        }

        .spoon-powder {
            position: absolute;
            top: -20px;
            left: 50%;
            width: 20px;
            height: 8px;
            background: #fff;
            border-radius: 50%;
            transform: translateX(-50%);
            display: none;
        }

        @keyframes tilt-pour {
            0% { transform: translateX(-50%) rotate(-20deg); }
            20% { transform: translateX(-50%) rotate(30deg); display: block; }
            100% { transform: translateX(-50%) rotate(30deg); }
        }

        .powder-stream {
            position: absolute;
            top: 20px;
            left: 50%;
            width: 6px;
            height: 0;
            background: rgba(255, 255, 255, 0.9);
            display: none;
            animation: pour-powder 3s forwards;
            transform-origin: top center;
            filter: blur(1px);
        }

        @keyframes pour-powder {
            0% { height: 0; opacity: 0; display: block; }
            20% { height: 80px; opacity: 1; }
            100% { height: 0; opacity: 0; }
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

        @keyframes show-bubbles {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }

        .bubble {
            position: absolute;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: rise 1.5s infinite;
        }

        @keyframes rise {
            0% { 
                transform: translateY(0) translateX(var(--x-start));
                opacity: 0.8;
                width: var(--size);
                height: var(--size);
            }
            100% { 
                transform: translateY(-120px) translateX(var(--x-end));
                opacity: 0;
                width: calc(var(--size) * 2);
                height: calc(var(--size) * 2);
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 style="text-align: center; margin-bottom: 2em;">Virtual Chemistry Lab 🧪</h1>', unsafe_allow_html=True)

    st.subheader("Choose your reaction type:")
    reaction_type = st.selectbox("", ["", "Acid-Base (baking soda & vinegar)", "Exothermic (Warning: Explosive!)", "Indicator"])

    # Baking Soda and Vinegar Reaction
    if reaction_type == "Acid-Base (baking soda & vinegar)":
        if st.button("Add Baking Soda"):
            st.markdown("""
                <div class='beaker'>
                    <div class='liquid'></div>
                    <div class='spoon'></div>
                    <div class='spoon-powder'></div>
                    <div class='powder-stream'></div>
                    <div class='bubbles'>
                        <div class='bubble' style='--x-start: 10px; --x-end: 20px; --size: 10px; animation-delay: 0s;'></div>
                        <div class='bubble' style='--x-start: -15px; --x-end: -25px; --size: 15px; animation-delay: 0.5s;'></div>
                        <div class='bubble' style='--x-start: 5px; --x-end: -10px; --size: 12px; animation-delay: 1s;'></div>
                        <div class='bubble' style='--x-start: -8px; --x-end: 15px; --size: 8px; animation-delay: 1.5s;'></div>
                        <div class='bubble' style='--x-start: 12px; --x-end: -20px; --size: 14px; animation-delay: 2s;'></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            st.write("Step 1: Adding baking soda to the vinegar solution...")
            st.write("Step 2: Observing the vigorous bubble formation and reaction progress...")
            time.sleep(2)  # Pause for effect
            st.write("Reaction: NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")

elif reaction_type == "Exothermic (Warning: Explosive!)":
                st.markdown("""
            <div class='beaker'>
                <div class='liquid' style='background: rgba(255,255,255,0.9);'></div>
                <div class='powder-container'></div>
                <div class='powder-stream'></div>
                <div class='explosion'></div>
                <div class='fire'></div>
                <div class='sparks'>
                    <div class='spark' style='--x-end: 120px; --y-end: -100px; animation-delay: 3.2s;'></div>
                    <div class='spark' style='--x-end: -100px; --y-end: -80px; animation-delay: 3.4s;'></div>
                    <div class='spark' style='--x-end: 80px; --y-end: -120px; animation-delay: 3.6s;'></div>
                    <div class='spark' style='--x-end: -120px; --y-end: -90px; animation-delay: 3.8s;'></div>
                    <div class='spark' style='--x-end: 100px; --y-end: -110px; animation-delay: 4.0s;'></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("Step 1: Carefully adding sodium to water...")
        st.write("Step 2: Observing the violent reaction...")
        st.write("2Na(s) + 2H₂O(l) → 2NaOH(aq) + H₂(g) + Energy")
        
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
        
        st.write("Step 1: Dipping black pH strips into solutions...")
        st.write("Step 2: Observing color changes:")
        st.write("- Acidic solution: Strip turns red")
        st.write("- Neutral solution: Strip turns green")
        st.write("- Basic solution: Strip turns blue")

if __name__ == "__main__":
    lab()


