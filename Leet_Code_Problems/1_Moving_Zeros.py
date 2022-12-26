"""
Moving Zeros

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Logic:
1. Iterate over the list using 'for loop'.
2. Check if lst[i] != 0
    - Do swapping based on the previous_index value of zero '0'
    - Increment the previous_index
"""

lst = [0,1,0,3,12]
print("Before Moving Zeros: ", lst)
zero_index_value = 0

for i in range(len(lst)):
    if lst[i] != 0:
        # Swapping Logic
        temp = lst[zero_index_value] # Storing the zero_index_value of the lst i.e '0'
        lst[zero_index_value] = lst[i] # swapping the zero_index_value of the lst i.e '0' with the swapping number present in the lst
        lst[i] = temp # swapping the number present in the lst with the temp variable i.e '0'
        zero_index_value += 1 # After swapping incrementing the zero_index_value.
print("After Moving zeros: ",lst)