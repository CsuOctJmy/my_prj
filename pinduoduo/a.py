def f(x,y):
    b = []
    for i in y:
        a = []
        tmps = 0
        for j in x:
            tmp = int(i)*int(j)
            tmpg = tmp % 10 + tmps
            tmps = tmp / 10
            a.append(tmpg)
        b.extend(a)
    res = 0
    yiwei = 0
    for i in b:
        res += i<<yiwei
        yiwei += 1
    return res
sin = raw_input().split()[:2]
print f(sin[0],sin[1])
