n = int(raw_input())
s = raw_input().split()[:n]
a = []
l = range(n)
l.reverse()
for i in l:
    if s[i] not in a:
        a.append(s[i])
s = ''
mm = range(len(a))
mm.reverse()
for i in mm:
    s += a[i]+' '
print s[:n-1]
'''
a = list(set(s))
a.sort(key=s.index)
print a

for i in s:
    loc = s.index(i)
    if i not in s[loc+1:]:
        print i
        a.append(i)
        #print i,loc
print a

    
print s
for i in xrange(n-1):
    print s[i]
    #if s[i] in s[i+1:n]:
        #s.pop(i)
#print s
'''
