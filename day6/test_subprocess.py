#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import subprocess
# subprocess.call('ls')
# ret = subprocess.check_call(["ls", "-al"])
# ret1 = subprocess.check_call("ls -al",shell=True)
#
# print(ret1)



obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
obj.stdin.write("print(1)\n")
obj.stdin.write("print2")
obj.stdin.close()

cmd_out = obj.stdout.read()
obj.stdout.close()
cmd_error = obj.stderr.read()
obj.stderr.close()

print(cmd_out)
print(cmd_error)