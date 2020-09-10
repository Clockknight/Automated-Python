import re

excess = input('Please input string to be stripped: ')

excessRegex = re.compile(r'\S')
mo = excessRegex.search(excess)
mo.group()

print(mo.group())
