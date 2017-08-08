n = int(raw_input())
h = map(int,raw_input().split()[:n])
m = int(raw_input())
w = map(int,raw_input().split()[:n])
h.sort()
w.sort()
res = 0
i = 0
while((i < len(h)) and (i < len(w))):
    if w[i] >= h[i]:
        res += 1
    i += 1
print res
    
