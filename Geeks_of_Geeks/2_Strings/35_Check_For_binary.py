"""
Given a non-empty sequence of characters str, return true if sequence is Binary, else return false

Example:
Input:
str = 101
Output:
1
Explanation:
Since string contains only 0 and 1, output is 1.
"""
def isBinary(str_):

    lst = []
    for i in str_:
        if i == '0' or i == '1':
            pass
        else:
            lst.append(i)

    if len(lst) > 0:
        return 0
    else:
        return 1

# Driver Code

str_ = '384'
result = isBinary(str_)
print(result)