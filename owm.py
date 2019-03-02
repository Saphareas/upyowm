URL = "http://api.openweathermap.org/data/3.0/stations?appid="
API_KEY = "8ba12643391132924304024194d67a9a"
# "http://api.openweathermap.org/data/3.0/stations?appid=8ba12643391132924304024194d67a9a"

import ujson
payload = {
"external_id": "CB_TEST001",
"name": "Cottbus Test Station Indoor",
"latitude": 51.7563108,
"longitude": 14.3328679,
"altitude": 75
}
header = {"Content-Type": "application/json"}

import urequests
response = urequests.post("http://api.openweathermap.org/data/3.0/stations?appid=8ba12643391132924304024194d67a9a", json=payload, headers=header)
print(response.text)
