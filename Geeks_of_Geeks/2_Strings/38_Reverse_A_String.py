"""
Reverse a String

Example:
Input: S = "GeeksforGeeks"
Output: "skeeGrofskeeG"
Explanation: Element at first is at last and last is at first, second is at second last and
second last is at second position and so on .
"""

def reverse_Str(S):
    res_ = S[::-1]

    return res_


# Driver Code
S = 'GeeksforGeeks'
result = reverse_Str(S)
print(result)