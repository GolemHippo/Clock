# Importing the library
import time
        
# Function Show LocalTime
def localtime():
    print()
    print("Horaire Local")
    global hours, minutes, seconds
    hours = 00
    minutes = 00
    seconds = 00
    while True:
        timeis = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
        print(timeis)
        time.sleep(1)
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
        if hours == 24:
            hours = 0
        

# Function DisplayClock
def afficher_heure():
    print()
    print("Horaire réglée à 10:30:20")
    global hours, minutes, seconds
    hours = 10
    minutes = 30
    seconds = 20
    while True:
        timeis = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
        print(timeis)
        time.sleep(1)
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
        if hours == 24:
            hours = 0


# MAIN
while True:
    print()
    choice = int(input("Que voulez-vous faire ?\n- Afficher l'heure actuel '1'\n- Régler l'heure '2'\nChoix :  "))
    if choice == 1:
        localtime()
    if choice == 2:
        afficher_heure()
