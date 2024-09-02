import xlrd
import os

DataFile ="data/2013_ERCOT_Hourly_Load_Data.xls"
DataDir = ""

def parse_file(datafile):
    
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    
    data = [[sheet.cell_value(r, col)
             for col in range(sheet.ncols)]
             for r in range(sheet.nrows)]
    
    print("\nList Comprehension".rjust(80))
    print(data[3][2])
            
            
    print('\nCell in a Nested loop')
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            if row == 50:
                print(sheet.cell_value(row, col))
                
    print(sheet.cell_type(3,2))
    print(sheet.nrows)
    print(sheet.cell_value(3,2))
    print(sheet.col_values(3, start_rowx=1, end_rowx=4))

if __name__ == "__main__":
    path = os.path.join(DataDir, DataFile)
    d = parse_file(path)