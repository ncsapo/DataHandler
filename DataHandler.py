from openpyxl import load_workbook
import requests

test_csv = "/Users/nickcsapo/Downloads/SalesJan2009.csv"
test_xlsx = "/Users/nickcsapo/Downloads/Financial Sample.xlsx"

#returns value in a defined cell
def get_cell(data, col_num, row_num):
    return data[col_num-1][row_num-1]

#returns values in a defined column
def get_col(data, col_num, col_max):
    return data[col_num-1::col_max]

#returns the html of a webpage
def get_webpage(address):
    html = requests.get(address).text
    return html

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
    col_count = len(data)
    row_count = len(data[0])
    transposed_data = []
    for row in range(row_count):
        temp = []
        for col in range(col_count):
            temp.append(data[col][row])
        transposed_data.append(temp)
    return transposed_data

print(get_webpage("https://www.google.com"))
print("DataHandler.py Loaded")