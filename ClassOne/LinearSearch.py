'''
Linear Search O(n)
'''

def linear_search(array, value):

    for i in range(len(array)):
        if array[i] == value:
            return True
        
    return False

n = 100
test_array = [7] * n
test_value = 8

print(linear_search(test_array, test_value))
