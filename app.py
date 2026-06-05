# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

# 對照簡報：methods 必須包含 GET（打開頁面）與 POST（送出表單）
@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    
    # 對照簡報：當使用者點擊按鈕送出表單時
    if request.method == "POST":
        # 使用 request.form.get() 讀取前端 input 的 name 屬性值
        username = request.form.get("name")
        user_hobby = request.form.get("hobby")
        
        # 組合文字：做出個人化的自我介紹
        if username and user_hobby:
            message = f"✨ 大家好，我是 {username}！我的興趣是 {user_hobby}。很高興認識大家！"
        else:
            message = "⚠️ 填寫不完整，請輸入姓名與興趣喔！"
            
    # 將組合好的自我介紹字串（message）傳給 index.html 顯示
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
