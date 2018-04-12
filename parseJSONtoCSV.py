import json
import csv
import os

path_of_json_files = './response/'
json_files = [json_file for json_file in os.listdir(path_of_json_files) if json_file.endswith('.json')]
#print(json_files)
flag=0
data_header = ['position', 'status', 'banking', 'bonus', 'contract_name', 'available_bike_stands', 'last_update', 'number', 'bike_stands', 'available_bikes', 'name', 'address']
for j_file in json_files:

    #open a csv file to save the parsed data

    csv_bikes_data = open('atest_Data.csv','a')

    csv_bikes_data_writer = csv.writer(csv_bikes_data)

    if flag == 0:
        #data_header = data.keys()
        #print(data_header)
        csv_bikes_data_writer.writerow(data_header)
        flag += 1

    with open('response/'+j_file, 'r') as f:
        bikes_data_parsed = json.load(f)


    for data in bikes_data_parsed:
        #print(j_file)
        data_values = []
        for keys in data_header:
            data_values.append(data.get(keys))
        csv_bikes_data_writer.writerow(data_values)

    csv_bikes_data.close()
