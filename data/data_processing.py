import pandas as pd
import requests

data = pd.read_csv("test.csv", delimiter=';') # Read CSV file
data = data.dropna() # delete null values

# convert lambert coordinates to GPS longitude and latitude
def LambertToGPS(x,y) :
    import pyproj
    lambert = pyproj.Proj(
        '+proj=lcc +lat_1=49 +lat_2=44 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs')
    wgs84 = pyproj.Proj('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
    long, lat = pyproj.transform(lambert, wgs84, x, y)
    return long,lat

# get ressource from api
def getCity(x,y):
    long,lat=LambertToGPS(x, y)
    api_adress = 'https://api-adresse.data.gouv.fr/reverse/'
    ploads = {'long':long,'lat':lat} # get request parameter
    r = requests.get(api_adress, params=ploads)
    response = r.json()  # get response in Json format
    try :
        city = response ['features'][0]['properties']['city']
        return (city)
    except :
        pass

print("processing Data .....")

data['city'] = data.apply(lambda row: getCity(row['X'],row['Y']), axis=1) # find city for each row
data = data.dropna() # delete null values
data.to_csv('preprocessed_data.csv', sep=';', index=False) # save new processed csv file

