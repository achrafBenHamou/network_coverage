import csv
from app import config

data_path = config.Configuration.data # get Data path from config file
nb_providers = len(config.Configuration.providers) # get number of nework providers from config file
"""
def getNetworkCoveragee(x,y):
    with open(data_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';') # Read csv file
        next(reader) # This skips the first row of the CSV file
        providers_ids = []
        providers_data = []
        while (len(providers_ids)<nb_providers):
            for row in reader:
                try:
                    if (x-10 <= int(row[1]) or int(row[1]) <= x+10) and (y-10 <= int(row[2]) or int(row[2])  <= y+10):
                        if (row[0] not in providers_ids):
                            providers_ids.append(row[0])
                            providers_data.append(row)
                except :
                    pass
        return providers_data
"""
def getNetworkCoverage(city):
    with open(data_path, newline='') as csvfile :
        reader = csv.reader(csvfile, delimiter=';') # Read csv file
        next(reader) # This skips the first row of the CSV file.
        providers_ids = []
        providers_data = []
        isNotTerminited = True
        while (len(providers_ids)<nb_providers and isNotTerminited):
            for row in reader :
                if row[6] == city :
                    providers_ids.append(row[0])
                    providers_data.append(row)
            isNotTerminited = False
        return providers_data

#print(getNetworkCoverage("Paris"))
