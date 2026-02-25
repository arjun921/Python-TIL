# https://www.educative.io/interview-prep/coding/remove-nth-node-from-end-of-list
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_last_node(head, n):
    if not head:
        return head
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0 and right:
        right = right.next
        n -= 1
    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next
