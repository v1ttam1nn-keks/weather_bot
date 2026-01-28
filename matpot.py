import matplotlib.pyplot as plt
from weather import add_base_in_dict

dict = add_base_in_dict('test.kml')
coords = list(dict.keys())
clouds = list(dict.values())
x = range(len(coords))
y = clouds

plt.scatter(x, y, s=50)
plt.plot(x, y)
labels = [f"{lat:.4f}, {lon:.4f}" for lat, lon in coords]
plt.xticks(x, labels, rotation=45, ha='right')

plt.tight_layout()
plt.savefig("plot.png")


plt.savefig("plot.png") 



print(coords)
print(clouds)
