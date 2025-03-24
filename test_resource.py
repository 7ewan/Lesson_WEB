import requests

# right request get
print(requests.get('http://127.0.0.1:8080/api/v2/users/1').json())

# bad request get
print(requests.get('http://127.0.0.1:8080/api/v2/users/10').json())

# right request delete
print(requests.delete('http://127.0.0.1:8080/api/v2/users/1').json())

# bad request delete
print(requests.delete('http://127.0.0.1:8080/api/v2/users/10').json())

# right request get
print(requests.get('http://127.0.0.1:8080/api/v2/users').json())

# right request post
user = {
    'surname': 'Lox',
    'name': 'Luter',
    'age': 23,
    'position': 'lox',
    'speciality': 'loshara',
    'address': 'Moskovskya1',
    'email': 'lox@mail.ru',
    'hashed_password': '12325553243'
}
print(requests.post('http://127.0.0.1:8080/api/v2/users', json=user).json())

# bad request post
user = {
    'surname': 'Lox',
    'name': 'Luter',
    'age': 23,
    'position': 'lox',
    'speciality': 'loshara',
    'address': 'Moskovskya1',
    'hashed_password': '12325553243'
}
print(requests.post('http://127.0.0.1:8080/api/v2/users', json=user).json())
