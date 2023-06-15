import requests

endpoint = "http://127.0.0.1:8000/api/products/10/update/"

data = {
    "title": "A Brand New Updated Hello World",
    "price": 299.90
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())