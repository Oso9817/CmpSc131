height = float(input('Enter your height in inches: '))
weight = float(input('Enter your weight in pounds: '))
BMI = round((weight * 703 / height**2), 1) 
health = 'test'

if BMI < 18.5:
	health = 'Your BMI indicates you are underweight.'

if BMI > 25:
	health = 'Your BMI indicates you are overweight.'

if 18.5 < BMI < 25:
	health = 'Your BMI indicates you are optimal weight.'

print('Your BMI is: ', BMI)
print(health)
