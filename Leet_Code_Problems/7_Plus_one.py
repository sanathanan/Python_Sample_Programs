"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Logic:
1. Need to add +1 to last digit.
2. After adding +1 -> last digit value is less than 10, then return all the element in the list
    - After adding +1 -> last digit value is equal 10, the add 0 to the last digit and
      add 1 to the previous digit.

"""

digits =[1,9,9]

for i in reversed(range(len(digits))):
    digits[i] += 1
    if digits[i] < 10:
        break
    else: # 89
        digits[i] = 0

    if digits[0] == 0: # 99--> This case it will be [0,0] -> we need to add 1 before the first digit 0 according to our logic.
        digits.insert(0,1)
print(digits)


