#-*-coding:utf-8-*-
#/usr/bin/env python
import re
# #字符匹配(普通字符,元字符)
# print(re.findall('alex','asasaalexdasaalex'))  #所有匹配的字符以列表形式返回
# #元字符: .^$*+?{}[]|()\
# # .表示任意一个字符
# print(re.findall('alex.a','asasaalexdxasaalexda'))
# #^表示以alex起始的字符串
# print(re.findall('^alex','alexasasaalexdxasaalexda'))
# #$表示以该字符串结尾
# print(re.findall('xda$','alexasasaalexdxasaalexda'))
# #*重复0到多次
# print(re.findall('sa*','alexasasaalexdxasaalexda'))
# print(re.findall('(sa)*','alexasasaalexdxasasaalexda'))
# #+重复一到多次
# print(re.findall('(sa)+','alexasasaalexdxasasaalexda'))
#?匹配0到1次
# print(re.findall('alex?','alexasasaalexdxasasaaleda'))
# #{}重复固定次数
# print(re.findall('alex{3,5}','asadadasalexxxxxxx'))
#[]取[]中任意的字符
# print(re.findall('a[bc]d','abdacdabcdaas'))
# #元字符在字符集里面没有意义
# print(re.findall('[a-z]','sds'))
# print(re.findall('[1-5]','asa37'))
# #^在字符集里面反转
# print(re.findall('[^1-5]','asa37'))
#反斜杠后面跟元字符,去除元字符特殊功能
#反斜杠后面跟普通字符实现特殊功能
#引用序号对应的字组所匹配的字符串
# print(re.search(r"(allan)(fenda)com\2","allanfendacomfendaa").group())
#\d匹配任意十进制数,等于[0-9]
#\D匹配任意非数字字符,等于[^0-9]
#\s匹配任何空字符,等于 [ \t\n\r\f\v]
#\S匹配任意非空字符,等于 [^ \t\n\r\f\v]
#\w匹配任何字母数字字符,等于[a-zA-Z0-9]
#\W匹配任何非字母数字字符,等于[^a-zA-Z0-9]
#\b匹配一个单词边界,也就是指单词和空格间的位置
# print(re.findall(r"\babc\b"," abc sda"))
# print(re.findall('\d','asa2da33de3'))
# print(re.findall('\w','asa2da33de3'))
# print(re.findall('\s','asa2da3 3de3'))
#search 只找到一个并返回一个
#match 只匹配开头的字符串
#贪婪匹配
# print(re.findall("a(\d+)","a234a2"))
# #非贪婪模式
# print(re.findall("a(\d+?)","a234a2"))
# print(re.findall(r"a(\d)*","a234a2"))    #???

#re.I不区分大小写
# re.L做本地化识别匹配
# re.M 多行匹配,影响^$
# re.S 匹配换行符在内的字符
#替换
# result = re.sub("g.t","have",'i get a, i got b, i gut c')
# print(result)
text = "good is good boy, he is cool"
regex = re.compile(r'\w*oo\w*')
print(regex.findall(text))