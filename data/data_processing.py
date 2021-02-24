import pandas as pd
import requests

# Read CSV file
data = pd.read_csv("2018_01_Sites_mobiles_2G_3G_4G_France_metropolitaine_L93.csv", delimiter=';')
data = data.dropna()  # delete null values


# Convert from Lambert 93 to GPS coordinates
def LambertToGPS(x, y):
    import pyproj
    lambert = pyproj.Proj(
        '+proj=lcc +lat_1=49 +lat_2=44 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs')
    wgs84 = pyproj.Proj('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
    long, lat = pyproj.transform(lambert, wgs84, x, y)
    return long, lat


# get ressource from api
def getCodeZip(x, y):
    long, lat = LambertToGPS(x, y)  # Convert from Lambert 93 to GPS coordinates
    api_adress = 'https://api-adresse.data.gouv.fr/reverse/'
    ploads = {'long': long, 'lat': lat}  # get request parameter
    r = requests.get(api_adress, params=ploads)
    response = r.json()  # get response in Json format
    try:
        code_zip = response['features'][0]['properties']['postcode']
        print("X=", x, "Y=", y, "====> zip_code=", code_zip)
        return code_zip
    except Exception as e:
        print("Zip code is not exist for this address. ", e)
        pass

print("This process will take a time")
print("processing Data .....")

data['postcode'] = data.apply(lambda row: getCodeZip(row['X'], row['Y']), axis=1)  # find Zip code for each row
data = data.dropna()  # delete null values
data.to_csv('preprocessed_data.csv', sep=';', index=False)  # save new processed csv file
print("Done.")
