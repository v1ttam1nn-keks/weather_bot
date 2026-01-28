from alg import GetCloudBase
from kml import Kml_Parser
class CreateFullDict:
    def full_dict_from(self, kml_dict, kml_path):
        kml_class = Kml_Parser()
        kml_dict = kml_class.parce
        base_alt_dict = kml_dict(kml_path)
        if base_alt_dict is False:
            return False
        for coords in base_alt_dict:
            lat, lon = coords








def add_base_in_dict(kml_from_bot):
    base_alt_dict =parse_kml(kml_from_bot)
    if base_alt_dict is False:
        return False
    
    for coords in base_alt_dict:
        lat , lon = coords

        base_alt_dict[coords] = api_request_yandex(lat, lon)
    #print(base_alt_dict)
    return(base_alt_dict)