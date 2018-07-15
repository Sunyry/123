import random

# 玩家出数
player = int(input())

# 电脑出数
computer = random.randint(1,10)
if player == computer:
    print('胜利')
else:
    print('loser')
