from app.model.data_provider import getNetworkCoverage
from app.service.entry_point import getAdressRessource
from app.views.view import ressourcePresentation, getCityfromRessource


def get_data(adress):
    ressource = getAdressRessource(adress)
    #x,y,city = getXYfromRessource(ressource)
    city = getCityfromRessource(ressource)
    #print(city)
    #ressource = getNetworkCoveragee(x,y)
    ressource = getNetworkCoverage(city)
    print('ressource',ressource)
    response = ressourcePresentation(ressource)
    return response
