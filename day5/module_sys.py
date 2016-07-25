#-*-coding:utf-8-*-
#/usr/bin/env python
__aurthor__="Allan"
import sys
import os
import time
# #获取给脚本传入的参数
# print(sys.argv)

# if sys.argv[0] == 'sleepy':
#     print("Go to sleep")
# else:
#     print("Go on!")

# os.mkdir(sys.argv[1])
for i in range(20):
    sys.stdout.write('\r')
    sys.stdout.write("%s%% |%s" %(int(i/20*100),int(i/20*100)*'*'))
    sys.stdout.flush()
    time.sleep(0.5)