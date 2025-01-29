"""
Test Queue Linear
"""

from queue import LinearQueue

# Queue Instance
test_queue = LinearQueue(5)
print(test_queue)

# Enqueues
test_queue.enqueue("A")
print(test_queue)

# Dequeues
reutrn_value = test_queue.dequeue()
print(test_queue)