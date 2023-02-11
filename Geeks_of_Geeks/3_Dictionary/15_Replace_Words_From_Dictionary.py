"""
Given String, replace it’s words from lookup dictionary.

Example:
Input : test_str = ‘geekforgeeks best for geeks’,

repl_dict = {“geeks” : “all CS aspirants”}

Output : geekforgeeks best for all CS aspirants

"""

print("-------------Method 1 --------------")
str_1 = "geekforgeeks best for geeks"
repl_dict = {"geeks" : "all CS aspirants"}

lst = []
for i in str_1.split():
    lst.append(repl_dict.get(i,i))

print(" ".join(lst))
