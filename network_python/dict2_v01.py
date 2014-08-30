from xlrd import open_workbook, cellname, XL_CELL_TEXT   #importing open_workbook in xlrd 
 
book = open_workbook('C:\\Users\\Administrator\\Desktop\\ScientificPythonTutorial\\network_python\\a.xlsx')  #identify location of data file and define book 

dict2 = {} #create dictionary2

for s in book.sheets(): #for sheets in book 

    
    #print 'Sheet:',s.name #print sheet name

    for row in range (s.nrows):

        book_num = s.cell(row,1)
        order_num = s.cell(row,0)
        values = []
        values.append(book_num.value)
        #print values

        if dict2.has_key(order_num.value):
            pass
        else:
            dict2[order_num.value]=values

    print dict2
        

