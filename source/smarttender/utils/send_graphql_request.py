import json

import requests
import urllib3

from app.settings import AUTH_TOKEN, GRAPHQL_URL


def send_graphql_request(query):
    headers = {
        'Authorization': f'Bearer {AUTH_TOKEN}',
        'Content-Type': 'application/json'
    }
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    try:
        response = requests.post(GRAPHQL_URL, json={'query': query}, headers=headers, verify=False)
        response.raise_for_status()
        return response.json().get('data')
    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        return None
