#-*-coding:utf-8-*-
#/usr/bin/env python

li = [11,2,33,4,555,66,75,66]
for j in range(1,len(li)):
    for i in range(len(li) -1 ):
        current = li[i]
        next_value = li[i + 1]
        if current > next_value:
            #current,next_value = next_value,current
            # temp = li[i]
            # li[i] = li[i+1]
            # li[i + 1] = temp
            li[i],li[i+1]=li[i+1],li[i]

print(li)
