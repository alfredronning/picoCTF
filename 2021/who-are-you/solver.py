import requests

url = "http://mercury.picoctf.net:52362/"
headers = {
    "User-Agent": "PicoBrowser",
    "referer": url,
    "accept-datetime": "Thu, 31 May 2018 20:35:00 GMT",
    "date": "Thu, 31 May 2018 20:35:00 GMT",
    "dnt": "1",
    "Accept-Language": "en_SV",
    "origin": "sv.wikipedia.se",
    "host": "sv.wikipedia.se",
    "from": "example@mail.se",
    "via": "example@mail.se",
    "x-forwarded-for": "31.3.152.55",

}

reponse = requests.get(url, headers=headers)
print(reponse.text)
