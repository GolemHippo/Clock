#Importing the library
import time


#Function Infinite loop asking the user what to do
def main():
    while True:
        menu = int(input("What do you want to do ? : Insert '1' to show local time | Insert '2' to edit time | Insert '3' to set an alarm | : "))
        try:
            if menu == 1:  # Show local time
                localtime()

            if menu == 2:  #Set time
                displayclock()
                
            if menu == 3:  # Set an alarm
                alarm()
        except ValueError:
            print('Please enter a valid choice 1/2/3')
            

# Function that displays local time
def localtime():
    print()
    while True:
        global hours, minutes, seconds
        timeis = time.strftime('%T')
        print(timeis)
        time.sleep(1)
#Function that act as a clock        
def clockrunning():
    global hours, minutes, seconds
    seconds += 1
    if seconds >= 60:
        seconds = 0
        minutes += 1

    if minutes >= 60:
        minutes = 0
        hours += 1

    if hours >= 24:
        hours = 0
#Function that displays set time
def displayclock():
    global hours, minutes, seconds
    hours = int(input('To edit time you will need to enter hours, minutes and seconds\nHours : '))
    minutes = int(input('Minutes : '))
    seconds = int(input('Seconds : '))
    print()
    while True:
        clockrunning()
        time.sleep(1)
        timeis = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
        print(timeis)              
# Function that set an alarm
def alarm():
    print()
    hours_alarm = input("Set an alarm...(with this model 00, 01, 02)\nEnter the hour : ")
    minutes_alarm = input("Enter the minute : ")
    seconds_alarm = input("Enter the second : ")
    print(f"Alarm set at {str(hours_alarm).zfill(2)} : {str(minutes_alarm).zfill(2)} : {str(seconds_alarm).zfill(2)}")
    print()
    while True:
        hours = time.strftime('%H')
        minutes = time.strftime('%M')
        seconds = time.strftime('%S')
        print(hours,':',minutes,':',seconds)
        time.sleep(1)
        if hours_alarm == hours and minutes_alarm == minutes and seconds_alarm == seconds:
            print("ALARM !!!")

            



#Second Menu V12h
def main_12h():
    
    while True:
        
        menu2 = int(input("What do you want to do ? : Insert '1' to show local time | Insert '2' to edit time | Insert '3' to set an alarm | : "))

        if menu2 == 1:  # Show local time
            localtime2()
            
        if menu2 == 2:  #Set time
            displayclock2()
            
        if menu2 == 3:  # Set an alarm
            alarm2()

        else:
            print('Please enter a valid choice')
            
            
            
#Local Time V12h
def localtime2():
    print()
    while True:
        global hours, minutes, seconds
        timeis = time.strftime('%r')
        print(timeis)
        time.sleep(1)
#Function Clock V12H
def clockrunning2():
    global hours, minutes, seconds, afternoon
    seconds += 1
    if seconds >= 60:
        seconds = 0
        minutes += 1

    if minutes >= 60:
        minutes = 0
        hours += 1

    if hours > 12:
        afternoon = 1
    
    if hours < 12:
        afternoon = 0

    if hours >= 24:
        hours = 0
#Function Display V12H
def displayclock2():
    global hours, minutes, seconds, afternoon
    hours = int(input('To edit the time,\nPlease enter the Hours (0-24h) : '))
    minutes = int(input('Please enter the minutes : '))
    seconds = int(input('Please enter the seconds : '))
    while True:
        clockrunning2()
        time.sleep(1)
        if afternoon == 1:
            timestamp = 'PM'
            hours -= 12
        else:
            timestamp = 'AM'
        print(str(hours).zfill(2),':',str(minutes).zfill(2),':',str(seconds).zfill(2),timestamp)
#Alarm V12h
def alarm2():
    print()
    afternoon = input('Enter the Meridiem AM/PM : ')
    hours_alarm = input("Set an alarm in the 12h Format...(with this model 00, 01, 02)\nEnter the hour : ")
    minutes_alarm = input("Enter the minute : ")
    seconds_alarm = input("Enter the second : ")
    print(f"Alarm set at {str(hours_alarm).zfill(2)} : {str(minutes_alarm).zfill(2)} : {str(seconds_alarm).zfill(2)} {afternoon}")
    print()
    while True:
        hours = time.strftime('%I')
        minutes = time.strftime('%M')
        seconds = time.strftime('%S')
        hours_afternoon = 0
        if afternoon == 'PM':
            hours_afternoon = hours
            hours_afternoon += 12
            print(hours_afternoon,':',minutes,':',seconds,afternoon)
        if afternoon == 'AM':
            print(hours,':',minutes,':',seconds,afternoon)
        time.sleep(1)
        if hours_alarm == hours and minutes_alarm == minutes and seconds_alarm == seconds:
            print("ALARM !!!")
        if hours_alarm == hours_afternoon and minutes_alarm == minutes and seconds_alarm == seconds:
            print("ALARM !!!")




#Menu
while True:
    
    format = input("Do you want to use 24h (A) or 12h (B) format? : ")

    try:
        if format == 'A':
            print("You use the 24h format")
            main()

        elif format == 'B':
            print("You use the 12h format")
            main_12h()

    except ValueError:
        print('Please enter a valid choice')
