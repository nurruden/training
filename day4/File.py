#-*-coding:utf-8-*-
#/usr/bin/env python
#open(文件名,模式)
#默认只读模式
# f = open('ha.log')
# data = f.read()
# f.close()
# print(data)
#只读模式
# f = open('ha.log','r')
# f.write('dad')
# f.close()
#只写模式,不可读,如果文件不存在,创建新文件.文件存在,原内容清空
# f = open('ha1.log','w')
# f.write("1234")
# f.close()
#x模式只写模式,不可读,如果文件不存在,创建新文件.文件存在,报错
# f = open('ha1.log','x')
# f.write("1234")
# f.close()
#追加模式,不可读,不存在,创建文件,存在,追加到文件末尾
# f = open('ha1.log','a')
# f.write("12346")
# f.close()
#
# f = open('ha1.log','a')
# data = f.read()
# f.close()
# print(data)
# Traceback (most recent call last):
#   File "/Users/northstar/PythonData/MY_Test/training/day4/File.py", line 27, in <module>
#     data = f.read()
# io.UnsupportedOperation: not readable

#py3以字节方式打开,rb
# f = open("ha.log",'rb')
# data = f.read()
# f.close()
# print(data)
# print(type(data))

#一二进制方式只写
# f = open("ha1.log",'wb')
# f.write(bytes("周六",encoding="utf-8"))
# f.close()
# f = open("ha1.log",'rb')
# data = f.read()
# f.close()
# print(data)
# str_data = str(data,encoding="utf-8")
# print(str_data)
# #b'\xe5\x91\xa8\xe5\x85\xad'
#周六
#Need read and write.r+,w+,x+a+
#r+ read and write
#w+ write and read
#x+ write and read
#a+ write and read
#r+ ,w, pointor move to the end
# f = open("ha.log",'r+')
# print(f.tell())
# data = f.read(3)
# print(type(data),data)
# print(f.tell())
# f.write("ok")
# f.seek(0)
# # data = f.read()
# print(type(data),data)
# f.close()

#w+, need to clean up first, after writting, you can read
# f = open("ha.log",'w+',encoding='utf-8')
# f.write("cacaca")
# f.seek(0)
# data = f.read()
# f.close()
# print(data)

#x+, if file exist, pop up error, the rest same with w+


#a+, when you open the file, the pointor has been moved to the end
f = open("ha.log",'a+',encoding='utf-8')
print(f.tell())
data = f.read()

f.seek(0)
data = f.read()
print(data)
f.close()

