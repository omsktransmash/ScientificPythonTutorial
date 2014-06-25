import random

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
    
    def __init__(self):
        self.p = 0.2
    


f = 0.05

max_step = 10
num_trees_row = 20
num_trees_col = 20

trees = []


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
#    for tree in trees:
#        if random.random() <= tree.p:
#            tree.grow()

    for row in range(len(trees)):
        for col in range(len(trees[row])):
            tree = trees[row][col]
            if random.random() <= f:
                tree.burn(row,col,trees)
    
##    for t_index in range(0,len(trees)):
##        tree = trees[t_index]
##        if random.random() <= f:
##            tree.burn(t_index,trees)
    
    count = 0
    for row in range(len(trees)):
        for col in range(len(trees[row])):
            tree = trees[row][col]
            if tree.grown:
                count =count+ 1

##    for tree in trees:
##        if tree.grown:
##            count = count + 1

    #Disply Result
    print "\n\nSimulation#"+str(step)+" :\t " + str(count) + " trees survived."
    print "\nForest---------------------------------"

    for row in range(len(trees)):
        row_result = ""
        for col in range(len(trees[row])):
            tree = trees[row][col]
            if tree.grown:
                row_result += "1 "
            else:
                row_result += "0 "
        print row_result


##    for tree in trees:
##        if tree.grown:
##            print "1",
##        else:
##            print "0",
            
    print "---------------------------------------"

    if count > max_count:
        max_count = count
        max_count_step = step

   

print "\n\nSimulation Finished."
print "Num of Simulation: "+str(max_step)
print "Maximum trees: "+ str(max_count) + " ( Simulation #"+str(max_count_step)+" )"
