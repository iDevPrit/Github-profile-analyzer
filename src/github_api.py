import requests
import streamlit as st

class GitHubAPI:
    BASE_URL = "https://api.github.com"

    def __init__(self, token=None):
        self.headers = {"Authorization": f"token {token}"} if token else {}

    @st.cache_data(ttl=300)  # cache for 5 mins
    def get_user(self, username: str) -> dict:
        """Fetch user profile — name, bio, followers, repos count"""
        res = requests.get(f"{self.BASE_URL}/users/{username}", headers=self.headers)
        return res.json() if res.status_code == 200 else None

    @st.cache_data(ttl=300)
    def get_repos(self, username: str) -> list:
        """Fetch all public repos — name, stars, forks, language"""
        repos = []
        page = 1
        while True:
            res = requests.get(
                f"{self.BASE_URL}/users/{username}/repos",
                params={"per_page": 100, "page": page, "sort": "updated"},
                headers=self.headers
            )
            data = res.json()
            if not data: break
            repos.extend(data)
            page += 1
        return repos

    @st.cache_data(ttl=300)
    def get_commit_activity(self, username: str, repo: str) -> dict:
        """Weekly commit frequency for a repo"""
        res = requests.get(
            f"{self.BASE_URL}/repos/{username}/{repo}/stats/commit_activity",
            headers=self.headers
        )
        return res.json() if res.status_code == 200 else []
