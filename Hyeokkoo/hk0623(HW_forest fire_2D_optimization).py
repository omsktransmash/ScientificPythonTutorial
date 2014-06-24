
import random

result_set=[]

for grow_rate in range(101):
    for fire_rate in range(101):
        class Tree:

            grown = False
            
            def grow(self):
                self.grown= True
                
            def burn(self, my_row_index, my_column_index, trees):            ## recursive
                if self.grown== True:
                    self.grown= False

                    if my_column_index >0 :
                        left_tree=trees[my_row_index][my_column_index-1]
                        left_tree.burn(my_row_index, my_column_index-1, trees)

                    if my_column_index < len(trees[0])-1:
                        right_tree=trees[my_row_index][my_column_index+1]
                        right_tree.burn(my_row_index, my_column_index+1, trees)
                    

                    if my_row_index >0 :
                        above_tree=trees[my_row_index-1][my_column_index]
                        above_tree.burn(my_row_index-1, my_column_index, trees)

                    if my_row_index < len(trees)-1:
                        below_tree=trees[my_row_index+1][my_column_index]
                        below_tree.burn(my_row_index+1, my_column_index, trees)
                    

            def __init__(self):
                self.p=(grow_rate+0.00)/100


        f=(fire_rate+0.00)/100

        count=0
        max_step = 10       ## number of iteration
        num_trees_row = 25
        num_trees_column= 10

        trees=[]

        ## generate forest

        for row_index in range (num_trees_row):
            trees_row = []
            for index in range (num_trees_column):
                trees_row.append(Tree())
            trees.append(trees_row)



        ## iteration 

        for step in range(max_step):

            ## generate tree 
            
            for i in range(num_trees_row):
                for j in range(num_trees_column):
                    if random.random()<=trees[i][j].p:
                        trees[i][j].grow()

            ## burning
                        
            for i in range(num_trees_row):
                for j in range(num_trees_column):
                    if random.random()<=f:
                        trees[i][j].burn(i,j,trees)

            for i in range(num_trees_row):
                for j in range(num_trees_column):
                    if trees[i][j].grown:
                        count=count+1       ## total number of trees during max_step



        result=[trees[1][1].p,f,count]
        print result
        result_set.append(result)
 

## global optimum

max_count_global=0
global_optimization_set=[]

for result in result_set:
    if result[1]>0:
        if result[2]>max_count_global:
            if global_optimization_set is not None:
                del global_optimization_set[:]
            global_optimization_set.append(result)
            max_count_global=result[2]


print "\n", "global optimum :", "p=", global_optimization_set[0][0], "f=", global_optimization_set[0][1], "count=",global_optimization_set[0][2], "\n"


            
## locam optimum

from operator import itemgetter
sorted_result_set=sorted(result_set, key=itemgetter(1))

f=0.00
p=0
max_count_local=0
for result in sorted_result_set:
    if result[1]==f:
        if result[2]>=max_count_local:
            max_count_local=result[2]
            p=result[0]
    if result[1]>f:
        print "For f=", f,   ", optimal p is ", p, ". count=", max_count_local
        p=result[0]
        f=result[1]
        max_count_local=result[2]
        













        
        

