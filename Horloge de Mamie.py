# Importing the library
import time
import keyboard


def get_localtime():
    global hours, minutes, seconds
    hours = int(time.strftime('%H'))
    minutes = int(time.strftime('%M'))
    seconds = int(time.strftime('%S'))
    
def time_prank():
    if (hours + minutes + seconds)%7 == 0:
        time.sleep(7) 

def time_running():
    global seconds, minutes, hours
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
    if hours == 24:
        hours = 0
    time.sleep(1)
    time_prank()

def show_time():
    global seconds, hours, minutes
    timeis = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    print(f"\r{timeis}", end="")
    time_running()

# Function Show Local Time (fixed)
def localtime():
    print()
    print("Local Time Hold 'escape' to return to menu")
    get_localtime()
    while True:
        show_time()
        if keyboard.is_pressed('esc'):
            print()
            break
        
# Function Show Custom Clock (fixed)
def set_time():
    print()
    print("Time set at 10:30:20 \nHold 'escape' to return to menu")
    global hours, minutes, seconds
    hours = 10
    minutes = 30
    seconds = 20
    while True:
        show_time()
        if keyboard.is_pressed('esc'):
            print()
            break
    

def ask_alarm():
    global alarm_hours, alarm_minutes, alarm_seconds
    alarm_hours = int(input("Set an alarm...\nEnter a hour (00-23) : "))
    alarm_minutes = int(input("Enter a minute (00-59) : "))
    alarm_seconds = int(input("Enter a second (00-59) : "))
    print()


# Function Alarm Set Local Time
def alarm_localtime():
    global alarm_hours, alarm_minutes, alarm_seconds, seconds, hours, minutes
    print()
    ask_alarm()
    print(f"Alarm set at {str(alarm_hours).zfill(2)}:{str(alarm_minutes).zfill(2)}:{str(alarm_seconds).zfill(2)}\nHold 'escape' to return to menu")
    get_localtime()
    while True:
        show_time()
        if hours == alarm_hours and minutes == alarm_minutes and seconds == alarm_seconds:
            print("\nDING DING !!!")
            break
        if keyboard.is_pressed('esc'):
            print()
            break

            
# Function Alarm Set Custom Clock
def alarm_customtime():
    print()
    global hours, minutes, seconds
    ask_alarm()
    print(f"Alarm set at {str(alarm_hours).zfill(2)}:{str(alarm_minutes).zfill(2)}:{str(alarm_seconds).zfill(2)}\nHold 'escape' to return to menu")
    hours, minutes, seconds = 10, 30, 20
    while True:
        show_time()
        if hours == alarm_hours and minutes == alarm_minutes and seconds == alarm_seconds:
            
            print("\nDING DING !!!")
            break
        if keyboard.is_pressed('esc'):
            print()
            break
            


# Menu
def main():
    while True:
        print("\n---- MENU ----")
        print("1. Show Local Time")
        print("2. Set Custom Time")
        print("3. Set Alarm on Local Time")
        print("4. Set Alarm on Custom Time")
        print('5. Display time on 12h Format')
        print("6. Leave")
        choice = int(input("Your choice : "))
        
        if choice == 1:
            localtime()
            
        elif choice == 2:
            set_time()
            
        elif choice == 3:
            alarm_localtime()
            
        elif choice == 4:
            alarm_customtime()
        
        elif choice == 5:
            main_12h()
            
        elif choice == 6:
            print()
            print("GoodBye !")
            print()
            exit()
        else:
            print()
            print("Error, retry...")


# Program execute
if __name__ == "__main__":
    main()