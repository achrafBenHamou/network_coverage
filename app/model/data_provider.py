import csv
from app import config

data_path = config.Configuration.data  # get Data path from config file
nb_providers = len(config.Configuration.providers)  # get number of network providers from config file

def getNetworkCoverage(ZipCode):
    """ Input : zip code as parameter
        Output : list of csv rows that has the same zip code for each network provider  """
    if ZipCode != 0:
        with open(data_path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')  # Read csv file
            next(reader)  # This skips the first row of the CSV file
            output = []
            controller = True
            while len(output) < nb_providers and controller:
                for row in reader: # Example of row: ['20801', '102980', '6847973', '1', '1', '0', '42100']
                    #print(row[6])
                    #if row[6] == ZipCode:
                    if row[-1] == ZipCode: #zip code is in the last column of row
                        output.append(row)
                controller = False # return False if we finished to treat all rows of csv
            return output
    else:
        return ZipCode