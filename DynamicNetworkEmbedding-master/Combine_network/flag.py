f=open('amherst_558_0.25_nw_init')
fw=open('flag','w')
node=set()
for i in range(0,10433):
    node.add(i)
print(max(node))
c=0
for p in node:
    if c==5:
        fw.write(str(p) + ' ' + str(c) + '\n')
        c=0
    else:
        fw.write(str(p)+' '+str(c)+'\n')
        c+=1
