string = input('输入一串字符串:')
s = string.lower()
d ={}
for i in s:
    if i in d:
         d[i]+=1
    else:
        d[i]=1
print(d)
