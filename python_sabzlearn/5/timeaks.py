import time
import os
while True:
    
    select = input('start or not (y/n): ').lower()
    
    if 'y' in select:
        hour = int(input('hour: '))
        minute = int(input('minute: '))
        second = int(input('second: '))
        total = (hour * pow(60, 2)) + (minute * 60) + second
        
        time.sleep(1)
        while total > 0:
            print(total)
            total -= 1
            time.sleep(1)
            os.system('clear')
    else:
        break
    
    