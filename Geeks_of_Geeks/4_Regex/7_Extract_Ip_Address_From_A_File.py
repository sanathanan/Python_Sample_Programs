"""
Extract IP Adress from a file
"""
import re

# Reading the file
with open('file.txt', 'r') as file:
    fh = file.readlines()
print(fh)

pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
lst=[]
for i in fh:
    #print(i)
    # line = i.rstrip()
    ip_Address = re.search(pattern,i)
    print(ip_Address)
    if ip_Address:
        lst.append(ip_Address.group(0))

print(lst)
