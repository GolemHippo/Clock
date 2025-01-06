import time

while True:
    hours = time.strftime('%H')
    minutes = time.strftime('%M')
    seconds = time.strftime('%S')
    print(hours,':',minutes,':',seconds)
    time.sleep(1)
    
