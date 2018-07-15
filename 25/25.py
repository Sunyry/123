'''
求1~100之间能被7整除，但是同时不能被5整除的所有整数
'''
num = 1 
while num<100:
    if num%7 ==0 and num%5 !=0:
        print('%d'%num)
    num+=1

