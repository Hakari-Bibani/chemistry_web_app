import streamlit as st
from time import sleep

def lab():
  """
  Displays a Streamlit app simulating a baking soda and vinegar reaction.
  """

  # CSS styles for animations and visuals
  st.markdown("""
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
      background: rgba(255, 255, 255, 0.9);
      transition: all 0.5s;
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
      animation: tilt-pour 3s forwards;
      transform-origin: bottom right;
    }

    @keyframes tilt-pour {
      0% { transform: translateX(-50%) rotate(-5deg); }
      20% { transform: translateX(-50%) rotate(45deg); }
      80% { transform: translateX(-50%) rotate(45deg); }
      100% { transform: translateX(-50%) rotate(-5deg); }
    }

    .powder-stream {
      position: absolute;
      top: 40px;
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
        width: calc(var(--size) * 2
