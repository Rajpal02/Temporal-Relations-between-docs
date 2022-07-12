
import json
import csv
import pandas as pd


'''
description: Coverting JSON to CSV 
param {*} jsonfilename
param {*} csvfilename
return {*}
Date: 2022-03-25 12:08:46
'''
def jsontocsv(jsonfilename,csvfilename,encoding):

    with open(jsonfilename,encoding=encoding) as json_file:
        jsondata = json.load(json_file)
    data_file = open(csvfilename, 'w', newline='',encoding=encoding)
    csv_writer = csv.writer(data_file)
    count = 0
    for data in jsondata:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(data.values())
    data_file.close
    return


def data_processes(datafile):
    data = pd.read_csv(datafile)
    print(data)
    
    return

if __name__ =="__main__":
    #News Dataset to csv
    #jsontocsv('News_Category_Dataset copy.json','News_Category_Dataset copy.json',"utf-8")

    data_processes("article_list.csv")
    


# with open('News_Category_Dataset copy.json',encoding="utf-8") as json_file:
#     jsondata = json.load(json_file)
 
# data_file = open('News.csv', 'w', newline='',encoding="utf-8")
# csv_writer = csv.writer(data_file)
 
# count = 0
# for data in jsondata:
#     if count == 0:
#         header = data.keys()
#         csv_writer.writerow(header)
#         count += 1
#     csv_writer.writerow(data.values())
 
# data_file.close()