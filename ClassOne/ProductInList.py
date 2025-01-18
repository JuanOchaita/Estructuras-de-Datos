'''
Product in List O(n^2)
'''

''' O(n^2): 1 + 1 + 1 + (n * 2n + 1) + 1'''

array = [1] * 100                           # O(1)
product = 2                                 # O(1)
product_in_array = False                    # O(1)

for i in range(len(array)):                 # O(n)
    for j in range(len(array)):             #   O(n)
        if array[i] * array[j] == product:  #   O(n)
            product_in_array = True         #   O(1)

print(product_in_array)                     # O(1)