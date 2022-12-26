"""
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1
(where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example:

Input: 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 1:
num = 2  ==> set{2,4,16,37,58,89,145, 42, 20} --> 20^2 will give 4... (Then it loops). So it is not a Happy Number

Example 2:
num = 19 ==> set{19, 82, 68, 100, 1} (It is Happy Number, Because it ends at 1).

Logic:
Example: 19
1. First we need to get each digit
   a. 'mod' operator will gives us last digit of the given number
       19 mod 10 = 9
   b. Now, we need to get first digit.
        divide number/10 i.e, 19/10 --> will give value in float. To get number before decimal value use 'math.floor'
        math.floor(19/10) --> Give us 1
2. sqr.sum = 9^2
   sqr.sum += 1^2

3. For the above condition, we need to check the 'number' is repeating or not. For this, we can use 'set'.
   Because 'set' will have only unique elements.

   If the 'number' not exist in set:
        - add the number to set
        - Initialize squ.sum
        - Iterate over each digit and add to the squ.sum
        - if squ.sum == 1 --> return True. (It is a Happy Number).
   else:
        return False (It is not a Happy Number)

"""
import math

number = 19 # Given Number
number_exist = set() # Initializing 'set' which can store unique elements

# If "given number' not in 'set' go inside of 'while' loop
while number not in number_exist:
    number_exist.add(number) # If number not exist in 'set' add the number to 'set'
    
    # Initializing squ_Sum 
    squ_Sum = 0
    # Iterating through each digit. So, it will keep on repeat until the value is greater than 0
    while number > 0: # It will do the squaring operation until the number is greater than 1
        squ_Sum += ((number%10)*(number%10)) # Using 'mod' operator and taking the last digit and squaring that digit.
        number = math.floor(number/10) # Getting the first digit from the given number.
        
    if squ_Sum == 1: # Checking if squared sum of each digit is '1'
        print(True)
        break
    
    # If the squared sun of each digit is not 1, then assigning the corresponding value to a number, which will repeat the process.
    number = squ_Sum

# If the given number exist in 'set' then return false.
else:
    print("False")

