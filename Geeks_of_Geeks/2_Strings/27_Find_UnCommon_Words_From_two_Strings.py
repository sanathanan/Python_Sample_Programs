"""
Find Uncommon words from two strings

Input : A = “Geeks for Geeks”,  B = “Learning from Geeks for Geeks”
Output : [‘Learning’, ‘from’]

Input : A = “apple banana mango” , B = “banana fruits mango”
Output : [‘apple’, ‘fruits’]
"""

# Method 1
print("--------Method 1 -------------")
a = 'Geeks for Geeks'
b = 'Learning from Geeks for Geeks'

A = a.split()
B = b.split()

lst = []
for i in A:
    if i not in B:
        lst.append(i)
for j in B:
    if j not in A:
        lst.append(j)

print(lst)

# Method 2
print("------------Method 2 ----------------")

aa = 'apple banana mango'
bb = 'banana fruits mango'
dict={}
lst_2 = []
for i in aa.split():
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

for i in bb.split():
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

for i,j in dict.items():
    if j == 1:
        lst_2.append(i)

print(lst_2)