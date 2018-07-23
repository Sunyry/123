num = 0
for i in range(1,100):
    if i%7 == 0:
        num+=1
        continue
    elif i%10 == 7:
        num+=1
print(num)
