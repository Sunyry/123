def function_bmi(name,weight,height):

    BMI = weight/height**2
    if BMI < 18.5:
        a = '过轻'
    elif BMI > 18.5 and BMI <24.9:
        a = '正常'
    elif BMI >24.9 and BMI <29.9:
        a = '过重'
    elif BMI >29.9:
        a = '肥胖'
    print('%s的身高为:%.02f米  体重为:%dkg\n%s的BMI指数为:\n您的体重%s'%(name,weight,height,BMI,a))


function_bmi('路人甲',60,1.83)
print('*'*60)
function_bmi('路人乙',50,1.6)
