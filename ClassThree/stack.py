'''
Stack Implementation
'''

class Stack:
    def __init__(self, size: int):
        self.Top = -1
        self.Max = size
        self.Elements = [None] * size

    def __repr__(self):
        return f"Current stack: {self.Elements} | Top: {self.Top}"

    def Push(self, value: int) -> None:
        if self.Top == self.Max -1:
            print("OVERFLOW :/")
        else:
            self.Top += 1
            self.Elements[self.Top] = value
