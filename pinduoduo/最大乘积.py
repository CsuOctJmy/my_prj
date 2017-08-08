# -*- coding: utf-8 -*-
'''
find 2 nin -
find 3 max +
'''
n = int(raw_input())
A = map(int,raw_input().split()[:n])
def f(a):
    resf = resz = 0
    zh1 = zh2 = zh3 = 0#最大的三个正数，按从大到小排列
    fu1 = fu2 = 0 #最小的两个负数，按从小到大排列
    flag = 0 #标记列表中是否有0
    for i in a:
        if i == 0:
            flag = 1
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
                zh3 = zh2
                zh2 = i
            elif i > zh3:
                zh3 = i
    if(fu1 != 0 and fu2 != 0 and zh1 != 0):
        resf = fu1 * fu2 * zh1#两负一正
    if(zh1 != 0 and zh2 != 0 and zh3 != 0):
        resz = zh1 * zh2 * zh3#三正
    return max(resf,resz)
print f(A)
