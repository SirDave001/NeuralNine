import threading

def Function1():
    for x in range(100):
        print('f1')
def Function2():
    for x in range(100):
        print('f2')
t1 = threading.Thread(target=Function1)
t2 = threading.Thread(target=Function2)

t1.start()
t2.start()

# TO WAIT FOR THREAD TO WAIT AND RUN SEQUENTIALLY
def F():
    for x in range(100):
        print('1')
ST = threading.Thread(target=F)
ST.start()
ST.join()

print('new')