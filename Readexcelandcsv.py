

#Reading excel file using pandas
import pandas as pd
import os,sys
csv_path=os.path.join('C:/Users/max/Desktop','ie_data.xls')
#csv_path=os.path.join("C:\\Users\\max\\Desktop",'ie_data.xls')
df = pd.read_excel(csv_path,sheetname="Data")
print("Column headings:")
print(df)

# Read CSV file using CSV module
import csv
with open('C:/Users/max/Desktop/TSLA.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        
# Read CSV file using pandas
with open('C:/Users/max/Desktop/TSLA.csv','r') as f:
    reader = pd.read_csv(f)
    for row in reader:
        print(row)