"""
Finding Dictionary Values Mean

Example:
Input : test_dict = {"Gfg" : 4, "is" : 4, "Best" : 4, "for" : 4, "Geeks" : 4}
Output : 4.0
Explanation : (4 + 4 + 4 + 4 + 4) / 4 = 4.0, hence mean.
"""
# Method 1
print("--------Method 1 ------------")
test_dict = {"Gfg" : 4, "is" : 4, "Best" : 4, "for" : 4, "Geeks" : 4}

lst = []
for i in test_dict:
    lst.append(test_dict[i])

mean = sum(lst)/len(lst)
print(mean)

# Method 2
print("--------Method 2 ------------")
test_dict_2 = {"Gfg" : 4, "is" : 4, "Best" : 4, "for" : 4, "Geeks" : 4}

result_2 = sum(test_dict_2.values())/len(test_dict_2)
print(result_2)