def str_list_to_float(str_list):
    return [float(item) for item in str_list]


def str_list_to_int(str_list):
    return [int(item) for item in str_list]


def read_edges(train_filename):
    graph = {}
    nodes = set()
    train_edges = read_edges_from_file(train_filename)

    for edge in train_edges:
        nodes.add(edge[0])
        nodes.add(edge[1])
        if graph.get(edge[0]) is None:
            graph[edge[0]] = []
        if graph.get(edge[1]) is None:
            graph[edge[1]] = []
        graph[edge[0]].append(edge[1])
        #graph[edge[1]].append(edge[0])  #isdereat

    return len(nodes), graph,nodes

def read_edges_from_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        edges = [str_list_to_int(line.split()) for line in lines]
    return edges
network_path='network_05'
_,graph,_,=read_edges(network_path)
fw=open('user_fileasdsa','w')
for i,j in graph.items():
    if i<5000:
        #fw.write(str(i)+' '+str(len(j))+'\n')
        for node in j:
            if node<5000:
               fw.write(str(node)+' '+str(i)+'\n')
        #fw.write('\n')


