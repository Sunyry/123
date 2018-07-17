for i in range(7,101):
    n=1
    for j in range (2,int(i/2)+1):
        if i%j==0:
            n=0
    if n==1:
        print(i,end=',')
        print()
