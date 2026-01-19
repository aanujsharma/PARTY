import streamlit as st
from datetime import date
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Happy Birthday Kanchan 🎉",
    page_icon="🎂",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fbc2eb);
}
h1, h2, h3, p {
    text-align: center;
    color: white;
}
.card {
    background: rgba(255,255,255,0.18);
    padding: 25px;
    border-radius: 22px;
    margin: 20px 0;
    box-shadow: 0 10px 25px rgba(0,0,0,0.25);
}
.glow {
    animation: glow 2s infinite alternate;
}
@keyframes glow {
    from { text-shadow: 0 0 10px #fff; }
    to { text-shadow: 0 0 30px #ff4081; }
}
.signature {
    animation: fade 2s infinite alternate;
}
@keyframes fade {
    from { opacity: 0.5; }
    to { opacity: 1; }
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR (≡ NAVIGATION) ----------------
st.sidebar.title("🎀 Birthday Menu")
page = st.sidebar.radio(
    "Navigate",
    ["🎂 Home", "📸 Memories", "⏳ Countdown", "🎁 Surprise"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("💖 **For Kanchan**")
st.sidebar.markdown("🎉 20th Birthday")
st.sidebar.markdown("📅 3 February")

# ---------------- HOME ----------------
if page == "🎂 Home":
    st.markdown("<h1 class='glow'>🎂 Happy 20th Birthday Kanchan 🎂</h1>", unsafe_allow_html=True)
    st.markdown("<h3>3rd February – A very special day 💕</h3>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>✨ 20 Years of Awesomeness ✨</h2>
        <p>
        May your life be filled with happiness, love, success and smiles.<br>
        Keep shining always 🌟
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Music (optional)
    try:
        st.audio("birthday.mp3", loop=True)
    except:
        st.info("🎵 Add birthday.mp3 to enable music")

    with st.spinner("🎂 Preparing the cake..."):
        time.sleep(2)
    st.success("🎉 Cake is ready!")

# ---------------- MEMORIES ----------------
elif page == "📸 Memories":
    st.markdown("<h1 class='glow'>📸 Beautiful Memories</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <p>Some moments that will always stay close to the heart 💖</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("images/photo1.jpg", use_container_width=True)
    with col2:
        st.image("images/photo2.jpg", use_container_width=True)
    with col3:
        st.image("images/photo3.jpg", use_container_width=True)

# ---------------- COUNTDOWN ----------------
elif page == "⏳ Countdown":
    st.markdown("<h1 class='glow'>⏳ Birthday Countdown</h1>", unsafe_allow_html=True)

    today = date.today()
    birthday = date(today.year, 2, 3)

    if today > birthday:
        birthday = date(today.year + 1, 2, 3)

    days_left = (birthday - today).days

    st.markdown(f"""
    <div class="card">
        <h2>🎉 {days_left} Days To Go 🎉</h2>
        <p>The big day is almost here 💖</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- SURPRISE ----------------
elif page == "🎁 Surprise":
    st.markdown("<h1 class='glow'>🎁 Special Surprise</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h3>Click the button below 🎈</h3>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🎉 Open Surprise"):
        st.balloons()
        st.markdown("""
        <div class="card">
            <h2>💖 Dear Kanchan 💖</h2>
            <p>
            On your 20th birthday, I wish you endless happiness,
            success and beautiful moments.<br>
            You deserve the best always ✨
            </p>
            <h3 class="signature">— From Anuj 💌</h3>
        </div>
        """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("<br><p style='text-align:center;'>🎂 Made with ❤️ using Streamlit 🎂</p>", unsafe_allow_html=True)
