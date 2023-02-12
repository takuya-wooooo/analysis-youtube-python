import json
import os
import requests
import config
import datetime

date = datetime.datetime.now().strftime('%Y%m%d-%H:%M')

# Youtube Data API キー
apiKey = config.apikey

# APIリクエストを送信して、動画の情報を取得
url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id=xWXbFl_k0KA&key={apiKey}"
response = requests.get(url)
data = json.loads(response.text)

os.chmod(f'response', 0o777)
os.makedirs(f'response/{date}', exist_ok=True)
# レスポンス結果をファイルに書き込む
with open(f'response/{date}/videos.txt', 'w') as file:
    file.write(str(json.dumps(response.json(), indent=4)))