import random

max_prob_step=100
max_probcount=-1


for prob_step in range(max_prob_step):

    

    class Tree:
        grown = False

        def grow(self):
            self.grown = True

        def burn(self, my_row, my_col, trees):

            if self.grown == True:
                
                self.grown = False
                
                #Row Action
                if my_row > 0:
                    left_tree = trees[my_row - 1][my_col]
                    left_tree.burn(my_row - 1, my_col, trees)
                if my_row < len(trees) -1:
                    right_tree = trees[my_row + 1][my_col]
                    right_tree.burn(my_row +1, my_col, trees)

                #Column Action
                if my_col > 0:
                    up_tree = trees[my_row][my_col - 1]
                    up_tree.burn(my_row, my_col - 1,trees)
                if my_col < len(trees[my_row]) -1:
                    down_tree = trees[my_row][my_col + 1]
                    down_tree.burn(my_row, my_col +1, trees)
        
        #probablility change function
        def __init__(self):
            self.p = (prob_step+0.00)/max_prob_step
        
        

    f = 0.05

    max_step = 10
    num_trees_row = 20
    num_trees_col = 20

    trees = []


    #forest
    for row in range(num_trees_row):
        newRow = []
        for col in range(num_trees_col):
            newRow.append(Tree())
        trees.append(newRow)




    max_count = -1
    max_count_step = -1

    for step in range(max_step):

        for row in range(len(trees)):
            for col in range(len(trees[row])):
                tree = trees[row][col]
                if random.random() <= tree.p:
                    tree.grow()

        for row in range(len(trees)):
            for col in range(len(trees[row])):
                tree = trees[row][col]
                if random.random() <= f:
                    tree.burn(row,col,trees)
        
        count = 0
        for row in range(len(trees)):
            for col in range(len(trees[row])):
                tree = trees[row][col]
                if tree.grown:
                    count =count+ 1



        if count > max_count:
            max_count = count
            max_count_step = step
            


##    print "\nprobability: "+str(tree.p)
##    print "Maximum trees: "+ str(max_count) + " ( Simulation #"+str(max_count_step)+" )"
    
    
    if max_count > max_probcount:
        max_probcount= max_count
        max_prob =tree.p


print "\nOptimal probability : "+str(max_prob)
print "number of trees: " +str(max_probcount)


    
