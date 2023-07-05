import requests

headers = {"Authorization": "Bearer 26c8bc94e8475ac705bf1f123506846b3219ee46"}
endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "New Title For This One",
    "price": 299.90,
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
