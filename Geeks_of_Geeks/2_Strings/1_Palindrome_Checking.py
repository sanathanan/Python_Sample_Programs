"""
Palindrome / Symmetrical checking in a given string
"""

# user_str = 'amaama'
user_str = 'malayalam'
# print(len(user_str))
half= int(len(user_str)/2)

if len(user_str) %2 == 0:
    first_half = user_str[:half]
    second_half = user_str[half:]
else:
    first_half = user_str[:half]
    second_half = user_str[half+1:]

if first_half == second_half:
    print("It is Symmetrical")
else:
    print("It is not a symmetrical")

if first_half == second_half[::-1]:
    # print(second_half[::-1])
    print("It is Palindrome")
else:
    print("it is not a Palindrome")

