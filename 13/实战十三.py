print('为了您和他人的安全，严禁酒后驾车!')
a = int(input('请输入每100毫升血液的酒精含量'))
if a>20:
    if a>=20 and a<=80:
        print('已经到达酒后驾驶标准，请不要开车!')
    else:
        print('已经到达醉酒驾驶标准，请不要开车!') 
else:
    print('您还构不成饮酒行为，可以开车，但是要注意安全')
