"""
Program to count Even and Odd Numbers in a list
Input: list1 = [2, 7, 5, 64, 14]
Output: Even = 3, odd = 2
"""
# Method 1
print("-----------Method 1 ---------")
lst_1 = [2, 7, 5, 64, 14]
even_count = []
odd_count= []
for i in lst_1:
    if i%2 == 0:
        even_count.append(i)
    else:
        odd_count.append(i)
print("Even Count in a list: ", len(even_count))
print("Odd Count in a list: ", len(odd_count))

# Method 2
print("-----------Method 2 ---------")
lst_2 = [2, 7, 5, 64, 14]
even_count_2 = 0
odd_count_2= 0
i = 0

while i<len(lst_2):
    if lst_2[i]%2 == 0:
        even_count_2 += 1
    else:
        odd_count_2 += 1
    i += 1

print("Even Count in a list: ", even_count_2)
print("Odd Count in a list: ", odd_count_2)