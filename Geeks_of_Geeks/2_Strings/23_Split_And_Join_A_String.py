"""
Program to Split and Join a String

Split the string into list of strings:
Input : Geeks for Geeks
Output : ['Geeks', 'for', 'Geeks']

Join the list of strings into a string based on delimiter ('-')
Input :  ['Geeks', 'for', 'Geeks']
Output : Geeks-for-Geeks
"""
# Method 1:
print("--------Method 1 ----------")

str_1 = 'Geeks for Geeks'
print("Input String:", str_1)

lst_str_1 = str_1.split()
print("Splitting String to List: ", lst_str_1)

del_str_1 = "-".join(lst_str_1)
print("Delimeter string:", del_str_1)

# Method 2
print("--------Method 2 ----------")

str_2 = 'Geeks for Geeks'
print("Input String:", str_1)

print("Splitting String to List: ", str_2.split())

print("Delimeter string:", '-'.join(str_2.split()))