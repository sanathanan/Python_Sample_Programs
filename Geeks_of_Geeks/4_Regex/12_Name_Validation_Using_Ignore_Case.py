"""
Name Validation Using IgnoreCase

UseCase:
Let’s consider an example of a form where the user is asked to enter their name and we have to validate it using RegEx.
The format for entering name is as follow:

Mr. or Mrs. or Ms. (Either one) followed by a single space
First Name, followed by a single space
Middle Name(optional), followed by a single space
Last Name(optional)

Example:
Input : Mr. Albus Severus Potter
Output : Valid

Input : Lily and Mr. Harry Potter
Output : Invalid
"""
import re


def ignore_Case_Check(str):

    # ^(Mr\.|Mrs\.|Ms\.) - Checking for string starts with Mr. (or) Mrs. (or) Ms.
    # ( [a-z]+) - Looking for characters from a to z, with one or more occurances
    # ( [a-z]+)* - Looking for characters from a to z, with one or more occurances and one or zero or more occurances of word
    # ( [a-z]+)*$ - Looking for characters from a to z, with one or more occurances and one or zero or more occurances of word and ends with


    pattern = re.compile(r'^(Mr\.|Mrs\.|Ms\.)( [a-z]+)( [a-z]+)*( [a-z]+)*$',re.IGNORECASE)

    result = re.search(pattern, str)

    if result:
        return "Valid"
    else:
        return "No Valid"

def main():
    print(ignore_Case_Check('Mr. Albus Severus Potter'))
    print(ignore_Case_Check('Lily and Mr. Harry Potter'))

main ()

