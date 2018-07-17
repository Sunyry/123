friend_name='@大学生精英班@扎克伯格@俞敏洪'
print('您@的好友有：')
for i in friend_name.split('@'):
    if i == '':
        pass
    else:
        print(i)
