import time
import keyboard

#Function1 to choose a format 
def choose_a_format():
    while True:
        try:
            format = int(input("choose a format 24h or 12h : "))
            if format == 24:
                return format
            elif format == 12:
                return format
        except ValueError:
            print("Enter valid numeric values.")

 #FUNCTION SET A TIME
def set_a_time():
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
            timeis = (hours, minutes, seconds)
            return timeis
        else:
            print("Hours must be between 0-23 and minutes between 0-59.")

#Function Origin set/local
def origin():
     while True:
        try:
            choice = input("Enter 1 to set time or 2 for local time: ")
            if choice == "2":
                hours = int(time.strftime('%H'))
                minutes = int(time.strftime('%M'))
                seconds = int(time.strftime('%S'))
                return hours, minutes, seconds
            elif choice == "1":
                return set_a_time()
            else:
                print("Please enter 1 or 2.")
        except ValueError:
            print("Enter valid numeric values.")

#Function set alarme
def set_alarm():
    while True:
        h = input("Enter an hour (0-23): ")
        m = input("Enter minutes (0-59): ")
        try:
            h = int(h)
            m = int(m)
        except ValueError:
            print("Enter valid numeric values.")
            continue
        if 0 <= h < 24 and 0 <= m < 60:
            s = 0
            timeis = (h, m, s)
            return timeis
origin()