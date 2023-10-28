import openai
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

import argparse

# パーサーを作成
parser = argparse.ArgumentParser(description='This is a demo script.')

# 引数を追加
parser.add_argument('arg1', type=str, help='an integer argument')

# 引数を解析
args = parser.parse_args()

# 引数を表示
print(args.arg1)

openai.api_key = os.getenv("OPENAI_API_KEY")

model = os.getenv("TUNING_MODEL")

completion = openai.ChatCompletion.create(
  model=model,
  messages=[
    {"role": "user", "content": args.arg1}
  ]
)
print(completion.choices[0].message.content)