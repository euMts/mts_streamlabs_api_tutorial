import requests

url = "https://streamlabs.com/api/v1.0/user"
parametros = {
    "access_token":"SUA_ACCESS_TOKEN"
}

response = requests.get(url, params=parametros)

print(response.text)