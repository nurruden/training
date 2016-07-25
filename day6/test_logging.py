#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"

import logging
logging.basicConfig(filename='test.log',
                    format='%(asctime)a - %(name)s - %(levelname)s - %(module)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=10,)
logging.error("This is an error")
#创建文件
file_1_1 = logging.FileHandler('11_1.log','a')
#创建格式
fmt = logging.Formatter(fmt='%(asctime)s - %(name)s -%(levelname)s -%(module)s: %(message)s')
#文件应用格式
file_1_1.setFormatter(fmt)

#创建文件
file_1_2 = logging.FileHandler('11_2.log','a')
#创建格式
fmt = logging.Formatter()
#文件应用格式
file_1_2.setFormatter(fmt)

logger1 = logging.Logger('s1',level=logging.ERROR)

logger1.addHandler(file_1_1)
logger1.addHandler(file_1_2)

logger1.critical('11111')
