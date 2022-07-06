# You are given the heads of two sorted linked lists list1
# and list2.
#
# Merge the two lists in a one sorted list. The list should be made by
# splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy

    while l1 and l2:  # both lists not empty
        if l1.val < l2.val:  # comparing each value
            tail.next = l1  # inserting the value in the tail
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next  # updating the tail regardless of which node we insert

    # checking if one of the list is empty and the other is not empty

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next

