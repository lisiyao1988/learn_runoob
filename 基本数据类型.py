# python3基本数据类型
# Python中的变量不需要声明，每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# 在python中，变量就是变量，它没有类型，我们所说的类型是变量所指的内存中对象的类型
# 等号（=）用来给变量赋值；
# 等号(=)运算符左边是一个变量名,等号(=)运算符右边是存储在变量中的值,例如:
# counter = 100 #整型变量
# miles = 1000.0 #浮点型变量
# name = "runoob" #字符串
# print(counter)
# print(miles)
# print(name)
# ----------------------------------------------------------------------
# 多个变量赋值
# python允许你同时为多个变量赋值,例如
a = b = c = 1
# print(a)#1
# print(b)#1
# print(c)#1
# 以上实力，创建一个整形对象，值为1，从后面向前赋值，三个变量都被赋予相同的数值。
# 您也可以为多个对象指定多个变量。例如：
# a,b,c = 1,2,"aaa"
# print(a,b,c)#1 2 aaa
# 以上实例，两个整形对象1和2的分配给变量a和b，字符串对象"aaa"分配给变量c
# -------------------------------------------------------------------------
# 标准数据类型
# python3中有六个标准的数据类型
# Number(数字)
# String（字符串）
# List（列表）
# Tuple（元祖）
# Dictionary（字典）
# Set(集合)
# Python3的六个标准数据类型中
# 不可变数据（3个）：number(数字)、String（字符串）、Tuple(元组);
# 可变数据（3个）：List(列表)、Dictionary(字典)、Set（集合）。
# --------------------------------------------------------------------------
# Number(数字)
# Python3支持int、float、bool、complex（复数）。
# 在Python3里，只有一种整数类型int、表示为长整型，没有python2中的long。
# 像大多数语言一样，数值类型的赋值和计算机都是很直观的
# 内置的type()函数可以用来查询变量所指的对象类型
# a, b, c, d = 20, 5.5, True, 4+3j
# print(type(a),type(b),type(c),type(d))
# # <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
#此外 还可以用isinstance来判断
# a = 111
# if isinstance(a,int):
#     print("zhen")
# else:
#     print("jia")
# isinstance()和 type()区别在于：
# type()不会认为子类是一种父类类型
# isinstance()会认为子类是父类类型
class A:
    pass
class B:
    pass
if isinstance(A(),A):
    print("ture")
else:
    print("fales")
if type(A()) == A:
    print("ture")
else:
    print("fales")
if isinstance(B(), A):
    print("ture")
else:
    print("fales")
if type(B()) == A:
    print("ture")
else:
    print("fales")
