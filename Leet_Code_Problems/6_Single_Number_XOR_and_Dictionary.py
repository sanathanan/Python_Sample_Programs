"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [4,1,2,2,1]
Output: 4

Logic:
1. We can do this by dictionary.
2. Create empty dictionary.
3. Iterate over the list and check if that number exist in dictionary.
    - If the number not exist, then add that number in dictionary and assign the value = 1
    - If the number exist in dictionary, increment the value by 1
4. Now, Step 1 to 3, will create dictionary.
5. Now, iterate over list again and check, if dictionary[number] == 1
    - print(number).
"""

# Method 1 (Using Dictionary)

input = [4,1,2,2,1]

dict ={}

for i in input:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
print("The Dictionary :", dict)

for i in input:
    if dict[i] == 1:
        print("The number which appear only one time is: ",i)

