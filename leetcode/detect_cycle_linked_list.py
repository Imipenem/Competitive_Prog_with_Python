# LEETCODE 142. Linked List Cycle II and 141. Linked List Cycle


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        else:
            hare = head.next
            turtoise = head

            while hare != turtoise:
                if hare is None or hare.next is None:
                    return False
                else:
                    hare = hare.next.next
                    turtoise = turtoise.next
            return True

    def hasCycleII(self, head: ListNode) -> bool:  # 9times faster than above lol
        if head is None:
            return False
        else:
            hare = head.next
            turtoise = head
            while hare and turtoise:
                if hare == turtoise:
                    return True
                else:
                    try:
                        hare = hare.next.next
                        turtoise = turtoise.next
                    except:
                        return False
            return False

# finds the start node of the cycle if a cycle exists, returns none if no cycle is detected
    def find_start_if_has_cycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        else:
            hare = head.next
            turtoise = head
            while hare and turtoise:
                if hare == turtoise:
                    size = 1
                    hare = hare.next

                    while hare != turtoise:
                        size += 1
                        hare = hare.next

                    hare, turtoise = head

                    for i in range(size):
                        hare = hare.next

                    while hare != turtoise:
                        hare = hare.next
                        turtoise = turtoise.next
                    return turtoise

                else:
                    try:
                        hare = hare.next.next
                        turtoise = turtoise.next
                    except:
                        return None
            return None


if __name__ == '__main__':
    print("hello")
