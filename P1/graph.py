 # by using adjacentary matrix
nodes=[]
graph=[]
node_count=0

def add_node(n):
    global node_count
    if n in nodes:
        print("node already present")
    else:
        node_count+=1
        nodes.append(n)
        for n in graph: # here n is nested list in graph
            n.append(0)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)
# #
# deleting the node
def delete_node(n):
    global node_count
    if n not in nodes:
        print("not present in nodes")
    else:
        index1=nodes.index(n)
        node_count-=1
        nodes.remove(n)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)
# # # deleting the edge
# #
def delete_edge(v1,v2):
    if v1 not in nodes:
        print("not present")
    elif v2 not in nodes:
        print("v2 not present")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=0
        graph[index2][index1] = 0



# add edge
def add_edge(n1,n2,cost):
    if n1 not in nodes:
        print("not present in nodes")
    elif n2 not in nodes:
        print("not present in nodes")
    else:
        index1=nodes.index(n1)
        index2=nodes.index(n2)
        graph[index1][index2]=cost # undirected graph
        graph[index2][index1] = cost # undirected graph
        # if perform add edge on directed graph
        # index1 = nodes.index(n1) # directed graph
        # index2 = nodes.index(n2)# directed graph
        # graph[index1][index2] = cost # directed graph

# #
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"3"), end=" ")
            # print(graph[i][j],end=" ")
        print()

print("before adding")
print(nodes)
print(graph)
print("after adding")
add_node("A")
add_node("B")
add_node("C")
add_edge('A','B',10)
add_edge('A','C',20)
add_edge('B','C',30)
print(nodes)
print(graph)
print_graph()
delete_node("C")
delete_edge('B','C')
print("after deleting edge")
print_graph()
