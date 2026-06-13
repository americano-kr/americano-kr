import requests
import re

USERNAME = "americano-kr"
API_URL = f"https://api.github.com/users/{USERNAME}/followers"

response = requests.get(API_URL)

if response.status_code == 200:
    followers = response.json()
    
    if len(followers) > 0:
        latest_follower = followers[-1]
        username = latest_follower['login']
        profile_url = latest_follower['html_url']
        avatar_url = latest_follower['avatar_url']

        # Perbaikan di sini: Menggunakan tag HTML <strong> untuk bold, dan 
        # atribut CSS vertical-align: middle untuk kesejajaran. Ukuran width disesuaikan.
        replacement_text = f"""<br>

<div align="center">
  <a href="{profile_url}">
    <img src="{avatar_url}" width="25" alt="{username}" style="border-radius: 50%; vertical-align: middle;" />
  </a> Hello, <a href="{profile_url}"><strong>{username}</strong></a>! It is nice to meet you, thanks 4 following me (╹ڡ╹ )!
</div>

<br>"""

    else:
        replacement_text = """<br>

<div align="center">
  No followers yet. Be the first to follow me! (╹ڡ╹ )
</div>

<br>"""

    with open("README.md", "r", encoding="utf-8") as file:
        readme_content = file.read()

    # Regex ini mencari persis dari "### Latest Follower:" sampai bagian gambar marquee
    pattern = r'(### Latest Follower:).*?(<div align="center">\s*<img height="120" width="100%" src="https://raw\.githubusercontent\.com/BrunnerLivio/brunnerlivio/master/images/marquee\.svg")'
    
    new_content = re.sub(
        pattern,
        rf'\1\n{replacement_text}\n\2',
        readme_content,
        flags=re.DOTALL
    )

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(new_content)
else:
    print(f"Gagal mengambil data. Status code: {response.status_code}")
