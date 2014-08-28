import random
import networkx as nx
import sys

GLOBAL_NUM_AGENTS= 50
GLOBAL_MAX_STEPS = 1000
GLOBAL_ERROR = 0.01

class Pig:
    
    def flip(self):
        if self.fashion == 0:
            self.fashion =1
        elif self.fashion == 1:
            self.fashion =0
        else:
            print "wtf"

    
    def cope_with_friends(self,G):
        counts = {0:0,1:0}
        friends = G[self]
        for friend in friends:
            if friend.fashion == 0:
                counts[0] = counts[0] + 1
            elif friend.fashion == 1:
                counts[1] = counts[1] + 1
            else:
                print "error"

        if counts[0] == counts[1]:
            pass


        elif counts[0] > counts[1]:
            self.fashion = 0

        elif counts[0] < counts[1]:
            self.fashion = 1
            
        else:
            print "erropr"


        if random.random() < GLOBAL_ERROR:
            self.flip()


            




        

        

    def __init__(self):
        self.fashion = random.randint(0,1)

pigs = []
for i in range(GLOBAL_NUM_AGENTS):
    pigs.append(Pig())

G = nx.Graph()
for i in range(GLOBAL_NUM_AGENTS):
    if i == 0:
        G.add_edge(pigs[0],pigs[GLOBAL_NUM_AGENTS-1])
    else:
        G.add_edge(pigs[i-1],pigs[i])



for s in range(GLOBAL_MAX_STEPS):
    output = ""
    for pig in pigs:
        output = output + str(pig.fashion)
    print output

    for pig in pigs:
        pig.cope_with_friends(G)







    


    

