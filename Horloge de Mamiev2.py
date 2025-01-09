import time

def time_getlocaltime():
    hours = int(time.strftime('%H'))
    minutes = int(time.strftime('%M'))
    seconds = int(time.strftime('%S'))
    timeis= hours, minutes, seconds
    return timeis

def time_running(timeis):
    hours=timeis[0]
    minutes=timeis[1]
    seconds=timeis[2]
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
    if hours == 24:
        hours = 0
    timeis = hours, minutes, seconds
    return timeis

def time_localtime():
        time_getlocaltime()
        time_running(time_getlocaltime())
        time_display()


def time_display(timeis):
    while True:
        print(f"\r{timeis[0]:02}:{timeis[1]:02}:{timeis[2]:02}", end="")
        time_running()
        time.sleep(1)

def alarm_ask():
    while True:
        try:
            hours = int(input('At what hour do you want the alarm?'))
            minutes = int(input('What minutes?'))
            seconds = int(input('What seconds?'))
            if 0<=hours<24 and 0<=minutes<60 and 0<=seconds<60:
                return hours, minutes, seconds
            else:
                print('Error, \nPlease try again with valid numbers')
        except ValueError:
            print('Error, \nPlease try again with valid numbers')

def time_set():
    hours = int(input('What is the new time ?\nPlease enter the hours:'))
    minutes = int(input('Please enter the minutes:'))
    seconds = 0
    timeis = hours, minutes, seconds
    return timeis

time_localtime()