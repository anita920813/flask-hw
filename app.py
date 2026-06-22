from flask import Flask, render_template, request

app = Flask(__name__)

# ==========================================
# 1. 蓁蓁的黃金音樂資料庫 (11首完美矩陣)
# ==========================================
MUSIC_DATABASE = {
    # ☀️ 晴天矩陣 (Clear)
    "Clear_Relaxed": "https://www.youtube.com/embed/rKi3oL2UDew?si=xpm8T4ecVOAtH_i-",
    "Clear_Tired": "https://www.youtube.com/embed/zde7oFYW4Zg?si=fkRRoGSmOU86P0rZ",
    "Clear_Anxious": "https://www.youtube.com/embed/w4oLP7fa9Vk?si=XWnS6vUD6h2vnf3f",
    "Clear_Lazy": "https://www.youtube.com/embed/VW7u5CKBXHg?si=Xip1N9UBmF2rVDQn",
    "Clear_Happy": "https://www.youtube.com/embed/xakBzg5atsM?si=v2uwO_PN4Mk0On71",

    # 🌧️ 雨天矩陣 (Rainy)
    "Rainy_Anxious": "https://www.youtube.com/embed/hCtwi8XkB4o?si=kwByuTyKZMaX2T2r",
    "Rainy_Tired": "https://www.youtube.com/embed/1t1Rp9Nx--M?si=S_hUz2feiEQLr68I",
    "Rainy_Relaxed": "https://www.youtube.com/embed/Abc-M-X3jmQ?si=20awqEx6OCgjihEz",
    "Rainy_Calm": "https://www.youtube.com/embed/HGMQbVfYVmI?si=Xq9-kHIPCZAp5aY5",
    "Rainy_Emo": "https://www.youtube.com/embed/O5FStz6_oEg?si=bCVIB-3DxPX9tx8b",
    
    # 🧠 不受天氣限制的特殊狀態：深度專注讀書
    "All_Focus": "https://www.youtube.com/embed/TQvXEza4fPc?si=_9d1t1Kh5pmD5Ds1"
}

# ==========================================
# 2. 核心路由：掌控天氣與心情的交織
# ==========================================
@app.route("/", methods=["GET", "POST"])
def index():
    # 預設狀態：初次載入網頁時的初始值
    current_weather = "Clear"
    user_mood = "Relaxed"
    
    # 當使用者點擊網頁上的任何按鈕，觸發 POST 請求時
    if request.method == "POST":
        # 接收前端傳回來的天氣與心情數值
        user_mood = request.form.get("mood", "Relaxed")
        current_weather = request.form.get("weather", "Clear")
        
    # --- 【微氣象與心境共振之動態對流矩陣判斷】 ---
    if user_mood == "Focus":
        # 如果點擊的是「進入心流」，則跨越時空限制，直接指派超長讀書音樂
        matrix_key = "All_Focus"
    else:
        # 基礎心情則根據「天氣_心情」拼接成尋找音樂的鑰匙 (例如: "Rainy_Anxious")
        matrix_key = f"{current_weather}_{user_mood}"
        
    # 從資料庫撈出對應的 YouTube 嵌入網址，若找不到則給予預設晴天放鬆樂
    selected_music = MUSIC_DATABASE.get(matrix_key, MUSIC_DATABASE["Clear_Relaxed"])
    
    # --- 【環境氛圍動態調色盤】 ---
    # 根據不同的天氣，現場指派不同的文青背景顏色與色調
    if user_mood == "Focus":
        bg_color = "#1E1E1E"  # 進入心流時：變成極簡極客的暗黑高專注模式（低干擾）
    elif current_weather == "Rainy":
        bg_color = "#D5DBDB"  # 雨天時：沉穩低飽和度的文青深灰色、雨天感
    else:
        bg_color = "#FEF9E7"  # 晴天時：溫暖明亮、煦煦陽光的淡黃色
        
    # ==========================================
    # 3. Jinja2 魔術印章：將活資料啪的一下送去前端渲染
    # ==========================================
    return render_template(
        "index.html", 
        music_url=selected_music, 
        weather=current_weather, 
        mood=user_mood,
        bg_color=bg_color
    )

if __name__ == "__main__":
    app.run(debug=True)
