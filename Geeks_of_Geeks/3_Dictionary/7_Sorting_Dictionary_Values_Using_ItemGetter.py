"""
Sorting Dictionary Values using Item Getter
"""
# Method 1
from operator import itemgetter

list = [{"name": "Nandini", "age": 20},
        {"name": "Manjeet", "age": 20},
        {"name": "Nikhil", "age": 19}]
result1 = sorted(list, key=itemgetter('age'))
result2 = sorted(list, key=itemgetter('age', 'name'))
result3 = sorted(list, key=itemgetter('age', 'name'), reverse=True)
print(result1)
print(result2)
print(result3)