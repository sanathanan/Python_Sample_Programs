"""
Python program to count number of vowels using sets in given string

Example:
Input : GeeksforGeeks
Output : No. of vowels : 5

Input : Hello World
Output : No. of vowels :  3
"""

# Method 1

str = 'Hello World'
vowels = set('aeiouAEIOU')

count = 0
for i in str:
    if i in vowels:
        count += 1
print("The number of vowels present in string: ", count)
