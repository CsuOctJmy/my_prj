n = int(raw_input())
word = []
arr = []
count = 0
for i in range(0,n):
    word.append(raw_input())
for i in range(0,len(word)):
    if(word[i] not in arr) :
       count = count + 1
       for j in range(0,len(word[i])-1):
            arr.append(word[i][j+1:]+word[i][:j+1])
print count
