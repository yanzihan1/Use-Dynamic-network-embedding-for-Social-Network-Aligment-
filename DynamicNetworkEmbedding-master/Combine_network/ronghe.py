#this function shows how to combine to network
f_t=open('twitter/following1.number')#twitter
f_f=open('foursquare/following1.number')#foursqare
f_train=open('train')#train_anchor
fw=open('network_05','w')

train=[]
twitter=[]
foursqare=[]
mat=[]
for train_node in f_train:
    train.append(int(train_node))
for t_node in f_t:#base on t_node
    t_nodes=t_node.split()
    # node 5313 is total number
    if int(t_nodes[0]) in train and int(t_nodes[0]) not in train:
        mat.append(int(t_nodes[0]))
        mat.append(int(t_nodes[1])+5313)
        twitter.append(mat)
        mat=list()
    if int(t_nodes[1]) in train and int(t_nodes[0]) not in train:
        mat.append(int(t_nodes[1]))
        mat.append(int(t_nodes[0])+5313)
        twitter.append(mat)
        mat=list()
    if int(t_nodes[1]) in train and int(t_nodes[0]) in train:
        mat.append(int(t_nodes[1]))
        mat.append(int(t_nodes[0]))
        twitter.append(mat)
        mat = list()
    else:
        mat.append(int(t_nodes[1])+5313)
        mat.append(int(t_nodes[0])+5313)
        twitter.append(mat)
        mat = list()
#foursqare
fo=[]
for f_node in f_f:
    f_nodes=f_node.split()
    fo.append(int(f_nodes[0]))
    fo.append(int(f_nodes[1]))
    foursqare.append(fo)
    fo=[]
#total
total=[]
l=[]
for line in twitter:
    l.append(line[0])
    l.append(line[1])
    foursqare.append(l)
    l=[]
for t_line in foursqare:
    t_lines=[str(x) for x in t_line]
    t_liness=" ".join(t_lines)
    fw.write(t_liness+'\n')




