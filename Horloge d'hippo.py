import time #Import Time module

hours, minutes, seconds = 0, 0, 0 #INITIALISATION VARIABLES

def set_hour(hour):
    global hours, minutes, seconds
    hours, minutes, seconds = hour #INITIALISATION TUPLE hour

def hour_working(): #Clock system that refresh hours, minutes and seconds
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

def display_settime(): #Clock display with new set time
    set_hour((3, 30, 45))
    while True:
        hour_working()
        time.sleep(1)
        hour_format = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
        print(hour_format)

def set_alarm(): #Alarm Input to create Time Tuple as a parameter
    try:
        alarm_hours = int(input('h'))
        alarm_minutes = int(input('m'))
        alarm_seconds = int(input('s'))
        global time_tuple
        time_tuple=alarm_hours,alarm_minutes,alarm_seconds
        check_alarm(time_tuple)
    except ValueError:
        print('f u')
    
def check_alarm(time_tuple): #Alarm and Clock display, checking if the time is equal to that of the alarm setting
    if hours == time_tuple[0] and minutes == time_tuple[1] and seconds == time_tuple[2]:
        print('alarm')
    else:
        print('f u')