class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

def middleNode(head: ListNode) -> ListNode:
    turtle, hare = head
    while True:
        if not hare or not hare.next: return turtle
            turtle = turtle.next
            hare = hare.next.next



