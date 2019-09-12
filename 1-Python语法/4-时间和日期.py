# coding=utf-8
# !/usr/bin/ env python
"""
@作者：AllenQ
@文件名：4-时间和日期.PY
@时间：2019/9/3  11:32
@文档说明:
"""

# python 时间和日期库  time  和calendar
import time

# 1. 时间的模块的所有方法
print(dir(time))
# 2.time.time()方法
tick=time.time()
print( "2 每个时间戳都是以1970年1月1日开始的'浮点小数',当前时间戳为====>>>", tick)
# 3,时间元组 很多Python函数用一个元组装起来的9组数字处理时间
    # 序号	字段	值
    # 0	    4位数年	2008
    # 1	    月	     1 到 12
    # 2	    日	     1到31
    # 3	    小时	  0到23
    # 4	    分钟	  0到59
    # 5	    秒	     0到61 (60或61 是闰秒)
    # 6	    一周的第几日	0到6 (0是周一)
    # 7	    一年的第几日	1到366 (儒略历)
    # 8	    夏令时	-1, 0, 1, -1是决定是否为夏令时的旗帜
    # 序号	属性	值
    # 0	    tm_year	2008
    # 1	    tm_mon	1 到 12
    # 2	    tm_mday	1 到 31
    # 3	    tm_hour	0 到 23
    # 4	    tm_min	0 到 59
    # 5	    tm_sec	0 到 61 (60或61 是闰秒)
    # 6	    tm_wday	0到6 (0是周一)
    # 7	    tm_yday	1 到 366(儒略历)
    # 8	    tm_isdst	-1, 0, 1, -1是决定是否为夏令时的旗帜
# 4.获取当前时间 从浮点数的时间戳转换为时间元组,只需要将浮点数传递给localtime之类的函数
localtime=time.localtime(time.time())
print("3 浮点数===>>时间元组的函数localtime,本地时间为:",localtime)
# 5.获取格式化的时间
localtime=time.asctime(time.localtime(time.time()))
print("4 time.asctime() 方法 格式化时间: 将时间元组格式化float==>>stru_time",localtime)
# 6.格式化日期 使用time模块的strftime方法来格式化日期
    #格式化微2016-03-20 11:45:39的格式
print("6 time.strftime()方法.格式化日期stuc_time==>>str",time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 7.将字符串的日期 转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print("7.time.strptime()方法.将字符串解析为时间元组-'时间元组相当于Java里面的Date类'",time.strptime(a,"%a %b %d %H:%M:%S %Y"))
print("8.time.mktime()方法:将时间元组格式化为时间浮点数,strc_time==>>float",time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

import calendar
print("======================calendar日历模块=====================")

print("小结:calendar模块的所有方法:",dir(calendar))
cal =calendar.month(2016,1)
print("1,以下输出2016年1月份的日历")
print(cal)