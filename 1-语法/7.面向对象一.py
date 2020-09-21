# coding=utf-8
# !/usr/bin/ env python

# 类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
# 方法：类中定义的函数。
# 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
# 数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
# 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
# 局部变量：定义在方法中的变量，只作用于当前实例的类。
# 实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
# 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
# 实例化：创建一个类的实例，类的具体对象。
# 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

class Demo:
    """
    定义Demo类
    """

    def __init__(self):
        print("这是类自带一个初始化方法")

    demo_field = 123456

    def demo_method(self):
        print("this is a method")


"""
实例化Demo类
"""
print("=====================1.类基础介绍==========================")
demo = Demo()
print(demo.demo_field)
demo.demo_method()
print("=====================华丽的分界线===========================")
print()
print()
print()
print("=====================2.类的基本属性和私有属性==================")


class People:
    """
    类的基本属性和私有属性
    """
    name = ""
    age = 0
    __sex = ""  # 私有属性在类外部无法直接进行访问

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.__sex = sex


people = People("张三", 23, "男")
print(people.name)
print("私有属性类外部不能访问")
print("=====================华丽的分界线===========================")
print()
print()
print()
print("=====================3.Python中的单继承=====================")


class Student(People):
    """
    单继承示例
    """
    grade = 99.9

    def __init__(self, name, age, grade):
        super().__init__(name, age, "xxx")
        self.age = age
        self.grade = grade
        """
        初始化方法
        :param name:
        :param age:
        :param sex:
        :param grade:
        """

        print("单继承示例")

    def speek(self):
        """
        说话的方法
        :return:
        """
        print("%d 岁的 %s  年级是%d" % (self.age, self.name, self.grade))


student = Student("李四", 28, 23)
student.speek()
print(student)
print("=====================华丽的分界线===========================")
print()
print()
print()

print("=====================4.Python中的多继承=======================")


class Coder:
    """
    程序员
    """
    # 体重
    weight = ""

    def __init__(self, weight):
        self.weight = weight

    def speek(self):
        print("说话的    %s" % self.weight)


class Man:
    """
    男人
    """
    money = 0.0

    def __init__(self, money):
        self.money = money

    def speek(self):
        print("说话的    %f" % self.money)


class Speeker(Man, Coder):
    """
    演讲人 继承 Man 和 Coder
    """

    def __init__(self, money, weight):
        Man.__init__(self, money)
        Coder.__init__(self, weight)


aa = Speeker(88.88, "188kg")
aa.speek()
print("多继承调用父类方法,方法名同，默认调用的是在括号中排前地父类的方法")
print("=====================华丽的分界线===========================")
print()
print()
print()