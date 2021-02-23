## install requirements 
lancer la commande 
pip install requirements.txt

## Data pre-processing
j'ai utilise le fichier XYTocity pour faire le preprocessing des donnees.
le but de ce script est de trouver la ville a travaers les coordonnes Lambert93 X,Y.
et d'eleminer les valeurs nulls qui existeent dans les donnees
a la fin le script va produire un nouveau fichier csv qui contient une nouvelle colonne city.
pour que l'api peut trouver des resultas plus rapidement, et sans envoyer des requetes a chaque fois.
le fichier resultat est nommee : preprocessed_data
### pour lancerle fichier 
cd data
python XYToCity.py

## Run Project
python main.py