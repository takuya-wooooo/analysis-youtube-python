import json
import os
import requests
import config
import datetime

date = datetime.datetime.now().strftime('%Y%m%d-%H:%M')

# Youtube Data API キー
apiKey = config.apikey

# APIリクエストを送信して、動画のコメントを取得
url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=eu7EqtVZ-Jo&key={apiKey}&textFormat=plainText"
response = requests.get(url)
data = json.loads(response.text)

os.chmod(f'response', 0o777)
os.makedirs(f'response/{date}', exist_ok=True)
# レスポンス結果をファイルに書き込む
with open(f'response/{date}/commentThreads.txt', 'w') as file:
    file.write(json.dumps(response.json(), indent=4, ensure_ascii=False)) # ensure_ascii=Falseでファイル書き込み時の日本語の文字化けを防ぐ