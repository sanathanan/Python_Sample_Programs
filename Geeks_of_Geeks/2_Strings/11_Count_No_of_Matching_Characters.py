"""
Counting the number of matching characters in a pair of string

Example 1:
Input : str1 = 'abcdef'
        str2 = 'defghia'
Output : 4
(i.e. matching characters :- a, d, e, f)

Example 2:
Input : str1 = 'aabcddekll12@'
        str2 = 'bb22ll@55k'
Output : 5
(i.e. matching characters :- b, 1, 2, @, k)
"""

# Method 1
print("------------Method 1 ----------------")
str1 = 'aabcddekll12@'
str2 = 'bb22ll@55k'

lst = []
for i in str1:
    for j in str2:
        if i == j:
            lst.append(i)
print("The Matched Strings: ", set(lst))
print("The number of matched strings: ", len(set(lst)))

# Method 2
print("------------Method 2 ----------------")
str1 = 'aabcddekll12@'
str2 = 'bb22ll@55k'

set_str1 = set(str1)
set_str2 = set(str2)

count = 0
lst_2 = []
for i in set_str1:
    for j in set_str2:
        if i == j:
            lst_2.append(i)
            count += 1
print("The Matched Strings: ", set(lst_2))
print("The number of matched strings: ", count)


# Method 3
print("------------Method 3 ----------------")
str1 = 'aabcddekll12@'
str2 = 'bb22ll@55k'

set_str3 = set(str1)
set_str4 = set(str2)

matched_string = set_str3 & set_str4
print("The Matched Strings: ", matched_string)
print("The number of matched strings: ", len(matched_string))