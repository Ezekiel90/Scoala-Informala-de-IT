# file = open('data.txt', 'r+')
# file.write("hello ana")
# file.close()

# r - read only
# w - write, if does not exist, it will add it
# a - write and appends
# r+ - read, write (overwrite)

# file = open('data1.txt', 'w')
# try:
#     file.write("hello")
# finally:
#     file.close()

# with open('data2.txt', 'w') as file:
#     file.write("hello2")

# with open('data.txt', 'r') as file:
#     for line in file.readlines():
#         print(line)

# with open('data.txt', 'r') as file:
#     for line in list(file):
#         print(line)

# with open('data.txt', 'r') as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print (line)

# import csv

# with open('fisiercsv.csv', 'r') as csv_file:
#     rows = csv.reader(csv_file, delimiter=',')
#     for row in rows:
#         print(row)

import csv

new_cars = [
    ['Dacia', 'Logan', 2005, 75],
    ['Renault', 'Clio', 2005, 75]
]
with open('fisiercsv.csv', 'a') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for new_car in new_cars:
        csv_writer.writerow(new_car)



