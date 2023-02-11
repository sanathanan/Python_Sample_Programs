"""
Keys having multiple inputs
"""
# Example 1
print("------Method 1 ---------")

dict_1 = {}

x, y, z = 10, 20, 30
dict_1[x, y, z] = x + y - z;

x, y, z = 5, 2, 4
dict_1[x, y, z] = x + y - z;

print(dict_1)

# Example 2
print("----------Method 2 ----------")
places = {("19.07'53.2", "72.54'51.0"):"Mumbai", ("28.33'34.1", "77.06'16.6"):"Delhi"}

lat = []
longitude = []
plac = []
for i in places:
    lat.append(i[0])
    longitude.append(i[1])
    plac.append(places[i])
print(lat)
print(longitude)
print(plac)
