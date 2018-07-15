while True:
    print("能量来源如下：生活缴费、行走捐、共享单车、线下支付、网络购票")
  #定义一个变量energy
    energy = input ('查询能量来源！退出程序请输入0:')  
    if energy =='生活缴费':
        print('300')
        print()
    elif energy =='行走捐':
        print('200')
        print()
    elif energy =='共享单车':
        print('350')
        print()
    elif energy =='线下支付':
        print('380')
        print()
    elif energy =='网络购票':
        print('500')
        print()
    elif energy == '0':
        print('已退出')
        break
