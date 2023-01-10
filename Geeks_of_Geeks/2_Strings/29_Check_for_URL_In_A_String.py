"""
Check for URL in a string

Input : string = 'I am a blogger at https://geeksforgeeks.org'
Output : URL :  ['https://geeksforgeeks.org']
"""

# Method 1
import re

print("---------Method 1-----------")
str_1 = 'I am a blogger at https://geeksforgeeks.org'

lst=[]
for i in str_1.split():
    if i.startswith('https:') or i.startswith('http:'):
        lst.append(i)
print(i)

# Method 2
print("---------Method 2-----------")
str_2 = 'I am a blogger at https://geeksforgeeks.org'

regex = re.compile(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))")

result = re.findall(regex, str_2)
print(result[0][0])