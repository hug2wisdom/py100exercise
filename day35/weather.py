import requests

MY_APPKEY = "DNG3NUM6NUMT"
DAYS = 7


class Weather:
    def __init__(self, location_input):
        self.location_input = location_input
        self.code = self.get_location()

    def get_location(self):
        url = "https://api.gugudata.com/weather/weatherinfo/region"
        para = {
            "appkey": MY_APPKEY,
            "keyword": self.location_input,
        }
        response = requests.get(url=url, params=para)
        response.raise_for_status()
        data = response.json()
        code = data["Data"][0]["Code"]
        return code

    def get_weather(self):
        url = "https://api.gugudata.com/weather/weatherinfo"
        para = {
            "appkey": MY_APPKEY,
            "code": self.code,
            "days": DAYS,
        }
        response = requests.get(url=url, params=para)
        response.raise_for_status()
        data = response.json()
        weather_list = []
        for index in range(0, 7):
            info = data["Data"][index]["WeatherInfo"]
            temperature_high = data["Data"][index]["TemperatureHigh"]
            temperature_low = data["Data"][index]["TemperatureLow"]
            weather = {
                "date": data["Data"][index]["WeatherDate"],
                "weather_info": f"天气是:{info}, 最高温是: {temperature_high}, 最低温是: {temperature_low}",
            }
            weather_list.append(weather)
        return weather_list
