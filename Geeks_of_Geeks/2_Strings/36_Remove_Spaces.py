"""
Removing Spaces

Given a string, remove spaces from it.

Example:
Input:
S = "geeks  for geeks"
Output: geeksforgeeks
Explanation: All the spaces have been removed.
"""
def modify(s):

    str_ = s.replace(' ','')
    return str_


# Driver code
s = 'geeks  for geeks'
result = modify(s)
print(result)