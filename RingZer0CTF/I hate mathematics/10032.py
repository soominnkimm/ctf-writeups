from bs4 import BeautifulSoup
import requests

s = requests.session()
site = s.get("http://challenges.ringzer0team.com:10032/")
html = str(BeautifulSoup(site.text, "html.parser"))
ques = str(html.split("\n")[42].replace("<br/>", " ").strip())
first_val = int(ques[0:4])
second_val = int(ques[ques.index("+ ")+len("+ "):ques.index(" -")], 16)
third_val = int(ques[ques.index("- ")+len("- "):ques.index(" =")], 2)
ans = first_val + second_val - third_val
flag = BeautifulSoup(s.get(f"http://challenges.ringzer0team.com:10032/?r={ans}").text, "html.parser")
print(flag)
