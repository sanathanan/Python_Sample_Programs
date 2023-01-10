"""
Program to check if a string contains any special character.

Input : Geeks$For$Geeks
Output : String is not accepted.

Input : Geeks For Geeks
Output : String is accepted
"""
# Method 1
import re

print("--------Method 1 -----------")
str_1 = 'Geeks$For$Geeks'

for i in str_1:
    if not (i.isdigit() or i.isalpha() or i== ' '):
        print("Not Accepted")
        break
    else:
        continue

# Method 2
print("--------Method 2 -----------")
str_2 = 'Geek$sFor$Geeks'
lst_2 = '[@_!#$%^&*()<>?/\|}{~:]'

c = 0
for i in str_2:
    if i in lst_2:
        c += 1
    else:
        continue

if c == 0:
    print("Accepted")
else:
    print("Not Accepted")

# Method 3
print("--------Method 3 -----------")
str_3 = 'GeeksForGeeks'
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

res_3 = regex.search(str_3)
if res_3 == None:
    print("Accepeted")
else:
    print("Not Accepted")