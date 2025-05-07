"""
Test of reverse method for Linkedlist
"""

from linked_list import Node, LinkedList

node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("B")

ll = LinkedList()
print(ll)

ll.insert_at_end(node_a)
ll.insert_at_end(node_b)
ll.insert_at_end(node_c)
ll.insert_at_end(node_d)
print(ll)

# Test Reverse Method
ll.reverse()
print(ll)