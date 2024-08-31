import os
import csv
import pprint

DataDir = ""
DataFile = "data/historical_energy_data.csv"

def Read_file(datafile):
    data = []
    with open(datafile, 'r') as f:
        r = csv.DictReader(f)
        for i in r:
            data.append(i)
    return data

if __name__ == "__main__":
    datafile = os.path.join(DataDir, DataFile)
    d = Read_file(DataFile)
    pprint.pprint(d)