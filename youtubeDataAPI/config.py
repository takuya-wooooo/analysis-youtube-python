import json
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenvPath = join(dirname(__file__), '.env')
load_dotenv(dotenvPath)

# .envで設定したAPIキーを取得
apikey = os.environ.get('YOUTUBE_DATA_API_KEY')
oauthClientID = os.environ.get('OAUTH_CLIENT_ID') 
