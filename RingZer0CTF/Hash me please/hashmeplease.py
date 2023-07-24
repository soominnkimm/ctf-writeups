import hashlib
import requests
from bs4 import BeautifulSoup

s = requests.session()
site = s.get("http://challenges.ringzer0team.com:10013")
html = str(BeautifulSoup(site.text, "html.parser").div)
hash = html.split("\n")[2].replace("<br/>", " ").strip().encode('utf-8')
encrypted_hash = str(hashlib.sha512(hash).hexdigest())
flag = BeautifulSoup(s.post(f"http://challenges.ringzer0team.com:10013/?r={encrypted_hash}").text, "html.parser")
print(flag)
