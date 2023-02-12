# analysis-youtube-python

# .gitignore
/.env YouTube DATA API Keyの値を設定


# YouTube APIについて
1.クエリで動画 ID とチャンネル ID を取得する
  https://www.googleapis.com/youtube/v3/search
  例：https://www.googleapis.com/youtube/v3/search?part=snippet&q=soccer%20fifa&key=[YOUR_API_KEY]
  レスポンス：videoId、チャンネルID、動画タイトルなど

2.動画ID を使用して動画の統計データを取得する
  https://www.googleapis.com/youtube/v3/videos
  例：https://www.googleapis.com/youtube/v3/videos?part=statistics&id=UCZf__ehlCEBPop-_sldpBUQ&key=[YOUR_API_KEY]
  レスポンス：再生回数、いいね数、Bad数、コメント数など

3.動画のコメントを取得する
  https://www.googleapis.com/youtube/v3/commentThreads
  例：https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=eu7EqtVZ-Jo&key=[YOUR_API_KEY]
  レスポンス：コメント内容、コメントのいいね数、コメント投稿日時など

4.チャンネル ID でチャンネルの情報を取得する
  https://www.googleapis.com/youtube/v3/channels
  例：https://www.googleapis.com/youtube/v3/channels?part=snippet%2Cstatistics&id=UCZf__ehlCEBPop-_sldpBUQ&key=[YOUR_API_KEY]
  レスポンス：再生回数、いいね数、Bad数、コメント数など
