import math

def epsi(RH, T): 
    #Формула для расчета температуры точки росы
    T_d = T - (100 - RH)/5
    #print(T_d)
    #ФОРМУЛА ЭПСИ
    H_cloud = 122 * (T - T_d)
    print(H_cloud)

P = 745 
T = -11
RH = 83

def from_mm_to_Gpa(P): 
    Gpa = P * 1.333
    #print(Gpa)
    return Gpa
    

Gpa = from_mm_to_Gpa(P)

def claus(RH,T,Gpa):
    eT=6.112 * math.exp((17.67*T) / (T+243.5))
    e = (RH/100) * eT
    
print(epsi(84, 35))
    

#Формула Ипполитова






claus(0,0,Gpa)
        
 
    
