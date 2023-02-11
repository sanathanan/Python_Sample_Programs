"""
Sorting Dictionary Values using Lambda
"""
list = [{"name": "Nandini", "age": 20},
        {"name": "Manjeet", "age": 20},
        {"name": "Nikhil", "age": 19}]

result1 = sorted(list, key=lambda x:x['age'])
result2 = sorted(list, key=lambda x:(x['age'], x['name']))
result3 = sorted(list, key=lambda x: (x['age'], x['name']), reverse=True)
print(result1)
print(result2)
print(result3)