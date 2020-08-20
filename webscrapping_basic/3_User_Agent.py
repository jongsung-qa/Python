import requests
url = "http://jongsung-qa.tistory.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
res = requests.get(url, headers=headers) # 403
res.raise_for_status()

with open("user_agent.html", "w", encoding="utf8") as f:
    f.write(res.text)


