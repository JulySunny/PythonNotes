# coding=utf-8
# !/usr/bin/ env python
list = ["aa", "bb", "cc", "dd", "ee"]
print(dir(list))
# 1.append()方法  向列表尾部添加元素
list.append("ff")
print("append()方法:::::::::::::%s" % list)
# 2.insert()方法 向指定索引位置添加元素 如果索引大于列表长度则添加至列表末尾,***列表并不会扩容***
list.insert(9, "00")
print("insert()方法:::::::::::::%s" % list)
# 3.list[索引值] 修改元素 如果索引值大于当前列表的长度 则会报错,索引越界异常
# list[0]="gg"
print("list[索引值]:::::::::::::%s" % list)
# 4.count()方法 计算列表中的指定元素的个数
print("count()方法::::::::::::::%s" % list.count("a"))
# 5.index() 查看指定元素在列表list中的索引位置 ***********如果指定元素不存在,则会报错************
print("index()方法::::::::::::::%s" % list.index("aa"))
# 6.判断列表中是否存在指定元素 指定元素 in list 返回布尔值 True 或者False
print("element in list::::::::::%s" % "aaa" in list)
# 7.删除列表中的元素 del list[索引值],list.remove("指定元素") list.pop()末尾的元素,不用传参
del list[1]
print("del()方法删除元素无返回值::::")
# 注意:
#   1.list.remove()和pop()方法 如果不存在要移除的值,就会报错
#   2.pop方法都会返回删除的元素 remove不会 会返回None
print("remove()方法:::::::::::::%s" % list.remove("dd"))
print("pop()方法:::::::::::::%s" % list.pop())
# 8.翻转方法 reverse() 该方法没有返回值,但是会将list里面的元素翻转
list.reverse()
print("reverse()方法:::::::::%s" % list)
# 9.sort() 将列表排序  可选参数 reverse 默认不翻转
list.sort()
print("sort()方法::::::::::::%s" % list)
# 10.sorted(list) 临时排序,返回排序后的列表
print("sorted(列表)::::::::::%s" % sorted(list))
# 11.extend() 方法 连接两个列表
list1 = ["yy"]
list1.extend(list)
print("list.extend(list1)::::::::%s" % list1)
