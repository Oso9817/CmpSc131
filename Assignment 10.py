print('This program tells you how far an object will fall in a number of seconds.')
while True:
	eta = int(input('Enter the falling time in seconds: '))
	if eta < 0:
		break
	distance = (1/2)*9.8*eta**2
	print(f'The distance the object will fall in {eta} seconds, is : {round(distance, 1)} meters.')