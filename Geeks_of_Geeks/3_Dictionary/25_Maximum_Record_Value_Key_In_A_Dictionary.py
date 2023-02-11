"""
Maximum Record Value in a dictionary
Sometimes, while working with dictionary records, we can have problem in which we need to find the
key with maximum value of particular key of nested records in list.


"""
# Method 1
print("--------Method 1 --------")
test_dict = {'gfg' : {'Manjeet' : 5, 'Himani' : 10},
             'is' : {'Manjeet' : 18, 'Himani' : 9},
             'best' : {'Manjeet' : 10, 'Himani' : 15}}

# initializing search key
key = 'Manjeet'

result = ''
compare = 0
for i in test_dict:
    if test_dict[i][key] >= compare:
        compare = test_dict[i][key]
        result = i

print(result)

