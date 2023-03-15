"""
Converting String to Lower Case

Example:
Input: S = "ABCddE"
Output: "abcdde"
Explanation: A, B, C and E are converted to a, b, c and E thus all uppercase characters
of the string converted to lowercase letter.
"""

def to_Lower(S):

    res = S.lower()

    return res


# Driver Codes
S = 'LMNOppQQ'
result = to_Lower(S)
print(result)