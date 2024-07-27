import requests

url = "https://graph.facebook.com/v20.0/404351599425986/messages"
headers = {
    "Authorization": "Bearer EAAL94kJVcC4BOZBxxajbZAT9Ijab3MIggc5c3F3hVrnXaZBMOLZAlTFZCQhsMUwF5KHMK5CXl0ZBprNVi6VsZCrH0eafmfmqrACU45Y7yRQdB6GVr3LcRDJc0wBPV2VHewZCqIJUbxPigw1s41gbUgjBJWIHZAnxeOjoJpDISKr9pdkQZBBpMaqRSIBzoBFnLXa01X7f1ZBSZAQAYVN9dktXxDmuDy98IB0ZD",
    "Content-Type": "application/json"
}
data = {
    "messaging_product": "whatsapp",
    "to": "4184159383",  # Insira o número de telefone do destinatário aqui
    "type": "template",
    "template": {
        "name": "promo",
        "language": {
            "code": "en"
        }
    }
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
