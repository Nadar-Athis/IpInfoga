import os
import json
import urllib.request
import terminal_banner

print('''
  _____      _____        __                  
 |_   _|    |_   _|      / _|                 
   | |  _ __  | |  _ __ | |_ ___   __ _  __ _ 
   | | | '_ \ | | | '_ \|  _/ _ \ / _` |/ _` |
  _| |_| |_) || |_| | | | || (_) | (_| | (_| |
 |_____| .__/_____|_| |_|_| \___/ \__, |\__,_|
       | |                         __/ |      
       |_|                        |___/       \n ''') 

print("Coded By NadarAthis v1.0 \n\n")

while True:
	ip = input("ENTER THE IP ADDRESS OF THE TARGET SYSTEM: ")
	api = "http://ip-api.com/json/"
	response = urllib.request.urlopen(api + ip)
	data = response.read()
	value = json.loads(data)

	print("IP: " + value['query'])
	print("ISP: " + value['isp'])
	print("Country: " + value['country'])
	print("RegionName: " + value['regionName'])
	print("Region: " + value['region'])
	print("City: " + value['city'])
	print("PinCode: " + value['zip'])
	print("Org: " + value['org'])
	break
	
