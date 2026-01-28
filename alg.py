import math

class GetCloudBase:
    def formula_epsi(self, RH : int, T: int) -> int:
        b = 237.7 
        a = 17.27
        RH = RH / 100 
        fun = (a * T) / (b * T) + math.log(RH) 
        Tp = (b * fun) / (a - fun) 
        H_cloud = 208 * (T - Tp)
        return H_cloud
    def from_windy_api(self):
        pass    
