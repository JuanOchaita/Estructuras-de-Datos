'''
Linear Search O(n)
'''

# O(n): 1 + 1 + 1 + n + n + 1 + 1

array = [6] * 100               # O(1)
value = 9                       # O(1)
value_in_array = False          # O(1)

for i in range(len(array)):     # O(n)
    if array[i] == value:       # O(n)
        value_in_array = True   # O(1)

print(value_in_array)           # O(1)