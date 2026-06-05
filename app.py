from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # 對照簡報：建立一個 Python 變數，並透過 render_template 傳給前端
    username = "謝宜蓁"
    return render_template("index.html", name=username)

if __name__ == "__main__":
    app.run(debug=True)
