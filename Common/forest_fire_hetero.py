import random


n_spot = 20
g = 0.5
f = 0.2
adjust = 0.1


class Tree:

    def adjust_g(self):
        if self.burnt == True:
            self.g = self.g - adjust
        else:
            self.g = self.g + adjust

        ## fire burned any tree which has large g
            
        self.burnt = False

        if self.g < 0.0:
            self.g = 0.0
        if self.g > 1.0:
            self.g = 1.0

    def spread(self,trees,index):
        ##burn left
        if index > 0:
            index_left = index -1
            trees[index_left].burn(trees)
        ##burn right
        if index < (len(trees)-1):
            index_right = index +1
            trees[index_right].burn(trees)

    def burn(self,trees):
        self.burnt = True
        
        if self.status == True: ##if tree is here
            self.status = False
            self.spread(trees,self.index)

    def grow(self):
        if random.random() <= self.g:
            self.status = True

    def __init__(self,index,g):
        self.index = index
        self.g = g
        self.status = False
        self.burnt = False
        

trees = []
for index in range(0,n_spot):
    trees.append(Tree(index,g))
    
#for tree in trees:
#    print tree.status,
#print

for stage in range(0,100):

    ##grow phase

    for tree in trees:
        tree.grow()
        
    for tree in trees:
    #    print tree.status,
    #print
        pass

    ##strike phase
    for tree in trees:
       if random.random() <= f: ##lightning strike
           tree.burn(trees)
           
    for tree in trees:
        tree.adjust_g()

    total_g = 0.0
    for tree in trees:
        print "%3.2f" %tree.g,
        total_g = total_g + tree.g
    print total_g/len(trees)




        
