# coding=utf-8
# !/usr/bin/ env python
# 命名空间(Namespace)是从名称到对象的映射，大部分的命名空间都是通过 Python 字典来实现的。
# 命名空间提供了在项目中避免名字冲突的一种方法。各个命名空间是独立的，没有任何关系的，所以一个命名空间中不能有重名，但不同的命名空间是可以重名而没有任何影响。
# 我们举一个计算机系统中的例子，一个文件夹(目录)中可以包含多个文件夹，每个文件夹中不能有相同的文件名，但不同文件夹中的文件可以重名。


# 一般有三种命名空间：
#
# 内置名称（built-in names）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
# 全局名称（global names），模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
# 局部名称（local names），函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）

# 命名空间查找顺序:
# 假设我们要使用变量 runoob，则 Python 的查找顺序为：局部的命名空间去 -> 全局命名空间 -> 内置命名空间。
# 如果找不到变量 runoob，它将放弃查找并引发一个 NameError 异常:


# 命名空间的生命周期：
# 命名空间的生命周期取决于对象的作用域，如果对象执行完成，则该命名空间的生命周期就结束。
# 因此，我们无法从外部命名空间访问内部命名空间的对象。

# var1 是全局名称
var1 = 5


def some_func():
    # var2 是局部名称
    var2 = 6

    def some_inner_func():
        # var3 是内嵌的局部名称
        var3 = 7


g_count = 0  # 全局作用域


def outer():
    o_count = 1  # 闭包函数外的函数中

    def inner():
        i_count = 2  # 局部作用域


# 内置作用域是通过一个名为 builtin 的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，所以必须导入这个文件才能够使用它。
# 在Python3.0中，可以使用以下的代码来查看到底预定义了哪些变量:

import builtins

print(dir(builtins))

# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
# 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问，如下代码：
print("==============================华丽的分割线====================================")
print()
print()
print()
print("===============================1.global和nonlocal关键字=======================")
print("===============================1.1 global====================================")
# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
# 以下实例修改全局变量 num：

num = 1


def fun1():
    global num
    print(num)
    num = 123
    print(num)


fun1()
print(num)
print("===============================1.2 nonlocal====================================")


# 果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了，如下实例：
def outer():
    num1 = 10

    def inner():
        nonlocal num1
        num1 = 100
        print(num1)

    inner()
    print(num1)


outer()
