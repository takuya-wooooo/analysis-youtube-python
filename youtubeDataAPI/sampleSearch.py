import json
import os
import requests
import config
import datetime

date = datetime.datetime.now().strftime('%Y%m%d-%H:%M')

# Youtube Data API キー
apiKey = config.apikey

# APIリクエストを送信して、動画の一覧を取得
url = f"https://www.googleapis.com/youtube/v3/search?key={apiKey}&part=snippet&q=サッカー&order=viewCount&maxResults=50" # maxResultsで取得上限数を設定可能
response = requests.get(url)
data = json.loads(response.text)

os.chmod(f'response', 0o777)
os.makedirs(f'response/{date}', exist_ok=True)
# レスポンス結果をファイルに書き込む
with open(f'response/{date}/search.txt', 'w') as file:
    file.write(str(json.dumps(response.json(), indent=4)))