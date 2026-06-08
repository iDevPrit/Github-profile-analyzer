<div align="center">

#  GitHub Profile Analyzer 🔍

**Analyze any GitHub profile — scores, stats, top repos, language breakdown — all in one place.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-5.18+-3F4F75?style=flat&logo=plotly&logoColor=white)](https://plotly.com)
[![GitHub API](https://img.shields.io/badge/GitHub-REST%20API%20v3-181717?style=flat&logo=github&logoColor=white)](https://docs.github.com/en/rest)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=flat)](LICENSE)

[Live Demo](#) · [Report Bug](../../issues) · [Request Feature](../../issues)

<!-- Add your screenshot here after first run:
![App Screenshot](assets/screenshot.png)
-->

</div>

---

## ✨ Features

- **Developer Score** — weighted score (0–100) based on followers, stars, forks, repos, and account age
- **Profile Overview** — avatar, bio, location, follower stats, top 5 repos at a glance
- **Repository Analysis** — sort/filter repos by stars, forks, or date; interactive charts
- **Language Breakdown** — donut chart + bar chart showing your language distribution
- **Smart Caching** — API responses cached for 5 minutes so repeat searches are instant
- **Token Support** — add a GitHub token for 5000 req/hour (vs 60 without)

---

## 📸 Screenshots

> _Add screenshots here after running the app. Suggested shots:_
> - Overview tab with score gauge
> - Repos tab with bar chart
> - Languages tab with donut chart

| Overview | Repositories | Languages |
|----------|-------------|-----------|
| _coming soon_ | _coming soon_ | _coming soon_ |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend/UI | Streamlit |
| Charts | Plotly Express + Graph Objects |
| API | GitHub REST API v3 |
| Data | Pandas |
| Language | Python 3.10+ |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- A GitHub account (optional: personal access token for higher rate limits)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/github-profile-analyzer.git
cd github-profile-analyzer
```

**2. Create and activate a virtual environment**

```bash
# macOS / Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Set up your GitHub token (optional but recommended)**

Create a `.env` file in the root directory:

```env
GITHUB_TOKEN=ghp_your_token_here
```

> Get a free token: GitHub → Settings → Developer Settings → Personal Access Tokens → Tokens (classic) → Generate new token (no scopes needed for public data)

**5. Run the app**

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📁 Project Structure

```
github-profile-analyzer/
│
├── app.py                  # Main Streamlit entry point
├── requirements.txt        # Python dependencies
├── .env                    # GitHub token (DO NOT commit this)
├── .gitignore
├── README.md
│
├── src/
│   ├── github_api.py       # GitHub REST API calls + caching
│   ├── analyzer.py         # Scoring algorithm + stats logic
│   ├── charts.py           # Plotly chart functions
│   └── utils.py            # Helper functions
│
├── pages/
│   ├── overview.py         # Tab 1: Profile summary + score
│   ├── repos.py            # Tab 2: Repository analysis
│   └── languages.py        # Tab 3: Language breakdown
│
└── assets/
    └── style.css           # Custom Streamlit CSS
```

---

## 🧮 Developer Score Algorithm

The score (0–100) is calculated using a weighted formula:

| Factor | Weight | Max Points |
|--------|--------|-----------|
| Total stars across all repos | 30% | 30 |
| Public repositories count | 20% | 20 |
| Followers count | 20% | 20 |
| Total forks | 15% | 15 |
| Account age | 15% | 15 |

---

## ☁️ Deploy for Free (Streamlit Cloud)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New app** → select your repo → set `app.py` as entry point
4. Add your token in **Secrets** (not `.env`):

```toml
GITHUB_TOKEN = "ghp_your_token_here"
```

5. Click **Deploy** — your live link is ready in ~2 minutes!

---

## 🔧 Usage

1. Enter any GitHub username in the sidebar
2. Optionally paste your GitHub token for higher rate limits
3. Explore the three tabs:
   - **Overview** — score, metrics, top repos
   - **Repositories** — filter, sort, and visualize all repos
   - **Languages** — see your language distribution

---

## 🤝 Contributing

Contributions are welcome! Here's how:

```bash
# Fork the repo, then:
git checkout -b feature/your-feature-name
git commit -m "Add: your feature description"
git push origin feature/your-feature-name
# Open a Pull Request
```

---

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

---

## 👤 Author

**Your Name**
- GitHub: [@your_username](https://github.com/your_username)
- LinkedIn: [your_linkedin](https://linkedin.com/in/your_linkedin)

---

<div align="center">
  <sub>Built with ❤️ using Python + Streamlit</sub>
</div>
