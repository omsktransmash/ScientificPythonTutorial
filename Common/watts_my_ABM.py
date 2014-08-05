import matplotlib.pyplot as plt
import networkx as nx
import random

n = 100
k = 2   ## k < n/2 !!
p = 0.3


class Node:

    def __init__(self,id):
        self.id = id
        self.friends = list()

    def make_friend(self,target_node):
        self.friends.append(target_node)

    def remove_friend(self,target_node):
        self.friends.remove(target_node)


connected = False

while connected == False:

    G = nx.Graph()

    nodes = list()
    for index in range(n):
        node = Node(index)
        nodes.append(node)

    for node in nodes:
        ##connect each node to k/2 neighbors
        for j in range (1, k//2 +1):
            my_id = node.id

            target_node_id_left = my_id - j
            if target_node_id_left < 0:
                target_node_id_left = n + (my_id - j)
            
            target_node_left = nodes[target_node_id_left]
            node.make_friend(target_node_left)

            target_node_id_right = my_id + j
            if target_node_id_right > n-1:
                target_node_id_right = my_id+j - n

            target_node_right = nodes[target_node_id_right]
            node.make_friend(target_node_right)

 

    ##recombination

    for node in nodes:
        for friend in node.friends:
            if random.random() < p :

                is_new_friend_good = False

                while is_new_friend_good == False:
                    
                    new_target = random.choice(nodes)
                    
                    if new_target != node and new_target != friend:
                        is_new_friend_good = True


                node.friends.remove(friend)
                node.friends.append(new_target)
        

    G = nx.Graph()
    
    for node in nodes:
        
        for friend in node.friends:

            G.add_edge(node.id,friend.id)    
    


    connected = nx.is_connected(G)

nx.draw(G)
plt.show()
print nx.average_shortest_path_length(G)
