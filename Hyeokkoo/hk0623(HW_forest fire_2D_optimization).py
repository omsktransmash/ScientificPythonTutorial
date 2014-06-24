
import random

result_set=[]

for grow_rate in range(101):
    for fire_rate in range(101):
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
                self.p=(grow_rate+0.00)/100


        f=(fire_rate+0.00)/100

        count=0
        max_step = 10
        num_trees_row = 25
        num_trees_column= 25

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



        result=[trees[1][1].p,f,count]
        print result
        result_set.append(result)




max_count=0
optimization_set=[]

for result in result_set:
    if result[1]>0:
        if result[2]>max_count:
            if optimization_set is not None:
                del optimization_set[:]
            optimization_set.append(result)
            max_count=result[2]


print optimization_set
            
    

