class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# iterative solution

def reverseList(head: ListNode) -> ListNode:
    prev, curr = None, head

    while curr:
        nxt = curr.next  # temp var
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


# recursive solution

def reverseListRecursive(head: ListNode) -> ListNode:
    if not head:
        return None

    new_head = head
    if head.next:
        new_head = reverseListRecursive(head.next)
        head.next.next = head  # reversing the link
    head.next = None

    return new_head


# another recursive solution

def reverseListRecTwo(head):
    def reverse(cur, prev):
        if cur is None:
            return prev
        else:
            next = cur.next  # saving new next node
            cur.next = prev  # reverse
            return reverse(next, cur)   # reversing the rest of the list
    return reverse(head, None)