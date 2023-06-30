import requests

# Изменение данных о питомце
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
data = {"id": 9223372036854775807, "category": {"id": 0, "name": "string"}, "name": "Jonatan",
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}], "status": "available"}
res = requests.put('https://petstore.swagger.io/v2/pet', headers=headers, json=data)
print(f'Статус кода: {res.status_code}\n')
print(res.json(), '\n\n', '-' * 100)

