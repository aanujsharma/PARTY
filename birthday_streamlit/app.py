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
    ["🎂 Birthday", "⏳ Countdown", "💌 Message"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("🎉 **Kanchan Turns 20**")
st.sidebar.markdown("🎂 3 February")
st.sidebar.markdown("✨ Celebrate with smiles & love ✨")

# ---------------- BIRTHDAY PAGE ----------------
if page == "🎂 Birthday":
    st.markdown("<h1 class='glow float'>🎂 Happy 20th Birthday Kanchan 🎂</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Today is a day full of smiles, surprises & sweet vibes 🎉✨</h3>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>🌟 A Very Special Day 🌟</h2>
        <p>
        May this birthday bring you countless happy moments 🌸<br>
        Your laughter is like music to everyone around 🎀<br>
        Keep sparkling, dreaming & loving life ✨
        </p>
    </div>
    """, unsafe_allow_html=True)

    try:
        st.audio("birthday.mp3", loop=True)
    except:
        st.info("🎵 Add birthday.mp3 for soft romantic music")

    with st.spinner("🎂 Preparing your cake & wishes..."):
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
        <p>
        The countdown to cake, smiles & sweet memories has started 🌟
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- MESSAGE ----------------
elif page == "💌 Message":
    st.markdown("<h1 class='glow'>💌 Romantic Birthday Message 🌸</h1>", unsafe_allow_html=True)

    choice = st.radio(
        "Choose message type ✨",
        ["👭 Best Friend", "🦋 Like Sister", "🌟 Romantic Note"]
    )

    if st.button("🎉 Show Message"):
        st.balloons()

        if choice == "👭 Best Friend":
            st.markdown("""
            <div class="card">
                <h2>🌸 My Best Friend 🌸</h2>
                <p>
                You make every moment brighter ✨<br>
                Thank you for the laughter, the talks, and the crazy memories 🎀<br>
                Life is happier with you around 🌈
                </p>
                <h3 class="signature">— Your Best Friend Anuj 🎉</h3>
            </div>
            """, unsafe_allow_html=True)

        elif choice == "🦋 Like Sister":
            st.markdown("""
            <div class="card">
                <h2>🦋 Like My Sister 🦋</h2>
                <p>
                You are my family away from home 🌸<br>
                A bond full of trust, care and endless smiles ✨<br>
                Grateful for you always 🎀
                </p>
                <h3 class="signature">— From Anuj 🌟</h3>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown("""
            <div class="card">
                <h2>🌟 Romantic Note 🌟</h2>
                <p>
                Kanchan, your smile lights up my days 🌸<br>
                Every moment with you feels magical 🎀<br>
                I hope this year brings dreams, laughter, and endless happiness ✨<br>
                You are a star in my sky 🌟
                </p>
                <h3 class="signature">— From Anuj 🎉</h3>
            </div>
            """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("<br><p style='text-align:center;'>🎂 Birthday vibes • Colours • Smiles • Love ✨</p>", unsafe_allow_html=True)

