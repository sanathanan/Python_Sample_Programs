"""
Validate an IP Address

Example:
Input: 110.234.52.124
Output: Valid Ip address

Input: 666.1.2.2
Output: Invalid Ip address
"""
import re

print("----------Method 1 -----------")

def ip_Address_Check(str):

    pattern = re.compile(r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})')
    result = re.search(pattern, str)

    if result:
        return "Valid IP Address"
    else:
        return "Non Valid IP Address"


def main():
    print(ip_Address_Check('110.234.52.124'))
    print(ip_Address_Check('666.1.2.2'))


main()

# Method 2
import ipaddress
print("-------Method 2 ----------")

def check_ip(str):

    try:
        result2 = ipaddress.ip_address(str)
        print("Valid IP Address")
    except:
        print("Non Valid IP Address")


def main_2():
    check_ip('110.234.52.124')
    check_ip('666.1.2.2')

main_2()