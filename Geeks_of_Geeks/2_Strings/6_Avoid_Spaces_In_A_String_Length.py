"""
Given a String, compute all the characters, except spaces.

Input : test_str = ‘geeksforgeeks 33 best'
Output : 19
Explanation : Total characters are 19
"""

# Method 1
print("-------Method 1-------------------")
input_1 = 'geeksforgeeks 33 best'
print("Total Length with Space: ", len(input_1))
count = 0
for i in input_1:
    if i == ' ': # This method will work only, if it has one space
        continue
    else:
        count += 1
print("Total Length with out space: ",count)

# Method 2
print("-------Method 2-------------------")
input_2 = 'geeksforgeeks    33 best'
print("Total Length with Space: ", len(input_2))

str_2 = input_2.replace(' ','')
result_2 = len(str_2)
print("Total Length with out space: ",result_2)

# Method 3
print("-------Method 3-------------------")
input_3 = 'geeksforgeeks    33 best'
print("Total Length with Space: ", len(input_3))
count_3 = 0
for i in input_3:
    if i.isspace():
        continue
    else:
        count_3 += 1
print("Total Length with out space: ",count_3)