# # #how to implement stack
# # # by using list
# # # from django.template.defaultfilters import length
# # #
# # # stack1=[]
# # # n=int(input("enter how many elements in stack"))
# # # def stack():
# # #
# # #     if length(stack1)==n:
# # #         print("stack is full")
# # #     else:
# # #         for i in range(n):
# # #             element = int(input("enter ur element"))
# # #             stack1.append(element)
# # #     return stack1
# # #
# # # s1=stack()
# # # print(s1)
# #
# # # now we are discus about queue
# #
# # # queue define by using list
# #
# # queue=[]
# # n=int(input("enter how many elements in queue"))
# #
# # def Queue():
# #     if len(queue)==n:
# #         print("queue is full")
# #     else:
# #         for i in range(n):
# #             element=int(input("enter element"))
# #             queue.insert(0,element)
# #         return queue
# #
# # q1=Queue()
# # print(q1)
# #
#
#
#  # by using adjacentary matrix
# nodes=[]
# graph=[]
# node_count=0
#
# def add_node(n):
#     global node_count
#     if n in nodes:
#         print("node already present")
#     else:
#         node_count+=1
#         nodes.append(n)
#         for n in graph: # here n is nested list in graph
#             n.append(0)
#         temp=[]
#         for i in range(node_count):
#             temp.append(0)
#         graph.append(temp)
# # #
# # deleting the node
# def delete_node(n):
#     global node_count
#     if n not in nodes:
#         print("not present in nodes")
#     else:
#         index1=nodes.index(n)
#         node_count-=1
#         nodes.remove(n)
#         graph.pop(index1)
#         for i in graph:
#             i.pop(index1)
# # # # deleting the edge
# # #
# def delete_edge(v1,v2):
#     if v1 not in nodes:
#         print("not present")
#     elif v2 not in nodes:
#         print("v2 not present")
#     else:
#         index1=nodes.index(v1)
#         index2=nodes.index(v2)
#         graph[index1][index2]=0
#         graph[index2][index1] = 0
#
#
#
# # add edge
# def add_edge(n1,n2,cost):
#     if n1 not in nodes:
#         print("not present in nodes")
#     elif n2 not in nodes:
#         print("not present in nodes")
#     else:
#         index1=nodes.index(n1)
#         index2=nodes.index(n2)
#         graph[index1][index2]=cost # undirected graph
#         graph[index2][index1] = cost # undirected graph
#         # if perform add edge on directed graph
#         # index1 = nodes.index(n1) # directed graph
#         # index2 = nodes.index(n2)# directed graph
#         # graph[index1][index2] = cost # directed graph
#
# # #
# def print_graph():
#     for i in range(node_count):
#         for j in range(node_count):
#             print(format(graph[i][j],"3"), end=" ")
#             # print(graph[i][j],end=" ")
#         print()
#
# print("before adding")
# print(nodes)
# print(graph)
# print("after adding")
# add_node("A")
# add_node("B")
# add_node("C")
# add_edge('A','B',10)
# add_edge('A','C',20)
# add_edge('B','C',30)
# print(nodes)
# print(graph)
# print_graph()
# delete_node("C")
# delete_edge('B','C')
# print("after deleting edge")
# print_graph()
# #
# # graph implementation by using adjacentary list
# #
# graph={}
# def add_node(n):
#     if n in graph:
#         print("already present")
#     else:
#         graph[n]=[]
# def add_edge(v1,v2,cost):
#     if v1 not in graph:
#         print("not in graph")
#     elif v2 not in graph:
#         print("not in graph")
#     else:
#         # graph[v1].append(v2)
#         # graph[v2].append(v1)
#         # perform with weighted graph
#         l1=[v2,cost]
#         l2=[v1,cost]
#         graph[v1].append(l1)
#         graph[v2].append(l2)
#
# # deleting node and edge
#
# def delete_node(n):
#     if n not in graph:
#         print("not present")
#     else:
#         graph.pop(n)
#         for i in graph:
#             list1=graph[i]
#             if n in list1:
#                 list1.remove(n)
#
# def delete_edge(v1,v2):
#     if v1 not in graph:
#         print("not present")
#     elif v2 not in graph:
#         print("not present")
#     else:
#         if v1 in graph[v2]:
#             graph[v1].remove(v2)
#             graph[v2].remove(v1)
#
#
# add_node('A')
# add_node('B')
# add_node('C')
# add_edge('A','B',20)
# add_edge('A','C',30)
# print(graph)
# print("after deleting node")
# delete_edge('A','C')
# print(graph)
# from P1.DSA.ex import stack


# def even(n):
#     odd_list=[]
#     even_list=[]
#     integers=[]
#     while n<=20:
#         integers.append(n)
#         if n%2==0:
#             even_list.append(n**2)
#         elif n%2!=0:
#             odd_list.append(n**2)
#         n+=1
#     print("integers")
#     for i in integers:
#         print(i, end=" ")
#     print()
#     print("integers in reverse")
#     print(integers[::-1])
#     print()
#     print("even numbers")
#     for i in even_list:
#         print(i,end=" ")
#     print()
#     print("odd numbers")
#     for i in odd_list:
#         print(i,end=" ")
# res1=even(1)


# a,b=map(str,input("enetr ur values by separating space").split(" "))
# print(a,b)










# def Math_Table(n):
#     i=0
#     while i<=10:
#         print(f'{5}x{i}=={n*i}')
#         i+=1
# a1=Math_Table(5)

# 65,66,67,68,69,70
# print(ord('a'))
# def Alp(alphabet1,alpabet2):
#     n=ord(alphabet)
#     n2=ord(alpabet2)
#     while n <= n2:
#         print(chr(n),end=" ")
#         char=chr(n)
#         print(ord(char),end=" ")
#         n += 1
# alphabet=(input("enter ur alphabet1"))
# alphabet2=(input("enter ur alphabet2"))
# Alp(alphabet,alphabet2)

#

# def Genarate_Prime(n):
#     for i in range(5,0,-1):
#         for j in range(5,0,-1):
#             print(i,end=" ")
#         print()
# Genarate_Prime(5)


# stack implementation by using list
#
# def Stack1():
#     stack1=[1,2,3,4]
#     size=int(input("enter ur size of the stack"))
#     n=int(input("enter ur option"))
#     i=1
#     while i<=size:
#         if n == 1:
#             ele = int(input("enter ur element"))
#             stack1.append(ele)
#         elif n == 2:
#             print(stack1[-1])
#             pop_ele = stack1.pop()
#             print(pop_ele)
#         else:
#             pass
#         i+=1
#         print(stack1)
# Stack1()

#
# n=5
# for i in range(n):
#     print(" "*(n-i-1)+'*'*(2*i+1))
#
# for j in range(1,6):
#     print("*",end=" ")
# print()
# for k in range(1,5):
#     for i in range(1,6):
#         if i == 1 or i == 5:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
# #     print()
# for r in range(1,6):
#     print("*",end=" ")

# n=6
# for i in range(1,n+1):
#     print("*"*i+ " "*(2*(n-i)) +"*"*i)
# for j in range(n,0,-1):
#     print("*" * j + " " * (2 * (n - j)) + "*" * j)

#
n=6
for i in range(n):
    for j in range(n):
        print(" ",end="")
    n=n-1
    for k in range(2*i+1): # 0,1
        if k==0 or k==2*i:
            print("*",end=" ")
        else:
            print(" ",end="")
    print()
for i in range(n):
    for j in range(n,0,-1):
        print(" ",end="")
    n=n-1
    for k in range(2*i+1): # 0,1
        if k==0 or k==2*i:
            print("*",end=" ")
        else:
            print(" ",end="")
    print()



























