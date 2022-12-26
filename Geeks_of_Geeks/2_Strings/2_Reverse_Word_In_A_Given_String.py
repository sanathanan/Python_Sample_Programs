"""
Reverse word in a given string
"""

# Method 1
input = 'Hello How Are You'

lst_input = input.split()
reverse_lst = lst_input[::-1]
new_reverse_lst = ' '.join(reverse_lst)

print("---------Method 1 -----------")
print(new_reverse_lst)
print(type(new_reverse_lst))

# Method 2
input2 = 'Hello How Are You'

lst_input2 = input2.split()
reverse_lst2 = lst_input2[::-1]

lst=[]
for i in reverse_lst2:
    lst.append(i)
print("---------Method 2 -----------")
print(' '.join(lst))
print(type(' '.join(lst)))

# Method 3
input3 = 'Hello How Are You'

lst_input3= input3.split()
reversed_string = ' '.join(reversed(lst_input3))
print("---------Method 3 -----------")
print(reversed_string)
print(type(reversed_string))

