import random

class Tree:
    grown = False

    def grow(self):
        self.grown = True

    def burn(self,row_index,col_index,trees):

        if self.grown == True:            
            self.grown = False

            if row_index > 0:
                up_tree = trees[row_index-1][col_index]
                up_tree.burn(row_index-1, col_index, trees)
            if row_index < len(trees) -1:
                down_tree = trees[row_index+1][col_index]
                down_tree.burn(row_index +1,col_index, trees)
            if col_index > 0:
                left_tree= trees[row_index][col_index-1]
                left_tree.burn(row_index, col_index-1, trees)
            if col_index < len(trees)-1:
                right_tree = trees[row_index][col_index+1]
                right_tree.burn(row_index, col_index+1, trees)

            
    def __init__(self):
        self.p = 0.2    


f = 0.05


max_step = 10
tree_row = 5
tree_col = 5


row_list=[]
col_list=[]
trees = []


for row_index in range(tree_row):
    for col_index in range(tree_col):
        row_list.append(Tree())
    trees.append(row_list)
        

for step in range(max_step):
    
    for row in range(tree_row):
        for col in range(tree_col):
            if random.random() <= trees[row][col].p:
                trees[row][col].grow()

    
    for row in range(tree_row):
        for col in range(tree_col):
            if random.random() <= f:
                trees[row][col].burn(row,col,trees)
    
    count = 0
    
    for row in range(tree_row):
        for col in range(tree_col):
            if trees[row][col].grown:
                count = count + 1

    #print count

    for row in range(tree_row):
        for col in range(tree_col):
            if trees[row][col].grown:
                print "1",
            else:
                print "0",
                
    print ""






