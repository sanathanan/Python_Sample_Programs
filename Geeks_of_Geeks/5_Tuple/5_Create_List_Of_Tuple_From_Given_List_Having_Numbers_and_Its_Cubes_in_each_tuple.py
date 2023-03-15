"""
Create a list of tuples from given list having number and its cube in each tuple

Example:
Input: list = [1, 2, 3]
Output: [(1, 1), (2, 8), (3, 27)]
"""
# Method 1
print("----------Method 1 ------------")
lst_1 = [1, 2, 3]

result = [(i,i**3) for i in lst_1]
print(result)