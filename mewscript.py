#!/usr/bin/python3

import json
import requests

url = "http://dummy.restapiexample.com/api/v1/employees"

#headers = {
   # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  #  "Accept-Language": "en-US,en;q=0.5",
 #   "Accept-Encoding": "gzip, deflate"
#}
response = requests.get('https://api.github.com')
response_2 = requests.get(url)#, headers)
print(response.status_code)
print(response_2.status_code)


#name = set()
#data = response.json()
# for p in data:
#   name.add(p['employee_name'])#.encode('utf-8'))
#name_list = list(name)
# name_list.sort()
#print("\n\n\nemployee names are: " + str(name_list))
# sys.stdout.flush()
