from app import config

providers = config.Configuration.providers # get dictionnary of providers with key =  id and value = provider
networks = config.Configuration.networks # ["2G","3G","4G"]

def getXYfromRessource(ressource): # takes response of geo api as parameter
    response = ressource['features'][0]['properties']
    print(response)
    geo_coordinate = (int(response['x']),int(response['y']),response['city'])
    return (geo_coordinate) # return Lambert93 coordinates

def getCityfromRessource(ressource): # takes response of geo api as parameter
    response = ressource['features'][0]['properties']
    print(response)
    city = response['city']
    return city # return city

def RessourcePresentation(ressource_list):
    output = {} # dictionary
    for l in ressource_list:
        #result_map = list(map(lambda x:int(x),l[:-1])) # transform all element of each list to integer
        result_map = l
        network_output ={}
        for i in range (3,len(networks)+3):
            if (int(result_map[i]==1)):
                network_output[networks[i - 3]] = True
            else :
                network_output[networks[i - 3]] = False
        output[providers[int(result_map[0])]]=network_output
    return output


