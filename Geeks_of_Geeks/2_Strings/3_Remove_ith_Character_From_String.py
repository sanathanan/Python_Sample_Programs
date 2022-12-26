"""
Removing ith character from a string
"""

# Method 1
input = "Hello"
lst=[]
for i in range(len(input)):
    if i != 2:
        lst.append(input[i])
print("----Method 1 ------")
print(''.join(lst))
print(type(''.join(lst)))

# Method 2
input_2 = 'How Are You'
str_2 = ''
for i in range(len(input_2)):
    if i != 4:
        str_2 = str_2 + input_2[i]
print("----Method 2 ------")
print(str_2)

# Method 3
input_3 = 'Hefegelooooo'
removed_input_3 = input_3.replace('e','',1) # It will remove 'e' only one time which is occuring first.
                                            # We can't able to remove 'e' at 6th position.
print("----Method 3 ------")
print(removed_input_3)