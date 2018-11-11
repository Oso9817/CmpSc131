packs = int(input('Enter the number of packages ordered: '))
cost = packs*100
if 0 < packs < 10:
	print('The total cost of your purchase was ${0} with a discount of $0.00'.format(cost))

if 9 < packs < 20:
	discount = (cost)*.1
	print('The total cost of your purchase was ${0} with a discount of ${1}'.format(cost - discount, discount))

if 19 < packs < 50:
	discount = (cost)*.2
	print('The total cost of your purchase was ${0} with a discount of ${1}'.format(cost - discount, discount))

if 49 < packs < 100:
	discount = (cost)*.3
	print('The total cost of your purchase was ${0} with a discount of ${1}'.format(cost - discount, discount))

if 99 < packs:
	discount = (cost)*.4
	print('The total cost of your purchase was ${0} with a discount of ${1}'.format(cost - discount, discount))



