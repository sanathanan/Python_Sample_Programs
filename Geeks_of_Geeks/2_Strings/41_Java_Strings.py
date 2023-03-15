"""
Java Strings - Set 1
Given two strings S1 and S2 as input. Your task is to concatenate two strings and then reverse the string.
Finally print the reversed string.

Example:
Input: S1 = "Geeks" , S2 = "forGeeks"
Output: "skeeGrofskeeG"
Explanation: Concatenating S1 and S2 to get "GeeksforGeeks" then reversing it to "skeeGrofskeeG".
"""
def conRevstr(s1,s2):

    res_ = s1 + s2

    result = res_[::-1]

    return result



# Driver Code
s1 ='Geeks'
s2 = 'forGeeks'
result = conRevstr(s1,s2)
print(result)