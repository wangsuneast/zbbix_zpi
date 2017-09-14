#!/usr/bin/env python"hostid":
# -*- coding: utf-8 -*-
import json
import urllib2

from login import login

url = "http://127.0.0.1/zabbix/api_jsonrpc.php"
headers = {"Content-Type":"application/json"}
def user_get():
    """
    获取主机的唯一标识码
    hostid:
    """
    data = json.dumps({
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": ["hostid"],             #输出内容
            "filter": {                     #匹配信息
                "host": [                   #匹配主机名称
                    "Zabbix server",        #主机
    #                 "127agent",
                ]
            }
        },
        "auth": login(),
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

    datas = response['result']
    print json.dumps(datas, indent=4)
    return datas[0]

#print user_get()
def create_items():
    data = json.dumps({
        "jsonrpc": "2.0",
        "method": "item.create",
        "params": {
            "name": "1111check_redis service",
            "key_":"check1",
            "hostid": user_get()["hostid"],
            "interfaceid": "1",
            "type": 0,
            "value_type": "3",
            "data_type": "3",
            "history": "10",
            "delay": "200",
            "trends": "30",
        },
        "auth": login(),
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
    print response
    #datas = response['result']
    #print datas

if __name__ == "__main__":
    create_items()
