# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        import copy
        num_1 = ""
        num_2 = ""
        
        while l1.next:
            num_1 += str(l1.val)
            l1.val, l1.next = l1.next.val, l1.next.next
            
        num_1 += str(l1.val)
        
        while l2.next:
            num_2 += str(l2.val)
            l2.val, l2.next = l2.next.val, l2.next.next

        num_2 += str(l2.val)
        
        num_1, num_2 = int(num_1[::-1]),int(num_2[::-1])
        
        
        sum_nodes = num_1+num_2
        
        sum_nodes = str(sum_nodes)
        
        
        sum_ll = ListNode(int(sum_nodes[0]))
        for elem in sum_nodes[1:]:
            sum_ll.next = copy.copy(sum_ll)
            sum_ll.val = int(elem)
        
        return sum_ll