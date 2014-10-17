__author__ = 'karthikb'
'''
The program reorders a linklist which is of the form
L: L0->L1->.. ->Ln-1 ->Ln to L0->Ln->L1->Ln-1->L2->Ln-2->
Given {1,2,3,4}, reorder it to {1,4,2,3}
'''

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class List:
    def __init__(self):
        self.head = None

    def insert_element(self,data):
        new_node = ListNode(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        if current is None:
            return
        while current.next is not None:
            print str(current.val)+ "->"
            current = current.next
        print current.val

    def get_length(self):
        current = self.head
        length = 0
        if current:
            while current.next is not None:
                current = current.next
                length += 1
        return length

    def reorderList(self ):

        if self.head is None:
            return
        current = self.head
        length = 0
        stack = []
        while current.next is not None:
            current = current.next
            length += 1

        #computing half length
        half_length = length /2
        print "Half length",half_length
        #Appending the values to stack
        length = 0
        current = self.head
        while current.next is not None:
            current = current.next
            length += 1
            if length == half_length:
                future = current
                while future.next is not None:
                    future = future.next
                    stack.append(future.val)
                current.next = None
        print stack
        current = self.head
        length = 0
        while current.next is not None and stack:
            future = current.next
            new_node = ListNode(stack.pop())
            new_node.next = future
            current.next = new_node
            current = future
        if stack:
            current.next = ListNode(stack.pop())



class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):

        if head is None:
            return
        current = head
        length = 0
        stack = []
        while current.next is not None:
            current = current.next
            length += 1

        #computing half length
        half_length = length /2
        length = 0
        current = head
        while current.next is not None and stack:
            current = current.next
            length += 1
            if length > half_length:
                stack.add(current.val)
        current = head
        length = 0
        '''
        while current.next is not None:
            previous = current
            new_node = ListNode(stack.pop())
            previous.next = new_node
            new_node.next = current.next
            current = current.next
        '''








list = List()
list.insert_element(1)
list.insert_element(2)
list.print_list()
list.reorderList()
list.print_list()