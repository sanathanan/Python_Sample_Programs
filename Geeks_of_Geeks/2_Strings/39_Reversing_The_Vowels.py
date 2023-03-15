"""
Reversing the Vowels

Example:
S = "geeksforgeeks"
Output: geeksforgeeks
Explanation: The vowels are: e, e, o, e, e
Reverse of these is also e, e, o, e, e.
"""
def modify(S):

    vowels = ('a','e','i','o','u')

    lst = ''
    for i in S:
        if i in vowels:
           lst += i
    reversed_lst = lst[::-1]
    # print(reversed_lst)
    reversed_lst_1 = list(reversed_lst)
    # print(reversed_lst_1)

    new_lst=[]
    count = 0
    for i in S:
        if i not in vowels:
            new_lst.append(i)
        else:
            new_lst.append(reversed_lst_1[count])
            count += 1

    # print(new_lst)

    res = ''.join(map(str,new_lst))

    return res


# Driver Code
S = 'geeksforgeeks'
result = modify(S)
print(result)