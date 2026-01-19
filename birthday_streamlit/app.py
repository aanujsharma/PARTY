import streamlit as st
from datetime import date
import time

# Page config
st.set_page_config(
    page_title="Happy Birthday Kanchan 🎉",
    page_icon="🎂",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background: linear-gradient(120deg, #ff758c, #ff7eb3);
}
h1, h2, h3, p {
    color: white;
    text-align: center;
}
.blink {
    animation: blink 1.5s infinite;
}
@keyframes blink {
    0% {opacity: 1;}
    50% {opacity: 0.4;}
    100% {opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='blink'>🎂 Happy 20th Birthday Kanchan 🎂</h1>", unsafe_allow_html=True)
st.markdown("<h3>3rd February – A very special day 💖</h3>", unsafe_allow_html=True)

st.write("")

# Cake animation (simple)
with st.spinner("Cutting the cake 🎂..."):
    time.sleep(2)

st.success("🎉 Cake Cut Successfully 🎉")

# Age
st.markdown("<h2>🎉 20 Years of Awesomeness 🎉</h2>", unsafe_allow_html=True)

# Images
st.markdown("<h3>📸 Beautiful Memories</h3>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/photo1.jpg", use_container_width=True)
with col2:
    st.image("images/photo2.jpg", use_container_width=True)
with col3:
    st.image("images/photo3.jpg", use_container_width=True)

# Button for wish
if st.button("🎁 Click for Birthday Wish"):
    st.balloons()
    st.markdown("""
    <h2>💖 Dear Kanchan 💖</h2>
    <p>
    May your life be filled with love, happiness, success and endless smiles.<br>
    Keep shining and stay amazing always ✨🎉
    </p>
    <h3>— From Someone Special 💌</h3>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<br><p style='text-align:center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
