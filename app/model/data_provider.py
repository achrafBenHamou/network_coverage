import csv
from app import config

data_path = config.Configuration.data  # get Data path from config file
nb_providers = len(config.Configuration.providers)  # get number of network providers from config file

def getNetworkCoverage(city):
    with open(data_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')  # Read csv file
        next(reader)  # This skips the first row of the CSV file
        providers_data = []
        controller = True
        while len(providers_data) < nb_providers and controller:
            for row in reader:
                if row[6] == city: providers_data.append(row)
            controller = False
        return providers_data
