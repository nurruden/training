#-*-coding:utf-8-*-
#/usr/bin/env python
__author__ = "Allan"

l1 = ["alex",22,33,44,55]
l2 = ["is",22,33,44,55]
l3 = ["good",22,33,44,55]
l4 = ["guy",22,33,44,55]

com = zip(l1,l2,l3,l4)
for i in com:
    if i == ('alex', 'is', 'good', 'guy'):
        str = "_"
        print(str.join(i))
    else:
        pass
#输出结果:
#alex_is_good_guy