import socket
import threading
from queue import Queue

target = "127.0.0.1"
queue = Queue()
openPorts = []

# PREPARING THE PORTS
def portScan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False
    
def getPorts(mode):
    if mode == 1:
        for port in range(1, 1024):
            queue.put(port)
    elif mode == 2:
        for port in range(1, 49152):
            queue.put(port)
    elif port == 3:
        ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]
        for port in ports:
            queue.put(port)
    elif mode == 4:
        ports = input('Enter your ports (separate by blanks): ')
        ports = ports.split()
        ports = list(map(int, ports))
        for port in ports:
            queue.put(port)
            
# MULTITHREADING
def worker():
    while not queue.empty():
        port = queue.get()
        if portScan(port):
            print(f'Port {port} is open!')
            openPorts.append(port)
            
def runScanner(threads, mode):
    getPorts(mode)
    threadList = []
    for t in range(threads):
        thread = threading.Thread(target=worker)
        threadList.append(thread)
    for thread in threadList:
        thread.start()
    for thread in threadList:
        thread.join()
    print(f'Open ports are: {openPorts}')
    
    
runScanner(50, 1)