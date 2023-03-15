"""
Convert List to List of Dictionaries

Example:
Input : test_list = [“Gfg”, 3, “is”, 8], key_list = [“name”, “id”]
Output : [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}]
Explanation : Values mapped by custom key, “name” -> “Gfg”, “id” -> 3.
"""
# Method 1
print("---------Method 1 ------------")
lst_1=["Gfg", 3, "is", 8]
key_list = ["name", "id"]

lst=[]
for i in range(0,len(lst_1),2):
    lst.append({key_list[0]:lst_1[i], key_list[1]:lst_1[i+1]})

print(lst)
