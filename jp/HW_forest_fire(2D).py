import random

max_step = 100
num_rows = 10
num_columns = 10
result_set=[]
result=[]

## Growth rate        
for y in range (1, 100):
    class Tree:
        grown = 0

        def grow(self):
            self.grown = 1

        def burn(self,index_row, index_col, trees):

            if self.grown == 1:            
                self.grown = 4 # Burned tree 
                
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
            self.p = y * 0.01




    
    ## fire rate 
    for x in range (1, 100):

        fire = x * 0.01
        growth = y * 0.01 

        surviv_vol = 0
        survived = 0
        burned = 0
        surviv_rate = 0

        print " fire=", fire, " growth=", growth    
        # iteration 
        for step in range(max_step):
#            print "step=", step

            ## Matrix - forest       
            trees = []
            nth_row = []  
            for row in range(num_rows):
                nth_row = []
                for col in range(num_columns):
                    nth_row.append(Tree())
                trees.append(nth_row)

            
            ## forest  
            for row in range(num_rows):
                for col in range(num_columns):
                    if random.random() <= trees[row][col].p :
                        trees[row][col].grow()
                        
            ##(Forest display)
#                        print "1", 
#                    else :
#                        print "0",
#                print "\n",        
#            print " -- Forest_Fire -- \n",
            
            ## forest_fire
            for row in range(num_rows):
                for col in range(num_columns):
                    if random.random() <= fire: 
                        trees[row][col].burn(row, col, trees)

            ##(Forest display)
#            for row in range(num_rows):
#                for col in range(num_columns):
#                    if trees[row][col].grown:
#                        print trees[row][col].grown,
#                    else:
#                        print trees[row][col].grown,
#                print "\n", 
#            print " --  -- \n",
            
            for row in range(num_rows):
                for col in range(num_columns):
                    if trees[row][col].grown == 1:
                        surviv_vol = surviv_vol + 1
                    elif trees[row][col].grown == 4:
                        burned = burned +1

            initial_vol = surviv_vol + burned
            if initial_vol > 0:
                surviv_rate = float(surviv_vol) / float(initial_vol)
            else:
                surviv_rate = 0
        surviv_vol = float (surviv_vol)/float(max_step)
        burned = float (burned)/float(max_step)
        print "survival", surviv_vol, "Burned", burned, "Survival_Rate", surviv_rate #Acumulated count
        print "\n"

        result = [fire, growth, surviv_vol, burned, surviv_rate]
        result_set.append(result)
            
##optimal p (suviv_vol)
print "optimal p given f (production volume)"
print "fire\t", "opt_p\t" , "production"  
for x in range (1,100):

    fire = x * 0.01
    opt_growth = 0.0
    max_surviv_vol = 0.0
    dummy_max = 0.0
    for i in range(0, len(result_set)):
        if result_set[i][0] == fire:
            if result_set[i][2] >= dummy_max:
                opt_growth = result_set[i][1]
                dummy_max = result_set[i][2]
          
    print fire,"\t", opt_growth,"\t", dummy_max        

print "\n"

## optimal p (suviv_rate)
print "optimal p given f (survival rate)"
print "fire\t", "opt_p\t" , "survival rate"  
for x in range (1,100):

    fire = x * 0.01
    opt_growth = 0.0
    max_surviv_vol = 0.0
    dummy_max = 0.0
    for i in range(0, len(result_set)):
        if result_set[i][0] == fire:
            if result_set[i][4] >= dummy_max:
                opt_growth = result_set[i][1]
                dummy_max = result_set[i][4]
         
    print fire,"\t", opt_growth,"\t", dummy_max                

        


