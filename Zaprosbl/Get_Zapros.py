import requests

# Запрос списка доступных питомцев
status = 'available'
res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept': 'application/json'})
print(f'Статус кода: {res.status_code}\n')
print(res.text, '\n\n', '-' * 100)