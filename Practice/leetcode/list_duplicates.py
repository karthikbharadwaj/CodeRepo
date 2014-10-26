__author__ = 'karthikb'
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        noDup = {}

        if head:
            prev = head
            curr = head.next
            noDup[prev.val] = 1
            while curr is not None:
                if curr.val in noDup:
                    prev.next = curr.next
                    curr = curr.next
                else:
                    noDup[curr.val] = 1
                    prev = curr
                    curr = curr.next
        return head
