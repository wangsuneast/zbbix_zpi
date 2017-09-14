#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urllib2

url = "http://127.0.0.1/zabbix/api_jsonrpc.php"
headers = {"Content-Type":"application/json"}
def login():
    data = json.dumps(
    {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": "Admin",
            "password": "zabbix"
        },
        "id": 1
    })
    request = urllib2.Request(url,data)         
    for key in headers:
        request.add_header(key,headers[key])

    try:
        result = urllib2.urlopen(request)
    except Exception as e:
        print "Error" + e
    else:
        response = json.loads(result.read())
        result.close()

    token = response['result']
    return token

if __name__ == "__main__":
    login()
