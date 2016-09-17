#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"

import pickle
import json
accounts = {1000:{'name':'allan','email':'323@qq.com','password':'123','balance':15000,'phone':1233212123,'bank_acc':{'ICBC':1234,'CBC':12331}},
            1001:{'name':'felix','email':'123@qq.com','password':'321','balance':15000,'phone':1232212123,'bank_acc':{'ICBC':3234,'CBC':12231}}}
# print(pickle.dumps(accounts))
f =open('account.db','wb')
# f.write(pickle.dumps(accounts))
# f.close()

# account_db = pickle.dump(accounts,f)
# print(account_db)
# print(json.dumps(accounts))
f.write(bytes(json.dumps(accounts)))
f.close()