import random

class Tree:
    grown = False

    def grow(self):
        self.grown = True

    def burn(self,my_row_index,my_col_index,trees):

        if self.grown == True:
            
            self.grown = False

            if my_col_index > 0:
                left_tree = trees[my_row_index][my_col_index - 1]
                left_tree.burn(my_row_index, my_col_index - 1,trees)
            if my_col_index < len(trees) -1:
                right_tree = trees[my_row_index][my_col_index + 1]
                right_tree.burn(my_row_index, my_col_index +1, trees)
            if my_row_index > 0:
                up_tree = trees[my_row_index -1][my_col_index]
                up_tree.burn(my_row_index -1,my_col_index,trees)
            if my_row_index < len(trees) -1:
                down_tree = trees[my_row_index + 1][my_col_index]
                down_tree.burn(my_row_index +1,my_col_index, trees)
    
    def __init__(self):
        self.p = 0.2    


f = 0.05

max_step = 3
tree_row = 5
tree_col = 5

trees_row = []
trees_col = []
trees = []

##making land for trees
for row_index in range(tree_row):
    for col_index in range(tree_col):
        trees_row.append(Tree())
        trees_col.append(Tree())
    trees.append(trees_row)
    trees.append(trees_col)
        

##growing trees
for step in range(max_step):
    
        for i in range(tree_row):
            for j in range(tree_col):
                if random.random() <= trees[i][j].p:

                    trees[i][j].grow()
             


##trees burning  
        for i in range(tree_row):
            for j in range(tree_col):
              
               
             
                if random.random() <= f:
                    trees[i][j].burn(i,j,trees)
                    
        
        count = 0
        for row_tree in range(tree_row):
            for col_tree in range(tree_col):
                if trees[row_tree][col_tree].grown:
                    count = count +1
         

        #print count
        for row_tree in range(tree_row):
            for col_tree in range(tree_col):
                if trees[row_tree][col_tree].grown:
                    print "1",
                else:
                    print "0",
            print ""
        print ""





