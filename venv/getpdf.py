import csv
import re
import requests
import fileinput
import io
import shutil
import time



serialnum="88710830"
serialnumtwo = "88710831"
#88818671
#87003370

aaa="asdasd email 3243324"
sp = aaa.split("email")
print (sp[1])


#url="https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn="+serialnum+","+serialnumtwo+"&type=FTK"
url="https://tsdrapi.uspto.gov/ts/cd/casedocs/bundle.pdf?sn=88710339&type=OOA"
print(url)
payload = {}
headers = {
    'USPTO-API-KEY': 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCIsIng1dCI6Inp2UGxaU0dkVnBRdWRYc3JMcGR1c1Vfc05wayIsImtpZCI6Im9yYWtleSJ9.eyJzdWIiOiJtZWxhbmllX2VsYW5hQHlhaG9vLmNvbSIsIm9yYWNsZS5vYXV0aC51c2VyX29yaWdpbl9pZF90eXBlIjoiTERBUF9VSUQiLCJvcmFjbGUub2F1dGgudXNlcl9vcmlnaW5faWQiOiJtZWxhbmllX2VsYW5hQHlhaG9vLmNvbSIsImlzcyI6Ind3dy5vcmFjbGUuZXhhbXBsZS5jb20iLCJvcmFjbGUub2F1dGguc3ZjX3BfbiI6Ik9BdXRoU2VydmljZVByb2ZpbGUiLCJpYXQiOjE1OTEzNjIzOTcsIm9yYWNsZS5vYXV0aC5wcm4uaWRfdHlwZSI6IkxEQVBfVUlEIiwib3JhY2xlLm9hdXRoLnRrX2NvbnRleHQiOiJyZXNvdXJjZV9hY2Nlc3NfdGsiLCJleHAiOjE2MDY5MTQzOTcsInBybiI6Im1lbGFuaWVfZWxhbmFAeWFob28uY29tIiwianRpIjoiY2YzZTE5ZmMtNGVlNC00ODI4LTk3OWItZWFhMTgxZjE4NzRmIiwib3JhY2xlLm9hdXRoLmNsaWVudF9vcmlnaW5faWQiOiJSQkFDU2VydmljZXNPQXV0aEFQSUtleUNsaWVudCIsIm9yYWNsZS5vYXV0aC5zY29wZSI6IlRTRFJBUEkuUkVBRCIsInVzZXIudGVuYW50Lm5hbWUiOiJEZWZhdWx0RG9tYWluIiwib3JhY2xlLm9hdXRoLmlkX2RfaWQiOiIxMjM0NTY3OC0xMjM0LTEyMzQtMTIzNC0xMjM0NTY3ODkwMTIifQ.KesnbgQn_VzLhoCBk8KFbZ5YFUfCffBjqPOoxyrtRFMwrwbKo2x8Bopa5-gQJY6Ar8Z57gikkxzHAk2YkJnVKw71x9p8Q0FrVh2_hDt-ThBmMELVj2d2egZ2i3r6aShzv0iJv6WX1lMtANUNQSYnPwCGa8bMZr-Wm6sp866U0OM',
    'Cookie': 'StackCookie='}

r = requests.request("GET", url, headers=headers, data=payload)

print (r.content)

time.sleep(3)

with open('temp.pdf', 'wb') as f:
    f.write(r.content)
