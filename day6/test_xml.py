#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
from xml.etree import ElementTree as ET
# root = ET.XML(open('first.xml','r',encoding='utf-8').read())
# print(root.tag)
#
# for node in root:
#     print(node.tag,node.attrib,node.find('rank').text)
#     print(node.find('rank').text)
    # for node_node in node:
    #     print(node_node)

tree = ET.parse('first.xml')
root = tree.getroot()
print(dir(root))
# for node in root.iter('year'):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     del node.attrib['name']
#     # node.set('name','allan')
#     # node.set('age','19')
#
# tree.write("first.xml")
# for country in root.findall('country'):
#     print(country.attrib)
from xml.dom import minidom
def pretty(root):
    rough_string = ET.tostring(root,'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

new_str = pretty(root)
f = open('new_output.xml','w')
f.write(new_str)
f.close()