class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head: ListNode) -> ListNode:
    if not head or head.next is None: return head

    l, m, r = None, head, head.next

    while r is not None:
        m.next,l, m, r = l,m, r, r.next

    m.next = l
    return m


def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    if not head or head.next is None or m is n: return head
    ctr,l,mid,r,prev = 1,head,None,None,None

    while ctr < m:
        ctr += 1
        prev = l
        l = l.next
    mid, r = l.next, l.next.next

    while ctr < n-1:
        mid.next = l
        l,mid,r = mid,r,r.next
        ctr += 1

    mid.next = l
    tail = r  #first node after the nth node in the linked list

    if prev:
        prev.next.next = tail
        prev.next = mid
    if not prev:
        head.next = tail
        head = mid

    return head







if __name__ == '__main__':
   a = ListNode(1)
   b = ListNode(2)
   c = ListNode(3)
   d = ListNode(4)
   e = ListNode(5)

   a.next = b
   b.next = c
   c.next = d
   d.next = e

   res = reverseBetween(a,1,2)

   while res:
       print(res.val)
       res = res.next
