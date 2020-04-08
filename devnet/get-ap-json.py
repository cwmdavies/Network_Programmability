#!/usr/bin/env python3

from urllib.request import Request, urlopen
import ssl, json
ssl._create_default_https_context = ssl._create_unverified_context
req = Request('https://cmxlocationsandbox.cisco.com/api/config/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc=')
response = urlopen(req)
response_string = response.read().decode('utf-8')
# print(response_string)

json_object = json.loads(response_string)

access_points = json_object['accessPoints']

for ap in access_points:
 print('Access Point: ' + ap['name'] + '\t mac: ' + ap['radioMacAddress'])

response.close()

json_object = json.loads(response_string)
# print(json.dumps(json_object, sort_keys=True, indent=4))