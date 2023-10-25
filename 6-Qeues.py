import queue

numbers = [1,2,3,4,5,6,7,8,9]
# FIRST IN FIRST OUT QUEUE
q = queue.Queue()
for number in  numbers:
    q.put(number)


# LAST IN FIRST OUT QUEUE
q = queue.LifoQueue() 
for number in  numbers:
    q.put(number)
    
print(q.get())


# PRIORITY QUEUE

q = queue.PriorityQueue()
q.put((2, 'I am Groot'))
q.put((11, 99))
q.put((5, 7.5))
q.put((5, True))
q.put((1, False))

while not q.empty():
    print(q.get())
