import time
heures, minutes, secondes = 0, 0, 0

def regler_heure(heure):
    global heures, minutes, secondes
    heures, minutes, secondes = heure

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
    heure_formattee = f"{str(heures).zfill(2)}:{str(minutes).zfill(2)}:{str(secondes).zfill(2)}"

    print(heure_formattee)

regler_heure((3, 30, 45))

while True:
    afficher_heure()
    time.sleep(1)
    heure_formattee = f"{str(heures).zfill(2)}:{str(minutes).zfill(2)}:{str(secondes).zfill(2)}"
    print(heure_formattee)

