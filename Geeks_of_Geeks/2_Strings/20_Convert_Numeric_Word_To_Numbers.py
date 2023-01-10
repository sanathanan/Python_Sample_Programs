"""
Convert Numeric Words To Numbers
"""
# Method 1
print("----------Method 1 -----------")
test_str = "zero four zero one"

dict = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5',
        'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}

# dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5,
#         'six':6, 'seven':7, 'eight':8, 'nine':9, 'zero':0}

str_lower = test_str.lower()

res = ''
for i in test_str.split():
    res = res + ''.join(dict[i])
print(res)