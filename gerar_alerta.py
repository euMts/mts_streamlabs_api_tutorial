import requests

url = "https://streamlabs.com/api/v1.0/alerts"

parametros = {
    "access_token":"SUA_ACCESS_TOKEN",
    "type":"follow",
    "message":"tenham uma boa noite!",
    "name":"seguidor"
}

response = requests.post(url, data=parametros)

print(response.text)