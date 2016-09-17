#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
#百分号的方式,比较老,支持的功能相对format较少
#format支持的功能较多
# s = "I am %s,age %d" %('Allan',18)
# print(s)
# s1 = "I am %(n1)s,age %(n1)d" %{"n1":111}
# print(s1)
#
# #右对齐,占位符10个位置,
# s2 = "I am %(n1) + 10s" %{"n1":"Allan"}
# print(s2)
#
# #左对齐,占位符10个位置,
# s3 = "I am %(n1) - 10s" %{"n1":"Allan"}
# print(s3)
#
# s4 = "I am %(n1) - 10d" %{"n1":19}
# print(s4)
#
# s5 = "I am %(n1) + 10d" %{"n1":-19}
# print(s5)
#
# s6 = "I am %(n1) 0 10d" %{"n1":19}
# print(s6)
#
# s7 = "I am %f" %1.2
# print(s7)
# s8 = "I am %.2f" %1.2
# print(s8)
#
# #数字转换为unicode.
# s9 = "I am %c" %(342)
# print(s9)
#
# #十进制转换为八进制
# s10 = "I am %o" %(10)
# print(s10)
#
# s11 = "I am %e,%x" %(15,2)
# print(s11)
#
# s12 = "I am %s %%" %(10)
# print(s12)

#fill空白处填充一个字符
#align 对齐方式
#sign 有无符号数字
# #对于二进制,八进制,十六进制,加上#,会显示0b/0o/0x
#, 为数字添加分隔符 1,000

s = "I am {:b} how are you".format(12)
print(s)
s1 = "I am {:#b} how are you".format(12)
print(s1)
s2 = "I am {:.2%} how are you".format(2)
print(s2)
s3 = "I am {:%} how are you".format(2)
print(s3)

s4 = "I am {}, age {}, love {}.".format(*["Allan",18,"girl"])
print(s4)

s5 = "I am {0}, age {1}, love {0}.".format("Allan",18)
print(s5)
s6 = "I am {0}, age {1}, love {0}.".format(*["Allan",18])
print(s6)

s7 = "I am {name}, age {age}, love {name}.".format(name = "Allan",age = 18)
print(s7)

s8 = "I am {0[0]}, age {0[1]}, love {0[2]}.".format([1,2,3])
print(s8)

s9 = "I am {:s}, age {:d}, love {:f}.".format("Allan",12,2.3)
print(s9)