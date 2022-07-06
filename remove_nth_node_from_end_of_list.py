# Given the head of a linked list, remove the nth node
# from the end of the list and return its head.
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    left = dummy
    right = head

    # incrementing right pointer

    while n > 0 and right:
        right = right.next
        n -= 1

    # shifting pointers

    while right:
        left = left.next
        right = right.next

    # deleting the node

    left.next = left.next.next

    return dummy.next
