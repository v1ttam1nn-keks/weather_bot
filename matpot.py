import matplotlib.pyplot as plt
from weather import add_base_in_dict

dict = add_base_in_dict('test.kml')

coords = list(dict.keys())
clouds = list(dict.values())

plt.plot(coords, clouds)
plt.savefig("plot.png")
print(coords)
print(clouds)
