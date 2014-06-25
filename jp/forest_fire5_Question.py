import random

class Tree:
    grown = 0

    def grow(self):
        self.grown = 1

    def burn(self,index_row, index_col, trees):

        if self.grown == 1:            
            self.grown = 4
            
            if index_col > 0:
                left_tree = trees[index_row][index_col - 1]
                left_tree.burn(index_row, index_col - 1, trees)
            if index_col < num_columns -1:
                right_tree = trees[index_row][index_col + 1]
                right_tree.burn(index_row, index_col +1, trees)
            if index_row > 0:
                up_tree = trees[index_row -1][index_col]
                up_tree.burn(index_row -1, index_col, trees)
            if index_row < num_rows -1:
                down_tree = trees[index_row + 1][index_col]
                down_tree.burn(index_row + 1,index_col, trees)              
     
        
    def __init__(self):
        self.p = 0.5   


f = 0.2
max_step = 1
num_rows = 2
num_columns = 5
trees = []
nth_row = []

# Create Matrix         
for row in range(num_rows):
    nth_row = []
    for col in range(num_columns):
        nth_row.append(Tree())

    trees.append(nth_row)

for step in range(max_step):
    
    # forest  
    for row in range(num_rows):
        for col in range(num_columns):
            if random.random() <= trees[row][col].p :
                trees[row][col].grow()
                print "1", 
            else :
                print "0",
        print "\n",        
    print " -- Forest_Fire -- \n",
    
    # forest_fire
    for row in range(num_rows):
        for col in range(num_columns):
            print trees[row][col].grown
          
            if random.random() <= f: 
                trees[row][col].burn(row, col, trees)

    for row in range(num_rows):
        for col in range(num_columns):
            if trees[row][col].grown:
                print trees[row][col].grown,
            else:
                print "0",
        print ""

#    for nth_row in trees:
#        for tree in nth_row:
#            if tree.grown:
#                print tree.grown,
#            else:
#                print tree.grown,
#        print "\n",   
#    print ""   


