import requests
import pandas as pd

APP_ID = "ab9c62c41daad6570ff3414a3ae175e7" #APIキーを設定
API_URL  = "https://api.openweathermap.org/data/2.5/weather" #APIのエンドポイント

# 東京のパラメータ
params = {
    "appId": APP_ID, #APIキー
    "q" : "Tokyo", #都市名
    "units" : "metric", #温度を摂氏に設定
    "lang" : "ja" # 日本語を指定
}

# APIへリクエストを送信
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()

# 取得したデータの一部を抽出して表示
weather_main = data['weather'][0]['main']  # 天気の大分類（例：Clear, Clouds）
weather_description = data['weather'][0]['description']  # 詳細な天気説明
temperature = data['main']['temp']  # 気温
humidity = data['main']['humidity']  # 湿度
wind_speed = data['wind']['speed']  # 風速
city_name = data['name']  # 地域名

# DataFrameに格納
df = pd.DataFrame({
    '都市': [city_name],
    '天気': [weather_main],
    '詳細': [weather_description],
    '気温(℃)': [temperature],
    '湿度(%)': [humidity],
    '風速(m/s)': [wind_speed]
    })
print(df)
