import requests

# Qiita APIのエンドポイントURL
endpoint = "https://qiita.com/api/v2"
YOUR_ACCESS_TOKEN = "c1b1dc4fbf8d4f4e19a3fa90e4388f756f4acb12"

# アクセストークンを指定して、APIリクエストを送信する
headers = {"Authorization": "Bearer " + YOUR_ACCESS_TOKEN}
response = requests.get(f"{endpoint}/items", headers=headers)

# レスポンスを取得する
items = response.json()

# 取得したデータを表示する
for item in items:
    print(item["title"])
