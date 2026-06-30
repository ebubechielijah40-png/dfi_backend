"""
Lesson 2: Query Parameters, Filtering, and Error Handling
"""

import requests

# === 2.1 Query Parameters ===
print("=== 2.1 Query Parameters ===")

# Method 1: Manually in URL
resp1 = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1")
print(f"User 1 posts: {len(resp1.json())}")

# Method 2: Using params dict (cleaner)
params = {"userId": 2}
resp2 = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
print(f"User 2 posts: {len(resp2.json())}")
print(f"Actual URL: {resp2.url}")
print()

# === 2.2 Multiple Filters ===
print("=== 2.2 Multiple Filters ===")
params = {"userId": 1, "id": 5}
resp = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
print(f"Result: {resp.json()}")
print()

# === 2.3 Error Handling ===
print("=== 2.3 Error Handling ===")

try:
    bad = requests.get("https://jsonplaceholder.typicode.com/nonexistent")
    bad.raise_for_status()  # Raises HTTPError for 4xx/5xx
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")

try:
    timeout = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=0.001)
except requests.exceptions.Timeout:
    print("Timeout! The server took too long.")
except requests.exceptions.ConnectionError:
    print("Connection error (network may be slow or unreachable).")

try:
    garbage = requests.get("https://thissitedoesnotexist99999.com")
except requests.exceptions.ConnectionError:
    print("Connection Error! Could not reach the server.")
print()

# === 2.4 Timeouts (Always use them!) ===
print("=== 2.4 Timeouts ===")
try:
    resp = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=5  # seconds
    )
    print(f"Success with timeout: {resp.status_code}")
except requests.exceptions.Timeout:
    print("Request timed out")
