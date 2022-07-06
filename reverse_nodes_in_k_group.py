# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
#
# k is a positive integer and is less than or equal to the
# length of the linked list. If the number of nodes is not
# a multiple of k then left-out nodes, in the end,
# should remain as it is.
#
# You may not alter the values in the list's nodes,
# only nodes themselves may be changed.
#
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getKth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr


def reverseKGroup(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        kth = getKth(group_prev, k)
        if not kth:
            break
        group_next = kth.next

        # reversing group
        prev, curr = kth.next, group_prev.next
        while curr != group_next:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp

    return dummy.next