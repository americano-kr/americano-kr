import requests
import re

# Ganti dengan username GitHub kamu
USERNAME = "americano-kr"
API_URL = f"https://api.github.com/users/{USERNAME}/followers"

response = requests.get(API_URL)

# Pastikan request berhasil dan ada data follower
if response.status_code == 200:
    followers = response.json()
    
    if followers:
        # Mengambil follower terbaru
        latest_follower = followers[-1]
        username = latest_follower['login']
        profile_url = latest_follower['html_url']
        avatar_url = latest_follower['avatar_url']

        # Format HTML sesuai permintaan (Gambar dan Teks berdampingan)
        replacement_text = f"""<a href="{profile_url}">
  <img src="{avatar_url}" width="40" alt="{username}" style="border-radius:50%;" />
</a> Hello, <a href="{profile_url}">**{username}**</a>! It is nice to meet you, thanks 4 following me (╹ڡ╹ )!
"""

        # Membaca isi README
        with open("README.md", "r", encoding="utf-8") as file:
            readme_content = file.read()

        # Mengganti teks lama dengan teks baru
        new_content = re.sub(
            r'.*',
            replacement_text,
            readme_content,
            flags=re.DOTALL
        )

        # Menyimpan kembali ke README
        with open("README.md", "w", encoding="utf-8") as file:
            file.write(new_content)
else:
    print(f"Gagal mengambil data. Status code: {response.status_code}")
