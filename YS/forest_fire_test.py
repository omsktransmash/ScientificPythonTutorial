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
                down_tree = trees[row-index+1][col_index]
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
row = 10
col = 10



row= []
col = []
trees = [row, col]


for i in range(row):
    for j in range(col):
        row.append(Tree())
        col.append(Tree())
    trees.append(Tree())
        

for step in range(max_step):
    
    for row in range(row):
        for col in range(col):
            if random.random() <= tree[row][col].p:
                tree[row][col].grow()

    
    for row in range(row):
        for col in range(col):
            tree = trees[t_index]
            if random.random() <= f:
                tree[row][col].burn(row_index,col_index, trees)
    
    count = 0
    
    for row in range(row):
        for col in range(col):
            if tree[row][col].grown:
                count = count + 1

    #print count

    for row in range(row):
        for col in range(col):
            if tree[row][col].grown:
                print "1",
            else:
                print "0",
                
    print ""






