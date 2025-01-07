# Importing the library
import time
        
# Function Show LocalTime
def localtime():
    print()
    print("Local Time")
    global hours, minutes, seconds
    hours = 00
    minutes = 00
    seconds = 00
    while True:
        timeis = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
        print(f"\r{timeis}", end="")
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
    print("Time set at 10:30:20")
    global hours, minutes, seconds
    hours = 10
    minutes = 30
    seconds = 20
    while True:
        timeis = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
        print(f"\r{timeis}", end="")
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

# Function Alarm Set Local Time
def alarm_localtime():
    print()
    global hours, minutes, seconds
    alarm_hours = int(input("Set an alarm...\nEnter a hour (00-23) : "))
    alarm_minutes = int(input("Enter a minute (00-59) : "))
    alarm_seconds = int(input("Enter a second (00-59) : "))
    print()
    print(f"Alarm set at {str(alarm_hours).zfill(2)}:{str(alarm_minutes).zfill(2)}:{str(alarm_seconds).zfill(2)}")
    hours, minutes, seconds = 0, 0, 0 
    while True:
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
        if hours == 24:
            hours = 0
        timeis = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
        print(f"\r{timeis}", end="")
        time.sleep(1)
        if hours == alarm_hours and minutes == alarm_minutes and seconds == alarm_seconds:
            print()
            print("\nDING DING !!!")
            break

# Function Alarm Set Display Time
def alarm_customtime():
    print()
    global hours, minutes, seconds
    alarm_hours = int(input("Set an alarm...\nEnter a hour (00-23) : "))
    alarm_minutes = int(input("Enter a minute (00-59) : "))
    alarm_seconds = int(input("Enter a second (00-59) : "))
    print()
    print(f"Alarm set at {str(alarm_hours).zfill(2)}:{str(alarm_minutes).zfill(2)}:{str(alarm_seconds).zfill(2)}")
    hours, minutes, seconds = 10, 30, 20
    while True:
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
        if hours == 24:
            hours = 0
        timeis = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
        print(f"\r{timeis}", end="")
        time.sleep(1)
        if hours == alarm_hours and minutes == alarm_minutes and seconds == alarm_seconds:
            print()
            print("\nDING DING !!!")
            break


# MAIN
def main():
    while True:
        print("\n---- MENU ----")
        print("1. Show Local Time")
        print("2. Set Custom Time")
        print("3. Set Alarm on Local Time")
        print("4. Set Alarm on Custom Time")
        print("5. Leave")
        choice = int(input("Your choice : "))
        
        if choice == 1:
            localtime()
        elif choice == 2:
            afficher_heure()
        elif choice == 3:
            alarm_localtime()
        elif choice == 4:
            alarm_customtime()
        elif choice == 5:
            print()
            print("GoodBye !")
            print()
            break
        else:
            print()
            print("Error, retry...")


# Program execute
if __name__ == "__main__":
    main()
