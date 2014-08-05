import networkx as nx
import matplotlib.pyplot as plt
import random
import mysql.connector

cnx = mysql.connector.connect(
    user='abm',
    password='dpdlqldpa',
    host='137.68.160.158',
    database='abm_seminar')

cursor = cnx.cursor()


n = 100
k = 4
p = 0.002

for s in range(0,20):

    p = 0.05 * s
    
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


    for edge in G.edges():
        if random.random() < p:

            me = edge[0]
            friend = edge[1]

            new_target = random.choice(nodes)
            while new_target == me or new_target == friend:
                new_target = random.choice(nodes)

            G.remove_edge(me, friend)
            G.add_edge(me,new_target)

    s_p = nx.average_shortest_path_length(G)
    values = (p,s_p)
    print values
    
    sql = "INSERT INTO jp_hw (p, s_p) VALUES(%s,%s)"
    cursor.execute(sql,values)

cnx.commit()

cursor.close()
cnx.close()


