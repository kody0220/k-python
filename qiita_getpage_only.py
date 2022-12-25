import requests
import sys

# Qiita APIのエンドポイントURL
endpoint = "https://qiita.com/api/v2"

# アクセストークンを指定して、APIリクエストを送信する
headers = {"Authorization": "Bearer " + sys.argv[1]}
response = requests.get(f"{endpoint}/items", headers=headers)

# レスポンスを取得する
items = response.json()

# 取得したデータを表示する
for item in items:
    print(item["title"])
