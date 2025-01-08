# Importing the library
import time

def get_localtime():
    global hours, minutes, seconds
    hours = int(time.strftime('%H'))
    minutes = int(time.strftime('%M'))
    seconds = int(time.strftime('%S'))

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

def show_time():
    global seconds, hours, minutes
    timeis = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    print(f"\r{timeis}", end="")
    time_running()


def show_time12h():
    global hours, minutes, seconds, meridiem
    if hours == 12:
        meridiem = 'PM'
    elif hours > 12:
        meridiem = 'PM'
        m_hours = hours - 12
    else:
        meridiem = 'AM'
        m_hours = hours
    timeis = f"{str(m_hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}:{str(meridiem)}"
    print(f"\r{timeis}", end="")
    time_running()

# Function Show Local Time (fixed)
def localtime():
    print()
    print("Local Time")
    get_localtime()
    while True:
        show_time()

def localtime12h():
    print()
    print("Local Time")
    get_localtime()
    while True:
        show_time12h()
        
# Function Show Custom Clock (fixed)
def set_time():
    print()
    print("Time set at 10:30:20")
    global hours, minutes, seconds
    hours = 10
    minutes = 30
    seconds = 20
    while True:
        show_time()
    
def set_time12h():
    print()
    print("Time set at 10:30:20")
    global hours, minutes, seconds
    hours = 10
    minutes = 30
    seconds = 20
    while True:
        show_time12h()

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
    print(f"Alarm set at {str(alarm_hours).zfill(2)}:{str(alarm_minutes).zfill(2)}:{str(alarm_seconds).zfill(2)}")
    get_localtime()
    while True:
        show_time()
        if hours == alarm_hours and minutes == alarm_minutes and seconds == alarm_seconds:
            print("\nDING DING !!!")
            break
            
def alarm_localtime12h():
    print()
    global hours, minutes, seconds, meridiem, alarm_hours, alarm_minutes, alarm_seconds
    ask_alarm()
    if alarm_hours > 12:
        alarm_meridiem = 'PM'
        alarm_hours -= 12
    else:
        alarm_meridiem = 'AM'
    print(f"Alarm set at {str(alarm_hours).zfill(2)}:{str(alarm_minutes).zfill(2)}:{str(alarm_seconds).zfill(2)}:{str(alarm_meridiem)}")
    while True:
        get_localtime()
        if hours > 12:
            meridiem = 'PM'
            m_hours = hours - 12
        else:
            meridiem = 'AM'
            m_hours = hours    
        if m_hours == alarm_hours and minutes == alarm_minutes and seconds == alarm_seconds and meridiem == alarm_meridiem:
            show_time12h()
            print("\nDING DING !!!")
            break
        else:
            show_time12h()
            
# Function Alarm Set Custom Clock
def alarm_customtime():
    print()
    global hours, minutes, seconds
    ask_alarm()
    print(f"Alarm set at {str(alarm_hours).zfill(2)}:{str(alarm_minutes).zfill(2)}:{str(alarm_seconds).zfill(2)}")
    hours, minutes, seconds = 10, 30, 20
    while True:
        show_time()
        if hours == alarm_hours and minutes == alarm_minutes and seconds == alarm_seconds:
            
            print("\nDING DING !!!")
            break
            
def alarm_customtime12h():
    print()
    global hours, minutes, seconds, alarm_seconds, alarm_hours, alarm_minutes, meridiem
    ask_alarm()
    if alarm_hours > 12:
        alarm_meridiem = 'PM'
        alarm_hours -= 12
    else:
        alarm_meridiem = 'AM'
    print(f"Alarm set at {str(alarm_hours).zfill(2)}:{str(alarm_minutes).zfill(2)}:{str(alarm_seconds).zfill(2)}:{str(alarm_meridiem)}")
    hours, minutes, seconds = 10, 30, 20
    if hours > 12:
        meridiem = 'PM'
        m_hours = hours - 12
    else:
        meridiem = 'AM'
        m_hours = hours
    while True:
        show_time12h()
        if m_hours == alarm_hours and minutes == alarm_minutes and seconds == alarm_seconds and meridiem == alarm_meridiem:
            print("\nDING DING !!!")
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
            
def main_12h():
    while True:
        print("\n---- MENU ----")
        print("1. Show Local Time")
        print("2. Set Custom Time")
        print("3. Set Alarm on Local Time")
        print("4. Set Alarm on Custom Time")
        print('5. Display time on 24h Format')
        print("6. Leave")
        choice = int(input("Your choice : "))
        
        if choice == 1:
            localtime12h()
            
        elif choice == 2:
            set_time12h()
            
        elif choice == 3:
            alarm_localtime12h()
            
        elif choice == 4:
            alarm_customtime12h()
        
        elif choice == 5:
            main()
            
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