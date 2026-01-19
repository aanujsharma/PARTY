import streamlit as st
import time
import random

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
    background: linear-gradient(135deg, #ffe0f0, #fcb9e0, #f7d1ff, #d9c1ff);
    background-size: 400% 400%;
    animation: bgMove 12s ease infinite;
}
@keyframes bgMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
h1, h2, h3, p {text-align:center; color:#ffffff;}
.card {background: rgba(255,255,255,0.25); padding:25px; border-radius:25px; margin:20px 0; box-shadow: 0 12px 25px rgba(0,0,0,0.25);}
.glow {animation: glow 2s infinite alternate;}
@keyframes glow {from {text-shadow:0 0 8px #fff;} to {text-shadow:0 0 25px #ff9aa2;}}
.float {animation: float 3s ease-in-out infinite;}
@keyframes float {0% {transform:translateY(0);} 50% {transform:translateY(-10px);} 100% {transform:translateY(0);}}
.signature {animation: fade 2s infinite alternate;}
@keyframes fade {from {opacity:0.6;} to {opacity:1;}}
section[data-testid="stSidebar"] {background: linear-gradient(180deg, #ffb6c1, #ffd1dc);}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🎀 Birthday Menu 🎀")
page = st.sidebar.radio(
    "Navigate 🎉",
    ["🎂 Birthday", "💌 Special Message", "🎮 Fun Game"]
)
st.sidebar.markdown("---")
st.sidebar.markdown("🎉 **Kanchan Turns 20**")
st.sidebar.markdown("🎂 3 February")
st.sidebar.markdown("✨ Fun & Cute Surprises Inside ✨")

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
        st.info("🎵 Add birthday.mp3 (Happy Birthday melody) to play music")

# ---------------- SPECIAL COMBINED MESSAGE ----------------
elif page == "💌 Special Message":
    st.markdown("<h1 class='glow'>💌 A Cute Birthday Message 🌸✨</h1>", unsafe_allow_html=True)

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

# ---------------- FUN GAME ----------------
elif page == "🎮 Fun Game":
    st.markdown("<h1 class='glow'>🎮 Birthday Fun Game 🎀</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Guess the Lucky Number (1 to 5) 🎉</h3>", unsafe_allow_html=True)

    lucky_number = random.randint(1,5)
    guess = st.number_input("Enter your guess:", min_value=1, max_value=5, step=1)

    if st.button("🎯 Guess!"):
        if guess == lucky_number:
            st.balloons()
            st.success("🎉 You Won! 🎉")
            st.markdown("""
            <div class="card">
                <h2>✨ Special Surprise Message ✨</h2>
                <p>
                Yay! You are amazing 😄🎀<br>
                Kanchan, may your birthday be as fun, bright, and magical as this game 🌸✨<br>
                Keep laughing, smiling and enjoying every moment 🌈
                </p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error(f"Oops! The lucky number was {lucky_number} 😅 Try again!")

# ---------------- FOOTER ----------------
st.markdown("<br><p style='text-align:center;'>🎂 Birthday vibes • Colours • Smiles • Love 🌟✨</p>", unsafe_allow_html=True)

