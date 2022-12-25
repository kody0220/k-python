from flask import Flask

# Flask のアプリケーションインスタンスを作成
app = Flask(__name__)

# パス "/" にアクセスされたときに実行される関数を定義
@app.route("/")
def index():
    # Pythonで取得したデータ
    data = ["item1", "item2", "item3"]

    # 取得したデータを表示する HTML コードを返す
    return f"<h1>Data List</h1><ul>" + "".join([f"<li>{item}</li>" for item in data]) + "</ul>"

if __name__ == "__main__":
    # Webサーバを起動
    app.run()
