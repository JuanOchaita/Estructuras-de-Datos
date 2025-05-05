'''
Circular Queue testing.
'''

from CircularQueue import Queue

# Queue instance
print("\nStart Queue")
queue = Queue(3)
print(queue)

# Enqueues
print("\nEnqueue test")
queue.Enqueue('A')
print(queue)
queue.Enqueue('B')
print(queue)
queue.Enqueue('C')
print(queue)

# Dequeue
print("\nDequeue test")
queue.Dequeue()
queue.Dequeue()
queue.Dequeue()


# Dequeue
print("\nOverflow Test")
queue.Enqueue('A')
print(queue)
queue.Enqueue('B')
print(queue)
queue.Enqueue('C')
print(queue)

queue.Dequeue()
queue.Dequeue()

queue.Enqueue('D')
print(queue)
queue.Enqueue('E')
print(queue)
queue.Enqueue('F')
print(queue)