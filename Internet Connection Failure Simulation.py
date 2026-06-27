#This program simulates what it feels like to experience poor internet connection

from time import sleep
import time

attempts = 0
secs = 0
waitingIndicator = '...'
def connect_to_internet():
    global attempts, secs
    if attempts < 3:
        attempts += 1
        print(f'Trying to connect... {attempts}')
        sleep(secs)
        secs += 1
        print(f'Connection failed. Trying again...')
        sleep(secs)
        connect_to_internet()  #Recursion
    else:
        for dot in waitingIndicator:
            print(dot, end= '', flush= True)
            time.sleep(1)
        print()
        print(f'Connection Established!')

connect_to_internet()