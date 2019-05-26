"""Programme d'envoi automatique de données sur le channel ThingSpeak."""

# ---- IMPORTS DE MODULES ----
import urllib           # Requêtes URL
from time import sleep  # Fonction de mise en pause du programme.

# ---- CONFIG THINGSPEAK ----
TS_API_WRITE_KEY = 'SFQYYW6GII6TB1W6'       # Clé d'écriture de la chaîne ThingSpeak.
TS_FIELD_NAME = 'field1'          # Nom du champ de données.

TS_WRITE_URL = 'https://api.thingspeak.com/update?api_key={0}&{1}='.format( # URL d'écriture partiel des données de la chaîne ThingSpeak.
    TS_API_WRITE_KEY,
    TS_FIELD_NAME
)

min = int(input('Entrez un minimum : '))    # Minimum à entrer.
max = int(input('Entrez un maximum : '))    # Maximum à entrer.
step = int(input('Entrez le pas : '))       # Pas de la boucle à entrer
sleepTime = float(input('Entrez une durée de pause du programme à chaque boucle (en s): ')) #Temps de pause du programme à entrer.

print('ENVOI DES DONNÉES')
for n in range(min, max, step):   # Boucle d'envoi des données
    url = '{0}{1}'.format(TS_WRITE_URL, n)  # URL total d'envoi des données
    print('n = {}'.format(n))
    urllib.request.urlopen(url) # Envoi des données
    print('Données envoyées à : {}'.format(url))
    sleep(sleepTime)    # Pause programme de sleepTime
print('FIN ENVOI DES DONNÉES')