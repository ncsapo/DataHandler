import csv
from openpyxl import load_workbook

test_csv = "/Users/nickcsapo/Downloads/SalesJan2009.csv"
test_xlsx = "/Users/nickcsapo/Downloads/Financial Sample.xlsx"

#returns value in a defined cell
def get_cell(data, col_num, row_num):
    return data[col_num-1][row_num-1]

#returns values in a defined column
def get_col(data, col_num, col_max):
    return data[col_num-1::col_max]

#returns list of each value in csv file
def load_csv(file, delimiter = ',', exclusion_list = []):
    if not isinstance(exclusion_list, list): exclusion_list = [exclusion_list]
    values = []
    with open(file, "r") as imported_file:
        for row in imported_file:
            for value in row.split(delimiter):
                if value not in exclusion_list:
                    values.append(value)
    return values

#returns list of each value in xlsx file
def load_xlsx(file, sheet = 'Sheet1'):
    values = []
    wb = load_workbook(file)
    ws = wb[sheet]
    for row in ws.values:
        for value in row:
            values.append(value)
    return values

#Organizes data based on specified number of columns (steps)
def slice_data(data, step):
    return [data[i::step] for i in range(step)]

#Identical to .split but leaves delimiter
def split_data(data, delimiter):
    data = data.split(delimiter)
    [element.append(delimiter) for element in data]
    return data

#switches rows with columns
def transpose_data(data):
    new_2d_list = []
    for col in range(len(data)):
        temp_list = []
        for value in data[col]:
            temp_list.append(value)
        new_2d_list.append(temp_list)
    return new_2d_list

d = load_csv(test_csv)
e = slice_data(d, 13)
f = transpose_data(e)
print(f)

print("DataHandler.py Loaded")