import streamlit as st
from src.analyzer import get_language_stats
from src.charts import language_pie_chart

def render(repos: list):
    lang_stats = get_language_stats(repos)

    st.subheader("Language breakdown")
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(language_pie_chart(lang_stats), use_container_width=True)

    with col2:
        st.subheader("Stats")
        st.metric("Languages used", len(lang_stats))
        st.metric("Primary language", list(lang_stats.keys())[0])
        # bar chart: top 10 langs by repo count
        top10 = dict(list(lang_stats.items())[:10])
        st.bar_chart(top10)
