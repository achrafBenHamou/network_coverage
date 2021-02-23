from app.model.data_provider import getNetworkCoverage
from app.service.entry_point import getAdressRessource
from app.views.view import RessourcePresentation, getCityfromRessource


def get_data(adress):
    ressource = getAdressRessource(adress)
    #x,y,city = getXYfromRessource(ressource)
    city = getCityfromRessource(ressource)
    #print(city)
    #ressource = getNetworkCoveragee(x,y)
    ressource = getNetworkCoverage(city) # liste of
    print('ressource',ressource)
    response = RessourcePresentation(ressource)
    return response

#t(get_data('20 Avenue de Ségur 75007 Paris'))