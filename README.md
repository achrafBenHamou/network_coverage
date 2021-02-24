# Network Coverage
This project aims to build a api that we can request with
a textual address request and retrieve 2G/3G/4G 
network coverage for each operator (if available)
in the response
The goal is not to work on precise geographic match,
a city-level precision is enough.

## example of request 
```sh
Get : 
          http://127.0.0.1:5000/address/82 Rue des docteurs charcot 42100 st etienne 
Result : 
         {"Bouygues": { "2G": true, "3G": true, "4G": true }, 
          "Free": { "2G": false, "3G": true, "4G": true }, 
          "Orange": { "2G": true, "3G": true, "4G": true }, 
          "SFR": { "2G": true, "3G": true, "4G": true } }
```
## install requirements 
Start the command :
```sh
pip install -r requirements.txt
```

## Data processing
I used data_processing.py file to do the data processing.
The goal of this script is to find the zip code through the Lambert93 X, Y coordinates.
and eliminate any null values that exist in the data.
At the end, the script will produce a new csv file which contains a new zip_code column.
so that the API can find results faster, and without sending requests every time.
the resulting file is named: preprocessed_data.csv
To run the script again, run the following commands:
```sh
cd data
python data_processing.py
```
## Run Project
To run the project use the following command :
```sh
python main.py
```
## Data source
- https://www.data.gouv.fr/s/resources/monreseaumobile/20180228-174515/2018_01_Sites_mobiles_2G_3G_4G_France_metropolitaine_L93.csv
- https://adresse.data.gouv.fr/api
