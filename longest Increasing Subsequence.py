# length of longest increasing subsequence
import numpy as np
def LIS(arr):
	n = len(arr)
	
	# Declare the list (array) for LIS and
	# initialize LIS values for all indexes
	lis = [1]*n
	
	# Compute optimized LIS values in bottom up manner
	for i in range(1, n):
		for j in range(0, i):
			if arr[j] < arr[i] and lis[i] < lis[j] + 1:
				lis[i] = lis[j]+1
				# print(lis[i])
	
	# Initialize maximum to 0 to get
	# the maximum of all LIS
	maximum = 0
	
	# Pick maximum of all LIS values
	for i in range(n):
		maximum = max(maximum, lis[i])
	
	return maximum

# Driver program to test above function
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print(f"Longest integer subsequence is: {LIS(arr)}")
arr2 = [3, 10, 2, 1, 20]
print(f"Longest integer subsequence is: {LIS(arr2)}")
arr3 = [3, 2]
print(f"Longest integer subsequence is: {LIS(arr3)}")
arr3 = [50, 3, 10, 7, 40, 80]
print(f"Longest integer subsequence is: {LIS(arr3)}")
