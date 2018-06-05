#!/usr/bin/env python
import sys
import json
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth('root', 'D_Vay!_10&')
    headers = {'Accept': 'application/vnd.yang.data+json',
    'Content-Type': 'application/vnd.yang.data+json'
    }
url = 'https://ios-xe-mgmt.cisco.com:9443/restconf/api/config/native?deep'
response = requests.get(url, headers=headers, auth=auth)

response = json.loads(response.text)
json_response = json.dumps(response, indent=4)

with open('Git\\Projects\\Project_Restconf\\Outputs\\config.txt', 'w') as f:
    for capability in json_response:
        f.write(str(capability))