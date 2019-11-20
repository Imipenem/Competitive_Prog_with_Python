class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head: ListNode) -> ListNode:
    if not head or head.next is None: return head

    l, m, r = None, head, head.next

    while r is not None:
        m.next = l
        l, m, r = m, r, r.next

    m.next = l
    return m


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)
    g = ListNode(7)
    h = ListNode(8)
    i = ListNode(9)
    j = ListNode(10)
    k = ListNode(11)
    l = ListNode(12)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    g.next = h
    h.next = i
    i.next = j
    j.next = k
    k.next = l

    res = reverse_list(None)

    while res is not None:
        print(res.val)
        res = res.next
