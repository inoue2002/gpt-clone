import os
import time

import openai
from dotenv import load_dotenv

load_dotenv(verbose=True)

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.File.create(file=open("dataset.jsonl", "rb"), purpose="fine-tune")
file_id = response["id"]
suffix = time.strftime("%Y%m%d%H%M%S")

while True:
    res = openai.File.retrieve(file_id)
    if res["status"] == "processed":
        break
    print("waiting for processing")
    time.sleep(5)

print(file_id)

response_retrieve  = openai.FineTuningJob.create(
    training_file=file_id,
    model="gpt-3.5-turbo",
    suffix=suffix,
    hyperparameters={"n_epochs": 5},
)


print(response_retrieve.result_files)