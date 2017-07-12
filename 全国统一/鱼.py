def ischi(a,b):
    if((a>= 2*b and a<=10*b) or(b>=2*a and b<=10*a)):
        return 1
    else:
        return 0
s = raw_input()
minSize,maxSize = map(int,s.split())
#minSize,maxSize = raw_input().split(" ")
n = int(raw_input())
m = raw_input()
m = m.split()
if(n>len(m)):
    n = len(m)

fishSize = []
for i in range(0,n):
    fishSize.append(int(m[i]))
#fishSize.sort()#0最小 n-1最大,
#则放入鱼的size应满足：size<fishSize[0]*2 or size>fishSize[n-1]*10
#print f(minSize,maxSize,fishSize)
num = 0
for i in range(minSize,maxSize+1):
    f = 0
    for j in fishSize:
        if(ischi(i,j) == 1):
            f = 0
            break
        else:
            f = 1
    if(f):
        num = num+1
print num
