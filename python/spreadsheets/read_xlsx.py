from openpyxl import load_workbook

wb = load_workbook(filename='users.xlsx')

# List sheets available
sheets = wb.get_sheet_names()
print(sheets)

# Load active sheet or named sheet
sheet = wb.active
# sheet = wb['User Information']

print(sheet['A1'].value)  # Read a specific cell


# Reading and parsing spreadsheet by using xlrd module
import xlrd
book = xlrd.open_workbook('rate_table.xlsx')

# Get the sheet name by index
sheet = book.sheet_by_index(0) # Open first sheet. 

# Display the number of sheets
book.nsheets 

# Display the list of sheet names
book.sheet_names() 



headings = sheet.row(0)
data = {} 

for i, row in enumerate(sheet.get_rows()):
    if i == 0:
        headings = row 
        continue    

        rate = {}
    
    for key, value in zip(headings, row):
        rate[key.value] = value 
        
    
    data[row[0].value] = rate 
    
   


print(data)
