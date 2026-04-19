import os

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

api_key = os.environ["ORS_API_KEY"]
content = content.replace("ORS_API_KEY_PLACEHOLDER", api_key)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ API key injected successfully")
