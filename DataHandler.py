import csv
from openpyxl import load_workbook, Workbook
from requests import get

test_csv = "/Users/nickcsapo/Downloads/SalesJan2009.csv"
test_xlsx = "/Users/nickcsapo/Downloads/Financial Sample.xlsx"

#Creates a .csv file from data
def create_csv(data, location_and_name):
    concatenated_data = []
    for row_num in range(len(data)):
        for col_num in range(len(data[row_num])):
            concatenated_data.append(data[row_num][col_num])
    with open(location_and_name, 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(concatenated_data)

#Creates an excel sheet from data
def create_xlsx(data, location_and_name):
    wb = Workbook()
    ws = wb.active
    for row_num in range(len(data)):
        for col_num in range(len(data[row_num])):
            cell = ws.cell(row=row_num+1, column=col_num+1)
            cell.value = data[row_num][col_num]
    wb.save(location_and_name)
    return True

#returns value in a defined cell
def get_cell(data, col_num, row_num):
    return data[col_num-1][row_num-1]

#returns values in a defined column
def get_col(data, col_num, col_max):
    return data[col_num-1::col_max]

#returns the html of a webpage
def get_webpage(address):
    html = get(address).text
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
    transposed_data = []
    for row in range(len(data[0])):
        temp = []
        for col in range(len(data)):
            temp.append(data[col][row])
        transposed_data.append(temp)
    return transposed_data

d = load_csv(test_csv)
d = slice_data(d, 13)
dates = d[0]
costs = d[2]
print(dates)
print(costs)

import matplotlib.pyplot as plt

plt.plot(dates, costs)

'''
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x**2
x = np.linspace (start = 0, stop = 3, num = 51)
y = f(x)    # This is already vectorized, that is, y will be a vector!

def g(x):
    return x*np.exp(-x)
xx = np.arange  (start = 0, stop = 6, step = 0.05) # generate points between start and stop with distances of step apart from each other
yy = g(xx)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend( [ 'f(x) = x^2*exp(-x^2)'   # This is f(x)
            , 'g(x) = x*exp(-x)'       # This is g(x)
            ] )
plt.title('multiple Matplotlib curves in a single decorated figure');

plt.plot(xx, yy, 'r-')
plt.axis([0, 6, -0.05, 0.6]) # [xmin, xmax, ymin, ymax]
plt.plot(x, y)

plt.show()

#plt.savefig('multipleCurvesFullRangeDecorated.png') # produces a PNG file containing the figure
'''

print("DataHandler.py Loaded")