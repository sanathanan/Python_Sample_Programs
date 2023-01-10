"""
Program to find a smallest number from a list

Input : list1 = [10, 20, 4]
Output : 4
"""
# Method 1
print("---------Method 1 ----------")
lst_1 = [10,20,4]
lst_1.sort()
print("Smallest element is: ", lst_1[0])

# Method 2
print("----------Method 2 ------------")
lst_2 = [10,20,4]
lst_2.sort(reverse=True)
print(lst_2[-1])

# Method 3
print("----------Method 3 ------------")
lst_3 = [10,20,4]
print(min(lst_3))

# Method 4
print("----------Method 4 ------------")
lst_4 = [10,20,4,1,1,0]

min_element = lst_4[0]

for i in range(len(lst_4)):
    if lst_4[i] < min_element:
        min_element = lst_4[i]
    elif lst_4[i] == min_element:
        min_element = lst_4[i]
print(min_element)