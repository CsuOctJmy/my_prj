s = raw_input().split()
a = list(s[0])
b = list(s[1])
n = len(a)
n1 = len(b)
count = 0
if(n>n1):
    n = n1
for i in range(0,n):
    if((a[i] == 'A' and b[i] =='T') or (a[i] == 'T' and b[i] =='A')
       (a[i] == 'C' and b[i] =='G') or (a[i] == 'G' and b[i] =='C')):
        continue
    else:
        count = count+1
