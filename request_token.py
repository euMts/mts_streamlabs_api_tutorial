import requests

url = "https://streamlabs.com/api/v1.0/token"

parametros = {
    "grant_type":"authorization_code",
    "client_id":"SEU_CLIENT_ID",
    "client_secret":"SEU_CLIENT_SECRET",
    "redirect_uri":"http://localhost:8080/auth",
    "code":"SEU_CODIGO"
}

response = requests.post(url, data=parametros)

print(response.text)