accountc = '12345678'
passward = '123456'
money = 200
a1 = input()
p1 = input()
if a1 == accountc and p1 == passward:
    print('登陆成功，输入取钱金额')
    m1=int(input())
    if m1>money:
        print('没钱取毛线')
    else:
        print('取钱成功，还剩余',money-m1)
else:
    print('非法账户')

