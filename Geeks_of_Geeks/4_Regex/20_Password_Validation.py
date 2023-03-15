"""
Password Validation

Conditions:
Should have at least one number.
Should have at least one uppercase and one lowercase character.
Should have at least one special symbol.
Should be between 6 to 20 characters long.

Example:
Input :  Geek12#
Output : Password is valid.

Input :  asd123
Output : Invalid Password !!
"""
import re
# Method 1
print("------Method 1 --------")
str_1 = 'Geek12#'

def password_Check(str):
    special_Symbol=['$', '@', '#', '%']
    if len(str) < 6:
        return 'Password Length should be Greater than 6 digit less than 20 digit'
    if len(str) > 20:
        return 'Password Length should be Greater than 6 digit less than 20 digit'
    if not any(i.isdigit() for i in str):
        return 'Should have at least one number'
    if not any(i.isupper() for i in str):
        return 'Should have at least one uppercase'
    if not any(i.islower() for i in str):
        return 'Should have at least one lowercase'
    if not any(i in special_Symbol  for i in str):
        return 'Should have at least one special symbol'
    else:
        return "Valid Password"


def main():
    print(password_Check('Geek12#'))
    print(password_Check('asd123'))

main()