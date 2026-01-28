from alg import Alg

class Request:
    def yandex_req(self, lat, lon):
        headers = {
        'X-Yandex-Weather-Key': yandex_key
    }
    response = requests.get(f'https://api.weather.yandex.ru/v2/forecast?lat={coord_lat}&lon={coord_lon}', headers=headers)
    #print(response.json())
    _clean_requests_data = response.json() #dict
    json_parse = json.dumps(_clean_requests_data, indent=4, sort_keys = False, ensure_ascii=False)
    fact = _clean_requests_data["fact"]
    fact_pressure_pa = fact['pressure_pa']
    fact_temp = fact['temp']
    fact_condition = fact['condition']
    fact_prec_type = fact['prec_type'] # #0 — без осадков. 1 — дождь.2 — дождь со снегом.3 — снег.4 — град.
    fact_cloudness = fact['cloudness'] #0 — ясно 0.25 — малооблачно.0.5 — облачно с прояснениями.0.75 — облачно с прояснениями 1 — пасмурно.
    fact_humidity = fact['humidity']
    h_cloud = Alg()
    return h_cloud.epsi( fact_humidity : int, fact_temp: int):

















def api_request_yandex(coord_lat, coord_lon):
    headers = {
        'X-Yandex-Weather-Key': yandex_key
    }
    response = requests.get(f'https://api.weather.yandex.ru/v2/forecast?lat={coord_lat}&lon={coord_lon}', headers=headers)
    #print(response.json())
    _clean_requests_data = response.json() #dict
    json_parse = json.dumps(_clean_requests_data, indent=4, sort_keys = False, ensure_ascii=False)
    fact = _clean_requests_data["fact"]
    fact_pressure_pa = fact['pressure_pa']
    fact_temp = fact['temp']
    fact_condition = fact['condition']
    fact_prec_type = fact['prec_type'] # #0 — без осадков. 1 — дождь.2 — дождь со снегом.3 — снег.4 — град.
    fact_cloudness = fact['cloudness'] #0 — ясно 0.25 — малооблачно.0.5 — облачно с прояснениями.0.75 — облачно с прояснениями 1 — пасмурно.
    fact_humidity = fact['humidity']
    #print(fact_humidity, fact_temp)
    h_cloud = epsi(fact_humidity, fact_temp)
    print(h_cloud) 
    return h_cloud