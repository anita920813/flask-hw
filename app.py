from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # 這是老師簡報最後一頁教的：讓 Python 去控制並回傳 templates 資料夾底下的 index.html
    return "Hello World! This is my first Flask app."

if __name__ == "__main__":
    app.run(debug=True)
