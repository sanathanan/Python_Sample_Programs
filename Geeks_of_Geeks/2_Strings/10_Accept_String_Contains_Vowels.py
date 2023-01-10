"""
Given a string, the task is to check if every vowel is present or not.
We consider a vowel to be present if it is present in upper case or lower case.
i.e. ‘a’, ‘e’, ‘i’.’o’, ‘u’ or ‘A’, ‘E’, ‘I’, ‘O’, ‘U’ .
Examples :

Input : geeksforgeeks
Output : Not Accepted
All vowels except 'a','i','u' are not present

Input : ABeeIghiObhkUul
Output : Accepted
All vowels are present
"""

# Method 1:
print("-------------Method 1 ---------------")
str_1 = 'ABeeIghiObhkUul'
str_lower_1 = str_1.lower()
vowels_1 = ['a','e','i','o','u']

lst= set()
for i in str_lower_1:
    if i in vowels_1:
        lst.add(i)
    else:
         pass

if len(vowels_1) == len(lst):
    print('Accepted')
else:
    print("Not Accepted")

# Method 2
print("-------------Method 2 ---------------")
str_2 = 'ABeeIghiObhkUul'
str_lower_2 = str_2.lower()

vowel_2 = [str_lower_2.count('a'), str_lower_2.count('e'), str_lower_2.count('i'),
         str_lower_2.count('o'), str_lower_2.count('u'),]
print(vowel_2)

if vowel_2.count(0):
    print("Not Accepted")
else:
    print("Accepted")

# Method 3
print("-------------Method 3 ---------------")
str_3 = 'geeksforgeeks'
vowel_Set = set(str_3.lower()).intersection('a,e,i,o,u')
print(vowel_Set)
if len(vowel_Set) == 5:
    print("Accepted")
else:
    print('Not Accepted')