import requests

# правильный запрос
job = {
    'team_leader': 1,
    'job': 'rfefeww',
    'collaborators': '1,2,3',
    'work_size': 23,
    'is_finished': False
}
print(requests.post('http://127.0.0.1:8080/api/jobs', json=job).json())

# запрос с не всеми ключами
job = {
    'team_leader': 1,
    'job': 'rfefew',
    'collaborators': '1,2,3',
    'is_finished': False
}
print(requests.post('http://127.0.0.1:8080/api/jobs', json=job).json())

# запрос с пустым объектом
job = {}
print(requests.post('http://127.0.0.1:8080/api/jobs', json=job).json())

# запрос с полями неправильного типа
job = {
    'team_leader': 'one',
    'job': 'rfefew',
    'collaborators': '1,2,3',
    'work_size': 23,
    'is_finished': 0
}
print(requests.post('http://127.0.0.1:8080/api/jobs', json=job).json())
