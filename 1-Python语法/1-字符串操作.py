#coding=utf-8
#!/usr/bin/ env python
# 1.字符串的操作
str="abcdef"
print(dir(str))
# 1.title():将str作为标题,首字母大写输出
print("title()方法:::::::::::::::   %s"% str.title())
# 2.startwith():判断str是否以指定字符串开头  参数1:指定字符串,参数2:str起始索引,参数3:str结束索引
print("startwith()方法:::::::::::::::   %s"% str.startswith("b",0,1))
# 3.split():以指定字符串/字符去切割str
print("split()方法::::::::::::::::::   %s"% str.split("a"))
# 4.rstrip():移除右侧空白字符 strip() 移除两侧的空格
str=" ab cdef "
print("rstrip()方法:::::::::::::::::   %s"% len(str.rstrip()))
print("rstrip()方法:::::::::::::::::   %s"% len(str.strip()))
# 5.index():查询子串在父串中的索引位置 如果子串不存在 则报错
print("index():::::::::::::::::::::    %s"%str.index("ab "))
# 6.find():查找子串是否在父串中的索引位置 如果有多个则查找第一个,如果子串不存在则返回-1
print("find()::::::::::::::::::::::    %s"%str.find("d"))
# 7.字符串的切片操作
print("字符串的切片操作::::::::::::    %s"%str[:])
# 8.format()方法 字符串的格式化方法 有三种方法 去替换{}中的值
print("format()方法::::::::::::::::    %s"% "{0}::::::{1}".format("aa","bb"))
print("format()方法::::::::::::::::    %s"% "{}::::::{}".format("aa","bb"))
print("format()方法::::::::::::::::    %s"% "{占位符别名替换1}::::::{占位符别名替换2}".format(占位符别名替换1="aa",占位符别名替换2="bb"))
str="aabbbcccc"
# 9.count()方法 统计某个串在指定字符串中出现的次数 如果在Java中,实现比较复杂,可以用str.split去切割,根据切割后的子串数组[]的长度-1去判断
print("count()方法:::::::::::::::::    %s"%str.count("a"))
# 10 replace()替换的方法 参数1:要替换的旧串;参数2:替换后的新串;参数3:要替换的个数 0 表示不替换,默认为-1表示全部替换
print("replace()方法::::::::::::::     %s"%str.replace("a","f",0))

import requests
from bs4 import BeautifulSoup

r=requests.get("xxx")
soup=BeautifulSoup(r.text,'html.parser')

soup.find_all('a',class_='topic_title').


class User:
    age=0


    pass






