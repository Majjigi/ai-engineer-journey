import requests
import json


# r = requests.get('https://api.github.com/events')
# data = r.json()

# print(json.dumps(data, indent=2));


#Task 1

r2 = requests.get('https://api.github.com/users/Majjigi/repos')
repoResponse = r2.json()

if len(repoResponse) > 0:
    for repo in repoResponse:
        print(f"Repository: {repo['name']}" + f"Language: {repo['language']}")
       
