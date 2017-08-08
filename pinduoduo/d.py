'''
find 2 nin -
find 3 max +
'''
n = int(raw_input())
A = map(int,raw_input().split()[:n])
'''
zh = []
fu = []
for i in A:
    if i == 0:
        continue
    elif (i < 0):
        fu.append(i)
        ma = max(fu)
        if((len(fu)>=2) and (i < ma)):
            fu.remove(ma)
    elif i > 0:
        zh.append(i)
        mi = min(zh)
        if((len(zh)>=3) and (i>mi)):
            zh.remove(mi)
resf = 1
resz = 1
ma = max(zh)
if(len(fu) == 2) or (len(zh) == 3):
    for i in fu:
        resf *= i
    resf *= ma
    for i in zh:
        resz *= i
    print max(resf,resz)
else:
    print 0
'''
def f(a):
    zh1 = zh2 = zh3 = 1
    fu1 = fu2 = -1
    for i in a:
        if i == 0:
            continue
        elif i<0:
            if i < fu1:
                fu2 = fu1
                fu1 = i
            elif i < fu2:
                fu2 = i
        else:
            if i > zh1:
                zh3 = zh2
                zh2 = zh1
                zh1 = i
            elif i > zh2:
                zh1 = zh2
                zh2 = i
            elif i > zh3:
                zh3 = i
    resf = fu1 * fu2 * zh1
    resz = zh1 * zh2 * zh3
    return max(resf,resz)
print f(A)
