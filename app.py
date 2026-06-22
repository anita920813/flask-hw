from flask import Flask, render_template, request
import requests  # 💡 記得確保有導入 requests 套件來撈 API

app = Flask(__name__)

# 1. 蓁蓁的 11 首完美音樂資料庫 (保持不變)
MUSIC_DATABASE = {
    "Clear_Relaxed": "https://www.youtube.com/embed/rKi3oL2UDew?si=xpm8T4ecVOAtH_i-",
    "Clear_Tired": "https://www.youtube.com/embed/zde7oFYW4Zg?si=fkRRoGSmOU86P0rZ",
    "Clear_Anxious": "https://www.youtube.com/embed/w4oLP7fa9Vk?si=XWnS6vUD6h2vnf3f",
    "Clear_Lazy": "https://www.youtube.com/embed/VW7u5CKBXHg?si=Xip1N9UBmF2rVDQn",
    "Clear_Happy": "https://www.youtube.com/embed/xakBzg5atsM?si=v2uwO_PN4Mk0On71",
    "Rainy_Anxious": "https://www.youtube.com/embed/hCtwi8XkB4o?si=kwByuTyKZMaX2T2r",
    "Rainy_Tired": "https://www.youtube.com/embed/1t1Rp9Nx--M?si=S_hUz2feiEQLr68I",
    "Rainy_Relaxed": "https://www.youtube.com/embed/Abc-M-X3jmQ?si=20awqEx6OCgjihEz",
    "Rainy_Calm": "https://www.youtube.com/embed/HGMQbVfYVmI?si=Xq9-kHIPCZAp5aY5",
    "Rainy_Emo": "https://www.youtube.com/embed/O5FStz6_oEg?si=bCVIB-3DxPX9tx8b",
    "All_Focus": "https://www.youtube.com/embed/TQvXEza4fPc?si=_9d1t1Kh5pmD5Ds1"
}

# 💡 新增一個自動感知天氣的秘密武器函式
def get_auto_weather():
    try:
        # 向 wttr.in 請求目前 IP 所在地的天氣（格式設定為最純粹的代碼）
        # format=%C 代表回傳天氣狀態英文 (例如 Clear, Rain, Overcast 等)
        response = requests.get("https://wttr.in/?format=%C", timeout=5)
        weather_text = response.text.strip().lower()
        
        # 把外面的天氣狀態，對應回我們矩陣要的 "Rainy" 或 "Clear"
        if "rain" in weather_text or "shower" in weather_text or "cloud" in weather_text or "overcast" in weather_text:
            return "Rainy"
        else:
            return "Clear"
    except:
        # 如果網路斷線或 API 故障，預設給晴天作為備援方案
        return "Clear"

@app.route("/", methods=["GET", "POST"])
def index():
    # 預設狀態：一進網頁，大腦自動發動「雲端微氣象感知」抓取真實天氣！
    current_weather = get_auto_weather()
    user_mood = "Relaxed"
    
    if request.method == "POST":
        user_mood = request.form.get("mood", "Relaxed")
        # 如果使用者有手動在下拉選單切換，就以手動模擬優先（方便 Demo 展示）
        if request.form.get("weather"):
            current_weather = request.form.get("weather")
        
    if user_mood == "Focus":
        matrix_key = "All_Focus"
    else:
        matrix_key = f"{current_weather}_{user_mood}"
        
    selected_music = MUSIC_DATABASE.get(matrix_key, MUSIC_DATABASE["Clear_Relaxed"])
    
    if user_mood == "Focus":
        bg_color = "#1E1E1E"  
    elif current_weather == "Rainy":
        bg_color = "#D5DBDB"  
    else:
        bg_color = "#FEF9E7"  
        
    return render_template(
        "index.html", 
        music_url=selected_music, 
        weather=current_weather, 
        mood=user_mood,
        bg_color=bg_color
    )

if __name__ == "__main__":
    app.run(debug=True)
