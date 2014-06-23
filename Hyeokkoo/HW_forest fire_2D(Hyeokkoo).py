import random

class Tree:

    grown = False
    
    def grow(self):
        self.grown= True
        
    def burn(self, my_row_index, my_column_index, trees):           
        if self.grown== True:
            self.grown= False

            if my_column_index >0 :
                left_tree=trees[my_row_index][my_column_index-1]
                left_tree.burn(my_row_index, my_column_index-1, trees)

            if my_column_index < len(trees)-1:
                right_tree=trees[my_row_index][my_column_index+1]
                right_tree.burn(my_row_index, my_column_index+1, trees)
            

            if my_row_index >0 :
                above_tree=trees[my_row_index-1][my_column_index]
                above_tree.burn(my_row_index-1, my_column_index, trees)

            if my_row_index < len(trees[0])-1:
                below_tree=trees[my_row_index+1][my_column_index]
                below_tree.burn(my_row_index+1, my_column_index, trees)
            

    def __init__(self):
        self.p=0.5


f=0.1

count=0
max_step = 4    
num_trees_row = 5
num_trees_column= 5

trees=[]



for row_index in range (num_trees_row):
    trees_row = []
    for index in range (num_trees_column):
        trees_row.append(Tree())
    trees.append(trees_row)




for step in range(max_step):

    
    for i in range(num_trees_row):
        for j in range(num_trees_column):
            if random.random()<=trees[i][j].p:
                trees[i][j].grow()


    for i in range(num_trees_row):
        for j in range(num_trees_column):
            if random.random()<=f:
                trees[i][j].burn(i,j,trees)



for i in range(num_trees_row):
    for j in range(num_trees_column):
        if trees[i][j].grown:
            count=count+1
print "count after burning=", count



                
for i in range(num_trees_row):
    for j in range(num_trees_column):
        if trees[i][j].grown:
            print "1",
        else:
            print "0",
    print ""

            
    


