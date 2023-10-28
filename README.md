# gpt-clone

とりあえず動かしてみる基本的的な使い方
- `save.json`に`{"q": "こんにちは、何をしていますか？", "a": "プログラミングをしています。"}`のような質問と回答を配列で作成する
- create_data2.pyを使ってfine-tuningに使える形式にする。
- fine_tuning.pyを使ってfine-tuningを行う
- openaiのfine-tuningのコンソールで学習が終わったタイミングでモデルのidが発行される（ft:gpt-3.5-turbo-0613:personal:xxxxxxxxx）のでそのIDをモデルとする
- chat.pyに上で発行したモデルを選択して会話が行える。`$ python3 chat.py こんにちは`のように入力するとterminal上で返答が確認できる

Twitter投稿をもとに利用する使い方
- `tweets.json`にツイートの投稿を入れる
- create_user_data.pyを使って`save.json`を作る
- create_data2.pyを使って`dataset.json`を作る
- fine_tuning.pyでfine-tuningを行う
- chat.pyで会話

- 書き込み系のスクリプトはすべて追加するだけなので上書きしたい場合はあらかじめ消す