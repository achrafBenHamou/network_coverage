import csv
from models.provider_coverage import ProviderCoverage
from models.use_case import compare_result

def get_data_from_csv(zip_code,data_path,providers):
    """ Input : zip code
        Output : dictionnary of ProviderCoverage objects"""
    with open(data_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')  # Read csv file
        next(reader)  # This skips the first row of the CSV file
        output = {}

        # Example of row: ['20801', '102980', '6847973', '1', '1', '0', '42100']
        for row in reader:
            # Transform all elements of row into integer
            row = list(map(lambda x: int(float(x)), row))
            # zip code is in the last column of the row
            if row[-1] == zip_code:
                if(providers[row[0]] not in output.keys()):
                    new_provider_coverage = ProviderCoverage(id = row[0], zip_code= row[-1])
                    new_provider_coverage.setHas2G(row[3])
                    new_provider_coverage.setHas3G(row[4])
                    new_provider_coverage.setHas4G(row[5])
                    new_provider_coverage.setName(providers[row[0]])
                    # add object to the output
                    output[new_provider_coverage.name]= new_provider_coverage
                else :
                    new_provider_coverage = ProviderCoverage(id = row[0], zip_code= row[-1])
                    new_provider_coverage.setHas2G(row[3])
                    new_provider_coverage.setHas3G(row[4])
                    new_provider_coverage.setHas4G(row[5])
                    new_provider_coverage.setName(providers[row[0]])
                    old_provider_coverage = output[new_provider_coverage.name]
                    # takes the newest and the older and return the best network coverage in the city
                    best_provider_coverage = compare_result (new_provider_coverage,old_provider_coverage)
                    output[new_provider_coverage.name] = best_provider_coverage
        return output
