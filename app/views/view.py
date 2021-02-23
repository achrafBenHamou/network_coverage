from app import config

providers = config.Configuration.providers # get dictionnary of providers with key =  id and value = provider
networks = config.Configuration.networks # ["2G","3G","4G"]
"""
def getXYfromRessource(ressource): # takes response of geo api as parameter
    response = ressource['features'][0]['properties']
    print(response)
    geo_coordinate = (int(response['x']),int(response['y']),response['city'])
    return (geo_coordinate) # return Lambert93 coordinates
"""
def getCityfromRessource(ressource): # this function takes response of geo api as parameter
    response = ressource['features'][0]['properties']
    city = response['city']
    return city # return city

def ressourcePresentation(ressource_list):
    """
        this function takes list of rows finded in data as parameter,
        Example :
        [['20801', '102980', '6847973', '1', '1', '0', 'Paris'],
        ['20810', '102980', '6847973', '1', '1', '0', 'Paris'],
        ['20820', '102980', '6847973', '1', '1', '0', 'Paris'],
        ['20815', '102980', '6847973', '1', '1', '0', 'Paris']]
    """
    output = {} # dictionary
    for l in ressource_list:
        network_output ={}
        for i in range (3,len(networks)+3): # treat just the 3th to 5th elements of list
            if (int(l[i]==1)):
                network_output[networks[i - 3]] = True # networks = ["2G","3G","4G"]
            else :
                network_output[networks[i - 3]] = False
        output[providers[int(l[0])]] = network_output

    return output


