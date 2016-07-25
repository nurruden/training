#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"
import pickle
account = open('account.db','rb')
account_file = pickle.loads(account.read())
print(account_file)
account.close()
account_file[1000]['balance'] -= 500
f = open('account.db','wb')
f.write(pickle.dumps(account_file))
f.close()
