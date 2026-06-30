"""
Lesson 5: Pagination - Handling Large Datasets
"""

import requests

# === 5.1 Understanding Pagination ===
print("=== 5.1 GitHub Repos Pagination ===")
url = "https://api.github.com/orgs/python/repos"
params = {"per_page": 5, "page": 1}

resp = requests.get(url, params=params, timeout=10,
                    headers={"Accept": "application/vnd.github.v3+json",
                             "User-Agent": "APICourse"})
if resp.ok:
    repos = resp.json()
    print(f"Page 1: {len(repos)} repos")
    for repo in repos:
        print(f"  - {repo['name']} (⭐ {repo['stargazers_count']})")
print()

# === 5.2 Fetching Multiple Pages ===
print("=== 5.2 Multi-Page Fetch ===")
all_repos = []
for page in range(1, 4):  # Get first 3 pages
    params = {"per_page": 5, "page": page}
    resp = requests.get(url, params=params, timeout=10,
                        headers={"Accept": "application/vnd.github.v3+json",
                                 "User-Agent": "APICourse"})
    if resp.ok:
        repos = resp.json()
        all_repos.extend(repos)
        print(f"Page {page}: fetched {len(repos)} repos")

print(f"\nTotal repos collected: {len(all_repos)}")
print(f"Latest repo name: {all_repos[-1]['name'] if all_repos else 'N/A'}")
print()

# === 5.3 Link Headers (GitHub's pagination) ===
print("=== 5.3 Pagination via Link Header ===")
resp = requests.get(
    "https://api.github.com/orgs/python/repos?per_page=2",
    headers={"Accept": "application/vnd.github.v3+json",
             "User-Agent": "APICourse"}
)
link_header = resp.headers.get("Link")
print(f"Link Header: {link_header}")
# The Link header tells us about next/prev/last pages
