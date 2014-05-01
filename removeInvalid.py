import facebook
import re
from credentials_config import *
import requests
import json
import time

valid = re.compile("(Suche|Verschenke|SUCHE|VERSCHENKE)\s\(.*?\):.*")

print("Request...")
response = requests.request("GET","https://graph.facebook.com/v2.0/497830146989292/feed", timeout=5000, params={'access_token': access_token, "since": round(time.time())-400}).json()
print(response)
data = response['data']


for post in data:
    print("On:",post['message'])
    if not valid.match(post['message']):
        print("Invalid, trying to delete")
        requests.request("DELETE","https://graph.facebook.com/v2.0/" + post['id'], timeout=5000, params = {'access_token': access_token})
