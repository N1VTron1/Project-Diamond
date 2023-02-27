import socket,ssl
import urllib.parse, urllib.request
import json
import sys, os
import requests
import uuid
import datetime
from datetime import datetime

url = ("https://jsonplaceholder.typicode.com")
param = ("/posts/1/comments")
fullURL = url+param

"""
Description: Starting the connection between App1 and App2
Throws: Exception e
Returns: Secure transfer protocol
"""


def start_connection():
	activity_definition = "App1: Established connection to App 2"
	pass_activity = "true"
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ssl_sock = ssl.wrap_socket(s,
			ca_certs="server.crt",
			cert_reqs = ssl.CERT_REQUIRED)
		ssl_sock.connect(('localhost',8080))
		post_log(activity_definition, pass_activity)
	except:
		e = sys.exc_info()[0]
		print(e)
		pass_activity = "false"
		post_log(activity_definition, pass_activity)
	return ssl_sock

"""
Description: Retrieves JSON payload from the internet
Parameters: fullURL - the full URL of the JSON payload from the internet
Return: a JSON payload received from the web page
Throws: Exception e
"""


def get_payload(fullURL):
	activity_definition = "App1: Retrieved a JSON payload data from the Internet"
	pass_activity = "true"
	try:
		response = urllib.request.urlopen(fullURL)
		payload = response.read()
		post_log(activity_definition, pass_activity)
	except:
		e = sys.exc_info()[0]
		print(e)
		pass_activity = "false"
		post_log(activity_definition, pass_activity)
	return payload

"""
Description: Decodes the payload using UTF-8
Parameters: payload - a payload gathered with get_payload method
Return: payloadDecoded - the decoded payload
Throws: Exception e
"""


def decode_payload(payload):
	activity_definition = "App1: Decoded JSON payload using utf-8"
	pass_activity = "true"
	try:
		payloadDecoded = json.loads(payload.decode('utf-8'))
		post_log(activity_definition, pass_activity)
	except:
		e = sys.exc_info()[0]
		print(e)
		pass_activity = "false"
		post_log(activity_definition, pass_activity)
	return payloadDecoded


"""
Description: Locally saves the JSON payload as a text file
Parameters: payloadDecoded - the decoded payload
Throws: Exception e
"""


def save_payload(payloadDecoded):
	activity_definition = "App1: Locally saved JSON payload as a text file"
	pass_activity = "true"
	try:
		with open("send/App1jsonFile.json", "w") as outFile:
			jsonObj = outFile.write(json.dumps(payloadDecoded))

		post_log(activity_definition, pass_activity)

	except:
		e = sys.exc_info()[0]
		print(e)
		pass_activity = "false"
		post_log(activity_definition, pass_activity)

"""
Description: Sends the decoded payload to App2
Parameters: payloadDecoded - the decoded payload
	    ssl_sock - secure transfer protocol 
Throws: Exception e
"""


def send_payload(payloadDecoded, ssl_sock):
	activity_definition = "App1: Sent JSON payload to App 2"
	pass_activity = "true"
	try:
		ssl_sock.sendall(payload)
		ssl_sock.close()
		post_log(activity_definition, pass_activity)
	except:
		e = sys.exc_info()[0]
		print(e)
		pass_activity = "false"
		post_log(activity_definition, pass_activity)

"""
Description: Posts the log to database
Parameters: description - provides details of each activity
	    pass_activity - provides details on if each activity passed or failed
Throws: Exception e
"""


def post_log(description, pass_activity):
	uniqueID = str(uuid.uuid4())
	current_time = datetime.now()
	timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
	headers = {'Content-Type': 'application/json'}
	data = '[{"id": "'+uniqueID+'", "activityDescription": "'+description+'", "timestamp": "'+timestamp+'", "pass": "'+pass_activity+'"}]'
	response = requests.post('http://127.0.0.1:5000/logs', headers=headers, data=data)

try:
	ssl_sock = start_connection()
	payload = get_payload(fullURL)
	payloadDecoded = decode_payload(payload)
	save_payload(payloadDecoded)
	send_payload(payloadDecoded, ssl_sock)
except:
	e = sys.exc_info()[0]
	print("error: %s" %e)
