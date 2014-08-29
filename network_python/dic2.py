
from xlrd import open_workbook, cellname   #importing open_workbook in xlrd 
 
book = open_workbook('C:\\Users\\Administrator\\Desktop\\ScientificPythonTutorial\\network_python\\a.xlsx')  #identify location of data file and define book 

dict2 = {} #create dictionary2

for s in book.sheets(): #for sheets in book 

    
    print 'Sheet:',s.name #print sheet name
    

                                 ### Book_num is value and order_num is key.
                                 ### By reading down the row one by one, i created the value list and append value in each cell in second column. 
                                  
    for row in range(s.nrows):   #reading down by rows and creat list according one by one according to row
        book_num = s.cell(row,1)  #define book_num as second column
        order_num = s.cell(row,0) #define order_num as first colum
        values = []               #define value list
        values.append(book_num)   #append book_num into the value list by reading down the row
        
        
       # print values

        if dict2.has_key(order_num): #for not to overlap, check if there is key already exist in dictionary
            pass                     #if there is key in dictionary, pass
        else:                        #if there is no key in dictionary, insert value list according to the order_num
            dict2[order_num]=values


            #dict2[order_num].append(book_num)
            

    print dict2                     #print dictionary2
