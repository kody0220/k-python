import requests
import sys

# Qiita APIのエンドポイントURL
url = "https://qiita.com/api/v2/items"


# アクセストークン
headers = {"Authorization": "Bearer " + sys.argv[1]}

# いいね数が多い順に取得するためのパラメータ
params = {"sort": "likes_count"}

# APIリクエストを送信して結果を取得
response = requests.get(url, headers=headers, params=params)

# 結果を表示
if response.status_code == 200:
    items = response.json()
    for item in items:
        print(f"{item['title']}: {item['likes_count']}いいね")
else:
    print("Error: Qiita API request failed.")
