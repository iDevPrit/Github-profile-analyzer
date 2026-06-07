import plotly.express as px
import plotly.graph_objects as go

def language_pie_chart(lang_stats: dict):
    """Donut chart of top languages"""
    fig = px.pie(
        values=list(lang_stats.values()),
        names=list(lang_stats.keys()),
        hole=0.4,
        title="Language distribution"
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")
    return fig

def stars_bar_chart(repos: list):
    """Horizontal bar chart — top repos by stars"""
    top = sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)[:8]
    fig = px.bar(
        x=[r["stargazers_count"] for r in top],
        y=[r["name"] for r in top],
        orientation="h",
        title="Top repos by stars"
    )
    fig.update_layout(yaxis=dict(autorange="reversed"))
    return fig

def score_gauge(score: float):
    """Speedometer-style gauge for developer score"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        domain={"x": [0, 1], "y": [0, 1]},
        title={"text": "Developer Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#2da44e"},
            "steps": [
                {"range": [0, 40], "color": "#fee2e2"},
                {"range": [40, 70], "color": "#fef9c3"},
                {"range": [70, 100], "color": "#dcfce7"},
            ],
        }
    ))
    return fig

def repo_timeline(repos: list):
    """Scatter plot — repos created over time"""
    fig = px.scatter(
        x=[r["created_at"][:10] for r in repos],
        y=[r["stargazers_count"] for r in repos],
        hover_name=[r["name"] for r in repos],
        size=[max(r["forks_count"], 1) for r in repos],
        title="Repo activity over time"
    )
    return fig
