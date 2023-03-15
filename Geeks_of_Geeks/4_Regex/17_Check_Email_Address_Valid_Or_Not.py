"""
Checking Email address is valid or not

Example:
Input:  ankitrai326@gmail.com
Output: Valid Email

Input: my.ownsite@ourearth.org
Output: Valid Email

Input: ankitrai326.com
Output: Invalid Email
"""
import re
print("----------Method 1 ----------")

def email_Check(str):

    # pattern = re.compile('([a-zA-Z0-9.]+)\@([a-z]+)\.[comrg]')
    pattern = re.compile('[\w.]+\@[\w.]+')
    result = re.search(pattern, str)

    if result:
        return "Valid Email"
    else:
        return "Non Valid Email"


def main():
    print(email_Check("ankitrai326@gmail.com"))
    print(email_Check("my.ownsite@ourearth.org"))
    print(email_Check("ankitrai326.com"))

main()
