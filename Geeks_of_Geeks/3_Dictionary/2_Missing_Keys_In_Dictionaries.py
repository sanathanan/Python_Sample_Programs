"""
Handling Missing Keys in a Dictionary

Example:
# initializing Dictionary
d = { 'a' : 1 , 'b' : 2 }

# trying to output value of absent key
print ("The value associated with 'c' is : ")
print (d['c'])

Error :
Traceback (most recent call last):
  File "46a9aac96614587f5b794e451a8f4f5f.py", line 9, in
    print (d['c'])
KeyError: 'c'
"""

# Method 1
print("--------Method 1 ---------")
dict1 = {'a' : 1 , 'b' : 2 }

print(dict1.get('a','Not Found'))
print(dict1.get('c', 'Not Found'))  # get(key,def_val)--> If the key is not present, it will print teh default value

# Method 2
print("--------Method 2 ---------")
dict2 = {'a' : 1 , 'b' : 2 }
dict2.setdefault('c', 'Not Found')
print(dict2['b'])
print(dict2['c'])

# Method 3
print("--------Method 3 ---------")
import collections

dict3 = collections.defaultdict(lambda : 'Key Not Found')
dict3['aa'] = 11
dict3['bb'] = 22
print(dict3['aa'])
print(dict3['cc'])