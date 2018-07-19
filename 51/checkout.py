l =[]
while True:
    a = float(input('输入商品金额(输入0表示输入完毕)：'))
    if a == 0:
        break
    l.append(a)

def fun_checkout():
    Sum = 0
    for i in l:
        Sum +=i
    if Sum >500 and Sum <1000:
        b =0.9*Sum
        print('合计金额:%.2f 应用金额:%.2f'%(Sum,b))
    elif Sum>1000 and Sum<2000:
        b =0.8*Sum
        print('合计金额:%.2f 应用金额:%.2f'%(Sum,b))
    elif Sum>2000 and Sum<3000:
        b =0.7*Sum
        print('合计金额:%.2f 应用金额:%.2f'%(Sum,b))
    elif Sum>=3000:
        b =0.6*Sum
        print('合计金额:%.2f 应用金额:%.2f'%(Sum,b))
fun_checkout()
