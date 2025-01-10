def running(format, origin, alarm):
    hours, minutes, seconds = origin
    alarm_h, alarm_min, alarm_sec = alarm
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

    while True:
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

        elif hours == alarm_h and minutes == alarm_min and seconds == alarm_sec:
            print("\n DING DING !!!\n")

        elif keyboard.is_pressed('esc'):
            print("\n\n")
            break