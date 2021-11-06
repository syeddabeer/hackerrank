# efficiently remove duplicates from an array
import heapq

mylist = [8, 7, 1,2,3,4,5,7,3,2,7,6,9]

heapq.heapify(mylist)
unique_list = []

try:
	while True:
		e = heapq.heappop(mylist) #returns the lowest value
		print(f"popped element is {e}")
		if e not in unique_list:
			unique_list.append(e)
except IndexError as i:
	print(f"Final Result is {unique_list}")
