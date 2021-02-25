#from enum import Enum
class Configuration:
    """ if you need to add data with other network providers,
        you can just add its ids and names in the dictionary.
    """
    data = '../data/preprocessed_data.csv'    # processed data path
    api_address = 'https://api-adresse.data.gouv.fr/search/' # api web service

    # dictionary of network providers with ids
    providers = {20801: 'Orange',
                 20810: 'SFR',
                 20815: 'Free',
                 20820: 'Bouygues'
                 }

