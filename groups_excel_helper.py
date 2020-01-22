import csv

class Preference:
    def __init__(self,preferences):
        self.preference_dictonary = {
            "cover":{
                "0": int(preferences[0]),
                "1": int(preferences[1])
            },
            "paper": {
                "00": int(preferences[2]),
                "01": int(preferences[3]),
                "10": int(preferences[4]),
                "11": int(preferences[5])
            },
            "font": {
                "00": int(preferences[6]),
                "01": int(preferences[7]),
                "10": int(preferences[8]),
                "11": int(preferences[9]) 
            }
        }
        self.preferred_price = int(preferences[10])

def get_groups_csv_data(): 
    with open('csv_data_files/groups_data.csv',newline='') as groups_parameters:
        data = csv.reader(groups_parameters,delimiter=',', quotechar='"')

        rows_to_arrays = list(data)

        groups_dictonaries = []

        #process csv file data and create series of dictonaries represeting group preferences
        for i in range(1,len(rows_to_arrays)):
            groups_dictonaries.append(Preference(rows_to_arrays[i]))

        return groups_dictonaries

