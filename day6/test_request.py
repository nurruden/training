#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import requests

# response = requests.get("http://www.weather.com.cn/adat/sk/101050404.html")
# response.encoding = "utf-8"
# result = response.text
# print(result)
from xml.etree import ElementTree as ET
# R = requests.get('http://www.webxml.com.cn/webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=535890690714')
# result = R.text
#
# node = ET.XML(result)
# if node.text == "Y":
#     print("yes")
# else:
#     print("No")

r = requests.get('http://www.webxml.com.cn/webservices/TrainTimeWebService.asmx/getDetailInfoByTrainCode?TrainCode=K79&UserID=')
train_result = r.text
train_node = ET.XML(train_result)
# print(train_node)
for node in train_node.iter('TrainDetailInfo'):
    print(node.tag)
    print(node.find('TrainStation').text,node.find('StartTime').text)
#node.tag,node.attrib