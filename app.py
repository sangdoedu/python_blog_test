import streamlit as st

st.set_page_config(page_title="Wanderlust Diary", page_icon="🧳", layout="wide")

FEATURED = [
    {
        "emoji": "🏯",
        "title": "Hoi An After Dark: Lanterns, Lanes and Late-Night Cao Lau",
        "tag": "Vietnam",
        "date": "Oct 12, 2026",
        "read": "6 min",
        "excerpt": "Why the old town is best after sunset, and where to eat when the crowds thin out.",
    },
    {
        "emoji": "🏔️",
        "title": "Ha Giang Loop in 4 Days: What I Wish I Had Packed",
        "tag": "Adventure",
        "date": "Sep 28, 2026",
        "read": "9 min",
        "excerpt": "Winding passes, homestays and rice wine. A day-by-day route with real costs.",
    },
    {
        "emoji": "🍜",
        "title": "Hanoi Street Food: 12 Stalls Worth the Plastic Stool",
        "tag": "Food",
        "date": "Sep 10, 2026",
        "read": "7 min",
        "excerpt": "From bun cha to egg coffee, a walking map of the Old Quarter's best bites.",
    },
]

DESTINATIONS = [
    ("🌴", "Phu Quoc"),
    ("⛰️", "Sa Pa"),
    ("🏖️", "Da Nang"),
    ("🛶", "Mekong Delta"),
    ("🏙️", "Ho Chi Minh City"),
    ("🗻", "Fansipan"),
]

st.markdown(
    """
    <style>
    .hero {
        padding: clamp(2rem, 8vw, 4.5rem) 1.25rem;
        border-radius: 1.25rem;
        text-align: center;
        color: #fff;
        background: linear-gradient(135deg, #0f766e 0%, #0ea5e9 55%, #f59e0b 100%);
    }
    .hero h1 { font-size: clamp(1.75rem, 7vw, 3rem); margin: 0 0 .5rem; color: #fff; overflow-wrap: normal; }
    .hero p { font-size: 1.2rem; margin: 0; opacity: .95; }
    .card-emoji { font-size: 3rem; line-height: 1; }
    .meta { color: #64748b; font-size: .85rem; }
    </style>
    <div class="hero">
        <h1>🧳 Wanderlust Diary</h1>
        <p>Real routes, honest costs and stories from the road.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")
st.subheader("Latest stories")
for col, post in zip(st.columns(len(FEATURED)), FEATURED):
    with col, st.container(border=True):
        st.markdown(f'<div class="card-emoji">{post["emoji"]}</div>', unsafe_allow_html=True)
        st.caption(post["tag"].upper())
        st.markdown(f"**{post['title']}**")
        st.write(post["excerpt"])
        st.markdown(
            f'<span class="meta">{post["date"]} · {post["read"]} read</span>',
            unsafe_allow_html=True,
        )

st.write("")
st.subheader("Explore by destination")
for col, (emoji, name) in zip(st.columns(len(DESTINATIONS)), DESTINATIONS):
    with col, st.container(border=True):
        st.markdown(f"<div style='text-align:center'><div class='card-emoji'>{emoji}</div>{name}</div>", unsafe_allow_html=True)

st.write("")
about, newsletter = st.columns(2, gap="large")

with about:
    st.subheader("About the blog")
    st.write(
        "Hi, I'm a slow traveler who loves night markets, mountain roads and "
        "long train rides. This blog collects itineraries, budgets and "
        "lessons learned so your next trip is easier than my first."
    )
    stats = st.columns(3)
    stats[0].metric("Countries", 14)
    stats[1].metric("Stories", 86)
    stats[2].metric("Km traveled", "42k")

with newsletter:
    st.subheader("Get new stories by email")
    with st.form("newsletter", clear_on_submit=True):
        email = st.text_input("Email address", placeholder="you@example.com")
        if st.form_submit_button("Subscribe"):
            if "@" in email and "." in email.split("@")[-1]:
                st.success("Thanks for subscribing! 🎉")
            else:
                st.error("Please enter a valid email address.")

st.divider()
st.caption("© 2026 Wanderlust Diary · Made with Streamlit")
