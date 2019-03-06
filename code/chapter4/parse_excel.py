import pprint
import xlrd
#just a comment

book = xlrd.open_workbook('../../data/chapter4/SOWC 2014 Stat Tables_Table 9.xlsx')

# to get all the names of the sheet available in the current sheet
for sheet in book.sheets():
    print(sheet.name)

#we are concerned with the table 9 sheet so lets open that sheet

sheet = book.sheet_by_name('Table 9 ')
"""print(sheet.nrows)

#so  there are total 303 rows now we need to traverse each row so we will use the range function
for i in range(sheet.nrows):
    pass
    print(sheet.row_values(i))
    #now we can seee each row but we have to pull out the content of the each row
# we are going to use nested for loop to get output from each row each column  
for i in range(sheet.nrows):
    #output of this fucniton is not that readable sow we will use the counter variable to lmit the output
    pass
    row = sheet.row_values(i)
    for cell in row:
        print(cell)

counter = 0 
for i in range(sheet.nrows):
    if(counter <20):
        if(i >= 14):
            print(i , sheet.row_values(i))
        counter += 1


#now that wehave our data but we should arrange it in a dictonary and each dictonary key will be country name 
counter = 0
data = {}
for i in range(sheet.nrows):
    if(counter < 24):
        if(i >= 14):
            row = sheet.row_values(i)
            country = row[1]
            data[country] = {}
    counter += 1
print(data)
"""

#now we aill creae a empty structure to store our data
data = {}
for i in range(14 , 212):
    row = sheet.row_values(i)
    country = row[1]
    data[country] = {
        'child_labour':{
            'total' : [row[4], row[5]],
            'male' : [row[6], row[7]],
            'female' : [row[8], row[9]],
        },
        'child_marriage' : {
            'married_by_15' : [row[10], row[11]],
            'married_by_18' :[row[12], row[13]],
        }
    }

pprint.pprint(data)
