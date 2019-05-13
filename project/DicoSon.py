# ---- IMPORTS DE MODULES ----
import csv              # Lecture fichiers CSV
import urllib           # Requêtes URL.
import json             # Lecture JSON.
from time import sleep  # Fonction de pause du programme.

# ---- DICTIONNAIRE DES VILLES ----

CITIES = {
    # Ajouter villes (clé int, valeur str)...
}

# ---- CONFIG PROGRAMME ----
SLEEP_TIME = 0.05   # Durée de pause du programme à chque boucle (en s).
CSV_FILE_PATH = 'files/dico.csv'    # Emplacement du fichier CSV.

# ---- CONFIG THINGSPEAK ----

TS_CHANNEL_ID = ''          # ID chaîne ThingSpeak.
TS_API_READ_KEY = ''        # Clé de lecture de la chaîne ThingSpeak.
TS_JSON_FILE_NAME = ''      # Nom du fichier JSON contenant les données.
TS_FIELD_NAME = ''          # Nom du champ de données.

# URL ThingSpeak
TS_READ_URL = 'https://api.thingspeak.com/channels/{0}/fields/{1}?api_key={2}&results=1'.format(
    TS_CHANNEL_ID,
    TS_JSON_FILE_NAME,
    TS_API_READ_KEY
)

# ---- CONFIG CSV ----
VAL_SEPARATOR = ';' # Séparateur entre les valeurs.
IS_QUOTING_ENABLED = False # Y a-t-il des chaînes de caractères ?
STR_SEPARATOR = '' # Séparateur de chaîne de caractère.

# ---- FONCTIONS ----

def play(path):
    """Fonction de lecture du son.
    Paramètres :
        - path (str) : emplacement du fichier sonore à jouer.
    """
    print('Son joué :', path)   # Non implémentée !

# ---- PROGRAMME ----

# Création du dictionnaire
csvData = None  # Variable données CSV.

with open(CSV_FILE_PATH) as csvFile:    # Ouverture sécurisée fichier.
    csvRawData = csv.reader(
        csvFile, # Fichier CSV
        delimiter=VAL_SEPARATOR, # Séparateur valeurs
        quotechar=STR_SEPARATOR if IS_QUOTING_ENABLED else None # Modification du caractère de séparation des chaînes si il y a des chaînes.
    ) # Lecture données CSV
    csvData = list(csvRawData) # Conversion en liste
    csvFile.close() # Fermeture fichier.

# Initialisation dictionnaire.
CITIES = {}

# Suppression des virgules.
for i in csvData: # On parcourt les éléments de csvData
    i[0] = i[0].replace(',', '.') # On remplace les virgules par des points.

# Création dictionnaire
for c in csvData:
    CITIES[float(c[0])] = c[1] # Même procédure, mais on convertit en float c[0].

# Boucle principale
while True:
    # Récupération des données de distance.
    tsField = urllib.request.urlopen(TS_READ_URL)   # Requête au serveur.
    tsRawData = tsField.read()  # Lecture données binaires.
    tsTextData = tsRawData.decode('utf-8')  # Décodage données binaires.
    tsPythonData = json.loads(tsTextData)
    
    # Valeur distance.
    dist = tsPythonData['feeds'][0][TS_FIELD_NAME]

    # Vérification dans le dictionnaire.
    if dist in CITIES.keys():   # Vérification de l'existence de la clé, prévention KeyError.
        play(CITIES[dist])  # Jeu du son.
        del CITIES[dist]    # Suppression du son du dictionnaire, afin d'éviter de le jouer deux fois si la variation de la distance est nulle.

    # Pause.
    sleep(SLEEP_TIME)