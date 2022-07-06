# You are given two non-empty linked lists representing two
# non-negative integers. The digits are stored in reverse order, and
# each of their nodes contains a single digit. Add the two numbers
# and return the sum as a linked list.
#
# You may assume the two numbers do not contain any
# leading zero, except the number 0 itself.
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()  # creating dummy node
    cur = dummy

    carry = 0  # initializing carry

    while l1 or l2 or carry:  # 'or carry' -> 8 + 7, l1 and l2 are null but we have a carry to insert
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        # computing new digit
        val = v1 + v2 + carry
        # in case we have a new carry
        carry = val // 10
        val = val % 10
        cur.next = ListNode(val)  # actually inserting value in the node

        # updating pointers
        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next
