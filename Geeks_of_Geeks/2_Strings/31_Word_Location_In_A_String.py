"""
Word Location In A String

Example:
The original string is : geeksforgeeks is best for geeks
wrd = 'best'
The location of word is : 3
"""
# Method 1
print("-------Method 1 -----")
str_1 = 'geeksforgeeks is best for geeks'
match_1 = 'best'

for i in enumerate(str_1.split()):
    if i[1] == match_1:
        print(i[0]+1)

# Method 2
print("-------Method 2 -----")
str_2 = 'geeksforgeeks is best for geeks'
match_2 = 'best'

count = 0
for i in str_2.split():
    count += 1
    if i == match_2:
        print(count)


