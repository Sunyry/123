print('-----跳一跳，输入‘退出’即可游戏--------\n欢迎回来，请开始游戏\n请输入\\（中心、音乐模块、微信支付模块）')
#定义一个变量jump
while True:
    jump = input('请输入：')
    if jump =='中心':
        print('您的分数为32')
        print()
    elif jump =='音乐模块':
        print('您的分数为30')
        print()
    elif jump =='微信支付模块':
        print('您的分数为42')
        print()
    elif jump =='退出':
        print('已退出')
        break
    else:
        print('输入有误，请重新输入')

