import requests
import json

#This gives you back much data

url = 'http://inductor.eecs.umich.edu/miner'
payload = {'watts': {'$exists':True}}
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(payload), headers=headers)

print str(r.json())