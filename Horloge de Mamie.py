import time
from datetime import datetime, timedelta

class Horloge:
    def __init__(self):
        self.heure_actuelle = datetime.now()
        self.alarme = None

    def afficher_heure(self, heure_tuple=None):
        if heure_tuple:
            self.heure_actuelle = datetime.now().replace(hour=heure_tuple[0], minute=heure_tuple[1], second=heure_tuple[2])
        else:
            self.heure_actuelle += timedelta(seconds=1)
        
        print(self.heure_actuelle.strftime("%H:%M:%S"), end="\r")

    def regler_alarme(self, alarme_tuple):
        self.alarme = datetime.now().replace(hour=alarme_tuple[0], minute=alarme_tuple[1], second=alarme_tuple[2])
        print(f"Alarme réglée pour {self.alarme.strftime('%H:%M:%S')}")

    def verifier_alarme(self):
        if self.alarme and self.heure_actuelle.strftime("%H:%M:%S") == self.alarme.strftime("%H:%M:%S"):
            print("\nDRING DRING ! C'est l'heure du réveil !")
            self.alarme = None

    def run(self):
        while True:
            self.afficher_heure()
            self.verifier_alarme()
            time.sleep(1)

# Utilisation de la classe
horloge = Horloge()

# Régler l'heure (optionnel)
horloge.afficher_heure((16, 30, 0))

# Régler l'alarme (optionnel)
horloge.regler_alarme((16, 30, 10))

# Lancer l'horloge
horloge.run()
