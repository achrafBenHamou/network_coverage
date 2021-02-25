import csv

from models.provider_coverage import ProviderCoverage

def getNetworkCoverage(zip_code,data_path,providers):
    """ Input : zip code
        Output : list of ProviderCoverage objects"""
    with open(data_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')  # Read csv file
        next(reader)  # This skips the first row of the CSV file
        output = []
        id_providers = []
        for row in reader:           # Example of row: ['20801', '102980', '6847973', '1', '1', '0', '42100']
            row = list(map(lambda x: int(float(x)), row)) # Transform all elements of row to integer
            if row[-1] == zip_code:  # zip code is in the last column of the row
                if(row[0] not in id_providers):
                    if len(output) < len(providers):
                        provider = ProviderCoverage(id = row[0], zip_code= row[-1])
                        provider.setHas2G(row[3])
                        provider.setHas3G(row[4])
                        provider.setHas4G(row[5])
                        provider_name = providers[row[0]]
                        provider.setName(provider_name)
                        # add ProviderCoverage object to list
                        id_providers.append(provider.id)
                        output.append(provider) # add object to the output
                    else :
                        break
        return output
