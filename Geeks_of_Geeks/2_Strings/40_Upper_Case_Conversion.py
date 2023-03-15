"""
Upper Case Conversion

Given a string str, convert the first letter of each word in the string to uppercase.

Example:
Input:
str = "i love programming"
Output: "I Love Programming"
Explanation: 'I', 'L', 'P' are the first letters of  the three words.
"""

def transform(s):

    chars= ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    lst = []
    for i in s.split():
        if i[0] in chars:
            repl = i[0].upper() + i[1:]
            lst.append(repl)

    res = ' '.join(map(str,lst))

    return res



# Driver Code
s = 'i love programming'
result = transform(s)
print(result)