from configuration import config
from models.data_provider import get_data_from_csv
from service.entry_point import get_zip_code
from views.view import resource_representation

data_path   =  config.Configuration.data            # get Data path from config file
api_address =  config.Configuration.api_address     # get api adress from config file
providers   =  config.Configuration.providers       # get number of network providers from config file


def get_data(address):
    zip_code = get_zip_code(api_address,address)    # get Zip Code from the response of Geo API
    if type(zip_code) is dict:                      # if zip code do not exist, give response to the user
        response = zip_code
        return response

    # get network coverage data from csv of a city using its Zip code
    resource = get_data_from_csv(zip_code, data_path, providers)
    response = resource_representation(resource)    # Transform data to dictionnary (json format)
    return response
