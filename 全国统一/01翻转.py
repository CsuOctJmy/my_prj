i = raw_input().split()
A = i[0]
B = i[1]
K = i[2]
remain = A%K
count = A/k
s = A+B
if(A==0 || remain == 0):
    ;
elif((s<=k) || (remain%2 == 1 && K%2 == 0)):
    count = -1
elif((K+remain)%2 == 0 && count >0 && B+k*count>=2*K):
    count = count +1
