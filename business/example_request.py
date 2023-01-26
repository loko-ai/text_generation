import requests

response = requests.post("http://0.0.0.0:8083/run/text_gen", json={
  "data": [
    "hello world",
    100,
    2,
    False,
    0.3,
]}).json()

data = response["data"]
print(data)