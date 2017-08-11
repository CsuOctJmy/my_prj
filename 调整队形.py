a = raw_input()
bi = gi = bs = gs = 0
i = 0
for j in a:
    if j == 'B':
        bi += i
        bs += 1
    elif j == 'G':
        gi += i
        gs += 1
    i += 1
print bi,bs,gi,gs
#若把男孩放左边
bi -= (bs-1)*bs/2
#若把女孩放左边
gi -= (gs-1)*gs/2
if(bi>gi):
    print gi
else:
    print bi
