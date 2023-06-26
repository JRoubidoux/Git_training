import csv

with open(r"C:\Users\Jackson Roubidoux\Record Linking Lab\Git_training\Git_training\lists_of_food\big_list.tsv", 'r', newline='') as f:
    reader = csv.reader(f, delimiter='\t')
    big_list = []
    for row in reader:
        big_list.append(row[0])

list1 = big_list[:25000]
list2 = big_list[24000:]

outfile_for_list1 = r"C:\Users\Jackson Roubidoux\Record Linking Lab\Git_training\Git_training\lists_of_food\list1.txt"
outfile_for_list2 = r"C:\Users\Jackson Roubidoux\Record Linking Lab\Git_training\Git_training\lists_of_food\list2.txt"

with open(outfile_for_list1, 'w') as f:
    for item in list1:
        f.write(item + '\n')

with open(outfile_for_list2, 'w') as f:
    for item in list2:
        f.write(item + '\n')
