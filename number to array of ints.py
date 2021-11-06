def numberToArrayofIntegers(num):
	arr = [int(i) for i in str(num)]
	return arr

num = 985
print(numberToArrayofIntegers(num))