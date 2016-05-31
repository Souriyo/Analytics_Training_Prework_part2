#import package
import csv as csv
import numpy as np


#import file
test_file = open('C:/Users/AISSSOU/Desktop/data science/Analytics_Prework_part2/exo/data/test.csv', 'rb')
test_file_object = csv.reader(test_file)
header = test_file_object.next()
data=[]

#put csv data in data[]
for row in test_file_object:
    data.append(row)
data = np.array(data) 
