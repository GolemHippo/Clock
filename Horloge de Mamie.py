# Importing the library
import time



# Function that displays local time
def localtime():
    print()
    while True:
        global hours, minutes, seconds
        hours = time.strftime('%H')
        minutes = time.strftime('%M')
        seconds = time.strftime('%S')
        print(hours,':',minutes,':',seconds)
        time.sleep(1)
# Version 12h
def localtime2():
    print()
    while True:
        global hours, minutes, seconds
        hours = time.strftime('%r')
        print(hours)
        time.sleep(1)



# Function that set an alarm
def alarm():
    print()
    print("Set an alarm...")
    hours_alarm = input("Enter the hour : ")
    minutes_alarm = input("Enter the minute : ")
    seconds_alarm = input("Enter the second : ")
    print(f"Alarm set at {hours_alarm}:{minutes_alarm}:{seconds_alarm}")
    print()
    while True:
        hours = time.strftime('%H')
        minutes = time.strftime('%M')
        seconds = time.strftime('%S')
        print(hours,':',minutes,':',seconds)
        time.sleep(1)
        if hours_alarm == hours and minutes_alarm == minutes and seconds_alarm == seconds:
            print("ALARM !!!")
# Version 12h
def alarm2():
    print()
    print("Set an alarm...")
    hours_alarm = input("Enter the hour : ")
    minutes_alarm = input("Enter the minute : ")
    seconds_alarm = input("Enter the second : ")
    print(f"Alarm set at {hours_alarm}:{minutes_alarm}:{seconds_alarm}")
    print()
    while True:
        hours = time.strftime('%I')
        minutes = time.strftime('%M')
        seconds = time.strftime('%S')
        print(hours,':',minutes,':',seconds)
        time.sleep(1)
        if hours_alarm == hours and minutes_alarm == minutes and seconds_alarm == seconds:
            print("ALARM !!!")



# Function Infinite loop asking the user what to do
def main():
    while True:
        menu = int(input("What do you want to do ? : Insert '1' to show local time | Insert '2' to edit time | Insert '3' to set an alarm | : "))

        if menu == 1:  # Show local time
            localtime()

        if menu == 3:  # Set an alarm
            alarm()
# Version 12h
def main_12h():
    while True:
        menu2 = int(input("What do you want to do ? : Insert '1' to show local time | Insert '2' to edit time | Insert '3' to set an alarm | : "))

        if menu2 == 1:  # Show local time
            localtime2()

        if menu2 == 3:  # Set an alarm
            alarm2()





format = input("Do you want to use 24h (A) or 12h (B) format? : ")

if format == 'A':
    print("You use the 24h format")
    main()

if format == 'B':
    print("You use the 12h format")
    main_12h()