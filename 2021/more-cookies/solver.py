import requests
import base64

url = "http://mercury.picoctf.net:56136"
session = requests.Session()
response = session.get(url)
cookie_val = session.cookies["auth_name"]
cookie_dec = base64.standard_b64decode(cookie_val)
cookie_dec = base64.standard_b64decode(cookie_dec)
cookies = {"auth_name": cookie_val}

def find_flag():
    for i in range(len(cookie_dec)):
        print(i)
        for j in range(8):
            mod_cookie = cookie_dec[:i] + (cookie_dec[i] ^ 1 << j).to_bytes(1, "big") + cookie_dec[i+1:]
            mod_cookie = base64.standard_b64encode(mod_cookie)
            cookies = {"auth_name": base64.standard_b64encode(mod_cookie).decode()}
            response = requests.get(url, cookies=cookies)
            if "picoCTF{" in response.text:
                return response.text

print(find_flag())

