import requests
import json
import redis
import csv


jadu = redis.Redis(host='192.168.0.107', port=6379)
results = requests.get("https://api.github.com/users/neerajlove")
array = [ ]
a = (results.text)
data = json.loads(a)

print(type(data))
for login in a.[data]:
print(login)

  

'''
def get_data_from("username"):
    a = requests.get("https://api.github.com/users/" + username)
    print {
        json.dumps{{
            "cached" : False,
            "profile": result.json()
        }}
    }
    
get_data_from_git("neeraj")
'''