import requests
import json

# requests for the repo (use big repo to see the effect)
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

# json to dic is automatically converted 
details = response.json()

for i in range (len(details)):
    print(details[i]["user"]["login"])