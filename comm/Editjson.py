#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

newjsonpath = "C:\\Users\\fintell\\Desktop\\newjson.json"

# 编辑新json文件中，result一级结构字段值 例 "queryDate": "20181210"
def edit1stjsondata(key, value):
    with open(newjsonpath, 'r', encoding='utf-8') as newjson:
        jsondata = json.load(newjson)
        resultjson = jsondata['result']
        resultjson[key] = value
        jsondata = json.dumps(jsondata, ensure_ascii=False, indent=2)
    with open(newjsonpath, 'w', encoding='utf-8') as newjson:
        newjson.write(jsondata)
        newjson.close()

# 编辑新json文件中，result二级结构字段值,字段值以列表形式
# 例 criLoanInfoList.aboutDate ['20191201', '20200201', '20200111', '20200131']
def edit2ndjsondatalist(listname, key, valuelist):
    with open(newjsonpath, 'r', encoding='utf-8') as newjson:
        jsondata = json.load(newjson)
        lists = jsondata['result'][listname]
        for i in range(0, len(lists)):
            lists[i][key] = valuelist[i]
            i += 1
        jsondata = json.dumps(jsondata, ensure_ascii=False, indent=2)
    with open(newjsonpath, 'w', encoding='utf-8') as newjson:
        newjson.write(jsondata)
        newjson.close()

# 编辑新json文件中，result二级结构字段值,字段值以值的形式
# 例 criLoanInfoList.aboutDate = '20191201'
def edit2ndjsondata(listname, key, n, value):
    with open(newjsonpath, 'r', encoding='utf-8') as newjson:
        jsondata = json.load(newjson)
        lists = jsondata['result'][listname]
        lists[n][key] = value
        jsondata = json.dumps(jsondata, ensure_ascii=False, indent=2)
    with open(newjsonpath, 'w', encoding='utf-8') as newjson:
        newjson.write(jsondata)
        newjson.close()


if __name__ == '__main__':
    # 编辑数据
    # edit1stjsondata('queryDate', '20200101')  # 修改result.queryDate
    # aboutDate = ['20191102', '20200228', '20200210', '20200101','20191020', '20200302']  # 修改aboutDate，数目要等于n
    # edit2ndjsondatalist(listname='criLoanInfoList', key='aboutDate', valuelist=aboutDate)
    # financeType = ['汽车金融公司', '汽车金融公司', '汽车金融公司', '其他机构', '其他机构', '其他机构']
    # edit2ndjsondatalist(listname='criLoanInfoList', key='financeType', valuelist=financeType)
    # acctStatus = ['逾期', '逾期', '逾期', '逾期', '逾期', '逾期']
    # edit2ndjsondatalist(listname='criLoanInfoList', key='acctStatus', valuelist=acctStatus)
    loanType = ['个人消费贷款', '个人消费贷款', '个人消费贷款', '个人消费贷款', '个人消费贷款','个人消费贷款']
    edit2ndjsondatalist(listname='criLoanInfoList', key='loanType', valuelist=loanType)


