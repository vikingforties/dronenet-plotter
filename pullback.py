# https://lanched.ru/PortalGet/getPortals.php?
# offset=0&nelat=54.0&nelng=-1.73&swlat=53.8&swlng=-1.795
# 54 down to 53 and -1 to -2 - these slices remain constant
import requests
import json
import re
import time
from numpy import arange

nelat = 54.0  # ref
nelong = -2.8
swlat = 53.995  # ref
swlong = -3.0

request = 'https://lanched.ru/PortalGet/getPortals.php?offset=0&nelat=' + \
    str(nelat) + '&nelng=' + str(nelong) + '&swlat=' + str(swlat) + '&swlng=' + str(swlong)

for nelat in arange(53.000, 54.000, 0.005):
    swlat = nelat - 0.005
    request = 'https://lanched.ru/PortalGet/getPortals.php?offset=0&nelat=' + \
        str(nelat) + '&nelng=' + str(nelong) + '&swlat=' + str(swlat) + '&swlng=' + str(swlong)
    r = requests.get(request)
    with open('dump53to54_2to3.json', 'a') as dumpfile:
        dumpfile.write(r.text)
    print(str(nelat) + " to " + str(swlat))
    howmany = len(re.findall("guid", r.text))
    print(howmany)
    # print('##################' if howmany > 999)
    # print('kid' if age < 13
    time.sleep(5)
