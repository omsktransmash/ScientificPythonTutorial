import random


n_spot = 20
g = 0.5
f = 0.1

class Tree:

    def spread(self,trees,index):
        ##burn left
        if index > 0:
            index_left = index -1
            trees[index_left].strike(trees)
        ##burn right
        if index < (len(trees)-1):
            index_right = index +1
            trees[index_right].strike(trees)

    def strike(self,trees):
        if self.status == 1:
            self.status = 0
            self.spread(trees,self.index)

    def grow(self):
        if random.random() <= self.g:
            self.status = 1

    def __init__(self,index,g):
        self.index = index
        self.g = g
        self.status = 0
        

trees = []
for index in range(0,n_spot):
    trees.append(Tree(index,g))
    
#for tree in trees:
#    print tree.status,
#print

for stage in range(0,10):

    ##grow phase

    for tree in trees:
        tree.grow()
        
    for tree in trees:
        print tree.status,
    print 

    ##strike phase
    for tree in trees:
        if random.random() <= f: ##lightning strike
            print tree.index
            tree.strike(trees)
        
    for tree in trees:
        print tree.status,
    print 



        
