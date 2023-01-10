"""
Finding all the close matches of input string from a list

Input : patterns = ['ape', 'apple',
                  'peach', 'puppy'],
          input = 'appel'
Output : ['apple', 'ape']
"""

# Method 1
# difflib.getc_close_matches(word, possibilities, n, cutoff)

from difflib import *

patterns = ['ape', 'apple', 'peach', 'puppy']
word = 'appel'

closest_Match = get_close_matches(word, patterns)
print(closest_Match)