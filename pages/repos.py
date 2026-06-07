import streamlit as st
import pandas as pd
from src.charts import stars_bar_chart, repo_timeline

def render(repos: list):
    st.subheader("Repository analysis")

    # filters in a row
    col1, col2 = st.columns(2)
    sort_by  = col1.selectbox("Sort by", ["Stars", "Forks", "Updated", "Created"])
    min_stars = col2.slider("Min stars", 0, 100, 0)

    # filter + sort repos
    filtered = [r for r in repos if r["stargazers_count"] >= min_stars]
    key_map  = {"Stars": "stargazers_count", "Forks": "forks_count",
                "Updated": "updated_at", "Created": "created_at"}
    filtered.sort(key=lambda r: r[key_map[sort_by]], reverse=True)

    st.plotly_chart(stars_bar_chart(filtered), use_container_width=True)
    st.plotly_chart(repo_timeline(filtered),   use_container_width=True)

    # searchable dataframe
    df = pd.DataFrame([{
        "Name": r["name"], "Stars": r["stargazers_count"],
        "Forks": r["forks_count"],  "Language": r.get("language", "—"),
        "Updated": r["updated_at"][:10]
    } for r in filtered])
    st.dataframe(df, use_container_width=True, hide_index=True)
