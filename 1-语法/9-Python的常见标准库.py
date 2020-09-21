# coding=utf-8
# !/usr/bin/ env python
print("==============================1.操作系统接口 os模块====================================")
# 操作系统接口
# os模块提供了不少与操作系统相关联的函数。
import os

print(os.getcwd())  # 返回当前的工作目录
# os.chdir('/server/accesslog')  修改当前的工作目录
os.system('mkdir today')  # 指定系统命令 mkdir
# 在使用 os 这样的大型模块时内置的 dir() 和 help() 函数非常有用:
# help(os)
# dir(os)
# 针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口:
import shutil

# shutil.copyfile('data.db', 'archive.db')
# shutil.move('./', 'today')
print("==============================华丽的分割线====================================")
print()
print()
print()
print("==============================2.文件通配符====================================")
import glob

print(glob.glob("*.py"))
print("==============================华丽的分割线====================================")
print()
print()
print()

print("==============================3.命令行参数====================================")
import sys

# 通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。
# 例如在命令行中执行 "python demo.py one two three" 后可以得到以下输出结果:
# 例如在命令行中执行 "python demo.py one two three" 后可以得到以下输出结果:
print(sys.argv)
print("==============================华丽的分割线====================================")
print()
print()
print()

print("==============================4.字符串正则匹配====================================")
# re模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案:
import re

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
# 如果只需要简单的功能，应该首先考虑字符串方法，因为它们非常简单，易于阅读和调试:
print('tea for too'.replace('too', 'two'))
print("==============================华丽的分割线====================================")
print()
print()
print()

print("==============================5.数学====================================")
# math模块为浮点运算提供了对底层C函数库的访问:
import math

print(math.cos(math.pi / 4))
print(math.log(1024, 2))
# random提供了生成随机数的工具。
import random

print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))
print(random.random())
print(random.randrange(6))
print("==============================华丽的分割线====================================")
print()
print()
print()
print("==============================6.访问互联网====================================")
# 有几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib:
from urllib.request import urlopen

for line in urlopen('http://wwww.baidu.com'):
    line = line.decode('utf-8')
    # print(line)

print("==============================华丽的分割线====================================")
print()
print()
print()
print("==============================7.日期和时间====================================")
# datetime模块为日期和时间处理同时提供了简单和复杂的方法。
#
# 支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。
#
# 该模块还支持时区处理:
import datetime

print(datetime.date.today())
print(datetime.date(2020, 9, 16))
print(datetime.date.today().strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

birthday = datetime.date(1992, 7, 31)  # 生日
age = datetime.date.today() - birthday
print(age.days)
print(datetime.date.resolution)
# 今天
today = datetime.date.today()
print(today)
# 昨天
print(today - datetime.timedelta(days=1))
# 上个月
print("==============================华丽的分割线====================================")
print("", end="")  # end =""表示不换行
print()
print()
