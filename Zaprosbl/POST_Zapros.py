import requests

# Создание нового питомца
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
data = {"id": 9223372036854775807, "category": {"id": 0, "name": "string"},
        "name": "BOB", "photoUrls": ["string"], "tags": [{"id": 0, "name": "string"}],
        "status": "available"}
res = requests.post('https://petstore.swagger.io/v2/pet', headers=headers, json=data)
print(f'Статус кода: {res.status_code}\n')
print(res.json(), '\n\n', '-' * 100)

# res = requests.post(url, headers=headers, data=data) - шаблон строки POST запроса 
# data — это данные, отправляемые на сервер в теле запроса. Передаются в формате словаря data = {‘key1’: ‘value1’, ‘key2’: ‘value2’}