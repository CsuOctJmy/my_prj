n = int(raw_input())
tX = map(int,raw_input().split())
tY = map(int,raw_input().split())
loc = map(int,raw_input().split())
time = map(int,raw_input().split())
walk = (abs(loc[0])+abs(loc[1]))*time[0]#纯步行
#步行+打车
fast = walk
for i in xrange(n):
    tmp = (abs(tX[i])+abs(tY[i]))*time[0]+(abs(loc[0]-tX[i])+abs(loc[1]-tY[i]))*time[1]
    if(tmp < fast):
        fast = tmp
print fast
