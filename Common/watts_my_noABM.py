import matplotlib.pyplot as plt
import networkx as nx
import random

n = 100
k = 2   ## k < n/2 !!
p = 0.3


connected = False

while connected == False:

    nodes = list()

    G = nx.Graph()

    for index in range(n):
        nodes.append(index)

    for node in nodes:
        ##connect each node to k/2 neighbors
        for j in range (1, k//2 +1):
            my_id = node

            target_node_id_left = my_id - j
            if target_node_id_left < 0:
                target_node_id_left = n + (my_id - j)

            G.add_edge(node,target_node_id_left)

            target_node_id_right = my_id + j
            if target_node_id_right > n-1:
                target_node_id_right = my_id+j - n

            G.add_edge(node,target_node_id_right)


    #print nx.average_shortest_path_length(G)


    for edge in G.edges():
        s = edge[0]
        t = edge[1]

        if random.random() < p:
            new_t = random.choice(nodes)

            is_new_friend_good = False

            while is_new_friend_good == False:
                    
                new_t = random.choice(nodes)
                    
                if new_t != s and new_t != t:
                    is_new_friend_good = True



            G.remove_edge(s,t)
            G.add_edge(s,new_t)

    connected = nx.is_connected(G)

#nx.draw(G)
#plt.show()
print nx.average_shortest_path_length(G)
