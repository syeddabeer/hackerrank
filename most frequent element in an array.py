#most frequent element in an array

def mostFrequent(arr):
	n = len(arr)

	arr.sort()

	#linear traversal
	max_count=1
	res = arr[0]
	curr_count=1

	for i in range(1, n):
		if (arr[i] == arr[i - 1]):
			curr_count += 1
		else:
			if (curr_count > max_count):
				max_count = curr_count
				res = arr[i - 1]
             
			curr_count = 1
     
    # If last element is most frequent
	if (curr_count > max_count):
		max_count = curr_count
		res = arr[n - 1]
	return res

#driver code
arr = [1, 5, 2, 1, 3, 2, 1]
arr2= [1, 5, 2, 1, 3, 2, 1, 5, 6, 6, 6, 6]
print(mostFrequent(arr))
print(mostFrequent(arr2))
