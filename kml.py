import xml.etree.ElementTree as ET
from lxml import etree



class Kml_Parser:
    def parce(self, kml_filename: str) -> dict:
        tree = ET.parse(kml_filename)
        root = tree.getroot()
        
        ns = {"kml": "http://www.opengis.net/kml/2.2"}
        all_coords = []
        
        for coords_tag in root.findall(".//kml:coordinates", ns):
            coords_text = coords_tag.text.strip()
            for coord_str in coords_text.split():
                lon, lat, *_ = coord_str.split(",")
                all_coords.append((float(lat), float(lon)))
        
        total_coords = len(all_coords)
        
        if total_coords > 15000:
            return False
        
        step = self.calic_step(total_coords)
        
        coords_dict = {}
        for i in range(0, total_coords, step):
            coords_dict[all_coords[i]] = {"cloud_height": 0.0}

        return coords_dict


    def calic_step(self, total: int) -> int:
        
        if 5001 <= total <= 15000:
            step = 300
        elif 2501 <= total <= 5000:
            step = 200
        elif 1001 <= total <= 2500:
            step = 100
        elif 101 <= total <= 500:
            return 20
        return 1

