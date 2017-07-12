'''
共有以下几种情况：
1.n为0 ——mistake
2.n为1 ——若元素-1=0，只输出元素+1，否则输出元素-1，元素+1
3.n大于1——
 3.1若存在重复元素或相邻两元素的差大于2则输出mistake，跳出循环
 3.2若存在元素的下一个元素等于该元素+2,将其加入列表中，循环结束后
    若列表长度为1则输出该元素，否则输出mistake
 3.3若存在元素的下一个元素等于该元素+1，则将初值为1的迭代器自增1，
    循环结束后若迭代器的值为n,若第一个元素-1=0，只输出最后元素+1，
    否则输出第一元素-1，第二元素+1
'''
n = int(raw_input())
a = raw_input().split()
num = []
for i in range(0,n):
    num.append(int(a[i]))
num.sort()
a = []
z = 1
if(n>1):
    for i in range(0,n-1):
        if(num[i+1]==num[i]+1):
            z = z+1
        if(num[i+1]==num[i]+2):
            a.append(num[i]+1)
        elif(num[i+1]>num[i]+2 or num[i] == num[i+1]):
            print "mistake"
            break
        '''
        else:
            print "---"
            if(num[0]-1>0):
                print num[0]-1,num[n-1]+1
            else:
                print num[n-1]+1
            #print num[0]-1,num[n-1]+1
            '''
    if(len(a) == 1):
        print a[0]
    elif(len(a)>1):
        print "mistake"
    if(z == n):
        if(num[0]-1>0):
            print num[0]-1,num[n-1]+1
        else:
            print num[n-1]+1
elif(n == 1):
    if(num[0]-1>0):
        print num[0]-1,num[0]+1
    else:
        print num[0]+1

else:
    print "mistake"

