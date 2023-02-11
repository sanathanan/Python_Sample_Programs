"""
Substituting Patterns in Text
"""
# Method 1
import re
print("-------Method 1 ------")

str1 = 'It is raining outside.'
sub_str1 = 'sunny'
result_1 = re.sub('raining', sub_str1, str1)
print(result_1)

# Method 2
import re
print("-------Method 2 ------")
str_2 = '22 April is celebrated as Earth Day.'
sub_str2 = '0'
result_2 = re.sub('[a-z]',sub_str2, str_2)
print(result_2)

