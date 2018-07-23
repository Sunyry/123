d ={'考神套餐':'13元','单人套餐':'9.9元','情侣套餐':'20元'}
print('米线店套餐如下：',end='')
for i,v in enumerate(d.keys(),1):
    print('%d.%s'%(i,v),end=' ')
print()
for i,v in d.items():
    print('%s%s'%(i,v))
