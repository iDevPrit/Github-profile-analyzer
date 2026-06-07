def calculate_score(user: dict, repos: list) -> dict:
    """
    Developer Score = weighted formula:
      followers (20%) + repos (20%) + stars (30%) + forks (15%) + account_age (15%)
    Returns score out of 100 + breakdown dict
    """
    total_stars = sum(r["stargazers_count"] for r in repos)
    total_forks = sum(r["forks_count"] for r in repos)

    followers_score = min(user["followers"] / 1000 * 20, 20)
    repos_score     = min(len(repos) / 50 * 20, 20)
    stars_score     = min(total_stars / 500 * 30, 30)
    forks_score     = min(total_forks / 100 * 15, 15)
    age_score       = _account_age_score(user["created_at"])

    total = followers_score + repos_score + stars_score + forks_score + age_score

    return {
        "total": round(total, 1),
        "total_stars": total_stars,
        "total_forks": total_forks,
        "breakdown": {
            "Followers": round(followers_score, 1),
            "Repos": round(repos_score, 1),
            "Stars": round(stars_score, 1),
            "Forks": round(forks_score, 1),
            "Account age": round(age_score, 1),
        }
    }

def get_language_stats(repos: list) -> dict:
    """Count bytes per language across all repos"""
    lang_counts = {}
    for repo in repos:
        lang = repo.get("language")
        if lang:
            lang_counts[lang] = lang_counts.get(lang, 0) + 1
    return dict(sorted(lang_counts.items(), key=lambda x: x[1], reverse=True))

def get_top_repos(repos: list, n=5) -> list:
    """Top N repos by star count"""
    return sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)[:n]
