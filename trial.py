a = [1,2,3]
b = 4

if b not in a:
	a.append(b)

print(a)

# rough work for merge sort

def mergesort(arr):
	if len(arr)<=1:
		return arr 
	mid=len(arr)//2

	firsthalf=arr[:mid]
	secondhalf=arr[mid:]

	half_a = mergesort(firsthalf)
	half_b=mergesort(secondhalf)

	return merge(half_a, half_b)

def merge(sublist1, sublist2):
	i = j = 0
	mergedlist =[]

	while i<len(sublist1) and j<len(sublist2):
		if sublist1[i] < sublist2[j]:
			mergedlist.append(sublist1[i])
			i+=1
		else:
			mergedlist.append(sublist2[j])
			j+=1

	while i<len(sublist1):
		mergedlist.append(sublist1[i])
		i+=1

	while j<len(sublist2):
		mergedlist.append(sublist2[j])
		j+=1

	return mergedlist


# merge sort using the linked list

class LinkedList:

	def getMiddle(self, head):
		if head == None:
			return head

		slow = head
		fast = head

		while (fast.next ! = None and fast.next.next !=None):
			slow = slow.next
			fast = fast.next.next

		return slow


