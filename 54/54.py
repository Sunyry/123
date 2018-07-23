while True:
    A = ''
    B = ''
    s = input('请输入一串字符：')
    for i in range(len(s)):
        if i %2 == 0:
            A+=s[i]
        else:
            B+=s[i]
    print('A:',A)
    print('B:',B)
    print('合并后:',A+B)
