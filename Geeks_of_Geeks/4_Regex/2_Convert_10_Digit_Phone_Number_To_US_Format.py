"""
Converting 10 digit phone number to US format
"""
#  Method 1
import re
print("---------Method 1 -------")
s = 'geeks 0123456789'

# \d is used to check for numbers
# (\d{3}) - It will check for numbers that count to 3
# (\1) \2-\3:
    # (\1) - first 3 digit is sorrounded with brackets
    # \2 - second three digit
    # - - second three digit followed by '-'
    # \3 - Third 3 digit
res = re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', s)
print(res)