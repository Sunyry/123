while True:
    s = input('输入一串数字')
    count = 0
    for i in s:
        if i.isdigit() or i.islower() == True:
            count=count
        else:
            count+=1
            break
    if count == 0:
        print('您输入的字符全是由小写字母和数字构成')
    else:
        print('不符合条件')
