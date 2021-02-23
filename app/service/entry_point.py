import requests

# get ressource from api using textual adress
def getAdressRessource(adress):
    api_adress = 'https://api-adresse.data.gouv.fr/search/'
    ploads = {'q':adress} # get request parameter
    r = requests.get(api_adress, params=ploads)
    response = r.json() #get response in Json format
    return (response)

# get ressource from api using long lat
def getAdressRessource(adress):
    api_adress = 'https://api-adresse.data.gouv.fr/search/'
    ploads = {'q':adress} # get request parameter
    r = requests.get(api_adress, params=ploads)
    response = r.json() #get response in Json format
    return (response)


