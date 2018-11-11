femaleData = open('GirlNames.txt', 'r+t')
maleData = open('BoyNames.txt', 'r+t')

namesFemale = femaleData.read()
femaleList = namesFemale.split()

namesMale = maleData.read()
maleList = namesMale.split()

go = 1
print('Enter a name to see if it is a popular girls or boys name.\n')
while go:
	nCheck = input('Enter a name to check, or "stop" to stop: ').capitalize()
	
	if nCheck in femaleList:
		if nCheck in maleList:
			print(f'{nCheck} is a popular girls name and is ranked: {femaleList.index(nCheck) + 1}')
			print(f'{nCheck} is a popular boys name and is ranked: {maleList.index(nCheck) + 1}\n')

		else:
			print(f'{nCheck} is a popular girls name and is ranked: {femaleList.index(nCheck) + 1}')
			print(f'{nCheck} is not a popular boys name.\n')
		
		
	elif nCheck in maleList:
		if nCheck in femaleList:
			print(f'{nCheck} is a popular boys name and is ranked: {maleList.index(nCheck) + 1}')
			print(f'{nCheck} is a popular girls name and is ranked: {femaleList.index(nCheck) + 1}\n')
		else:
			print(f'{nCheck} is a popular boys name and is ranked: {maleList.index(nCheck) + 1}')
			print(f'{nCheck} is not a popular girls name.\n')

	elif nCheck not in femaleList and maleList:
		if nCheck == 'Stop':
			go = 0
		else:
			print(f'{nCheck} is not a popular girls name.')
			print(f'{nCheck} is not a popular boys name.\n')
	


femaleData.close()
maleData.close()