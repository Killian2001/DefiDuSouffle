# DefiDuSouffle

Ce dépôt a été créé dans le cadre de mon projet d'enseignement de spécialité Informatique et Science du Numérique (ISN), 
sur le &laquo;Défi du Souffle&raquo;, projet de lutte anti-tabac du lycée Notre Dame du Mur - Le Porsmeur.
Ce fichier README.md présente la structure du dépôt GitHub.

Le dépôt est conçu en grande partie pour fonctionner sous Jupyter Notebook avec Python 3 + IPython.

## 1. Les bloc-notes Jupyter.
Ces bloc-notes constituent &laquo;dossier-projet&raquo; numérique, exigé par les modalités d'examination de la spécialité ISN
dans le cadre du baccalauréat.
* Le bloc-note [`index.ipynb`](index.ipynb) est le bloc-note &laquo;sommaire&raquo; répertoriant l'ensemble des bloc-notes du 
dossier-projet, ainsi que quelques liens pratiques.
* Le bloc-note [`diapo.ipynb`](diapo.ipynb) sert de support visuel pour la prestation orale de l'épreuve d'ISN. Visionnable 
en mode diaporama, il est le condensé du dossier-projet.
* Le bloc-note [`presentation_besoin.ipynb`](presentation_besoin.ipynb) présente le projet dans sa globalité, fixe le besoin 
auquel il devra répondre et introduit ma participation au projet.
* Le bloc-note [`jeu_son.ipynb`](jeu_son.ipynb) présente une solution pour permettre de jouer un son sur Jupyter Notebook *via* 
Python et IPython.
* Le bloc-note [`dictionnaire_son.ipynb`](dictionnaire_son.ipynb) présente une solution pour associer un son et une
distance avec le type dictionnaire de Python.
* Le bloc-note [`données.ipynb`](données.ipynb) présente différentes solutions de stockage de données dans un fichier externe, 
avec JSON ou CSV
* Le bloc-note [`recup_donnees_thingspeak.ipynb`](recup_donnees_thingspeak.ipynb) présente une solution pour récupérer des 
informations d'un capteur depuis un ordinateur *via* l'API web ThingSpeak.

## 2. Les répertoires
Les répertoires contiennent différents fichiers nécessaires au bon fonctionnement du projet ou des démonstrations faites dans 
les bloc-notes.
* Le répertoire [`files`](files) contient les différents fichiers de données (texte, JSON, CSV...) nécessaire au projet.
* Le répertoire [`img`](img) contient les images permettant d'illustrer les bloc-notes ; il possède un sous répertoire 
[`presentation`](img/presentation) contenant les images permettant d'illustrer le support visuel de l'oral.
* Le répertoire [`project`](project) contient le code source du projet d'ISN. Voir le détail dans la section &laquo;Répertoire 
`project` ci-après.
* Le répertoire [`sounds`](sounds) contient les différents sons utilisés (format WAV de préférence) dans les bloc-notes.

## 3. Répertoire [`project`](project)
Le répertoire [`project`](project) contient le code source du projet d'ISN. Il contient :
* Un fichier Python [`DicoSon.py`](project/DicoSon.py), code source du programme créé dans le cadre du projet.
* Un fichier Python [`dataSender.py`](project/dataSender.py), code source d'un programme d'envoi de données ThingSpeak pour
tester le programme de [`DicoSon.py`](project/DicoSon.py).
* Deux bloc-notes Jupyter [`DicoSon.ipynb`](project/DicoSon.ipynb) et [`dataSender.ipynb`](project/dataSender.ipynb), permettant
d'exécuter les programmes Python [`DicoSon.py`](project/DicoSon.py) et [`dataSender.py`](project/dataSender.py).
* Un répertoire [`files`](project/files), qui contient les fichiers de données nécessaires en fonctionnement du programme.
* Un répertoire [`sounds`](project/sounds), qui contient les son utilisés par le programme (format WAV de préférence).
