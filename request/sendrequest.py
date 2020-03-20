import requests
import json

url = "http://localhost:3000/api/courses/1"
print("GET",url)
print(requests.get(url).text)
print("*************************\n")

headers = {'Context-Type':'application/json'}
url = "http://localhost:3000/api/courses"
obj={"name":"newcourse"}
p=json.dumps(obj,ensure_ascii=True,indent=None, separators=None, default=str)

print("POST",obj)
r = requests.post(url,data=p.encode('utf8'),headers=headers)
# r = requests.post(url,data=p.encode('utf8'),headers=headers)

print(r.text)
