import requests

# Удаление созданного питомца
res= requests.delete(f'https://petstore.swagger.io/v2/pet/{9223372036854775807}', headers={'accept': 'application/json'})
print(f'Статус кода: {res.status_code}\n')
print(res.json())