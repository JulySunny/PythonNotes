# coding=utf-8
# !/usr/bin/ env python
# 1.字符串的操作
print("======================Python中的字符串操作==================")
str = " abcbdef "
print("1.title()方法,将str作为标题,首字母大写输出:")
print(str.title())
print()
print("2.startwith()方法,判断str是否以指定字符串开头:")
print(str.startswith('aff', 0, 1))
print()
print("3.split()方法,以指定字符串/字符去切割str:")
print(str.split("b", 1))
print()
print("4.rstrip():移除右侧空白字符 strip() 移除两侧的空格:")
print(str.strip())
print(str.rstrip())
print(str.lstrip())
print()
print("5.index():查询子串在父串中的索引位置 如果子串不存在 则报错:")
print(str.index('a'))
print()
print("6.find():查找子串是否在父串中的索引位置 如果有多个则查找第一个,如果子串不存在则返回-1:")
print(str.find('a'))
print()
print("7.字符串的切片操作: ")
# 格式： 【start:end:step】
#  start:起始索引，从0开始，-1表示结束
#  end：结束索引
#  step：步长，end-start，步长为正时，从左向右取值。步长为负时，反向取值
print(str[-1:0:-1])
print()
print("8.format()方法,用于字符串的格式化: ")
str1="{}------{}"
print(str1.format(1,2))
print()
print("9.count()方法 统计某个串在指定字符串中出现的次数: ")
print(str.count("a"))
print()
print("10.replace()替换的方法 参数1:要替换的旧串;参数2:替换后的新串;参数3:要替换的个数 0 表示不替换,默认为-1表示全部替换: ")
print(str.replace("a","xxx"))
print()
print(dir(str))
