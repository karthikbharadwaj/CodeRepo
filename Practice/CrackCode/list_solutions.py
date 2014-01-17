__author__ = 'karthikb'

class Node:

    def __init__(self,data):

        self.data = data
        self.next = None


class LinkList:

    def __init__(self,data):
        self.head = Node(data)

    def add_item(self,data):

        if self.head == None:
            self.head = Node(data)
            print "Adding head node",self.head.data
        else:
            current = self.head

            while current.next!= None:
                current = current.next
            current.next = Node(data)


        return self.head

    def print_list(self):

        if self.head == None:
            return self.head
        else:
            current = self.head
            while current.next is not None:
                print current.data,'-->',
                current = current.next
            print current.data

    def last_nth_item(self,n):

        if self.head == None:
            print "Empty list"

        first = self.head
        second = self.head
        counter = 0
        while counter < n:
            counter += 1
            first = first.next

        if first is None:
            return None
        second = self.head

        while first.next is not None:
            first = first.next
            second = second.next

        return second.data
















link_list = LinkList(1)
link_list.add_item(2)
link_list.add_item(3)
link_list.add_item(5)
link_list.print_list()
print link_list.last_nth_item(1)

def solution_2_1(a):
    ''' Remove duplicates from unsorted array
    a = [3,4,3,4,1]
    '''
    dup_dict = {}
    result = []

    for item in a:
        if item in dup_dict:
            continue
        else:
            dup_dict[item]= 1
            result.append(item)
    return result

def solution_2_2(a,n):
    '''find nth to last element of link list'''
    i = 0
    n = len(a)





def solution_2_3(a,n):
    ''' find the nth element in the singly linklist a
    '''
    return
