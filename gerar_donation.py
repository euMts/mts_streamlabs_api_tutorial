import requests

url = "https://streamlabs.com/api/v1.0/donations"
parametros = {
    "name":"Segundo doador",
    "message":"Boa noite, novamente",
    "identifier":"Segundo_doador",
    "amount":"300.00",
    "currency":"BRL",
    "access_token":"SUA_ACCESS_TOKEN"
}

response = requests.post(url, data=parametros)

print(response.text)