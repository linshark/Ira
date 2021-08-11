import re
GREEN='\033[1;32m'
RED = '\033[91m'
NC='\033[0m'
f = open('pyt.txt', 'r')
z=f.read()
regexp = r'\bJobs\b'
print('String for search: '+regexp)
print('Text is: '+z)
match = re.search(regexp, z)
if (match):
	print(GREEN+"The test was successful"+NC)
else:
	print(RED+"The test was failed"+NC)
print('The string has found: '+match.group(0))