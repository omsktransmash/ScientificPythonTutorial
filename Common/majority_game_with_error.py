import random
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

GLOBAL_NUM_AGENTS = 100
GLOBAL_MAX_STEPS = 10000

class Pig:

    def flip(self):
        if self.fashion == 0:
            self.fashion = 1
        else:
            self.fashion = 0
        

    def cope_with_friends(self,G):
        
        counts = {0:0,1:0}

        for friend in G[self]:
            #print "friend", friend.fashion
            
            if friend.fashion == 0:
                counts[0] = counts[0] + 1
            elif friend.fashion == 1:
                counts[1] = counts[1] + 1
        if counts[0] == counts[1]:
            ##error ??
            if random.random() < 0.01:
                self.flip()
        elif counts[0] > counts[1]:
            ##switch to 0
            self.fashion = 0
        elif counts[0] < counts[1]:
            ##switch to 1
            self.fashion = 1

        ##error show shifting in trends
#        if random.random() < 0.01:
#           self.flip()

        
        #print counts
        #print "my", self.fashion
       

    def __init__(self):
        self.fashion = random.randint(0,1)


def gen_network():
    ##Generate A Ring Network

    pigs = []
    for i in range(GLOBAL_NUM_AGENTS):
        pigs.append(Pig())

    G = nx.Graph()
    for i in range(GLOBAL_NUM_AGENTS):
        if i == 0:
            G.add_edge(pigs[0],pigs[GLOBAL_NUM_AGENTS-1])
        elif i > 0:
            G.add_edge(pigs[i-1],pigs[i])

    return pigs,G


def play_majority_game(pigs,G):
    #nodes=G.nodes()[:]
    #random.shuffle(nodes)

    
    for pig in pigs:
        
        pig.cope_with_friends(G)
    


(pigs,G) = gen_network()

graph = []
for s in range(GLOBAL_MAX_STEPS):
    
    fashions = []
    output = ""
    for pig in pigs:
        output = output + str(pig.fashion)
        fashions.append(pig.fashion)
    
    print output
    graph.append(fashions)
    
    if (0 not in fashions) or (1 not in fashions):
        break
    
    play_majority_game(pigs,G)

#plt.imshow(graph)
#plt.show()


