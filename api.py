import requests, json

class Api_requests:
    def __init__(self, yandex_key=None, windy_key=None):
        self.yandex_key = yandex_key
        self.windy_key = windy_key

    def yandex_req(self, lat, lon):
        headers = {
            'X-Yandex-Weather-Key': self.yandex_key
        }
        response = requests.get(
            'https://api.weather.yandex.ru/v2/forecast',
            params={'lat': lat, 'lon': lon},
            headers=headers
        )
        return response.json() ##dict 
    def yandex_fact_temp(self, ya_responce: dict) -> float:
        fact = ya_responce["fact"]
        fact_temp = fact['temp']
        return fact_temp
    def yandex_fact_humidity(self, ya_responce: dict) -> int:
        fact = ya_responce["fact"]
        fact_humidity = fact['humidity']
        return fact_humidity        
    def yandex_fact_condition(self, ya_responce: dict) -> int:
        fact = ya_responce["fact"]
        fact_condition = fact['condition']
        return fact_condition   
    def yandex_fact_cloudness(self, ya_responce: dict) -> float:
        fact = ya_responce["fact"]
        fact_cloudness = fact['cloudness']
        return fact_cloudness

