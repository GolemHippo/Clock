""""Vous ajoutez une fonction nommée “afficher_heure” qui permet de
régler l'heure. Cette fonction devra prendre en paramètre une heure
sous la forme d'un tuple (heures, minutes, secondes) et devra mettre à
jour l'heure affichée grâce à la fonction “afficher_heure”."""

import time
heures, minutes, secondes = 0, 0, 0 #INITIALISATION DES VARIABLES

def regler_heure(heure):
    global heures, minutes, secondes
    heures, minutes, secondes = heure #INITIALISATION TUPLE HEURE

def afficher_heure():
    global heures, minutes, secondes
    secondes += 1
    if secondes >= 60:
        secondes = 0
        minutes += 1

    if minutes >= 60:
        minutes = 0
        heures += 1

    if heures >= 24:
        heures = 0

regler_heure((3, 30, 45))

while True:
    afficher_heure()
    time.sleep(1)
    heure_formattee = f"{str(heures).zfill(2)}:{str(minutes).zfill(2)}:{str(secondes).zfill(2)}"
    print(heure_formattee)

