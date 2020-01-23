import csv
from group import Group

def get_groups_csv_data(): 
    with open('csv_data_files/groups_data.csv',newline='') as groups_parameters:
        data = csv.reader(groups_parameters,delimiter=',', quotechar='"')

        rows_to_arrays = list(data)

        groups_dictonaries = []

        #process csv file data and create series of dictonaries represeting group preferences
        for i in range(1,len(rows_to_arrays)):
            groups_dictonaries.append(Group(rows_to_arrays[i]))

        return groups_dictonaries

