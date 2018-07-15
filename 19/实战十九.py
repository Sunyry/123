a =int( input('请输入身高'))
b =int(input('请输入身价'))
c =int(input('请输入颜值分'))
if a>180 and b>1000000 and c>99:
    print("高富帅")
elif b>1000000 and c>99:
    print('富帅')
elif c>99:
   print('帅')
elif a<160 and b<100 and c<60:
    print('矮锉穷')

