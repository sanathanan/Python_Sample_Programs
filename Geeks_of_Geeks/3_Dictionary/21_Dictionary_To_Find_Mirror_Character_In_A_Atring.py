"""
Finding Mirror Character in a string

Example:
Input : N = 3
        paradox
Output : paizwlc
We mirror characters from position 3 to end.
"""
# Method 1
print("-------------Method 1 ---------------")

n = 3
input = 'paradox'

prefix = input[0:n-1]
suffix = input[n-1:]
mirror = ''
# print(suffix)

#
alpha = 'abcdefghijklmnopqrstuvwxyz'
reverse_alpha = 'zyxwvutsrqponmlkjihgfedcba'

chars=dict(zip(alpha,reverse_alpha))

for i in suffix:
    if i in chars.keys():
        mirror += chars[i]

print(prefix+mirror)
