# merge sort using linked list
# create Node using class Node.
class LinkedNode:
    def __init__(self, value, tail=None):
        self.value = value
        self.next = tail
 
class LinkedList:
    def __init__(self, *start):
        """define none head and then call prepend for all arguments. linked lists in Python."""
        self.head  = None
        for _ in start:
            self.prepend(_)

    def prepend(self, value):
        """Prepend element into linked list."""
        self.head = LinkedNode(value, self.head)
    

    # Utility function to get the middle
    # of the linked list
    def getMiddle(self, head):
        if head == None:
            return head
        slow = head
        fast = head
        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next     
        return slow

    def mergesort(self, mylinkedlist):
         
        # Base case if head is None
        if mylinkedlist == None or mylinkedlist.next == None:
            return mylinkedlist
 
        # get the middle of the list
        middle = self.getMiddle(mylinkedlist)
        secondhalf = middle.next
 
        # set the next of middle node to None
        middle.next = None
 
        # Apply mergesort on left list
        half_a = self.mergesort(mylinkedlist)
         
        # Apply mergesort on right list
        half_b = self.mergesort(secondhalf)
 
        # Merge the left and right lists
        return self.sortedMerge(half_a, half_b)

    def sortedMerge(self, sublinkedlist1, sublinkedlist2):
        result = None
         
        # Base cases
        if sublinkedlist1 == None:
            return sublinkedlist2
        if sublinkedlist2 == None:
            return sublinkedlist1
             
        # pick either sublinkedlist1 or sublinkedlist2 and recur..
        if sublinkedlist1.value <= sublinkedlist2.value:
            result = sublinkedlist1
            result.next = self.sortedMerge(sublinkedlist1.next, sublinkedlist2)
        else:
            result = sublinkedlist2
            result.next = self.sortedMerge(sublinkedlist1, sublinkedlist2.next)
        return result
     
# Utility function to print the linked list
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.value, end = " ")
        curr_node = curr_node.next
    print(' ')
     
# Driver Code
if __name__ == '__main__':
    li = LinkedList()
     
    # Let us create a unsorted linked list
    # to test the functions created.
    # The list shall be a: 2->3->20->5->10->15
    li.prepend(15)
    li.prepend(10)
    li.prepend(5)
    li.prepend(20)
    li.prepend(3)
    li.prepend(2)
    print(f"Original Linked List is: ")
    printList(li.head) 
    # Apply merge Sort
    li.head = li.mergesort(li.head)
    print ("Sorted Linked List is:")
    printList(li.head)