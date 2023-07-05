import requests

headers = {"Authorization": "Bearer 0380fbd90c0f54cdb44db66f82b2ac97ce16da4a"}
endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "New Title For This One",
    "price": 299.90,
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
