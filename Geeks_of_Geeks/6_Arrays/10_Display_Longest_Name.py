"""
Display Longest Name

Given a list of names, display the longest name.

Example:
N = 5
names[] = { "Geek", "Geeks", "Geeksfor", "GeeksforGeek", "GeeksforGeeks" }

Output:
GeeksforGeeks
"""

def longest(arr,n):

    dict={}
    for i in arr:
        dict[len(i)] = i

    max_ =  max(dict.keys())
    result = dict[max_]

    return result


# Driver Code
n = 5
arr = ["Geek", "Geeks", "Geeksfor", "GeeksforGeek", "GeeksforGeeks" ]

result = longest(arr,n)
print(result)