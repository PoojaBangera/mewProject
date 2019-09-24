#!/usr/bin/python3

import json

# data = {}
# data['employee'] =
with open('/sapmnt/home/C5254930/Documents/JenkinsRepo/output.txt') as json_file:
    data = json.load(json_file)
dict = {}
for dict in data:
   print('EmployeeID', dict['id'].encode('utf-8')+ ' '+'Employee Name', dict['employee_name'].encode('utf-8'))

    #  print('EmployeeID: ' + p['id'])
   # print('Employee Name: ' + p['employee_name'])
    # print('')
