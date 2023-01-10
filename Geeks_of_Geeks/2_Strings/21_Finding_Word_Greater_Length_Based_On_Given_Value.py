"""
Find words which are greater than given length k

Input : str = "hello geeks for geeks
          is computer science portal"
        k = 4
Output : hello geeks geeks computer
         science portal
Explanation : The output is list of all
words that are of length more than k.

Input : str = "string is fun in python"
        k = 3
Output : string python
"""
# Method 1
print("-----------Method 1 ------------")
str_1 = "hello geeks for geeks is computer science portal"
k = 4

res_1 = [i for i in str_1.split() if len(i) > k]
print(res_1)

# Method 2
print("-----------Method 2 ------------")
str_2 = "hello geeks for geeks is computer science portal"
k = 4

res_2 = ' '
for i in str_2.split():
    if len(i) > k:
      res_2 = res_2 + ''.join(i) + " "
print(res_2)