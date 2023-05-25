import requests, json
from config import name, API_KEY, CLIENT_ID, METAL_APP_ID, index


headers = {
        "Content-Type": "application/json",
        "x-metal-api-key": API_KEY,
        "x-metal-client-id": CLIENT_ID,
    }


def index_with_text(id : str, text: str, metadata: dict):
    url = "https://api.getmetal.io/v1/index"
    
    data = {
        "index": METAL_APP_ID,
        "text": text,
        "id": id,
        "metadata": metadata
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    print(f"Data created, status: {response.status_code}")
    print(response.json())

def search_with_text(text: str, filters: list):
    url = "https://api.getmetal.io/v1/search"

    data = {
        "index": METAL_APP_ID,
        "text": text,
        "filters": filters
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    data = response.json()
    data = data['data']

    print(f"Search results ({len(data)}), status: {response.status_code}")
    print(data)

def tune_with_payload(idA: str, idB: str, label: str):
    url = "https://api.getmetal.io/v1/tune"

    data = {
        "index": METAL_APP_ID,
        "idA": idA,
        "idB": idB,
        "label": label
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    print(f"Tune results, status: {response.status_code}")
    print(response.json())

def create_index():
    url = "https://api.getmetal.io/v1/apps/{index}/indexes"

    data = {
        "model": "text-embedding-ada-002",
        "name": "Metal Collection",
        "dimensions": 600,
        "filters": [
            {
                "field": "genre",
                "type": "string"
            },
            {
                "field": "formed",
                "type": "number"
            },
            {
                "field": "origin",
                "type": "string"
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    print(f"create_index results, status: {response.status_code}")
    print(response.json())

def get_index():
    url = f"https://api.getmetal.io/v1/indexes"

    response = requests.get(url, headers=headers)

    print(f"Get index, status: {response.status_code}")
    print(response.json())


def delete_with_payload(indexId):

    url = f"https://api.getmetal.io/v1/indexes/{indexId}"

    response = requests.delete(url, headers=headers)

    print(f"Get index, status: {response.status_code}")
    print(response.json())

