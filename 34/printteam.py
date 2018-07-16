print('2017~2018赛季NBA西部联盟前8名')
l = ['火箭','勇士','开拓者','爵士','鹈鹕','马刺','雷霆','森林狼']
for t,v in enumerate (l):
    if t%2 == 0:
        print()
        print(v,end = '\t')
    else:
        print(v)
