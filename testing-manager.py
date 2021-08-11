import os
for file in os.listdir("tests"):
    if file.endswith(".py") or file.endswith(".tcl"):
        print(os.path.join("tests", file))
print('Please type the row number (1 or 2): ')
test_number = input()
print('The number of test is ' + test_number)
if test_number == '1' :
	os.system('sh first.sh')
if test_number == '2' :
	os.system('sh second.sh')
else:
	print('Bye bye!=)')