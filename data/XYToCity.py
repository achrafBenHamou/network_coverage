import pandas as pd
import requests
#import tqdm

data = pd.read_csv("2018_01_Sites_mobiles_2G_3G_4G_France_metropolitaine_L93.csv", delimiter=';')
data = data.dropna()

def LambertToGPS(x,y) :
    import pyproj
    lambert = pyproj.Proj(
        '+proj=lcc +lat_1=49 +lat_2=44 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs')
    wgs84 = pyproj.Proj('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
    #x = 102980
    #y = 6847973
    long, lat = pyproj.transform(lambert, wgs84, x, y)
    return long,lat

# get ressource from api using long lat
def getCity(x,y):
    long,lat=LambertToGPS(x, y)
    api_adress = 'https://api-adresse.data.gouv.fr/reverse/'
    ploads = {'long':long,'lat':lat} # get request parameter
    r = requests.get(api_adress, params=ploads)
    response = r.json() #get response in Json format
    try :
        city = response ['features'][0]['properties']['city']
        #print(x ,y ,city)
        return (city)
    except :
        pass


#print(data.head())
print("processing Data .....")
data['city'] = data.apply(lambda row: getCity(row['X'],row['Y']), axis=1)
data = data.dropna()
#data = data[['X','city']].groupby(['city'], as_index=False)
data.to_csv('preprocessed_data.csv')
print(data.head())
print(getCity(102980,6847973))
