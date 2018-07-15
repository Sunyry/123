rose = int(input('在古希腊的神话中，玫瑰集爱情与美丽于一身，所以人们常用玫瑰来表达爱情但是不同的朵数的玫瑰花代表的含义是不同的请您输入您想送几多玫瑰花，我会告诉你玫瑰花的含义:'))
# 可以考虑送1朵、3朵、99朵、108朵、999朵
if rose == 1:
    print('%d朵:你是我的唯一!'%rose)
elif rose == 3:
    print('%d朵:I LOVE YOU!'%rose)
elif rose == 10:
    print('%d朵:十全十美'%rose)
elif rose == 99:
    print('%d朵:天长地久'%rose)
elif rose == 999:
    print('%d:朵你真有钱'%rose)
else:
    print('我也不知道了，你可以考虑送1朵、3朵、10朵....')

