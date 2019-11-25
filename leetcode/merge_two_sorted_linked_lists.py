#21. Merge Two Sorted Lists
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#36ms beats 89% of submissions, bit of messy code though due to the min calls
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    elif not l2:
        return l1

    n1, n2 = l1, l2
    head = min([n1, n2], key=lambda n1: n1.val)
    if head is n1:
        n1 = n1.next
    else:
        n2 = n2.next
    new = head

    while n1 and n2:
        new.next = min([n1, n2], key=lambda n1: n1.val)
        if new.next is n1:
            n1 = n1.next
        else:
            n2 = n2.next
        new = new.next

    new.next = n1 or n2

    return head

#36ms beats 89% of submissions, dummy node, no min calls outside
def mergeTwoListsII(l1:ListNode, l2:ListNode) -> ListNode:
    n1, n2 = l1, l2
    dummy = ListNode(-1)
    new = dummy

    while n1 and n2:
        new.next = min([n1, n2], key=lambda n1: n1.val)
        if new.next is n1:
            n1 = n1.next
        else:
            n2 = n2.next
        new = new.next

    new.next = n1 or n2

    return dummy.next

#36ms beats 89% of submissions, dummy node, no min calls at all
def mergeTwoListsIII(l1: ListNode, l2: ListNode) -> ListNode:
    n1, n2 = l1, l2
    dummy = ListNode(-1)
    new = dummy

    while n1 and n2:

        if n1.val <= n2.val:
            new.next, n1 = n1, n1.next
        else:
            new.next, n2 = n2, n2.next

        new = new.next

    new.next = n1 or n2

    return dummy.next


if __name__ == "__main__":
    l11 = ListNode(1)
    l12 = ListNode(2)
    l13 = ListNode(4)

    l21 = ListNode(1)
    l22 = ListNode(3)
    l23 = ListNode(4)

    l11.next = l12
    l12.next = l13

    l21.next = l22
    l22.next = l23

    head = mergeTwoLists(l11, l21)

    while head:
        print(head.val)
        head = head.next
