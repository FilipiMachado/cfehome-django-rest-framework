import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query": "Hello World"}) # HTTP Request

# print(get_response.text)
print(get_response.json()) # Print raw text response