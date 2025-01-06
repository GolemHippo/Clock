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


# Infinite loop asking the user what to do
while True:
    menu = int(input("What do you want to do ? : Insert '1' to show local time | Insert '2' to edit time | Insert '3' to set an alarm | : "))

    if menu == 1:  # Show local time
        localtime()

    if menu == 3:  # Set an alarm
        alarm()