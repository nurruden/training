#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import pickle
username = "admin"
password = "123456"
data = {username:password}
output = open('data.pkl','wb')
pickle.dump(data,output)
output.close()
with open('data.pkl','rb') as r:
    m = pickle.load(r,encoding='utf-8')
    print(m,type(m))