"""
Remove all characters except letters and numbers
"""
import re
print("-----------Method 1 -----------")
def remove_unknown_Charc(str):

    pattern = re.compile('[\W_]+')
    #pattern=re.compile('[$_!%]')
    replace = ''

    result = re.sub(pattern, replace, str)

    return result

def main():
    print(remove_unknown_Charc('1234$$$$56abcdg_!%$'))

main()

