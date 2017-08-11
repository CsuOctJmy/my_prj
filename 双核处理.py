'''
n = int(raw_input())
m = raw_input().split()
a = []
s = set()
sum = 0
for i in range(0,n):
    tmp = int(m[i]/1024)
    ah.append(tmp)
    sum = sum+tmp
s.add(0)
for i in range(0,n):
    added = set()
    for j in range(0,len(s)):
        added.add()
'''
n = int(raw_input())
m = map(int,raw_input().split())
m = [i/1024 for i in m]
