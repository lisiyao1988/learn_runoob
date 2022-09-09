# python基础语法

# 编码
# -*- coding: cp-1252 -*-
# 默认情况下，Python 3 源码文件以 UTF-8 编码，所有字符串都是 unicode 字符串。 当然你也可以为源码文件指定不同的编码：

# 标识符
# 第一个字符必须是字母表中字母或下划线。
# 标识符的其他部分由字母、数字和下划线组成。
# 标识符对大小写敏感。
# 在python3中，可以用中文作为变量名，非ASCII标识符也是允许的了。

# python保留字
# 保留字即关键字，我们不能把它们作用任何标识符名称，python的标准库提供了一个keyword模块，可以输出当前版本的所有关键字；
import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
