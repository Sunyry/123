l = []
def function_BMI_upgrade(name,weight,height):
    BMI = weight/height**2
    if BMI < 18.5:
        return('BMI指数是:%f\n您的体重过轻\n'%BMI)
    elif BMI > 18.5 and BMI <24.9:
        return('BMI指数是:%f\n您的体重正常\n'%BMI)
    elif BMI >24.9 and BMI <29.9:
        return('BMI指数是:%f\n您的体重过重\n'%BMI)
    elif BMI >29.9:
        return('BMI指数是:%F\n您的体重肥胖\n'%BMI)

for i in range(1,6):
    name = input('姓名：')
    weight = float(input('体重'))
    height = float(input('身高'))
    r = function_BMI_upgrade(name,weight,height)
    d ={'name':name,'weight':weight,'height':height,'r':r}
    l.append(d)
for d in l:
    print('===========%s============\n体重:%.2fkg\t身高:%.2fm\n%s'%(d['name'],d['weight'],d['height'],r))

