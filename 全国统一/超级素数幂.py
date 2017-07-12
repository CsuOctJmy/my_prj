'''


import math
#n = int(raw_input())
prime = []
for i in range(2,math.pow(10,18)):
    for j in range(2,math.sqrt(i)):
        if(i%j == 0):
            break
    prime.append(i)
print prime
'''
import math
f = 0
n = long(raw_input())
sq1 = long(math.sqrt(n))
sq2 = long(math.sqrt(sq1))
for i in range(2,sq1):
    for j in range(2,sq2):
        if(i%j == 0):
            break
    p = i
    print p
    for k in range(2,n):
        if(n == p**k):
            f = 1
            print p,k
            break 
if(f!=1):
    print 'No'

