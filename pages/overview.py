import streamlit as st
from src.charts import score_gauge
from src.analyzer import get_top_repos

def render(user: dict, score: dict):
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(user["avatar_url"], width=150)
        st.subheader(user["name"] or user["login"])
        st.caption(user.get("bio", "No bio"))
        st.metric("Location", user.get("location", "Unknown"))

    with col2:
        # 4 metric cards in a row
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Followers",  user["followers"])
        m2.metric("Following",  user["following"])
        m3.metric("Public repos", user["public_repos"])
        m4.metric("Total stars", score["total_stars"])
        st.plotly_chart(score_gauge(score["total"]), use_container_width=True)

    st.subheader("Top repositories")
    # show top 5 repos as cards with name, stars, language
    top = get_top_repos(user["repos"])  # pass repos from app.py
    for repo in top:
        with st.container():
            st.markdown(f"**[{repo['name']}]({repo['html_url']})**")
            st.caption(f"⭐ {repo['stargazers_count']} · 🍴 {repo['forks_count']} · {repo.get('language','')}")
