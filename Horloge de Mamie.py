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
def running(hours, minutes, seconds, format):
    while True:
        if format == 'a':
            n_hours = hours
            if hours > 12:
                meridiem = 'PM'
                n_hours = hours - 12
            if hours < 12:
                meridiem = 'AM'
            if hours == 12:
                meridiem = 'PM'
            time_display = f"{(n_hours):02}:{(minutes):02}:{(seconds):02} {meridiem}"
            print(f"\r{time_display}", end="")
        if format == 'b':
            time_display = f"{(hours):02}:{(minutes):02}:{(seconds):02}"
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

        if (hours + minutes + seconds) % 31 == 0:
            pause()

        if keyboard.is_pressed('esc'):
            print("\n\n")
            break

# Function show Local Time
##############################################
def localtime(format):
    print("\n--- Local Time ---\nHold 'ESC' to return to the menu")
    hours, minutes, seconds = get_localtime()
    running(hours, minutes, seconds, format)

# Function show Custom Time
##############################################
def afficher_heure(format):
    print("\n--- Custom Time ---\nHold 'ESC' to return to the menu")
    while True:
        try:
            hours = int(input("Enter a hour (0-23) : "))
            minutes = int(input("Enter a minute (0-59) : "))
            seconds = int(input("Enter a second (0-59) : "))
            if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
                raise ValueError("\nInvalid choice, please retry")
            running(hours, minutes, seconds, format)
            break
        except ValueError:
            print("\nInvalid entry, please use a number")

# Function running clock with alarm
##############################################
def running_alarm(hours, minutes, seconds, alarm_h, alarm_min, alarm_sec, format):
    while True:
        if format == 'a':
            n_hours = hours
            if hours > 12:
                meridiem = 'PM'
                n_hours = hours - 12
            if hours < 12:
                meridiem = 'AM'
            if hours == 12:
                meridiem = 'PM'
            time_display = f"{(n_hours):02}:{(minutes):02}:{(seconds):02} {meridiem}"
            print(f"\r{time_display}", end="")
        if format == 'b':
            time_display = f"{(hours):02}:{(minutes):02}:{(seconds):02}"
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
        
        if hours == alarm_h and minutes == alarm_min and seconds == alarm_sec:
            print()
            print("\nDING DING !!!")
            print()

        if (hours + minutes + seconds) % 13 == 0:
            pause()

        if keyboard.is_pressed('esc'):
            print("\n\n")
            break

# Function Ask Alarm
##############################################
def ask_alarm():
    while True:
        if format == 'b':
            try:
                alarm_h = int(input("\nSet the alarm...\nEnter a hour (0-23): "))
                alarm_min = int(input("Enter a minute (0-59): "))
                alarm_sec = int(input("Enter a second (0-59): "))
                if not (0 <= alarm_h < 24 and 0 <= alarm_min < 60 and 0 <= alarm_sec < 60):
                    raise ValueError("\nInvalid time. Please try again.")
                print()
                print(f"Alarm set at {(alarm_h):02}:{(alarm_min):02}:{(alarm_sec):02}")
                return alarm_h, alarm_min, alarm_sec
            except ValueError:
                print("\nInvalid entry, please use numbers")
        if format == 'a':
            try:
                alarm_meridiem = input("\nEnter the meridiem (AM/PM) : ")
                n_alarm_h = int(input("\nSet the alarm...\nEnter a hour (0-12): "))
                alarm_min = int(input("Enter a minute (0-59): "))
                alarm_sec = int(input("Enter a second (0-59): "))
                if not (0 <= n_alarm_h < 13 and 0 <= alarm_min < 60 and 0 <= alarm_sec < 60):
                    raise ValueError("\nInvalid time. Please try again.")
                if not (alarm_meridiem == 'AM' or alarm_meridiem == 'PM'):
                    raise ValueError("\nInvalid meridiem. Please try again... 'AM'/'PM'")
                if alarm_meridiem == 'PM':
                    alarm_h = n_alarm_h + 12
                else:
                    alarm_h = n_alarm_h
                print()
                print(f"Alarm set at {(n_alarm_h):02}:{(alarm_min):02}:{(alarm_sec):02} {alarm_meridiem}")
                return alarm_h, alarm_min, alarm_sec
            except ValueError:
                print("\nInvalid entry, please use numbers")

# Function show Local Time with alarm
##############################################
def alarm_localtime(format):
    print("\n--- Alarm on Local Time ---\nHold 'ESC' to return to the menu")
    alarm_h, alarm_min, alarm_sec = ask_alarm()
    hours, minutes, seconds = get_localtime()
    print()
    running_alarm(hours, minutes, seconds, alarm_h, alarm_min, alarm_sec, format)

# Function show Custom Time with alarm
##############################################
def alarm_custom(format):
    print("\n--- Alarm on Custom Time ---\nHold 'ESC' to return to the menu")
    try:
        hours = int(input("\nSet clock\nEnter a hour (0-23): "))
        minutes = int(input("Enter a minute (0-59): "))
        seconds = int(input("Enter a second (0-59): "))
        if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
            raise ValueError("\nInvalid custom time. Please try again.")
        alarm_h, alarm_min, alarm_sec = ask_alarm()
        running_alarm(hours, minutes, seconds, alarm_h, alarm_min, alarm_sec, format)
    except ValueError:
        print("\nInvalid entry, please use numbers")


# Menu
##############################################
def main(format):
    while True:
        print("\n---- MENU ----")
        print("1. Local Time")
        print("2. Custom time")
        print("3. Set an alarm on local time")
        print("4. Set an alarm on custom time")
        print("5. Set the display format (12h/24H)")
        print("6. Leave")
        try:
            choice = int(input("Your choice : "))
            if choice == 1:
                localtime(format)
            elif choice == 2:
                afficher_heure(format)
            elif choice == 3:
                alarm_localtime(format)
            elif choice == 4:
                alarm_custom(format)
            elif choice == 5:
                menu()    
            elif choice == 6:
                print("\nAu revoir !")
                exit()
            else:
                print("\nInvalid choice, please retry")
        except ValueError:
            print("\nInvalid entry, please use a number")

# Format ask
##############################################
def format_ask():
    while True:
        format = input("\nDo you want to use 12h 'a' or 24h 'b' format ? : ")
        if format == 'a' or format == 'b':
            if format == 'a':
                print("You are using 12h format")
                return format
            if format == 'b':
                print("You are using 24h format")
                return format
        else:
            print("\nInvalid choice, please retry")


##############################################
def menu():
    while True:
        format = format_ask()
        main(format)


# Program execute
##############################################
if __name__ == "__main__":
    menu()
