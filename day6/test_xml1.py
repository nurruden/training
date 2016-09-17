#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
from xml.etree import ElementTree as ET
tree = ET.parse('out.xml')  #需要打开文件
#tree = ET.ElementTree(根节点(Element对象))    #找到根节点
root = tree.getroot()

son = ET.Element("pp",{"fk":"aad"})
ele2 = ET.Element("pl",{"ad":"123"})
son.append(ele2)
root.append(son)
tree.write('out.xml')


ele = ET.Element('family',{"age":"18"})
tree = ET.ElementTree(ele)
tree.write("out.xml")