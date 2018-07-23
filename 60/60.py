a = ['T40','长春-北京','00:12','12:20','12:08']
b = ['T298','长春-北京', '00:16','10:50','10:44']
c = ['Z158','长春-北京','12:48','21:06','08:18']
d = ['Z62','长春-北京','21:58','06:08','8:20']
o = [a,b,c,d]
for i in ['车次','出发站-到达站','出发时间','到达时间','历时']:
    print(i,end='\t\t')
print()
for i in o:
    print(i[0]+'\t\t'+i[1]+'\t\t'+i[2]+'\t\t\t'+i[3]+'\t\t\t'+i[4])
num = input('请输入购买车次：')
count = 0
while True:
    for i in o:
        if i[0]==num:
            count=1
            break
    if count == 0:
        num=input('输入错误，重新输入')
    else:
        break
people = input('请输入乘车人(用,隔开):')
for i in o:
    if i[0]==num:
        print('你已购%s次列车%s %s开，请%s尽快换取纸质车票。【铁路客服】'%(i[0],i[1],i[2],people))

    
