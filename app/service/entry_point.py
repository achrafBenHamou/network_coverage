import requests


# get resource from api using textual address
def getAddressResource(address):
    try:
        api_address = 'https://api-adresse.data.gouv.fr/search/'
        ploads = {'q': address}  # request parameter
        r = requests.get(api_address, params=ploads)
        response = r.json()  # get response in Json format
        return response
    except Exception as e:
        print(e)
        return 0
