print('电视剧收视率排行榜：')
l = [(1.4,'《Give up,hold on to me》'),(1.343,'《The private dishe of the husbands》'),(0.92,'《My father-in-lawwill do martiaiarts》'),(0.862,'《North Canton still believe in love》'),(0.553,'《Impossible task》'),(0.441,'《Sparrow》'),(0.164,'《East of dream Avenue》'),(0.394,'《Distant distance》'),(0.259,'《Theprodigal son of the new frontier town》')]
l.sort(reverse=True)
for i in l:
    print('%s 收视率：%.3f%%'%(i[1],i[0]),end = '\n')
