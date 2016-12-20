import requests

url = 'http://requestb.in/ovvqlwov'
json = {
    'month': 'May',
    'result': '1:0',
    'team': 'Manchester',
}

response = requests.post(url, params=json)
print(response.status_code)

url2 = 'http://httpbin.org/'

params = {
    'id': [1, 2, 3],
}
response = requests.get(url2, params=params)
print(response)

