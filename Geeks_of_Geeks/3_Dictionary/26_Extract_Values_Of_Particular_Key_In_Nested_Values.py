"""
Extract Values of Particular Key in Nested Values

Example:
Input : test_dict = {‘Gfg’ : {“a” : 7, “b” : 9, “c” : 12}, ‘is’ : {“a” : 15, “b” : 19, “c” : 20},
                    ‘best’ :{“a” : 5, “b” : 10, “c” : 2}},
        temp = “b”
Output : [9, 10, 19]
"""

# Method 1
print("----------Method 1 ------------")
test_dict = {"Gfg" : {"a" : 7, "b" : 9, "c" : 12}, "is" : {"a" : 15, "b" : 19, "c" : 20},
              "best" :{"a" : 5, "b" : 10, "c" : 2}}
temp = 'b'
lst =[]
for i in test_dict:
    lst.append(test_dict[i][temp])

print(sorted(lst))

# Method 2
print("----------Method 1 ------------")
test_dict_2 = {"Gfg" : {"a" : 7, "b" : 9, "c" : 12}, "is" : {"a" : 15, "b" : 19, "c" : 20},
                "best" :{"a" : 5, "b" : 10, "c" : 2}}
temp2='b'
lst2 =[]
for i,j in test_dict_2.items():
    if temp2 in j:
       lst2.append(j[temp2])

print(sorted(lst2))