#!/usr/bin/env python
#coding: utf-8

import urllib
import sys
import json

def query(word):
    url = 'http://fanyi.youdao.com/openapi.do?keyfrom=tinxing&key=1312427901&type=data&doctype=json&version=1.1&q=' + word
    return urllib.urlopen(url).read()

def liststr(str):
    return " ".join(str)

if __name__ == "__main__":
    arg = liststr(sys.argv[1:])
    data = query(urllib.quote_plus(arg))
    qdata = json.loads(data)

    if qdata["errorCode"] != 0:
        print "error:", qdata["errorCode"]
        print data

    print qdata["query"], "-", liststr(qdata["translation"])

    if qdata.has_key("basic"):
        if qdata["basic"].has_key("phonetic"):
            print qdata["basic"]["phonetic"]
        print liststr(qdata["basic"]["explains"])

    if qdata.has_key("web"):
        print
        for i in qdata["web"]: print i["key"], liststr(i["value"])
