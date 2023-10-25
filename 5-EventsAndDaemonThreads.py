import threading
import time

# EVENTS
# event = threading.Event()

# def MyEvent():
#     print('Waiting for the event to trigger...')
#     event.wait()
#     print('Performin action XYZ now...')
    
# t1 = threading.Thread(target=MyEvent)
# t1.start()
    
# x = input('Do you want to trigger the event? (y/n): ')
# if x == 'y':
#     event.set()
    
# DAEMON THREADS
# Daemon threads works in the background like constant reading of files in an endless loop which run
# every time in a program.

path = 'text.txt'
text = ""

def ReadFile():
    global path, text
    while True:
        with open('text.txt', 'r') as f:
            text = f.read()
        time.sleep(3)
def PrintLoop():
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=ReadFile, daemon=True)
t2 = threading.Thread(target=PrintLoop)

t1.start()
t2.start()
    