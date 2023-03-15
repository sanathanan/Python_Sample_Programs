"""
Extract words startinh with K in String List

Example:
Input : test_list = [“Gfg is good for learning”, “Gfg is for geeks”, “I love G4G”], K = l
Output : [‘learning’, ‘love’]
"""
# Method 1
print("-----------Method 1 ------------")
lst_1 = ["Gfg is good for learning", "Gfg is for geeks", "I love G4G"]
k = 'l'

result = []
for i in lst_1:
    for j in i.split():
        if j[0] == k:
            result.append(j)

print(result)

# Method 2
print("-----------Method 2 ------------")
lst_2 = ["Gfg is good for learning", "Gfg is for geeks", "I love G4G"]
k2 = 'l'

x= []
y=[]
for i in lst_2:
    x.extend(i.split())

for i in x:
    if i.startswith(k2.lower()) or i.startswith(k2.upper()):
       y.append(i)

print(y)