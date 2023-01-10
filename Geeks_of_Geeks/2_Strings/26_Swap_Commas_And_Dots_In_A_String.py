"""
Swap Commas and Dots in a String

Input : 14, 625, 498.002
Output : 14.625.498, 002
"""

# Method 1
input_1 = '14, 625, 498.002'

input_1 = input_1.replace('.', '...')
input_1 = input_1.replace(', ', '.')
input_1 = input_1.replace('...', ', ')
print(input_1)
