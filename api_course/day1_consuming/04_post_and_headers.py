"""
Lesson 4: POST Requests, Headers, and Authentication
"""

import requests

# === 4.1 POST Request ===
print("=== 4.1 POST - Creating Data ===")
new_post = {
    "title": "My API Course",
    "body": "Learning to consume and build APIs with Python",
    "userId": 1
}

resp = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post  # automatically sets Content-Type: application/json
)
print(f"Status: {resp.status_code}")
print(f"Created: {resp.json()}")
print()

# === 4.2 Custom Headers ===
print("=== 4.2 Custom Headers ===")
headers = {
    "User-Agent": "MyAPICourse/1.0",
    "Accept": "application/json",
    "X-Custom-Header": "learning-apis"
}
resp = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    headers=headers
)
print(f"Status: {resp.status_code}")
print(f"We sent custom headers to the server")
print()

# === 4.3 API with Authentication (Token) ===
print("=== 4.3 Token Auth (GitHub API) ===")
headers = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "APICourse"
}
resp = requests.get("https://api.github.com/rate_limit", headers=headers)
if resp.ok:
    data = resp.json()
    core = data["rate"]
    print(f"GitHub API remaining calls: {core['remaining']}/{core['limit']}")
print()

# === 4.4 PUT (Update) & DELETE ===
print("=== 4.4 PUT & DELETE ===")

# Update
update = {"title": "Updated Title", "body": "Updated body", "userId": 1}
put_resp = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=update
)
print(f"PUT Status: {put_resp.status_code}")
print(f"Updated: {put_resp.json()}")

# Delete
del_resp = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(f"DELETE Status: {del_resp.status_code}")
print(f"Deleted (empty on success): {del_resp.text}")
