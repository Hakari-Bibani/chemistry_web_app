import streamlit as st
from streamlit.components.v1 import html

def home():
    # Custom HTML & CSS for Advanced Home Page
    st.markdown("""
        <style>
            /* Background with animated particles */
            body {
                background: linear-gradient(135deg, #1b1b2f, #162447);
                overflow: hidden;
                font-family: 'Arial', sans-serif;
                color: white;
            }

            /* Particle effect */
            .particles-js-canvas-el {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                pointer-events: none;
                opacity: 0.6;
            }

            /* Hero Section */
            .hero-section {
                text-align: center;
                padding: 80px 20px;
                position: relative;
                z-index: 10;
            }

            .hero-title {
                font-size: 2.5em;
                color: #e43f5a;
                animation: text-glow 2s ease-in-out infinite alternate;
            }

            /* Glow Animation for Title */
            @keyframes text-glow {
                0% { text-shadow: 0 0 10px #e43f5a, 0 0 20px #e43f5a, 0 0 30px #e43f5a; }
                100% { text-shadow: 0 0 20px #e43f5a, 0 0 30px #ff5e5b, 0 0 40px #ff5e5b; }
            }

            /* Feature Section */
            .feature-card {
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid #ffffff30;
                border-radius: 10px;
                padding: 20px;
                margin: 10px;
                width: 200px;
                height: 250px;
                display: inline-block;
                position: relative;
                perspective: 1000px;
                cursor: pointer;
                transition: transform 0.5s ease;
            }

            .feature-card:hover {
                transform: rotateY(15deg) rotateX(10deg);
                background: rgba(255, 255, 255, 0.2);
            }

            /* Interactive 3D Flip */
            .flip-card {
                width: 100%;
                height: 100%;
                transition: transform 0.6s;
                transform-style: preserve-3d;
                position: relative;
            }

            .feature-card:hover .flip-card {
                transform: rotateY(180deg);
            }

            .flip-front, .flip-back {
                position: absolute;
                width: 100%;
                height: 100%;
                backface-visibility: hidden;
                border-radius: 10px;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 10px;
            }

            .flip-front {
                background: #1f4068;
                color: white;
            }

            .flip-back {
                background: #162447;
                color: #e43f5a;
                transform: rotateY(180deg);
            }

            /* Particle Glow */
            .glowing-particle {
                position: absolute;
                background: rgba(255, 255, 255, 0.5);
                border-radius: 50%;
                width: 5px;
                height: 5px;
                opacity: 0.6;
                animation: particle-move 5s infinite ease-in-out alternate;
            }

            /* Particle Movement */
            @keyframes particle-move {
                0% { transform: translate(0, 0); }
                100% { transform: translate(50px, -100px); }
            }
        </style>

        <!-- Hero Section -->
        <div class="hero-section">
            <h1 class="hero-title">Welcome to Your Virtual Chemistry Lab</h1>
            <p>Discover the fascinating world of chemistry through simulations, calculations, and interactive learning!</p>
        </div>

        <!-- Feature Section with Flip Cards -->
        <div style="display: flex; justify-content: center; flex-wrap: wrap; margin-top: 30px;">
            <div class="feature-card">
                <div class="flip-card">
                    <div class="flip-front">Perform chemical calculations</div>
                    <div class="flip-back">Learn to calculate pH, molarity, and more with step-by-step guidance.</div>
                </div>
            </div>
            <div class="feature-card">
                <div class="flip-card">
                    <div class="flip-front">Watch simulated reactions</div>
                    <div class="flip-back">Experience acid-base reactions, exothermic reactions, and more virtually!</div>
                </div>
            </div>
            <div class="feature-card">
                <div class="flip-card">
                    <div class="flip-front">Learn chemistry concepts</div>
                    <div class="flip-back">Understand the fundamentals of pH, pOH, molarity, and other key topics.</div>
                </div>
            </div>
        </div>

        <!-- Particle Background -->
        <div class="particles-js-canvas-el">
            <!-- Optional JS for particle effect if desired -->
        </div>
    """, unsafe_allow_html=True)

    # Custom JavaScript for Particle Animation
    st.markdown("""
        <script>
            // Basic Particle Animation
            const particleContainer = document.querySelector(".particles-js-canvas-el");

            // Function to create a glowing particle
            function createParticle() {
                const particle = document.createElement("div");
                particle.classList.add("glowing-particle");
                particle.style.left = `${Math.random() * window.innerWidth}px`;
                particle.style.top = `${Math.random() * window.innerHeight}px`;
                particleContainer.appendChild(particle);

                // Remove particle after animation
                setTimeout(() => particle.remove(), 5000);
            }

            // Create particles at intervals
            setInterval(createParticle, 200);
        </script>
    """, unsafe_allow_html=True)
