import requests 

# eStat APIのアプリID
APP_ID = "d6f8a2967ac79ebca8120c1f893c9079b0189f27"
# eStat APIのエンドポイント
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId":"0003005798", # 就業状態別15歳以上人口
    "cdArea":"00000", #全国のコード
    "cdCat01": "A1101",
    "metaGetFlg":"Y",
    "cntGetFlg":"N",
    "explanationGetFlg":"Y",
    "annotationGetFlg":"Y",
    "sectionHeaderFlg":"1",
    "replaceSpChars":"0",
    "lang": "J"  # 日本語を指定
}



#response = requests.get(API_URL, params=params)
# APIリクエスト送信
response = requests.get(API_URL, params=params)
# Process the response
# 取得したレスポンスをJSON形式で処理
data = response.json()
print(data)
