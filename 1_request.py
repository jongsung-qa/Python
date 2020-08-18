import requests
res = requests.get("http://google.com")
#res = requests.get("http://nadocoding.tistory.com") # 403

res.raise_for_status()  


'''
confirm 1 
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)

confirm 2
print("response code : ", res.status_code)

confirm 3
res.text

confirm 4
 print("response code : ", res.status_code) # 200이면 정상
 if res.status_code == requests.codes.ok:
     print("ok")
 else:
     print("something wrong. [error code : ", res.status_code, "]")
'''
