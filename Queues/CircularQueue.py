'''
Circular Queue
'''

class Queue():

    def __init__(self, capacity):
        self.front = -1
        self.rear = -1
        self.max = capacity
        self.data = [None] * capacity

    def __repr__(self):
        return f"Front: {self.front}    Rear: {self.rear}   Data: {self.data}"

    def Front(self):
        if self.front == -1:
            print(f"Front: {self.front}    Rear: {self.rear}   Data: {self.data}"+" Uninitialized Queue")
        else:
            print(f"Front: {self.front}    Rear: {self.rear}   Data: {self.data}")

    def Rear(self):
        if self.rear == -1:
            print(f"Front: {self.front}    Rear: {self.rear}   Data: {self.data}"+" Uninitialized Queue")
        else:
            print(f"Front: {self.front}    Rear: {self.rear}   Data: {self.data}")

    def Enqueue(self, value) -> None:
        
        # Initialization
        if self.front == -1 and self.rear == -1:
            self.front += 1
            self.rear += 1
            self.data[self.rear] = value
            return None
        
        # Overflow
        if (self.rear - self.front) % self.max == self.max - 1:
            print("Overflow")
            return None
        
        # Circle situation
        if self.rear == self.max - 1:
            self.rear = 0
            self.data[self.rear] = value
            return None

        # Enqueue
        self.rear += 1
        self.data[self.rear] = value

    def Dequeue(self):

        # Uninitialized Queue
        if self.front == -1 and self.rear == -1:
            print(f"Front: {self.front}    Rear: {self.rear}   Data: {self.data}"+" Uninitialized Queue")
            return None
        
        if self.front == self.rear:
            value = self.data[self.front]
            self.data[self.front] = None
            self.front = -1
            self.rear = -1
            print(f"Front: {self.front}    Rear: {self.rear}   Data: {self.data}"+f" Dequeue: {value}")
            return value
        
        # Circle situation
        if self.front == self.max - 1:
            value = self.data[self.front]
            self.data[self.front] = None
            self.front = 0
            print(f"Front: {self.front}    Rear: {self.rear}   Data: {self.data}"+f" Dequeue: {value}")
            return value
    
        # Dequeue  
        value = self.data[self.front]
        self.data[self.front] = None
        self.front += 1
        print(f"Front: {self.front}    Rear: {self.rear}   Data: {self.data}"+f" Dequeue: {value}")
        return value
