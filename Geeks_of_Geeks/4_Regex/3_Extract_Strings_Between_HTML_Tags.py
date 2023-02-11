"""
Extract Strings between HTML Tags

Input :  ‘<b>Gfg</b> is <b>Best</b>. I love <b>Reading CS</b> from it.’ , tag = “br”
Output : [‘Gfg’, ‘Best’, ‘Reading CS’]
"""
import re

str = '<b>Gfg</b> is <b>Best</b>. I love <b>Reading CS</b> from it.'
tag = 'b'

# Logic - (.*?)
# () - Capture and Group
# . - any number of character except new line character
# * - Zero or more occurances
# ? - Zero or one occurances
pattern = '<'+tag+'>(.*?)</'+tag+'>'
result = re.findall(pattern, str)
print(result)