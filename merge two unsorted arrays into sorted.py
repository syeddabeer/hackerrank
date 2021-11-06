import heapq
import numpy as np

def mergeTwoUnsortedArraysIntoSorted(arr1, arr2):
	heapq.heapify(arr1)
	heapq.heapify(arr2)
	sortedArr=[]
	try:
		while True:
			e = heapq.heappop(arr1)
			sortedArr.append(e)
	except IndexError as i:
		try:
			while True:
				e = heapq.heappop(arr2)
				sortedArr.append(e)
		except IndexError as i:
			sortedArr = np.sort(sortedArr)
	return sortedArr 

arr1 = [6,3,7,8,1]
arr2 = [9,3,5,7,2]
print(f"the sorted array is {mergeTwoUnsortedArraysIntoSorted(arr1, arr2)}")