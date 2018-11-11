from random import randint
data = open('random.txt', 'w')
print('This program writes random numbers to the random.txt file.')
span = int(input('How many numbers would you like to write: '))


for numbers in range(0, span):
	data.write(str(randint(1, 500)))
	data.write(' ')
print(f'{span} numbers were written to the random.txt file')
