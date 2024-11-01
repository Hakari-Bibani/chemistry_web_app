import streamlit as st
import time

def lab():
    st.markdown(
        """
        <style>
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
            background: rgba(255, 0, 0, 0.2); /* Light red color for vinegar */
            animation: liquid-move 3s infinite alternate ease-in-out;
        }

        @keyframes liquid-move {
            0% { transform: translateY(0); }
            100% { transform: translateY(-2%); }
        }

        .spoon {
            position: absolute;
            top: -50px;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 20px;
            background: #f5f5f5;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            animation: tilt-pour 2s forwards;
            transform-origin: right;
        }

        .spoon-powder {
            position: absolute;
            top: 2px;
            left: 5px;
            width: 50px;
            height: 12px;
            background: #fff;
            border-radius: 5px;
        }

        .powder-stream {
            position: absolute;
            top: 0;
            left: 50%;
            width: 6px;
            height: 0;
            background: rgba(255, 255, 255, 0.9);
            animation: pour-powder 3s forwards;
            filter: blur(1px);
            transform-origin: top center;
        }

        @keyframes pour-powder {
            0% { height: 0; opacity: 0; }
            20% { height: 60px; opacity: 1; }
            80% { height: 60px; opacity: 1; }
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
            background: rgba(200, 200, 200, 0.8);
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

    if reaction_type == "Acid-Base (baking soda & vinegar)":
        if st.button("Start Reaction"):
            st.markdown("""
                <div class='beaker'>
                    <div class='liquid'></div>
                    <div class='spoon'>
                        <div class='spoon-powder'></div>
                    </div>
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
            
            st.write("Step 1: Gradually adding baking soda to vinegar solution...")
            st.write("Step 2: Observing the vigorous fizzing reaction as bubbles form and rise to the surface...")
            st.write("NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")

    elif reaction_type == "Exothermic (Warning: Explosive!)":
        # Existing code for the Exothermic reaction
        pass

    elif reaction_type == "Indicator":
        # Existing code for the Indicator reaction
        pass

if __name__ == "__main__":
    lab()
