import requests
import json

url = "https://streamlabs.com/api/v1.0/donations"
parametros = {
    "access_token":"SUA_ACCESS_TOKEN"
}

response = requests.get(url, params=parametros)

obj = response.json()

print(json.dumps(obj, indent=4))
