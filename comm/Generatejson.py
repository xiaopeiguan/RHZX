#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

masterjsonpath = "C:\\Users\\fintell\\Desktop\\masterjson.json"
demojsonpath = "C:\\Users\\fintell\\Desktop\\demojson.json"
newjsonpath = "C:\\Users\\fintell\\Desktop\\newjson.json"

# 从全量json中获取目标list
def gettargetlistfrommasterjson(listname,n):
    with open(masterjsonpath, 'r', encoding='utf-8') as masterjson:
        jsondata = json.load(masterjson)
        targetlist = jsondata['result'][listname]
        masterjson.close()
        return targetlist[0:n]

# 生成新json文件
def generatenewjson(listname,listvalue):
    # 将json字符串转化为字典，转化为字段后按照pyhton字典数据类型进行取数
    with open(demojsonpath, 'r+', encoding='utf-8') as demojson:
        jsondata = json.load(demojson)
        resultjson = jsondata['result']
        dict = {listname: listvalue}
        resultjson.update(dict)
        jsondata = json.dumps(jsondata, ensure_ascii=False, indent=2)
    with open(newjsonpath, 'w', encoding='utf-8') as newjson:
        newjson.write(jsondata)
        newjson.close()


if __name__ == '__main__':
    # 获取list
    value = gettargetlistfrommasterjson(listname='criLoanInfoList', n=6)
    # 生成新的list
    generatenewjson(listname='criLoanInfoList', listvalue=value)


