import streamlit as st
from src.github_api import GitHubAPI
from src.analyzer import calculate_score
from pages import overview, repos, languages

st.set_page_config(
    page_title="GitHub Analyzer",
    page_icon="🔍",
    layout="wide"
)

# Load custom CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar - username input
st.sidebar.title("GitHub Profile Analyzer")
username = st.sidebar.text_input("Enter GitHub username", placeholder="e.g. torvalds")
token = st.sidebar.text_input("GitHub Token (optional)", type="password")

if username:
    api = GitHubAPI(token=token)
    with st.spinner("Fetching profile..."):
        user_data = api.get_user(username)
        repos_data = api.get_repos(username)

    if user_data:
        score = calculate_score(user_data, repos_data)
        tab1, tab2, tab3 = st.tabs(["Overview", "Repositories", "Languages"])
        with tab1: overview.render(user_data, score)
        with tab2: repos.render(repos_data)
        with tab3: languages.render(repos_data)
    else:
        st.error("User not found!")
else:
    st.info("Enter a GitHub username in the sidebar to start")
