number = int(input('今有物不知其数，三三之数剩二，五五之数剩三，七七之数是剩二，问几>    何请输入您认为符合条件的数'))
if number%3 == 2 and number%5 == 3 and number%7 == 2:
    print('符合条件')
else:
    print('不符合条件')

