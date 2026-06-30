"""
Lesson 1: Requests Basics - GET, Status Codes, JSON
"""

import requests

# === 1.1 The simplest GET request ===
print("=== 1.1 Basic GET ===")
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(f"Status Code: {response.status_code}")
print(f"Response (JSON): {response.json()}")
print()

# === 1.2 Understanding Status Codes ===
print("=== 1.2 Status Codes ===")
# 200 - OK
ok = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(f"200 OK: {ok.status_code}")

# 404 - Not Found
not_found = requests.get("https://jsonplaceholder.typicode.com/posts/99999")
print(f"404 Not Found: {not_found.status_code}")

# 201 - Created (when we POST)
new = requests.post("https://jsonplaceholder.typicode.com/posts", json={"title": "test"})
print(f"201 Created: {new.status_code}")

# Check response.ok (True for 2xx)
print(f"response.ok for 200: {ok.ok}")
print(f"response.ok for 404: {not_found.ok}")
print()

# === 1.3 Working with JSON ===
print("=== 1.3 JSON Handling ===")
data = response.json()
print(f"Parsed JSON type: {type(data)}")
print(f"Title: {data['title']}")
print(f"Body: {data['body'][:50]}...")
print()

# === 1.4 Headers & Metadata ===
print("=== 1.4 Response Headers ===")
print(f"Content-Type: {response.headers.get('Content-Type')}")
print(f"Server: {response.headers.get('Server')}")
print(f"Response Time (ms): {response.elapsed.microseconds / 1000}")
print()

# === 1.5 Checking before parsing ===
print("=== 1.5 Safe JSON Parsing ===")
safe_response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if safe_response.ok:
    print("Success!")
    data = safe_response.json()
    print(data["title"])
else:
    print(f"Failed with {safe_response.status_code}")
