import time
import keyboard

# Function pause prank
##############################################
def pause():
    time.sleep(5)

# Function get local time
##############################################
def get_localtime():
    local_time = time.localtime()
    hours = local_time.tm_hour
    minutes = local_time.tm_min
    seconds = local_time.tm_sec
    return hours, minutes, seconds

# Function show clock
##############################################
def running(hours, minutes, seconds):
    while True:
        time_display = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
        print(f"\r{time_display}", end="")
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

        if (hours + minutes + seconds) % 13 == 0:
            pause()

        if keyboard.is_pressed('esc'):
            break

# Function show Local Time
##############################################
def localtime():
    print("\n--- Local Time ---\nHold 'ESC' to return to the menu")
    hours, minutes, seconds = get_localtime()
    running(hours, minutes, seconds)

# Function show Custom Time
##############################################
def afficher_heure():
    print("\n--- Custom Time ---\nHold 'ESC' to return to the menu")
    try:
        hours = int(input("Enter a hour (0-23) : "))
        minutes = int(input("Enter a minute (0-59) : "))
        seconds = int(input("Enter a second (0-59) : "))
        if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
            raise ValueError("Invalid choice, please retry")
        running(hours, minutes, seconds)
    except ValueError:
        print(f"Invalid entry, please use a number")

# Function Alarm
##############################################
def alarm_localtime():
    print("NON")

def alarm_custom():
    print("NON")

# Menu
##############################################
def main():
    while True:
        print("\n---- MENU ----")
        print("1. Local Time")
        print("2. Custom time")
        print("3. Set an alarm on local time")
        print("4. Set an alarm on custom time")
        print("5. Leave")
        try:
            choice = int(input("Your choice : "))
            if choice == 1:
                localtime()
            elif choice == 2:
                afficher_heure()
            elif choice == 3:
                alarm_localtime()
            elif choice == 4:
                alarm_custom()
            elif choice == 5:
                print("\nAu revoir !")
                break
            else:
                print("Invalid choice, please retry")
        except ValueError:
            print("Invalid entry, please use a number")

# Program execute
##############################################
if __name__ == "__main__":
    main()
