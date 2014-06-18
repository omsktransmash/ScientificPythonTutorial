import random

class Tree:
    grown = False

    def grow(self):
        self.grown = True

    def burn(self,my_index,trees):

        if self.grown == True:
            
            self.grown = False

            if my_index > 0:
                left_tree = trees[my_index - 1]
                left_tree.burn(my_index - 1,trees)
            if my_index < len(trees) -1:
                right_tree = trees[my_index + 1]
                right_tree.burn(my_index +1, trees)
    
    def __init__(self):
        self.p = 0.2    


f = 0.05

max_step = 10
num_trees = 30

trees = []
for index in range(num_trees):
    trees.append(Tree())


for step in range(max_step):
    
    for tree in trees:
        if random.random() <= tree.p:
            tree.grow()

    
    for t_index in range(0,len(trees)):
        tree = trees[t_index]
        if random.random() <= f:
            tree.burn(t_index,trees)
    
    count = 0
    for tree in trees:
        if tree.grown:
            count = count + 1

    #print count

    for tree in trees:
        if tree.grown:
            print "1",
        else:
            print "0",
            
    print ""






