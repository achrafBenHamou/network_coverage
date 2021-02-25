import requests

# get resource from Geo api using textual address
def get_zip_code(api_address,address):
    try:
        ploads = {'q': address}  # request parameter
        r = requests.get(api_address, params=ploads)
        if r.status_code == 200:
            response = r.json()  # get response in Json format
            try:
                response= response['features'][0]['properties']
                zip_code = response['postcode']
                return int(zip_code)
            except Exception as e:
                print("Geo api Web service cannot find resources for this address,",e)
                return {"Result": " Geo api Web service cannot find resources for this address"}
        else:
            return {"Error": "Not found"}
    except requests.exceptions.RequestException as exception:
        print(exception)
        return {"Error": " Geo api Web service exception"}
