data = open('random.txt', 'r+t')
StringData = data.read()
Data_List = StringData.split()
Int_List = list(map(int, Data_List))
for numbers in Int_List:
	print(numbers)
print(f'The lowest number in the list is: {min(Int_List)}')
print(f'The highest number in the list is: {max(Int_List)}')
print(f'The total of the numbers is: {sum(Int_List)}')
print(f'The average of the numbers in the list is: {sum(Int_List)/len(Int_List)}')
data.close()