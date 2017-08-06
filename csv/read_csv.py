''' Notes
1. How to parse csv file data using csv module.
2. How to assign comma separated data to variables.
3. Place holders.
'''

import csv

# Print csv module functions
#print(dir(csv))

#***************** Read and print every row in csv file *******************

csv_file = open('test.csv')
for row in csv_file:
    print(row)
csv_file.close()

print()

#*********************** Using reader function ****************************

template = """{} is {}""" #{} is the place holder

# Using reader function
csv_file = open('test.csv')

reader = csv.reader(csv_file, delimiter=',')
next(reader) # Extract the first line in the csv file

for row in reader:
    id, name, email, weight = row
    if int(weight) > 100:
        msg = template.format(name,'Overweight')
    else:
        msg = template.format(name,'Healthy')
    print(msg)    

csv_file.close()