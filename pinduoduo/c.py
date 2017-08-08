size = map(int,raw_input().split()[:2])
M = size[0]
N = size[1]
mat = []
for i in M:
    s = raw_input()
    mm = []
    for j in s:
        mm.append(j)
    mat.extend(mm)
