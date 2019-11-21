class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    prev, curr, end = None, head, head
    ctr = 1

    while ctr < n:
        end = end.next
        ctr += 1

    if not end.next: return curr.next

    while end.next:
        if not prev:
            prev = head
        else:
            prev = prev.next

        curr, end = curr.next, end.next
    prev.next = curr.next
    return head


if __name__ == '__main__':
    print("hello")
