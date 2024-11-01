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
            background: rgba(255, 100, 100, 0.6);
            animation: wave 1.5s infinite ease-in-out;
        }

        @keyframes wave {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-3px); }
        }

        .powder-container {
            position: absolute;
            top: -80px;
            left: 50%;
            transform: translateX(-50%) rotate(-5deg);
            width: 40px;
            height: 60px;
            background: #fff;
            border: 2px solid #999;
        }

        .powder-stream {
            position: absolute;
            top: 35px;
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
            20% { height: 80px; opacity: 1; }
            80% { height: 80px; opacity: 1; }
            100% { height: 0; opacity: 0; }
        }

        .bubbles {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 100%;
            opacity: 0;
            animation: show-bubbles 3s forwards;
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
            opacity: 0;
        }

        @keyframes rise {
            0% { 
                transform: translateY(0);
                opacity: 1;
                width: 10px;
                height: 10px;
            }
            100% { 
                transform: translateY(-120px);
                opacity: 0;
                width: 20px;
                height: 20px;
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
            # Display beaker and reaction elements
            st.markdown("""
                <div class='beaker'>
                    <div class='liquid'></div>
                    <div class='powder-container'></div>
                    <div class='bubbles'>
                        <div class='bubble' style='left: 20%; animation-delay: 0s;'></div>
                        <div class='bubble' style='left: 40%; animation-delay: 0.2s;'></div>
                        <div class='bubble' style='left: 60%; animation-delay: 0.4s;'></div>
                        <div class='bubble' style='left: 80%; animation-delay: 0.6s;'></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            # Display animation details
            st.write("Step 1: Baking soda is poured into vinegar.")
            st.write("Step 2: Vigorous bubbling reaction is observed.")
            st.write("Chemical Reaction: NaHCO₃ + CH₃COOH → CO₂ + H₂O + NaCH₃COO")

            # Trigger the pouring animation
            st.markdown("<script>document.querySelector('.powder-stream').style.height='80px';</script>", unsafe_allow_html=True)

            # Delay to show the animation before displaying the results
            time.sleep(3)

            # Activate bubble animations
            st.markdown("<script>document.querySelector('.bubbles').style.opacity='1';</script>", unsafe_allow_html=True)
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


