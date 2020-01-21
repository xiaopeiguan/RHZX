#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
from comm import Ddate

newjsonpath = "C:\\Users\\fintell\\Desktop\\newjson.json"
# 获取result一级结构字段值 例 "queryDate": "20181210"
def get1stjsondata(key):
    # 将json字符串转化为字典，转化为字段后按照pyhton字典数据类型进行取数
    jsondata = json.load(open(newjsonpath, 'r', encoding='utf-8'))
    result = jsondata['result']
    if key in result.keys():
        value = result[key]
        # print(key + '的值为：' + value)
        return value

# 获取result二级结构字段值 例 criLoanInfoList.aboutDate
def get2ndjsondata(listname, key):
    # 将json字符串转化为字典，转化为字段后按照pyhton字典数据类型进行取数
    jsondata = json.load(open(newjsonpath, 'r', encoding='utf-8'))
    list = jsondata['result'][listname]
    valuelist = []
    for dict in list:
        if key in dict.keys():
            value = dict.get(key)
            valuelist.append(value)
    # print(key + '值结果序列为： ', valuelist)
    return valuelist

# 计算时间差值列表，相差月  例queryDate 和 criLoanInfoList.issueDate 的相隔天数并取绝对值，向上取值
def Dmonthlist(date, date1list):
    dmonthlist = []
    for a in date1list:
        b = Ddate.Dmonth(date, a)
        dmonthlist.append(b)
    # print('Dmonthlist值结果序列为： ', dmonthlist)
    return dmonthlist

# 获取需要计算字段的结果集
def getlist(list1, list2, list3, list4, list5):
    if len(list1) == len(list2) == len(list3) == len(list4) == len(list5):
        list = []
        for i in range(0, len(list1)):
            a = []
            a.append(list1[i]), a.append(list2[i]), a.append(list3[i]), a.append(list4[i]), a.append(list5[i])
            tup = tuple(a)
            list.append(tup)
        # print('提取字段的结果集为： ', list)
        return list
    else:
        print('几个list个数分别为：', len(list1), len(list2), len(list3), len(list4), len(list5))
        print('几个list个数不一致')


if __name__ == '__main__':
    queryDate = get1stjsondata('queryDate')
    aboutDate = get2ndjsondata('criLoanInfoList', 'aboutDate')
    dmonthlist = Dmonthlist(date=queryDate, date1list=aboutDate)
    loantype = get2ndjsondata('criLoanInfoList', 'loanType')
    financetype = get2ndjsondata('criLoanInfoList', 'financeType')
    acctStatus = get2ndjsondata('criLoanInfoList', 'acctStatus')
    repayPeriods = get2ndjsondata('criLoanInfoList', 'repayPeriods')
    valuelist = getlist(list1=dmonthlist, list2=loantype, list3=financetype, list4=acctStatus, list5=repayPeriods)
    for i in range(0, len(valuelist)):
        print(valuelist[i])






