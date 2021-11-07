# Given a number n, find the smallest number that has same set of digits as n and is greater than n. If n is the greatest possible number with its set of digits, then print “not possible”.

def findNextGreater(number: int)->int:
	myarray = [int(i) for i in str(number)]
	n = len(myarray)
	# start from right
	# find a digit lesser than its neighboring right digit
	for i in range(n-1, 0, -1):
		if myarray[i-1] < myarray[i]:
			break

	if i==1 and myarray[0] >= myarray[1]:
		#they are in descending order
		print(f"Next number is not possible")
		return

	AnchorDigit = myarray[i-1]
	smallestIndex = i

	#find the smallest digit to the right of the digit from AnchorIndex
	for j in range(i+1, n):
		if myarray[j]>AnchorDigit and myarray[j]<myarray[smallestIndex]:
			smallestIndex = j

	#swapping the smallest index digit and the anchor digit
	myarray[i-1], myarray[smallestIndex] = myarray[smallestIndex], myarray[i-1]

	# converst list of ints to list of strings
	ListOfStrings = [str(i) for i in myarray]
	# convert list of strings to full string
	FullString = ''.join(ListOfStrings)
	# convert full string to integer value
	result=int(FullString)
	
	return result 


number = 534976
print(f"Original number is {number}")
print(f"NextGreater(number) is {findNextGreater(number)}")