year = int(input())
if ((year%4 == 0 and year%100 != 0) or (year%400==0)):
    print('闰年%d'%year)
else:
    print('平年%d'%year)
