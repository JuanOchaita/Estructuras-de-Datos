"""
Stack Testing
"""

from stack import Stack

test_stack = Stack(5)
print(test_stack)

#Pushes
test_stack.Push("A")
print(test_stack)
test_stack.Push("B")
print(test_stack)
test_stack.Push("C")
print(test_stack)
test_stack.Push("D")
print(test_stack)
test_stack.Push("E")
print(test_stack)
test_stack.Push("F")
print(test_stack)
print()

# Pops
test_stack.Pop()
print(test_stack)
test_stack.Pop()
print(test_stack)
test_stack.Pop()
print(test_stack)
print("Peeked", test_stack.Peek())