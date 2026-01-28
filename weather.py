import os
from lxml import etree
from pathlib import Path
import requests, json
import time
from datetime import datetime, timezone
from fastkml import kml
import xml.etree.ElementTree as ET



yandex_key = 'asd'

def epsi(RH, T): 
    b = 237.7 
    a = 17.27
    RH = RH / 100 
    fun = (a * T) / (b * T) + math.log(RH) 
    Tp = (b * fun) / (a - fun)  
    print(Tp)
    H_cloud = 208 * (T - Tp)
    return H_cloud

epsi(75, -19)


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

