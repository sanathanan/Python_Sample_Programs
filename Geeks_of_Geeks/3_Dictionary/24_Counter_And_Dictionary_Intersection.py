"""
Given two strings, find if we can make first string from second by deleting some characters
from second and rearranging remaining characters.

Example:
Input : s1 = ABHISHEKsinGH
      : s2 = gfhfBHkooIHnfndSHEKsiAnG
Output : Possible
"""

# Method 1
from collections import Counter
print("-----------Method 1 -------")
# s1 = "ABHISHEKsinGH"
# s2 = "gfhfBHkooIHnfndSHEKsiAnG"

# s1 = "Hello"
# s2 = "dnaKfhelddf"

s1 = "GeeksforGeeks"
s2 = "rteksfoGrdsskGeggehes"


s1_count = dict(Counter(s1))
s2_count = dict(Counter(s2))
print("S1 Dictionary: ",s1_count)
print("S2 Dictionary: ",s2_count)

res = {}
for i in s2_count.keys():
    if i in s1:
        if i not in res:
            if s2_count[i] >= s1_count[i]:
                res[i] = s1_count[i]

print("Result :",res)

if s1_count == res:
    print("Possible")
else:
    print("Not Possible")

# Method 2
from collections import Counter
print("-----------Method 2 -------")
s11 = "ABHISHEKsinGH"
s22 = "gfhfBHkooIHnfndSHEKsiAnG"

s11_Count = Counter(s11)
s22_Count = Counter(s22)

print("S11 Count: ", s11_Count)
print("S22 Count: ", s22_Count)

# Taking intersection of 2 dictionaries
result_2 = s11_Count & s22_Count

if s11_Count == result_2:
    print("possible")
else:
    print("Not Possible")