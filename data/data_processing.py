# !/usr/local/bin/python
import pandas as pd
import requests

# Read CSV file
data = pd.read_csv("2018_01_Sites_mobiles_2G_3G_4G_France_metropolitaine_L93.csv", delimiter=';')
# Delete null values
data = data.dropna()


# Convert from Lambert 93 to GPS coordinates
def lambert_to_gps(x, y):
    import pyproj
    lambert = pyproj.Proj(
        '+proj=lcc +lat_1=49 +lat_2=44 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs')
    wgs84 = pyproj.Proj('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
    long, lat = pyproj.transform(lambert, wgs84, x, y)
    return long, lat


# get resource using GEO api
def get_code_zip(x, y):
    long, lat = lambert_to_gps(x, y)  # Convert from Lambert 93 to GPS coordinates
    api_address = 'https://api-adresse.data.gouv.fr/reverse/'
    ploads = {'long': long, 'lat': lat}  # get request parameters
    r = requests.get(api_address, params=ploads)
    response = r.json()  # get response in Json format
    try:
        code_zip = response['features'][0]['properties']['postcode']
        print("X=", x, "Y=", y, "====> zip_code=", code_zip)
        return code_zip
    except Exception as e:
        print("Zip code is not exist for this address. ", e)
        pass


print("Data processing.....")

data['postcode'] = data.apply(lambda row: get_code_zip(row['X'], row['Y']), axis=1)  # find Zip code for each row
data = data.dropna()  # delete null values
data.to_csv('preprocessed_data.csv', sep=';', index=False)  # save new processed csv file
print("Done.")
