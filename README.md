# Analytics_Training_Prework_part2

import csv as csv
import numpy as np

csv_file_object = csv.reader(open('C:/Users/AISSSOU/Desktop/data science/Analytics_Prework_part2/exo/data/train.csv', 'rb')) 
header = csv_file_object.next() 
data=[] 

for row in csv_file_object:
    data.append(row)
data = np.array(data) 

