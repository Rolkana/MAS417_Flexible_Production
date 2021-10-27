from io import BytesIO

import numpy as np
import requests
from PIL import Image



# This is directly the API call used by Geonorge here:
# https://kartkatalog.geonorge.no/kart?lat=6882011.719407242&lon=68429.52888256384&zoom=8.589318931685455
# .. when adding the "Digital overflatemodell WMS layer".
# For use in an application, please see requests user manual: https://docs.python-requests.org/en/latest/
# See the following examples on how to handle http request parameters / payload and so on:
# https://docs.python-requests.org/en/latest/user/quickstart/#passing-parameters-in-urls
request_url = 'https://wms.geonorge.no/skwms1/wms.hoyde-dom?' \
           'SERVICE=WMS&' \
           'VERSION=1.3.0&' \
           'REQUEST=GetMap&' \
           'FORMAT=image/png&' \
           'TRANSPARENT=false&' \
           'LAYERS=DOM:None&' \
           'CRS=EPSG:25833&' \
           'STYLES=&' \
           'WIDTH=1751&' \
           'HEIGHT=1241&' \
           'BBOX=-19.999984,56.619084,49.999977,81.181719'
response = requests.get(request_url, verify=True)  # SSL Cert verification explicitly enabled. (This is also default.)
print(f"HTTP response status code = {response.status_code}")
print(response)

img = Image.open(BytesIO(response.content))
np_img = np.asarray(img)
# Could do something with numpy here.
img = Image.fromarray(np.uint8(np_img))
# show image
img.show()
