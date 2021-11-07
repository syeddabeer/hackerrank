# this problem is somewhat like selection sort, but does not sort completely.
def numberOfSwaps(arr):
	swaps=0
	referencePosition = 0
	number = 0
	while referencePosition < len(arr) and number < len(arr):
		if arr[number] < arr[referencePosition]:
			arr[referencePosition], arr[number] = arr[number], arr[referencePosition]
			swaps+=1
			referencePosition, number = number, number+1
			print("result after each iteration:", arr)
		else:
			if number < len(arr)-2:
				number += 1
			else:
				break
	print(f"The final sorted array (numberOfSwaps): {arr}")
	return swaps
       
inputArray = [9, 1, 8, 4, 6, 5, 3, 2, 7]
print("input Array is: ", inputArray)
print(f"number of swaps is: {numberOfSwaps(inputArray)}")


inputArray2 = [3, 7, 1, 2]
print("input Array is: ", inputArray2)
print(f"number of swaps is: {numberOfSwaps(inputArray2)}")



############################# Program Description #############################
# You're a new Amazon Software Development Engineer (SDE). You've been asked to evaluate the efficiency of an old sorting algorithm. The following algorithm is used to sort an array of distinct n integers.

# For the input array arr of size n do:

# Try to find the smallest pair of indices:
# 0 \leq i < j \leq n - 1

# such that arr[i] > arr[j]. Here 'smallest' means usual alphabetical ordering of pairs, i.e. (i_1, j_1) < (i_2, j_2) if and only if i_1 < i_2 or (i_1 = j_1 and j_1 < j_2).

# If there is no such pair, stop.
# Otherwise, swap a[i] and a[j] and repeat finding the next pair.
# How efficient is this algorithm? Write a function that calculate the number of swaps performed by the above algorithm.

# For example, if the initial array is [5, 1, 4, 2], then the algorithm first picks pair (5, 1) and swaps it to produce array [1,5,4,2]. Next, it picks pair (5,4) and swaps it to produce array [1,4,5,2]. Next, pair (4,2) is picked and swapped to produce array [1,2,5,4], and finally pair (5,4) is swapped to produce the final sorted array [1,2,4,5], so the number of swaps performed is 4.

# Function description
# Complete the function howManySwaps in the editor below. The function should return an integer that denotes the number of swaps performed by the proposed algorithm on the input array.

# The function has the following parameter(s):

# arr: integer array of size n with all unique elements