# python基础语法

# 编码
# -*- coding: cp-1252 -*-
# 默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串。 当然你也可以为源码文件指定不同的编码：

# 标识符
# 第一个字符必须是字母表中字母或下划线。
# 标识符的其他部分由字母、数字和下划线组成。
# 标识符对大小写敏感。
# 在python3中，可以用中文作为变量名，非ASCII标识符也是允许的了。
# ---------------------------------------------------------------------
# python保留字
# # 保留字即关键字，我们不能把它们作用任何标识符名称，python的标准库提供了一个keyword模块，可以输出当前版本的所有关键字；
# import keyword
# print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# 注释
# Python中，单行注释以#号开头，示例如下：
# 第一个注释
# print("hello,python")#第二个注释
# 多行注释可以用#号，还有'''和"""
# ---------------------------------------------------------------------
# 行与缩进
# python最具特色的就是使用缩进表示代码块，不需要使用大括号{}
# 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数，实例如下
# if True:
#     print("ture")
# else:
#     print("false")
# 以下代码最后一行语句缩进数的空格不一致，会导致运行错误；
# if True:
#     print("answer")
#     print("True")
# else:
#     print("answer")
#   print("false") #缩进不一致，会导致运行错误
# IndentationError: unindent does not match any outer indentation level
# 缩进错误：未缩进不匹配任何外部缩进级别
# --------------------------------------------------------------------
# 多行语句
# python通常是一行写完一条语句，但如果语句很长，我们可以用反斜杠\来实现多行语句，例如：例如
# total=1+\
#     2+\
#     3
# print(total)#运行结果6
# # 在[],{}或()中的多行语句，不需要用反斜杠\，例如
# total = [1,2,3,
#          4,
#         5]
# print(total)#运行结果[1, 2, 3, 4, 5]
# -----------------------------------------------------------------------
# 数字（Number）类型
# python中数字有四种类型：整数、布尔型、浮点数和复数；
# int（整数），如1，只有一种整数类型int，表示为长整型，没有python2中的long
# bool（布尔型），如ture
# float（浮点数），如1.23、3E-2
# complex（复数），如1+2j、1.1+2.2j
# -------------------------------------------------------------------------
# 字符串（String）
# pyton中单引号'和双引号"使用完全相同
# 使用三引号（'''或"""）可以指定一个多行字符串
# 转义符\
# 反斜杠和以用来转义，使用r可以让反斜杠不发生转移。如
# print(r"this is a line with \n")#会显示，并不是换行。
# 按字面意义级联字符串，如"this""is""string"会被自动转为this is string
# 字符串可以用+运算符连接在一起，用*运算符重复。
# Ptyhon中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始。
# Python中的字符串不能改变
# Python没有单独的字符串类型，一个字符就是长度为1的字符串。
# 字符串的截取的语法格式如下：变量[头下标：尾下标：步长]
# word = "字符串"
# sentence = "这是一个句子"
# paragraph = """这是一个段落，
# 可以由多行组成"""
# print(word)#字符串
# print(sentence)#这是一个句子
# print(paragraph)
# 这是一个段落，
# 可以由多行组成
# ------------------------------------------------------------------
# 实例：
str = '123456789'
# print(str)#输出字符串
# print(str[0:8]) # 输出第一个到倒数第二个的所有字符
# print(str[0:-1])# 输出第一个到倒数第二个的所有字符
# # 输出12345678
# print(str[0]) #输出字符串第一个字符
# print(str[2:5])#输出从第三个开始到第五个字符
# print(str[2:])#输出从第三个开始后的所有字符
# print(str[1:5:2])#输出从第二个开始到第五个且每隔一个的字符（步长为2）
# print(str*2)#输出2次
# print(str+"你好")#连接字符串
# print("hello\nrunoob")#使用反斜杠(\)+n转义特殊字符(换行输出)
# print(r"hello\nrunoob")#在字符串前面加一个r,表示原石字符串，不会发生转义
# 这里的r指raw，即raw string，会自动将反斜杠转义
# --------------------------------------------------------------------
# 空行
# 函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。
# 空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两端不同功能或含义的代码，方便日后代码的维护或重构
# 记住：空行也是程序代码的一部分
# ---------------------------------------------------------------------
# 等待用户输入
# 执行下面的程序在按回车键后就会等待用户输入：
# input("\n\n按下 enter 键后推出。")#按两下空格退出
# ----------------------------------------------------------------------
# 同一行显示多条语句
# Python可以在同一行中使用多条语句，语句之间使用分号；分割，以下是一个简单的的实例：
# import sys;x = 'runoob';sys.stdout.write(x+'\n')
# -----------------------------------------------------------------------
# 多个语句构成代码组
# 缩进相同的一组语句构成也给代码块，我们称之为代码组。
# 像if、while、del和class这样的复合语句，首行以关键字开始，以冒号（：）结束，改行只有的一行或多行代码构成代码组
# 我们将首行以及后面的代码组成为一个字句（clause）
# if expression :
#    suite
# elif expression :
#    suite
# else :
#    suite
# -------------------------------------------------------------------------
# print输出
# print默认输出是换行的，如果要实现不换行需要在变量末尾加上end=""
# x="a"
# y="b"
# print(x)
# print(y)
# print('---------------------------------')
# # 不换行输出
# print(x,end="")
# print(y,end="")
# print()
# 以上实例执行结果为：
# a
# b
# ---------
# a b
# -----------------------------------------------------------------------------
# import 与 from...import
# 在python用import或者from...import来导入相应的模块。
# 将整个模块（somemodule）导入，格式为：import somemodule
# 从某个模块中导入某个函数，格式为:from somemodule import somefunction
# 从某个模块中导入多个函数，格式为：from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为：from somemodule import *
# 导入sys模块
# import sys
# print('---------------------python import mode--------------------------------')
# print('命令行参数为：')
# for i in sys.argv:
#     print(i)
# print('\n python 路径为',sys.path)
# 导入sys模块的argv，path成员
# from sys import argv,path #导入特定的成员
# print('=====================python from import===================================')
# print('path:',path) #因为已经导入path成员，所以此处引用是不需要加sys.path
-------------------------------------------------------------------------------------
# 命令行参数
# 很多程序可以执行一些操作来查看一些借本信息，Python可以使用-h参数查看各参数帮助信息
