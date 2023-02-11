"""
Finding files having a particular extension
"""
import re
file_names = ["gfg.html", "geeks.xml",
            "computer.txt", "geeksforgeeks.jpg"]

pattern = re.compile('\.jpg')
for file in file_names:
    match = re.search(pattern, file)
    if match:
        print("The file name is :", file)