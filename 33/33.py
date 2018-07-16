string = input('请输入一行字符串')
num = 0
for i in string:
    if i.isdigit():
        num+=1
print('字符串中包含数字的个数%d'%num)
