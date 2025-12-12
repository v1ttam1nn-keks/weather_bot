import os
from lxml import etree
from pathlib import Path
import requests, json
import time
from datetime import datetime, timezone
from fastkml import kml
import xml.etree.ElementTree as ET

API_key = "kIj535sb0zxhVA9FyFaefgNMAjw8qauP"



now_time = datetime.now(timezone.utc)
iso_time = now_time.isoformat()
split_date, split_time = iso_time.split(sep='T', maxsplit= -1)


#TEST_FUNC
#base_atl = api_request(55.749667, 37.578561)
#print(base_atl)

def api_request(coord_lat, coord_lon):
    cloud_base_today = 0.4
    return cloud_base_today


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
           




def parse_kml(kml_filename):
    tree = ET.parse(f"./{kml_filename}")
    root = tree.getroot()
    ns = {"kml": "http://www.opengis.net/kml/2.2"}
    coords_dict = {}
    for coords_tag in root.findall(".//kml:coordinates", ns):
        coords_text = coords_tag.text.strip()
        for coord_str in coords_text.split():
            lon, lat, *_ = coord_str.split(",")
            coords_dict[(float(lat), float(lon))] = {"cloud_height": 0.0}
    return coords_dict

def add_base_in_dict(kml_from_bot):
    base_alt_dict =parse_kml(kml_from_bot)     
    for coords in base_alt_dict:
        lat , lon = coords
        base_alt_dict[coords] = api_request(lat, lon)
    return(base_alt_dict)

print(add_base_in_dict('test.kml'))


    
        


    





#docks
#https://habr.com/ru/articles/960256/
#https://www.youtube.com/watch?v=rIhygmw9HZM
#https://ru.stackoverflow.com/questions/1395760/%D0%A0%D0%B0%D0%B7%D0%B4%D0%B5%D0%BB%D0%B8%D1%82%D1%8C-%D0%BA%D0%BE%D1%80%D1%82%D0%B5%D0%B6-%D0%BD%D0%B0-%D0%B4%D0%B2%D0%B5-%D1%87%D0%B0%D1%81%D1%82%D0%B8
#https://pythonworld.ru/tipy-dannyx-v-python/kortezhi-tuple.html