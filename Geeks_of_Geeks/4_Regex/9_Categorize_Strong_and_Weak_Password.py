"""
Categorize Password as Strong or weak Password

Given a password, we have to categorize it as a strong or weak one.
There are some checks that need to be met to be a strong password. For a weak password, we need to return the reason for it to be weak.

Conditions to be fulfilled are:

Minimum 9 characters and maximum 20 characters.
Cannot be a newline or a space
There should not be three or more repeating characters in a row.
The same string pattern(minimum of two character length) should not be repeating.

Example:
Input1 : Qggf!@ghf3
Output1 : Strong Password!

Input2 : aaabnil1gu
Output2 : Weak Password: Same character repeats three
or more times in a row
"""
import re


def password_Check(str):

    # Checking New line or Space
    if str == '\n' or str == ' ':
        return 'Password Cannot be a New line or Space'

    # Checking character count
    if 9 <= len(str) <= 20:

        # Checking for repeating characters in a row
        if re.search('(.)\1\1', str):
            return 'Repeating characters in a row'

        if re.search(r'(..)(.*?)\1', str):
            return "Weak password: Same string pattern repetition"

        else:
            return 'Strong Password'

    else:
        return 'Password should be a Minimum 9 characters and maximum 20 characters'


def main():
    print(password_Check('Qggf!@ghf3'))
    print(password_Check('aaabnil1gu'))
    print(password_Check('Geeksforgeeks'))
    print(password_Check('Aasd!feasnm'))
    print(password_Check('772*hdf77'))
    print(password_Check(' '))


main()