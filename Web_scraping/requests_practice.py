import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(res.raise_for_status())
print(type(res))
print(res.status_code == 200)
print(res.text[:250])

