#!/usr/bin/env python3

# Filename:                     restconf.py
# Command to run the program:   python3 restconf.py

import requests
import json

# Suppress HTTPS warnings
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Print a stream of bytes as pretty JSON
def printBytesAsJSON(bytes):
	print(json.dumps(json.loads(bytes), indent=2))

# Print a CaseInsensitiveDict as pretty JSON
def printDictAsJSON(cidict):
	print(json.dumps(dict(cidict), indent=2))


# Task example 1 - OPTIONS
response_opt = requests.options(
	url = 'https://192.168.56.101:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity',
	auth = ('cisco', 'cisco123!'),
	headers = {
		'Accept': 'application/yang-data+json'
	},
	verify = False)

# Pretty print our JSON response
print('Response Code for example 1 - OPTIONS: ' + str(response_opt.status_code))


# Task example 2 - POST
response_post = requests.post(
	url = 'https://192.168.56.101:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor',
	auth = ('cisco', 'cisco123!'),
	headers = {
		'Accept': 'application/yang-data+json',
		'Content-Type': 'application/yang-data+json'
	},
	data = json.dumps({
		"severity": "alerts"
	}),
	verify = False)

# Print the HTTP response code
print('Response Code for example 2 - POST: ' + str(response_post.status_code))


# Task example 3 - PUT
response_put = requests.put(
	url = 'https://192.168.56.101:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity',
	auth = ('cisco', 'cisco123!'),
	headers = {
		'Accept': 'application/yang-data+json',
		'Content-Type': 'application/yang-data+json'
	},
	data = json.dumps({
		"severity": "warnings"
	}),
	verify = False)

# Print the HTTP response code
print('Response Code for example 3 - PUT: ' + str(response_put.status_code))


# Task example 4 - PATCH
response_patch = requests.patch(
	url = 'https://192.168.56.101:443/restconf/data/Cisco-IOS-XE-native:native',
	auth = ('cisco', 'cisco123!'),
	headers = {
		'Accept': 'application/yang-data+json',
		'Content-Type': 'application/yang-data+json'
	},
	data = json.dumps({
		"native": {
			"logging": {
				"monitor": {
					"severity": "informational"
				}
			}
		}	
	}),
	verify = False)

# Print the HTTP response code
print('Response Code for example 4 - PATCH: ' + str(response_patch.status_code))


# Task example 5 - 
response_get = requests.get(
	url = 'https://192.168.56.101:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity',
	auth = ('cisco', 'cisco123!'),
	headers = {
		'Accept': 'application/yang-data+json',
		'Content-Type': 'application/yang-data+json'
	},
	verify = False)

# Print the HTTP response code
print('Response Code for example 5 - GET: ' + str(response_get.status_code))


# Task example 6 - 
response_delete = requests.delete(
	url = 'https://192.168.56.101:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity',
	auth = ('cisco', 'cisco123!'),
	headers = {
		'Accept': 'application/yang-data+json',
		'Content-Type': 'application/yang-data+json'
	},
	verify = False)

# Print the HTTP response code
print('Response Code for example 6 - DELETE: ' + str(response_delete.status_code))

# Print other info
print('Header for example 1 (but the same for all the other):')
printDictAsJSON(response_opt.headers)
print('Content for example 5 (the only one to have it):')
printBytesAsJSON(response_get.content)