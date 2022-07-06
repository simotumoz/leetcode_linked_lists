# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head:ListNode):
    slow, fast = head, head.next
    while fast and fast.next:  # fast is not null and the end of the list hasn't been reached yet
        # shifting pointers
        slow = slow.next  # shift by one
        fast = fast.next.next  # shift by two

    second = slow.next
    slow.next = None
    prev = None

    # reversing the second half of the list
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # merging the two halves

    first = head
    second = prev  # prev is the new head of the 2nd half

    while second:
        # actual merging
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        # shifting pointers
        first, second = tmp1, tmp2