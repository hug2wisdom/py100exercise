import requests

MY_LAT = 119.029109
MY_LNG = 33.501443

parameter = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 1,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
result = data["results"]
sunrise = result["sunrise"]
sunset = result["sunset"]
print(sunrise, sunset)