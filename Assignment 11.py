print('This program calculates the fahrenheit temperature and the wind speed.')
while True:
	temperature = int(input('Enter the fahrenheit temperature: '))
	speed = int(input('Enter the wind speed: '))
	print(f'The windchill is: {round((35.74 + 0.6215 * temperature - 35.75 * speed**0.16 + 0.4275 * temperature * speed**0.16), 1)}')
	persist = input('Would you like to calculate another windchill? Enter "y" or "n": ')
	if 'n' in persist.lower():
		break