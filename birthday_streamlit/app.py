import streamlit as st
from datetime import date
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Happy Birthday Kanchan 🎉",
    page_icon="🎂",
    layout="centered"
)

# ---------------- BACKGROUND + ANIMATION ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #ffe0f0,
        #fcb9e0,
        #f7d1ff,
        #d9c1ff
    );
    background-size: 400% 400%;
    animation: bgMove 12s ease infinite;
}
@keyframes bgMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

h1, h2, h3, p {
    text-align: center;
    color: #ffffff;
}

.card {
    background: rgba(255,255,255,0.25);
    padding: 25px;
    border-radius: 25px;
    margin: 20px 0;
    box-shadow: 0 12px 25px rgba(0,0,0,0.25);
}

.glow {animation: glow 2s infinite alternate;}
@keyframes glow {from {text-shadow:0 0 8px #fff;} to {text-shadow:0 0 25px #ff9aa2;}}

.float {animation: float 3s ease-in-out infinite;}
@keyframes float {0% {transform:translateY(0);} 50% {transform:translateY(-10px);} 100% {transform:translateY(0);}}

.signature {animation: fade 2s infinite alternate;}
@keyframes fade {from {opacity:0.6;} to {opacity:1;}}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffb6c1, #ffd1dc);
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR NAVIGATION ----------------
st.sidebar.title("🎀 Birthday Menu 🎀")
page = st.sidebar.radio(
    "Navigate 🎉",
    ["🎂 Birthday", "⏳ Countdown", "💌 Special Message"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("🎉 **Kanchan Turns 20**")
st.sidebar.markdown("🎂 3 February")
st.sidebar.markdown("✨ A day to celebrate smiles & love ✨")

# ---------------- BIRTHDAY PAGE ----------------
if page == "🎂 Birthday":
    st.markdown("<h1 class='glow float'>🎂 Happy 20th Birthday Kanchan 🎂</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Today is all about smiles, surprises & love 🎉✨</h3>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>🌟 A Special Day for You 🌟</h2>
        <p>
        May this birthday be filled with laughter, sweet moments and unforgettable memories 🌸✨<br>
        You light up every room with your smile 🎀<br>
        Keep shining, dreaming & enjoying life 🌈
        </p>
    </div>
    """, unsafe_allow_html=True)

    try:
        st.audio("birthday.mp3", loop=True)
    except:
        st.info("🎵 Add birthday.mp3 for soft music")

    with st.spinner("🎂 Preparing cake & wishes..."):
        time.sleep(2)
    st.success("🎉 Let the fun & love begin!")

# ---------------- COUNTDOWN ----------------
elif page == "⏳ Countdown":
    st.markdown("<h1 class='glow'>⏳ Birthday Countdown 🎈</h1>", unsafe_allow_html=True)

    today = date.today()
    birthday = date(today.year, 2, 3)
    if today > birthday:
        birthday = date(today.year + 1, 2, 3)

    days_left = (birthday - today).days

    st.markdown(f"""
    <div class="card">
        <h2>🎉 {days_left} Days To Go 🎉</h2>
        <p>The countdown to smiles, cake & fun has started 🌟✨</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- SPECIAL COMBINED MESSAGE ----------------
elif page == "💌 Special Message":
    st.markdown("<h1 class='glow'>💌 A Special Birthday Message 🌸✨</h1>", unsafe_allow_html=True)

    if st.button("🎉 Show Message"):
        st.balloons()
        st.markdown("""
        <div class="card">
            <h2>🌟 To My Favorite Person 🌟</h2>
            <p>
            Kanchan, you are not just my best friend, you are like family 🦋✨<br>
            Every moment with you is magical, full of laughter, warmth and joy 🎀🌸<br>
            I hope your 20th year brings endless smiles, dreams coming true, and happiness in every corner 🌈🌟<br>
            Keep being amazing, shining and lovely 💫
            </p>
            <h3 class="signature">— Always Yours, Anuj 🎉✨</h3>
        </div>
        """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("<br><p style='text-align:center;'>🎂 Birthday vibes • Colours • Smiles • Love 🌟✨</p>", unsafe_allow_html=True)

