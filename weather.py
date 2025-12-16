import os
from lxml import etree
from pathlib import Path
import requests, json
import time
from datetime import datetime, timezone
from fastkml import kml
import xml.etree.ElementTree as ET
import math


#API_key = "kIj535sb0zxhVA9FyFaefgNMAjw8qauP"
yandex_key = '4bbcdbc3-5885-44e3-8fda-b87c968678d5'


#now_time = datetime.now(timezone.utc)
#iso_time = now_time.isoformat()
#split_date, split_time = iso_time.split(sep='T', maxsplit= -1)
#
#
#in_date = 2025-12-22



#TEST_FUNC
#base_atl = api_request(55.749667, 37.578561)
#print(base_atl)

#def api_request(coord_lat, coord_lon):
#    cloud_base_today = 0.4
#    return cloud_base_today

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
    #print(fact_cloudness, fact_temp, fact_condition, fact_pressure_pa,fact_cloudness, fact_prec_type)
    #data = {
    #    "temp": fact["temp"],
    #    "humidity": fact["humidity"],
    #    "pressure_pa": fact["pressure_pa"],
    #    "cloudness": fact["cloudness"],
    #    "prec_type": fact["prec_type"],
    #    "condition": fact["condition"]
    #}
    #print(fact_temp)
    print(json_parse)
    #print(fact_humidity)
    return epsi(fact_humidity, fact_temp)

#api_request_yandex(55.727199, 37.575815)


def epsi(RH, T): 
    #print(RH)
    #print(T)
    T_d = T - (100 - RH)/5
    H_cloud = 122 * (T - T_d)
    return H_cloud
#cloud_base = epsi(RH, T)
#print(cloud_base)




#Функция для api запроса. Возращает значение cloudBase на coord_lat coord_lon
#def api_request(coord_lat, coord_lon):
#    r = requests.get(f'https://api.tomorrow.io/v4/weather/forecast?location={coord_lat},{coord_lon}&apikey={API_key}')
#    _clean_requests_data = r.json()
#    _JSON_DATA = json.dumps(_clean_requests_data, indent= 4, sort_keys = False, ensure_ascii=False)
#    data_str = json.dumps(_clean_requests_data, indent = 2)
#    data_dict = json.loads(data_str)
#    data_list = (data_dict['timelines']['minutely'])
#    for item in data_list:
#        if split_date in item['time']:
#            cloud_base_today = (item['values']['cloudBase'])
#            return cloud_base_today
#            break 

#def parse_kml(kml_filename):
#    tree = ET.parse(f"./{kml_filename}")
#    root = tree.getroot()
#    ns = {"kml": "http://www.opengis.net/kml/2.2"}
#    coords_dict = {}
#    for coords_tag in root.findall(".//kml:coordinates", ns):
#        coords_text = coords_tag.text.strip()
#        for coord_str in coords_text.split():
#            lon, lat, *_ = coord_str.split(",")
#            coords_dict[(float(lat), float(lon))] = {"cloud_height": 0.0}
#    a = len(coords_dict)
#    print(a)
#    if a > 100:
#        return False
#    else:
#        return coords_dict
def parse_kml(kml_filename):
    

    # Парсим KML
    tree = ET.parse(f"./{kml_filename}")
    root = tree.getroot()
    ns = {"kml": "http://www.opengis.net/kml/2.2"}
    # Собираем все координаты в список
    all_coords = []
    for coords_tag in root.findall(".//kml:coordinates", ns):
        coords_text = coords_tag.text.strip()
        for coord_str in coords_text.split():
            lon, lat, *_ = coord_str.split(",")
            all_coords.append((float(lat), float(lon)))

    total_coords = len(all_coords)
    print(f"Всего координат: {total_coords}")

    # Определяем шаг отбора
    if total_coords > 15000:
        return False
    elif 5001 <= total_coords <= 15000:
        step = 300
    elif 2501 <= total_coords <= 5000:
        step = 200
    elif 1001 <= total_coords <= 2500:
        step = 100
    elif 101 <= total_coords <= 500:
        step = 20
    else:  # 0-100 точек
        step = 1

    # Создаем словарь с нужными координатами
    coords_dict = {}
    for i in range(0, total_coords, step):
        coords_dict[all_coords[i]] = {"cloud_height": 0.0}

    print(f"Количество координат после фильтрации: {len(coords_dict)}")
    return coords_dict   


def add_base_in_dict(kml_from_bot):
    base_alt_dict =parse_kml(kml_from_bot)
    if base_alt_dict is False:
        return False
    
    for coords in base_alt_dict:
        lat , lon = coords
        base_alt_dict[coords] = api_request_yandex(lat, lon)
    #print(base_alt_dict)
    return(base_alt_dict)
    

#print(add_base_in_dict('gerber_first_track.kml'))

#docks
#https://habr.com/ru/articles/960256/
#https://www.youtube.com/watch?v=rIhygmw9HZM
#https://ru.stackoverflow.com/questions/1395760/%D0%A0%D0%B0%D0%B7%D0%B4%D0%B5%D0%BB%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D1%80%D1%82%D0%B5%D0%B6-%D0%BD%D0%B0-%D0%B4%D0%B2%D0%B5-%D1%87%D0%B0%D1%81%D1%82%D0%B8
#https://pythonworld.ru/tipy-dannyx-v-python/kortezhi-tuple.html