#coding=utf-8
#!/usr/bin/ env python
"""
@作者：AllenQ
@文件名：6.异常处理.PY
@时间：2019/9/11  23:41
@文档说明:Python中的异常处理
    1.try -except代码块捕获异常
      else代码块中定义的是正常流程的代码
"""
print("try-except-else代码块")
try:
    a=1
    b=a/0
    #捕获多个异常信息
except (Exception,IOError):
    print("error")
else:
    print("success")
print("=="*20)
print("3.try-finally代码块")
try:
    a=1
    b=a/0
except:
    print("try-except语句捕获所有发生的异常。但这不是一个很好的方式，我们不能通过该程序识别出具体的异常信息。因为它捕获所有的异常。")
else:
    print("success")
print("=="*20)
print("异常")
try:
    try:
        a=1
        print(a)
        b=a/0
        print(a+1)
    finally:
         #退出try时总会执行
        print("try-finally 语句无论是否发生异常都将执行最后的代码")
except:
    print("出现异常")
print("=="*20)
try:
    fh = open("testfile", "r",encoding="utf8")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print("关闭文件")
        fh.close()
except IOError:
    print ("Error: 没有找到文件或读取文件失败")
print("")

