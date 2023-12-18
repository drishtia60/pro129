import csv
import pandas as pd

file1 = 'unit_converted_stars.csv'
file2 = 'bright_stars.csv'

dataset1 = []
dataset2 = []

with open(file1, 'r', encoding='utf8') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        dataset2.append(i)
        
with open(file2, 'r', encoding='utf8') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        dataset1.append(i)

h1 = dataset1[0]
h2 = dataset2[0]

p_d1 = dataset1[1:]
p_d2 = dataset2[1:]

h = h1+h2

p_d =[]

for i in p_d1:
    p_d.append(i)
for j in p_d2:
    p_d.append(j)
    
with open("total_stars.csv", 'w', encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)   
    csvwriter.writerows(p_d)
    
df = pd.read_csv('total_stars.csv')
df.tail(8)