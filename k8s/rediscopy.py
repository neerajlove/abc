

import redis
import requests
import json

redis = redis.Redis(host='192.168.0.100', port=6379)


def get_github_profile(username):
    # Read from cache, otherwise fetch
    result = redis.get(username)

    if not result:
        fetch_github_profile(username)
    else:
        # Remember to convert to string, redis values are stored as bytes
        print(
            json.dumps({
                "cached": True,
                "profile": str(result)
            })
        )


def fetch_github_profile(username):
    # Get the result from Github and cache it
    result = requests.get("https://api.github.com/users/" + username)
   
    a = redis.set(username,  str(result.json()))
    print(a)
    print(
        json.dumps({
            "cached": True,
            "profile": result.json()
        })
    )

get_github_profile("neerajlove")
fetch_github_profile("neerajlove")




