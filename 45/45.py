a=float(input('请输入收入：'))
b= a - 3500
if a <= 3500:
    print('无税收')
elif b<=1500:
    print('税收为:%d'%(b*0.03))
    print('扣完税的收入:%d'%(a-b*0.03))
elif b>1500 and b<=4500:
    print('税收为:%d'%(b*0.1))
    print('扣完税的收入:%d'%(a-b*0.1))
elif b>4500 and b<=9000:
    print('税收为:%d'%(b*0.2))
    print('扣完税的收入:%d'%(a-b*0.2))
elif b>9000 and b<=35000:
    print('税收为:%d'%(b*0.25))
    print('扣完税的收入:%d'%(a-b*0.25))
elif b>35000 and b<=55000:
    print('税收为:%d'%(b*0.3))
    print('扣完税的收入:%d'%(a-b*0.3))
elif b>55000 and b<=80000:
    print('税收为:%d'%(b*0.35))
    print('扣完税的收入:%d'%(a-b*0.35))
elif b>80000:
    print('税收为:%d'%(b*0.45))
    print('扣完税的收入:%d'%(a-b*0.45))
