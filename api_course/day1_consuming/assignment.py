"""
Assignment: Build a GitHub Profile Explorer
-------------------------------------------
Combine everything you learned today:
  - GET requests & status codes
  - Query parameters & headers
  - JSON parsing
  - Pagination
  - Error handling

Instructions:
  Complete the functions below using the GitHub API.
  GitHub's public API docs: https://docs.github.com/en/rest

Tips:
  - Use Accept header: "application/vnd.github.v3+json"
  - Always set a User-Agent header
  - Use timeouts
  - Handle errors gracefully
"""

import requests

BASE_URL = "https://api.github.com"
HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "APICourse-Student"
}


def get_user_info(username):
    """
    Fetch and display GitHub user info.
    Return: dict with name, public_repos, followers, following
    """
    # TODO: GET /users/{username}
    # Handle 404 (user not found)
    pass


def get_user_repos(username, max_pages=2):
    """
    Fetch the user's public repositories across multiple pages.
    Return: list of repo dicts with name, stars, description
    """
    # TODO: Use pagination (per_page=10, page=1,2)
    pass


def search_repositories(query, sort="stars"):
    """
    Search GitHub repositories by keyword.
    Return: list of top 5 results with name, url, stars
    """
    # TODO: GET /search/repositories?q={query}
    pass


def get_repo_contributors(owner, repo, top_n=5):
    """
    Get top contributors for a repository.
    Return: list of dicts with login, contributions
    """
    # TODO: GET /repos/{owner}/{repo}/contributors
    pass


# === TEST YOUR CODE ===
# When run directly, uncomment to test:
# print(get_user_info("octocat"))
# print(get_user_repos("octocat"))
# print(search_repositories("python"))
# print(get_repo_contributors("python", "cpython"))
