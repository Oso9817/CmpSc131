def getNamesList(output):
	#'GirlNames.txt'
	if 'Girl' in output:
		print('test passed')
	raw_names = open(output, 'r+t')
	
	dataName = raw_names.read()
	return dataName.split()
	
	
	print(names)
def checkName(name, output):
	if name in getNamesList(output):
		print('test passed')

checkName('Riley', 'GirlNames.txt')