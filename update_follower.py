import requests
import re

USERNAME = "americano-kr"
API_URL = f"https://api.github.com/users/{USERNAME}/followers"

response = requests.get(API_URL)

if response.status_code == 200:
    followers = response.json()
    
    # Jika ada follower (lebih dari 0)
    if len(followers) > 0:
        latest_follower = followers[-1]
        username = latest_follower['login']
        profile_url = latest_follower['html_url']
        avatar_url = latest_follower['avatar_url']

        replacement_text = f"""<a href="{profile_url}">
  <img src="{avatar_url}" width="40" alt="{username}" style="border-radius:50%; align-items:center;" />
</a> Hello, <a href="{profile_url}">**{username}**</a>! It is nice to meet you, thanks 4 following me (╹ڡ╹ )!
"""

    # Jika follower masih 0
    else:
        replacement_text = """No followers yet. Be the first to follow me! (╹ڡ╹ )
"""

    with open("README.md", "r", encoding="utf-8") as file:
        readme_content = file.read()

    new_content = re.sub(
        r'.*',
        replacement_text,
        readme_content,
        flags=re.DOTALL
    )

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(new_content)
else:
    print(f"Gagal mengambil data. Status code: {response.status_code}")
