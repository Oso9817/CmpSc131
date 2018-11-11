C = int(input('Enter the number of celsius temperatures to display: '))
print('Celsius Farenheit')
for i in range(0,C+1):
	F = 9/5 * i + 32

	print(f'{i}\t {round(F, 1)}')
