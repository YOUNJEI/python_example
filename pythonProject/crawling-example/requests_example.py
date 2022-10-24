import requests

response = requests.get("https://www.naver.com")

print(response)
print(response.status_code)

#print(response.text)        # byte를 decode
#print(response.content)     # byte 그대로