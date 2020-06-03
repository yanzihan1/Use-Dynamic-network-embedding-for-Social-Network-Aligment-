d=open('following2.number')
fff=open('following1.number')
dd=set()
f=set()
ppp=[]
c=[]
for i in d:
    ii=i.split()
    ppp.append(int(ii[0]))
    ppp.append(int(ii[1]))
    c.append(ppp)
    ppp=[]
for j in fff:
    jj=j.split()
    f.add(int(jj[0]))
    f.add(int(jj[1]))
for line in c:
    if line[0] not in f and line[1] not in f:
        print(line)
print(len(c))