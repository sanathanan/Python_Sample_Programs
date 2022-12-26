# Driver Code
test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']



print("-----------Method 1 ------------")
print("Given String: ", test_list)
res = [i.replace('G','-').replace('e','G').replace('-','e') for i in test_list]
print("Replaced String: ", res)

