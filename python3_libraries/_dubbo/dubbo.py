#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author Rongzhong Xu 2016-09-06 wechat: pythontesting
"""
Name: dubbo.py

Tesed in python3.5
"""

import json
import telnetlib
import socket


class Dubbo(telnetlib.Telnet):

    prompt = 'dubbo>'
    coding = 'gbk'

    def __init__(self, host=None, port=0,
                 timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        super().__init__(host, port)
        self.write(b'\n')

    def command(self, flag, str_=""):
        data = self.read_until(flag.encode())
        self.write(str_.encode() + b"\n")
        return data

    def invoke(self, service_name, method_name, arg):
        command_str = "invoke {0}.{1}({2})".format(
            service_name, method_name, json.dumps(arg))
        self.command(Dubbo.prompt, command_str)
        data = self.command(Dubbo.prompt, "")
        data = json.loads(data.decode(Dubbo.coding,
                                      errors='ignore').split('\n')[0].strip())
        return data

if __name__ == '__main__':

    conn = Dubbo('183.131.22.99', 21881)

    content = {
        "sign": "FKeKnMEPybHujjBTzz11BrulB5av7pLhJpk=",
        "partnerOrder": "0511e0d38f334319a96920fa02be02a7",
        "productDesc": "hello",
        "paySuccessTime": "2016-08-25 18:33:04",
        "price": "1",
        "count": "1",
        "attach": "from_pay_demo",
        "date": "20160825",
    }
    content_json = json.dumps(content).replace('"', '\\"')

    json_data = {
        "requestId": "0511e0d38f334319a96920fa02be02a7",
        "reqUrl": 'http://www.oppo.com',
        "httpReqType": "POST",
        "headerMap": None,
        "reqContent": content_json,
        "appId": "10001",
        "productName": "test",
        "timeStamp": "1472121184957",
        "partnerId": "2031",
        "signType": "MD5",
        "sign": "23B621FBBF887373C65E553C2222258F",
        "successResult": "OK",
    }

    result = conn.invoke(
        "com.oppo.pay.notify.api.facade.NotifyApplyService",
        "httpNotify",
        json_data
    )
    print(result)
