import networkx as nx
import matplotlib.pyplot as plt
import random 

n = 100
k = 4
p = 0.002

G = nx.Graph()

nodes =[]

for index in range(n):
    nodes.append(index)

for node in nodes:
    for j in range(1,k//2+1):
        my_id = node

        target_node_id_left = my_id - j
        if target_node_id_left < 0:
            target_node_id_left = n + (my_id - j)

        target_node_id_right = my_id + j
        if target_node_id_right > n-1:
            target_node_id_right = my_id + j - n

        G.add_edge(node,target_node_id_left)
        G.add_edge(node,target_node_id_right)

print nx.average_shortest_path_length(G)

for edge in G.edges():
    if random.random() < p:

        me = edge[0]
        friend = edge[1]

        new_target = random.choice(nodes)
        while new_target == me or new_target == friend:
            new_target = random.choice(nodes)

        G.remove_edge(me, friend)
        G.add_edge(me,new_target)

print nx.average_shortest_path_length(G)

nx.draw(G)
plt.show()
