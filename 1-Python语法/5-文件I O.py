#coding=utf-8
#!/usr/bin/ env python
"""
@作者：AllenQ
@文件名：5-文件I O.PY
@时间：2019/9/9  21:42
@文档说明:
"""

# 1.raw_input函数 -python2.x里面的接收用户输入的函数 py3.x已经被废弃
# 2.input函数:接收用户输入
# 3.open函数
# ---你必须先用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。
# 例如:
file=open("text.txt","w")
file.write("Hello World")
print(dir(file))
# 注意 指针在开头还是结尾的问题
# 模式mode: r w r+ w+ 的指针都在开头 a a+的指针在结尾
# 4.File  对象的属性 closed, mode, name, softspace
# 5.close 函数
file.close()
# ---File 对象的close()方法刷新缓冲区里任何还没写入的信息,并关闭该文件,这之后便不能再进行写入。
# 6.write()方法
# --可以将任何字符串写入一个打开的文件,需要重点注意的是,Python字符串可以是二进制数据,而不仅仅是文字
# --**********不会在字符串的结尾添加换行符("\n")*********
file=open("text.txt","w") #不指定文件打开方方式,这里写入中文会乱码
# file=open("text.txt","w",encoding="utf8") --打开文件加上utf-8 写入文件就不会乱码
file.write("这是写入的值")
file.close()
# 7.read()方法
# --read()方法从一个打开的文件中读取一个字符串。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
file=open("text.txt","r")
text=file.read(10)
print("读取的字符串 %s"%text)
file.close()
# 8.tell()方法:文件定位,告诉你文件内的当前位置,下一次的读写会发生在文件开头这么多字节之后。
# 9.seek()方法:改变当前文件的位置
file=open("text.txt","r+")
str=file.read(10)
print(str)
# tell()查找当前的位置
position=file.tell()
print("tell()方法查找当前文件的位置: %s"%position)
# seek()定位到文件位置
position=file.seek(0,0)
str=file.read(10)
file.close()
print("seek()重新定位到文件位置后,重新读取字符串 %s"%str)
# 10.重命名和删除文件--依靠os模块
import os
# rename(当前文件名,新文件名) 方法 重命名
if not os.path.exists("txt1.txt"):
    os.rename("text.txt","txt1.txt")
    pass
# remove(文件明)方法
os.remove("text1.txt")
# 11.目录相关的方法
# mkdir()创建目录
# --在当前目录下创建新的目录
os.mkdir("新建的目录")
# chdir()改变当前的目录
# --改变当前的目录
# os.chdir("./改变的目录")
# --方法来改变当前的目录。chdir()方法需要的一个参数是你想设成当前目录的目录名称。
# os.getcwd()显示当前的工作目录
print(os.getcwd())
# os.rmdir()删除目录
