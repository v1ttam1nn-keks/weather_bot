import math
from api import Api_requests


class GetCloudBase:
    def formula_epsi(self, RH : int, T: int) -> int:
        b_const = 237.7 
        a_const = 17.27
        RH = RH / 100 
        fun = (a_const * T) / (b_const + T) + math.log(RH)
        Tp = (b_const * fun) / (a_const - fun)
        H_cloud = 125 * (T - Tp) 
        return H_cloud
    def from_windy_api(self):
        pass
        
