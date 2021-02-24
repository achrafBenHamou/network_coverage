import csv
from app import config

data_path = config.Configuration.data  # get Data path from config file
nb_providers = len(config.Configuration.providers)  # get number of network providers from config file

def getNetworkCoverage(zip_code):
    """ Input : zip code
        Output : list of csv rows that has the same zip code for each network provider  """
    if zip_code != 0:
        with open(data_path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')  # Read csv file
            next(reader)  # This skips the first row of the CSV file
            output = []
            controller = True
            while len(output) < nb_providers and controller:
                for row in reader:           # Example of row: ['20801', '102980', '6847973', '1', '1', '0', '42100']
                    if row[-1] == zip_code:  # zip code is in the last column of the row
                        output.append(row)
                controller = False           # return False if it treats all rows of csv
            return output
    else:
        return zip_code
