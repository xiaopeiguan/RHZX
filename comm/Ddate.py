#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import time
import math

# 计算相差天数的绝对值
def Ddate(date, date1):
    date = time.strptime(date, "%Y%m%d")
    date1 = time.strptime(date1, "%Y%m%d")
    date = datetime.datetime(date[0], date[1], date[2])
    date1 = datetime.datetime(date1[0], date1[1], date1[2])
    if date != date1:
        Ddatevalue = str(abs(date - date1))
        return Ddatevalue
    else:
        Ddatevalue = str('0')
        return Ddatevalue

# 计算相差月份：相隔天数取绝对值，向上取值，不足整月按照整月计算。
def Dmonth(date, date1):
    if date != date1:
        Ddatevalue = Ddate(date, date1)
        # ceil(x)函数是向上取整
        Dmonthvalue = math.ceil(int(Ddatevalue[0:(Ddatevalue.index('d') - 1)]) / 30)
        return Dmonthvalue
    if date == date1:
        Dmonthvalue = '1'
        return Dmonthvalue



if __name__ == '__main__':
    # Ddate('20200101', '20200131')
    print(Dmonth('20200101', '20191102'))
    print(Dmonth('20200101', '20200228'))
    print(Dmonth('20200101', '20200210'))
    print(Dmonth('20200101', '20200101'))
    print(Dmonth('20200101', '20191020'))
    print(Dmonth('20200101', '20200302'))

