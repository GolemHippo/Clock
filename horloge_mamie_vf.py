import time
import keyboard

#Function1 to choose a format 
def choose_a_format():
    while True:
        try:
            format = int(input("Choose a format 24h or 12h\n'24' or '12' : "))
            if format == 24:
                return format
            elif format == 12:
                return format
        except ValueError:
            print("Enter valid numeric values.")

#Function Origin set/local
def origin():
     while True:
        try:
            choice = input("Enter 1 to set time or 2 for local time: ")
            if choice == "1":
                return ask_time()
            elif choice == "2":
                hours = int(time.strftime('%H'))
                minutes = int(time.strftime('%M'))
                seconds = int(time.strftime('%S'))
                t_origin = hours, minutes, seconds
                return t_origin
            else:
                print("Please enter 1 or 2.")
        except ValueError:
            print("Enter valid numeric values.")

 #FUNCTION SET A TIME
def ask_time():
    while True:
        hours = input("Enter an hour (0-23): ")
        minutes = input("Enter minutes (0-59): ")
        try:
            hours = int(hours)
            minutes = int(minutes)
        except ValueError:
            print("Enter valid numeric values.")
            continue
        if 0 <= hours < 24 and 0 <= minutes < 60:
            seconds = 0
            t_origin = (hours, minutes, seconds)
            return t_origin
        else:
            print("Hours must be between 0-23 and minutes between 0-59.")

#Function set alarme
def set_alarm():
    while True:
        setalarm = input("Do you want to set an alarm?\n'y' or 'n' : ")
        if setalarm == 'y':
            h = input("Enter an hour (0-23): ")
            m = input("Enter minutes (0-59): ")
            try:
                h = int(h)
                m = int(m)
            except ValueError:
                print("Enter valid numeric values.")
                continue
            if 0 <= h < 24 and 0 <= m < 60:
                s = int(0)
                alarm = (h, m, s)
                return alarm
        if setalarm == 'n':
            alarm = (None, None, None)
            return alarm

def running(format, t_origin, alarm):
    hours, minutes, seconds = t_origin
    alarm_h, alarm_min, alarm_sec = alarm
    print("Hold 'ESC' to return to the menu")
    while True:
        if format == 12:
            if hours > 12:
                meridiem = 'PM'
                hours -= 12
            elif hours < 12:
                meridiem = 'AM'
            elif hours == 12:
                meridiem = 'PM'

        elif format == 24:
            meridiem = ''
        print(f"\r{(hours):02}:{(minutes):02}:{(seconds):02} {meridiem}", end="")
        if meridiem == 'PM'and hours != 12:
            hours +=12
        time.sleep(1)
        seconds += 1

        if seconds == 60:
            seconds = 0
            minutes += 1
        elif minutes == 60:
            minutes = 0
            hours += 1
        elif hours == 24:
            hours = 0
    
        elif (hours + minutes + seconds) % 31 == 0:
            time.sleep(3)

        if alarm_h==hours and alarm_min == minutes and alarm_sec== seconds:
            print("\n DING DING !!!\n")

        elif keyboard.is_pressed('esc'):
            print("\n\n")
            break
def menu():
    while True:
        running(choose_a_format(),origin(),set_alarm())
menu()
