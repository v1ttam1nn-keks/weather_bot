from kml import Kml_Parser
from alg import GetCloudBase
from api import Api_requests
import os
from dotenv import load_dotenv
load_dotenv('.env')
yandex_key = os.getenv("yandex_key")

class Dispatcher:
    def __init__(self):
        pass
    def create_parce_kml(self, kml_path: str) -> dict:
        k = Kml_Parser()
        kml_dict = k.parce(kml_path)
        return kml_dict
    def from_epsi(self, kml_origin_dict):                
        api = Api_requests(yandex_key)
        cloud_alg = GetCloudBase()        
        print(kml_origin_dict)
        for coords in kml_origin_dict:            
            lat, lon = coords           
            ya_response = api.yandex_req(lat, lon)                        
            T = api.yandex_fact_temp(ya_response)
            RH = api.yandex_fact_humidity(ya_response)            
            h_cloud = cloud_alg.formula_epsi(RH, T)
            cloudness = api.yandex_fact_cloudness(ya_response)
            kml_origin_dict[coords]["cloud_height"] = h_cloud
            kml_origin_dict[coords]["cloudness"] = cloudness       
        return kml_origin_dict     
    
        







