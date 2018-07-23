l = [1,2,3,4,5,6,7]
print(l)
for i,v in enumerate(l):
    lenth = int(len(l))
    n = lenth//2
    if i == n:
        print(v)
