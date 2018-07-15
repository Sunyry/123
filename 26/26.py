num = 100
while num>=100 and num<=999:
    a=num//100
    b=num//10%10
    c=num%10
    if num == a*a*a+b*b*b+c*c*c:
        print("%d"%num)
    num+=1
