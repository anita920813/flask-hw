# app.py
from flask import Flask, render_template, request
from openai import OpenAI
import os

app = Flask(__name__)

# 對照簡報安全觀念：從雲端環境變數讀取密鑰
# 注意：等一下去 Render 後台記得要新增這個變數喔！
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def home():
    # 1. 個人履歷設定（對照簡報個人化需求）
    my_info = {
        "name": "謝宜蓁",
        "title": "Web Developer & IoT Engineer",
        "bio": "熱衷於 5G 通訊、物聯網整合與 AI 應用的 Master 研發學生。擅長用程式碼解決生活中的實際問題！"
    }
    
    ai_text_response = ""
    ai_image_url = ""
    
    # 2. 處理前端送來的 AI 請求
    if request.method == "POST":
        action_type = request.form.get("action_type")
        user_prompt = request.form.get("prompt")
        
        if user_prompt:
            try:
                # 【文字生成功能】對照簡報最小範例
                if action_type == "text":
                    response = client.chat.completions.create(
                        model="gpt-4o-mini", # 採用官方目前標準輕量模型
                        messages=[{"role": "user", "content": user_prompt}]
                    )
                    ai_text_response = response.choices[0].message.content
                
                # 【圖片生成功能】對照簡報 Image-Generator
                elif action_type == "image":
                    response = client.images.generate(
                        model="dall-e-3",
                        prompt=user_prompt,
                        n=1,
                        size="1024x1024"
                    )
                    ai_image_url = response.data[0].url
            except Exception as e:
                ai_text_response = f"❌ 呼叫 AI 時發生錯誤，請檢查 API Key 是否正確設定。錯誤訊息: {str(e)}"

    return render_template("index.html", info=my_info, text_result=ai_text_response, image_result=ai_image_url)

if __name__ == "__main__":
    app.run(debug=True)
