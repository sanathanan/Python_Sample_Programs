"""
Reverse String

Input:['h','e','l','l','o']

Output:['o','l','l','e','h']

Logic:
1. Solving this by 'Two Pointer' approach.
2. Creating two pointers. one for 'left side of list' and other for  'right side of list'.
3. If pointer 'left side of list' is lesser than 'right side of list'
    - Do swapping
    - Incrementing both the pointers.

"""

lst1 = ['h', 'e', 'l', 'l', 'o']
lst= ['f', 'l', 'm', 'n', 'o', 'p']
print("Before reversing a String in the list: ", lst)

first_ptr_index = 0 # Left side pointer
last_ptr_index = len(lst)-1 # Right side pointer

while first_ptr_index < last_ptr_index: # Checking if left side pointer is lesser than right side pointer
    # Swapping Logic
    temp = lst[first_ptr_index]
    lst[first_ptr_index] = lst[last_ptr_index]
    lst[last_ptr_index] = temp

    first_ptr_index += 1 # Incrementing left side pointer of list
    last_ptr_index -= 1 # Incrementing right side pointer of list
print("After reversing the string in the list: ",lst)