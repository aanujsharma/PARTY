import streamlit as st
from datetime import date
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Happy Birthday Kanchan 🎉",
    page_icon="🎂",
    layout="centered"
)

# ---------------- BACKGROUND + CUTE ANIMATION CSS ----------------
st.markdown("""
<style>
.main {
    background: url("https://i.imgur.com/8YqGkYF.gif");
    background-size: cover;
    background-position: center;
}
h1, h2, h3, p {
    text-align: center;
    color: white;
}

.card {
    background: rgba(255,255,255,0.22);
    padding: 25px;
    border-radius: 22px;
    margin: 20px 0;
    box-shadow: 0 12px 30px rgba(0,0,0,0.3);
}

.glow {
    animation: glow 2s infinite alternate;
}
@keyframes glow {
    from { text-shadow: 0 0 10px #fff; }
    to { text-shadow: 0 0 30px #ffd1dc; }
}

.float {
    animation: float 3s ease-in-out infinite;
}
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

.signature {
    animation: fade 2s infinite alternate;
}
@keyframes fade {
    from { opacity: 0.6; }
    to { opacity: 1; }
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR NAVIGATION ----------------
st.sidebar.title("🎀 Birthday Menu")
page = st.sidebar.radio(
    "Navigate",
    ["🎂 Home", "📸 Memories", "⏳ Countdown", "💌 Message"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("🌸 **For Kanchan**")
st.sidebar.markdown("🎉 20th Birthday")
st.sidebar.markdown("📅 3 February")

# ---------------- HOME ----------------
if page == "🎂 Home":
    st.markdown("<h1 class='glow float'>🎂 Happy 20th Birthday Kanchan 🎂</h1>", unsafe_allow_html=True)
    st.markdown("<h3>3rd February – A day full of smiles ✨</h3>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>🌟 20 Years of Happiness 🌟</h2>
        <p>
        You bring positivity, laughter and sunshine wherever you go 🌸<br>
        May every day be as bright as your smile ✨
        </p>
    </div>
    """, unsafe_allow_html=True)

    try:
        st.audio("birthday.mp3", loop=True)
    except:
        st.info("🎵 Add birthday.mp3 for background music")

    with st.spinner("🎂 Decorating the cake..."):
        time.sleep(2)
    st.success("🎉 Cake is ready to celebrate!")

# ---------------- MEMORIES ----------------
elif page == "📸 Memories":
    st.markdown("<h1 class='glow'>📸 Sweet Memories</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <p>Moments that always bring a smile 🌼✨</p>
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
        <p>The celebration is getting closer 🌈</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- MESSAGE OPTION ----------------
elif page == "💌 Message":
    st.markdown("<h1 class='glow'>💌 A Special Message</h1>", unsafe_allow_html=True)

    choice = st.radio(
        "Choose message type 🌸",
        ["👭 Best Friend", "🦋 Like Sister"]
    )

    if st.button("✨ Show Message"):
        st.balloons()

        if choice == "👭 Best Friend":
            st.markdown("""
            <div class="card">
                <h2>🌸 My Best Friend 🌸</h2>
                <p>
                You are my constant laughter,
                my comfort zone and my favorite person to talk to ✨<br>
                Life feels lighter with you around 🌈
                </p>
                <h3 class="signature">— Your Best Friend Anuj 🎀</h3>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown("""
            <div class="card">
                <h2>🦋 Like My Sister 🦋</h2>
                <p>
                You are not just a friend,
                you are someone I trust like family 🌸<br>
                A bond full of care, support and endless smiles ✨
                </p>
                <h3 class="signature">— From Anuj 🌟</h3>
            </div>
            """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("<br><p style='text-align:center;'>🎂 Made with smiles, memories & good vibes ✨</p>", unsafe_allow_html=True)
st.markdown("""
<style>
/* REAL BACKGROUND FIX */
.stApp {
    background: linear-gradient(
        135deg,
        #ffdde1,
        #ee9ca7,
        #fbc2eb,
        #a18cd1
    );
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
}

/* Gradient animation */
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

h1, h2, h3, p {
    text-align: center;
    color: white;
}

/* Card design */
.card {
    background: rgba(255,255,255,0.22);
    padding: 25px;
    border-radius: 22px;
    margin: 20px 0;
    box-shadow: 0 12px 30px rgba(0,0,0,0.3);
}

/* Glow animation */
.glow {
    animation: glow 2s infinite alternate;
}
@keyframes glow {
    from { text-shadow: 0 0 10px #fff; }
    to { text-shadow: 0 0 30px #ffd1dc; }
}

/* Floating effect */
.float {
    animation: float 3s ease-in-out infinite;
}
@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

/* Signature animation */
.signature {
    animation: fade 2s infinite alternate;
}
@keyframes fade {
    from { opacity: 0.6; }
    to { opacity: 1; }
}
</style>
""", unsafe_allow_html=True)

