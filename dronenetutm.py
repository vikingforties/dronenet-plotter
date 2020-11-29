# data from https://lanched.ru/PortalGet/
# eample call: https://lanched.ru/PortalGet/getPortals.php?offset=0&nelat=54.5&nelng=-1.75&swlat=53.8&swlng=-1.795
# city datafrom, https://simplemaps.com/data/gb-cities

import matplotlib.pyplot as plt
import json
import utm

# %matplotlib inline
with open('dump53to54_1to2.json', 'r') as portalfile:
    portals = portalfile.read()
portalobj = json.loads(portals)
# print(portalobj["portalData"])
x = list()
y = list()
# https://github.com/Turbo87/utm
for portal in portalobj['portalData']:
    u = utm.from_latlon(portal['lat'], portal['lng'])
    # returns Eastings and Northings plus zone
    y.append(u[1])
    # print(portal['lat'])
    x.append(u[0])
    # print(portal['lng'])

ax = plt.gca()
home = utm.from_latlon(53.8535112, -1.764305)
homeplate = plt.Circle((home[1], home[0]), radius=250, color="blue")

for i in range(len(x)):
    circle = plt.Circle((x[i], y[i]), radius=250, color="green")
    ax.add_patch(circle)

# ax.add_patch(homeplate)

plt.axis("scaled")
plt.show()
