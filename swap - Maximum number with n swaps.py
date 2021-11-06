# swap - Maximum number formed from array with K number of adjacent swaps allowed

import sys

def finalprint(arr):
	for i in range(len(arr)):
		print(arr[i], end="")

	print()


def Swap(arr, currentPosition, targetPosition):
	for i in range(currentPosition, targetPosition, -1):
		#swap
		# print(f"before swap: {arr}")
		arr[i], arr[i-1] = arr[i-1], arr[i]
		# print(f"after swap: {arr}")


def maximizeArray(arr, swaps):
	# base condition
	if swaps==0:
		return

	for i in range(len(arr)):
		max_index=0 
		max=-(sys.maxsize-1)

		#search for the next k elements
		if (swaps+i)>len(arr):
			limit=len(arr)
		else:
			limit=swaps+i
        # Find index of the maximum
        # element in next K elements
		for j in range(i, limit + 1):
			if (arr[j] > max) :
				max = arr[j];
				max_index = j;

        # Update the value of
        # number of swaps
		swaps -= (max_index - i);
 
        # Update the array elements by
        # swapping adjacent elements
		Swap(arr, max_index, i);
		if (swaps == 0) :
			break;


# Driver code
if __name__ == "__main__" :
    arr = [ 1, 2, 9, 8, 1, 4, 9, 9, 9 ]
    swaps = 4
    maximizeArray(arr, swaps)
    finalprint(arr)

# Explanation of the problem
# Input : a[]={ 1, 2, 9, 8, 1, 4, 9, 9, 9 }, K = 4 
# Output : 9 8 1 2 1 4 9 9 9 
# After 1st swap a[ ] becomes 1 9 2 8 1 4 9 9 9 
# After 2nd swap a[ ] becomes 9 1 2 8 1 4 9 9 9 
# After 3rd swap a[ ] becomes 9 1 8 2 1 4 9 9 9 
# After 4th swap a[ ] becomes 9 8 1 2 1 4 9 9 9
# Input : a[]={2, 5, 8, 7, 9}, K = 2 
# Output : 8 2 5 7 9 